from __future__ import annotations

import os
import json
import time
import asyncio
import logging
import threading
from typing import List, Optional
from pathlib import Path
from typing_extensions import override

import httpx
import pytest
from respx import MockRouter

from dodopayments import DodoPayments, AsyncDodoPayments, workload_identity as workload_identity_module
from dodopayments._types import Omit
from dodopayments._exceptions import DodoPaymentsError, AuthenticationError, PermissionDeniedError
from dodopayments.workload_identity import (
    WorkloadIdentity,
    SubjectTokenContext,
    SubjectTokenProvider,
    static,
    vercel,
)

from .utils import update_env

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

TOKEN_PATH = "/workload-identity/token"
REVOKE_PATH = "/workload-identity/token/revoke"
IDENTITY_PROVIDER_ID = "wip_test"
SUBJECT_TOKEN = "subject-jwt"
EXCHANGE_BODY = {
    "grant_type": "urn:ietf:params:oauth:grant-type:token-exchange",
    "subject_token_type": "urn:ietf:params:oauth:token-type:jwt",
    "subject_token": SUBJECT_TOKEN,
    "identity_provider_id": IDENTITY_PROVIDER_ID,
}


class Recorder:
    """A respx side effect that keeps the requests and returns the responses in sequence."""

    def __init__(self, *responses: httpx.Response) -> None:
        self.requests: List[httpx.Request] = []
        self._responses = list(responses)

    def __call__(self, request: httpx.Request) -> httpx.Response:
        self.requests.append(request)
        response = self._responses[min(len(self.requests), len(self._responses)) - 1]
        return httpx.Response(response.status_code, headers=response.headers, content=response.content)

    @property
    def authorizations(self) -> List[Optional[str]]:
        return [request.headers.get("Authorization") for request in self.requests]


def tokens(*access_tokens: str, expires_in: int = 3600) -> Recorder:
    return Recorder(
        *(
            httpx.Response(
                200,
                json={
                    "access_token": access_token,
                    "issued_token_type": "urn:ietf:params:oauth:token-type:access_token",
                    "token_type": "Bearer",
                    "expires_in": expires_in,
                    "scope": "payments:read",
                },
            )
            for access_token in access_tokens
        )
    )


def ok() -> Recorder:
    return Recorder(httpx.Response(200, json={"ok": True}))


def workload_identity(provider: Optional[SubjectTokenProvider] = None) -> WorkloadIdentity:
    return WorkloadIdentity(identity_provider_id=IDENTITY_PROVIDER_ID, provider=provider or static(SUBJECT_TOKEN))


class SlowProvider(SubjectTokenProvider):
    @override
    def get_token(self, context: SubjectTokenContext) -> str:
        time.sleep(0.2)
        return SUBJECT_TOKEN

    @override
    async def aget_token(self, context: SubjectTokenContext) -> str:
        await asyncio.sleep(0.2)
        return SUBJECT_TOKEN


class TestWorkloadIdentity:
    def client(self, config: WorkloadIdentity) -> DodoPayments:
        return DodoPayments(base_url=base_url, workload_identity=config, _strict_response_validation=True)

    @pytest.mark.respx(base_url=base_url)
    def test_exchange_then_bearer(self, respx_mock: MockRouter) -> None:
        exchange, api = tokens("access-1"), ok()
        respx_mock.post(TOKEN_PATH).mock(side_effect=exchange)
        respx_mock.get("/foo").mock(side_effect=api)

        self.client(workload_identity()).get("/foo", cast_to=httpx.Response)

        assert len(exchange.requests) == 1
        assert exchange.authorizations == [None]
        assert json.loads(exchange.requests[0].content) == EXCHANGE_BODY
        assert api.authorizations == ["Bearer access-1"]

    @pytest.mark.respx(base_url=base_url)
    def test_concurrent_calls_exchange_once(self, respx_mock: MockRouter) -> None:
        exchange, api = tokens("access-1", "access-2"), ok()
        respx_mock.post(TOKEN_PATH).mock(side_effect=exchange)
        respx_mock.get("/foo").mock(side_effect=api)

        client = self.client(workload_identity(SlowProvider()))
        threads = [threading.Thread(target=lambda: client.get("/foo", cast_to=httpx.Response)) for _ in range(2)]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()

        assert len(exchange.requests) == 1
        assert api.authorizations == ["Bearer access-1", "Bearer access-1"]

    @pytest.mark.parametrize("expires_in, exchanges", [(200, 2), (3600, 1)])
    @pytest.mark.respx(base_url=base_url)
    def test_refresh_window(self, respx_mock: MockRouter, expires_in: int, exchanges: int) -> None:
        exchange = tokens("access-1", "access-2", expires_in=expires_in)
        respx_mock.post(TOKEN_PATH).mock(side_effect=exchange)
        respx_mock.get("/foo").mock(side_effect=ok())

        client = self.client(workload_identity())
        client.get("/foo", cast_to=httpx.Response)
        client.get("/foo", cast_to=httpx.Response)

        assert len(exchange.requests) == exchanges

    @pytest.mark.respx(base_url=base_url)
    def test_401_exchanges_and_retries_once(self, respx_mock: MockRouter) -> None:
        exchange = tokens("access-1", "access-2", "access-3")
        api = Recorder(httpx.Response(401, json={"message": "expired"}), httpx.Response(200, json={"ok": True}))
        respx_mock.post(TOKEN_PATH).mock(side_effect=exchange)
        respx_mock.get("/foo").mock(side_effect=api)

        response = self.client(workload_identity()).get("/foo", cast_to=httpx.Response)

        assert response.status_code == 200
        assert len(exchange.requests) == 2
        assert api.authorizations == ["Bearer access-1", "Bearer access-2"]

    @pytest.mark.respx(base_url=base_url)
    def test_second_401_surfaces(self, respx_mock: MockRouter) -> None:
        exchange = tokens("access-1", "access-2", "access-3")
        api = Recorder(httpx.Response(401, json={"message": "denied"}))
        respx_mock.post(TOKEN_PATH).mock(side_effect=exchange)
        respx_mock.get("/foo").mock(side_effect=api)

        with pytest.raises(AuthenticationError):
            self.client(workload_identity()).get("/foo", cast_to=httpx.Response)

        assert len(exchange.requests) == 2
        assert len(api.requests) == 2

    def test_bearer_token_and_workload_identity_conflict(self) -> None:
        with pytest.raises(DodoPaymentsError, match="mutually exclusive"):
            DodoPayments(base_url=base_url, bearer_token="My Bearer Token", workload_identity=workload_identity())

    @pytest.mark.respx(base_url=base_url)
    def test_exchange_403_raises_permission_denied(self, respx_mock: MockRouter) -> None:
        exchange = Recorder(
            httpx.Response(403, json={"error": "invalid_grant", "error_description": "no mapping matches the claims"})
        )
        respx_mock.post(TOKEN_PATH).mock(side_effect=exchange)

        with pytest.raises(PermissionDeniedError) as exc_info:
            self.client(workload_identity()).get("/foo", cast_to=httpx.Response)

        assert "invalid_grant" in str(exc_info.value)
        assert "no mapping matches the claims" in str(exc_info.value)
        assert len(exchange.requests) == 1

    @pytest.mark.respx(base_url=base_url)
    def test_revoke_clears_cache(self, respx_mock: MockRouter) -> None:
        exchange, revoke, api = tokens("access-1", "access-2"), Recorder(httpx.Response(204)), ok()
        respx_mock.post(TOKEN_PATH).mock(side_effect=exchange)
        respx_mock.post(REVOKE_PATH).mock(side_effect=revoke)
        respx_mock.get("/foo").mock(side_effect=api)

        client = self.client(workload_identity())
        client.workload_identity.revoke()
        assert len(revoke.requests) == 0

        client.get("/foo", cast_to=httpx.Response)
        client.workload_identity.revoke()
        client.get("/foo", cast_to=httpx.Response)

        assert revoke.authorizations == ["Bearer access-1"]
        assert len(exchange.requests) == 2
        assert api.authorizations == ["Bearer access-1", "Bearer access-2"]

    @pytest.mark.respx(base_url=base_url)
    def test_tokens_are_not_logged(self, respx_mock: MockRouter, caplog: pytest.LogCaptureFixture) -> None:
        respx_mock.post(TOKEN_PATH).mock(side_effect=tokens("access-1"))
        respx_mock.post(REVOKE_PATH).mock(side_effect=Recorder(httpx.Response(204)))
        respx_mock.get("/foo").mock(side_effect=ok())

        with caplog.at_level(logging.DEBUG):
            client = self.client(workload_identity())
            client.get("/foo", cast_to=httpx.Response)
            client.workload_identity.revoke()

        assert caplog.records
        assert SUBJECT_TOKEN not in caplog.text
        assert "access-1" not in caplog.text

    @pytest.mark.respx(base_url=base_url)
    def test_copy_shares_cache(self, respx_mock: MockRouter) -> None:
        exchange = tokens("access-1", "access-2")
        respx_mock.post(TOKEN_PATH).mock(side_effect=exchange)
        respx_mock.get("/foo").mock(side_effect=ok())

        client = self.client(workload_identity())
        client.get("/foo", cast_to=httpx.Response)
        client.with_options(max_retries=1).get("/foo", cast_to=httpx.Response)

        assert len(exchange.requests) == 1

    @pytest.mark.respx(base_url=base_url)
    def test_env_fallback(self, respx_mock: MockRouter, tmp_path: Path) -> None:
        token_file = tmp_path / "token"
        token_file.write_text(f"{SUBJECT_TOKEN}\n")
        exchange, api = tokens("access-1"), ok()
        respx_mock.post(TOKEN_PATH).mock(side_effect=exchange)
        respx_mock.get("/foo").mock(side_effect=api)

        with update_env(
            DODO_PAYMENTS_API_KEY=Omit(),
            DODO_PAYMENTS_IDENTITY_PROVIDER_ID=IDENTITY_PROVIDER_ID,
            DODO_PAYMENTS_IDENTITY_TOKEN_FILE=str(token_file),
            ACTIONS_ID_TOKEN_REQUEST_URL=Omit(),
            ACTIONS_ID_TOKEN_REQUEST_TOKEN=Omit(),
            TFC_WORKLOAD_IDENTITY_TOKEN=Omit(),
            TFC_WORKLOAD_IDENTITY_TOKEN_DODO=Omit(),
        ):
            DodoPayments(base_url=base_url, _strict_response_validation=True).get("/foo", cast_to=httpx.Response)

        assert json.loads(exchange.requests[0].content) == EXCHANGE_BODY
        assert api.authorizations == ["Bearer access-1"]

    @pytest.mark.respx(base_url=base_url)
    def test_vercel_exchanges_for_default_audience(
        self, respx_mock: MockRouter, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        monkeypatch.setattr(workload_identity_module, "VERCEL_TOKEN_URL", f"{base_url}/vercel/~token")
        vercel_stub = Recorder(httpx.Response(200, json={"token": "vercel-dodo-token", "expiry": 1}))
        exchange, api = tokens("access-1"), ok()
        respx_mock.post("/vercel/~token").mock(side_effect=vercel_stub)
        respx_mock.post(TOKEN_PATH).mock(side_effect=exchange)
        respx_mock.get("/foo").mock(side_effect=api)

        with update_env(VERCEL_OIDC_TOKEN="vercel-base-token", VERCEL_OIDC_TOKEN_FILE=Omit()):
            self.client(workload_identity(vercel())).get("/foo", cast_to=httpx.Response)

        assert json.loads(vercel_stub.requests[0].content) == {
            "token": "vercel-base-token",
            "aud": f"{httpx.URL(base_url).scheme}://{httpx.URL(base_url).netloc.decode('ascii')}",
        }
        assert json.loads(exchange.requests[0].content)["subject_token"] == "vercel-dodo-token"

        respx_mock.post("/vercel/~token").mock(return_value=httpx.Response(403, json={"error": "denied"}))
        with update_env(VERCEL_OIDC_TOKEN="vercel-base-token", VERCEL_OIDC_TOKEN_FILE=Omit()):
            with pytest.raises(DodoPaymentsError, match="status 403") as err:
                vercel().get_token(SubjectTokenContext(base_url=base_url, audience="https://live.dodopayments.com"))
        assert "vercel-base-token" not in str(err.value)


class TestAsyncWorkloadIdentity:
    def client(self, config: WorkloadIdentity) -> AsyncDodoPayments:
        return AsyncDodoPayments(base_url=base_url, workload_identity=config, _strict_response_validation=True)

    @pytest.mark.respx(base_url=base_url)
    async def test_exchange_then_bearer(self, respx_mock: MockRouter) -> None:
        exchange, api = tokens("access-1"), ok()
        respx_mock.post(TOKEN_PATH).mock(side_effect=exchange)
        respx_mock.get("/foo").mock(side_effect=api)

        await self.client(workload_identity()).get("/foo", cast_to=httpx.Response)

        assert len(exchange.requests) == 1
        assert exchange.authorizations == [None]
        assert json.loads(exchange.requests[0].content) == EXCHANGE_BODY
        assert api.authorizations == ["Bearer access-1"]

    @pytest.mark.respx(base_url=base_url)
    async def test_concurrent_calls_exchange_once(self, respx_mock: MockRouter) -> None:
        exchange, api = tokens("access-1", "access-2"), ok()
        respx_mock.post(TOKEN_PATH).mock(side_effect=exchange)
        respx_mock.get("/foo").mock(side_effect=api)

        client = self.client(workload_identity(SlowProvider()))
        await asyncio.gather(client.get("/foo", cast_to=httpx.Response), client.get("/foo", cast_to=httpx.Response))

        assert len(exchange.requests) == 1
        assert api.authorizations == ["Bearer access-1", "Bearer access-1"]

    @pytest.mark.parametrize("expires_in, exchanges", [(200, 2), (3600, 1)])
    @pytest.mark.respx(base_url=base_url)
    async def test_refresh_window(self, respx_mock: MockRouter, expires_in: int, exchanges: int) -> None:
        exchange = tokens("access-1", "access-2", expires_in=expires_in)
        respx_mock.post(TOKEN_PATH).mock(side_effect=exchange)
        respx_mock.get("/foo").mock(side_effect=ok())

        client = self.client(workload_identity())
        await client.get("/foo", cast_to=httpx.Response)
        await client.get("/foo", cast_to=httpx.Response)

        assert len(exchange.requests) == exchanges

    @pytest.mark.respx(base_url=base_url)
    async def test_401_exchanges_and_retries_once(self, respx_mock: MockRouter) -> None:
        exchange = tokens("access-1", "access-2", "access-3")
        api = Recorder(httpx.Response(401, json={"message": "expired"}), httpx.Response(200, json={"ok": True}))
        respx_mock.post(TOKEN_PATH).mock(side_effect=exchange)
        respx_mock.get("/foo").mock(side_effect=api)

        response = await self.client(workload_identity()).get("/foo", cast_to=httpx.Response)

        assert response.status_code == 200
        assert len(exchange.requests) == 2
        assert api.authorizations == ["Bearer access-1", "Bearer access-2"]

    @pytest.mark.respx(base_url=base_url)
    async def test_second_401_surfaces(self, respx_mock: MockRouter) -> None:
        exchange = tokens("access-1", "access-2", "access-3")
        api = Recorder(httpx.Response(401, json={"message": "denied"}))
        respx_mock.post(TOKEN_PATH).mock(side_effect=exchange)
        respx_mock.get("/foo").mock(side_effect=api)

        with pytest.raises(AuthenticationError):
            await self.client(workload_identity()).get("/foo", cast_to=httpx.Response)

        assert len(exchange.requests) == 2
        assert len(api.requests) == 2

    async def test_bearer_token_and_workload_identity_conflict(self) -> None:
        with pytest.raises(DodoPaymentsError, match="mutually exclusive"):
            AsyncDodoPayments(base_url=base_url, bearer_token="My Bearer Token", workload_identity=workload_identity())

    @pytest.mark.respx(base_url=base_url)
    async def test_exchange_403_raises_permission_denied(self, respx_mock: MockRouter) -> None:
        exchange = Recorder(
            httpx.Response(403, json={"error": "invalid_grant", "error_description": "no mapping matches the claims"})
        )
        respx_mock.post(TOKEN_PATH).mock(side_effect=exchange)

        with pytest.raises(PermissionDeniedError) as exc_info:
            await self.client(workload_identity()).get("/foo", cast_to=httpx.Response)

        assert "invalid_grant" in str(exc_info.value)
        assert "no mapping matches the claims" in str(exc_info.value)
        assert len(exchange.requests) == 1

    @pytest.mark.respx(base_url=base_url)
    async def test_revoke_clears_cache(self, respx_mock: MockRouter) -> None:
        exchange, revoke, api = tokens("access-1", "access-2"), Recorder(httpx.Response(204)), ok()
        respx_mock.post(TOKEN_PATH).mock(side_effect=exchange)
        respx_mock.post(REVOKE_PATH).mock(side_effect=revoke)
        respx_mock.get("/foo").mock(side_effect=api)

        client = self.client(workload_identity())
        await client.workload_identity.revoke()
        assert len(revoke.requests) == 0

        await client.get("/foo", cast_to=httpx.Response)
        await client.workload_identity.revoke()
        await client.get("/foo", cast_to=httpx.Response)

        assert revoke.authorizations == ["Bearer access-1"]
        assert len(exchange.requests) == 2
        assert api.authorizations == ["Bearer access-1", "Bearer access-2"]
