# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast
from datetime import datetime, timezone

import pytest
import standardwebhooks

from tests.utils import assert_matches_type
from dodopayments import DodoPayments, AsyncDodoPayments
from dodopayments.types import (
    WebhookDetails,
    WebhookRetrieveSecretResponse,
)
from dodopayments.pagination import SyncCursorPagePagination, AsyncCursorPagePagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebhooks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: DodoPayments) -> None:
        webhook = client.webhooks.create(
            url="url",
        )
        assert_matches_type(WebhookDetails, webhook, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: DodoPayments) -> None:
        webhook = client.webhooks.create(
            url="url",
            description="description",
            disabled=True,
            filter_types=["payment.succeeded"],
            headers={"foo": "string"},
            idempotency_key="idempotency_key",
            metadata={"foo": "string"},
            rate_limit=0,
        )
        assert_matches_type(WebhookDetails, webhook, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: DodoPayments) -> None:
        response = client.webhooks.with_raw_response.create(
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookDetails, webhook, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: DodoPayments) -> None:
        with client.webhooks.with_streaming_response.create(
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookDetails, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: DodoPayments) -> None:
        webhook = client.webhooks.retrieve(
            "webhook_id",
        )
        assert_matches_type(WebhookDetails, webhook, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: DodoPayments) -> None:
        response = client.webhooks.with_raw_response.retrieve(
            "webhook_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookDetails, webhook, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: DodoPayments) -> None:
        with client.webhooks.with_streaming_response.retrieve(
            "webhook_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookDetails, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            client.webhooks.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: DodoPayments) -> None:
        webhook = client.webhooks.update(
            webhook_id="webhook_id",
        )
        assert_matches_type(WebhookDetails, webhook, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: DodoPayments) -> None:
        webhook = client.webhooks.update(
            webhook_id="webhook_id",
            description="description",
            disabled=True,
            filter_types=["payment.succeeded"],
            metadata={"foo": "string"},
            rate_limit=0,
            url="url",
        )
        assert_matches_type(WebhookDetails, webhook, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: DodoPayments) -> None:
        response = client.webhooks.with_raw_response.update(
            webhook_id="webhook_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookDetails, webhook, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: DodoPayments) -> None:
        with client.webhooks.with_streaming_response.update(
            webhook_id="webhook_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookDetails, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            client.webhooks.with_raw_response.update(
                webhook_id="",
            )

    @parametrize
    def test_method_list(self, client: DodoPayments) -> None:
        webhook = client.webhooks.list()
        assert_matches_type(SyncCursorPagePagination[WebhookDetails], webhook, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: DodoPayments) -> None:
        webhook = client.webhooks.list(
            iterator="iterator",
            limit=0,
        )
        assert_matches_type(SyncCursorPagePagination[WebhookDetails], webhook, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: DodoPayments) -> None:
        response = client.webhooks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(SyncCursorPagePagination[WebhookDetails], webhook, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: DodoPayments) -> None:
        with client.webhooks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(SyncCursorPagePagination[WebhookDetails], webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: DodoPayments) -> None:
        webhook = client.webhooks.delete(
            "webhook_id",
        )
        assert webhook is None

    @parametrize
    def test_raw_response_delete(self, client: DodoPayments) -> None:
        response = client.webhooks.with_raw_response.delete(
            "webhook_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert webhook is None

    @parametrize
    def test_streaming_response_delete(self, client: DodoPayments) -> None:
        with client.webhooks.with_streaming_response.delete(
            "webhook_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert webhook is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            client.webhooks.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_retrieve_secret(self, client: DodoPayments) -> None:
        webhook = client.webhooks.retrieve_secret(
            "webhook_id",
        )
        assert_matches_type(WebhookRetrieveSecretResponse, webhook, path=["response"])

    @parametrize
    def test_raw_response_retrieve_secret(self, client: DodoPayments) -> None:
        response = client.webhooks.with_raw_response.retrieve_secret(
            "webhook_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookRetrieveSecretResponse, webhook, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_secret(self, client: DodoPayments) -> None:
        with client.webhooks.with_streaming_response.retrieve_secret(
            "webhook_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookRetrieveSecretResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve_secret(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            client.webhooks.with_raw_response.retrieve_secret(
                "",
            )

    def test_method_unwrap(self, client: DodoPayments) -> None:
        key = b"secret"
        hook = standardwebhooks.Webhook(key)

        data = """{"business_id":"business_id","data":{"amount":"amount","business_id":"business_id","created_at":"2019-12-27T18:11:19.117Z","currency":"currency","dispute_id":"dispute_id","dispute_stage":"pre_dispute","dispute_status":"dispute_opened","payment_id":"payment_id","remarks":"remarks","payload_type":"Dispute"},"timestamp":"2019-12-27T18:11:19.117Z","type":"dispute.accepted"}"""
        msg_id = "1"
        timestamp = datetime.now(tz=timezone.utc)
        sig = hook.sign(msg_id=msg_id, timestamp=timestamp, data=data)
        headers = {
            "webhook-id": msg_id,
            "webhook-timestamp": str(int(timestamp.timestamp())),
            "webhook-signature": sig,
        }

        try:
            _ = client.webhooks.unwrap(data, headers=headers, key=key)
        except standardwebhooks.WebhookVerificationError as e:
            raise AssertionError("Failed to unwrap valid webhook") from e

        bad_headers = [
            {**headers, "webhook-signature": hook.sign(msg_id=msg_id, timestamp=timestamp, data="xxx")},
            {**headers, "webhook-id": "bad"},
            {**headers, "webhook-timestamp": "0"},
        ]
        for bad_header in bad_headers:
            with pytest.raises(standardwebhooks.WebhookVerificationError):
                _ = client.webhooks.unwrap(data, headers=bad_header, key=key)


class TestAsyncWebhooks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncDodoPayments) -> None:
        webhook = await async_client.webhooks.create(
            url="url",
        )
        assert_matches_type(WebhookDetails, webhook, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDodoPayments) -> None:
        webhook = await async_client.webhooks.create(
            url="url",
            description="description",
            disabled=True,
            filter_types=["payment.succeeded"],
            headers={"foo": "string"},
            idempotency_key="idempotency_key",
            metadata={"foo": "string"},
            rate_limit=0,
        )
        assert_matches_type(WebhookDetails, webhook, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.webhooks.with_raw_response.create(
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookDetails, webhook, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.webhooks.with_streaming_response.create(
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookDetails, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDodoPayments) -> None:
        webhook = await async_client.webhooks.retrieve(
            "webhook_id",
        )
        assert_matches_type(WebhookDetails, webhook, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.webhooks.with_raw_response.retrieve(
            "webhook_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookDetails, webhook, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.webhooks.with_streaming_response.retrieve(
            "webhook_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookDetails, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            await async_client.webhooks.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncDodoPayments) -> None:
        webhook = await async_client.webhooks.update(
            webhook_id="webhook_id",
        )
        assert_matches_type(WebhookDetails, webhook, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncDodoPayments) -> None:
        webhook = await async_client.webhooks.update(
            webhook_id="webhook_id",
            description="description",
            disabled=True,
            filter_types=["payment.succeeded"],
            metadata={"foo": "string"},
            rate_limit=0,
            url="url",
        )
        assert_matches_type(WebhookDetails, webhook, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.webhooks.with_raw_response.update(
            webhook_id="webhook_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookDetails, webhook, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.webhooks.with_streaming_response.update(
            webhook_id="webhook_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookDetails, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            await async_client.webhooks.with_raw_response.update(
                webhook_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncDodoPayments) -> None:
        webhook = await async_client.webhooks.list()
        assert_matches_type(AsyncCursorPagePagination[WebhookDetails], webhook, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDodoPayments) -> None:
        webhook = await async_client.webhooks.list(
            iterator="iterator",
            limit=0,
        )
        assert_matches_type(AsyncCursorPagePagination[WebhookDetails], webhook, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.webhooks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(AsyncCursorPagePagination[WebhookDetails], webhook, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.webhooks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(AsyncCursorPagePagination[WebhookDetails], webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncDodoPayments) -> None:
        webhook = await async_client.webhooks.delete(
            "webhook_id",
        )
        assert webhook is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.webhooks.with_raw_response.delete(
            "webhook_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert webhook is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.webhooks.with_streaming_response.delete(
            "webhook_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert webhook is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            await async_client.webhooks.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_retrieve_secret(self, async_client: AsyncDodoPayments) -> None:
        webhook = await async_client.webhooks.retrieve_secret(
            "webhook_id",
        )
        assert_matches_type(WebhookRetrieveSecretResponse, webhook, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_secret(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.webhooks.with_raw_response.retrieve_secret(
            "webhook_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookRetrieveSecretResponse, webhook, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_secret(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.webhooks.with_streaming_response.retrieve_secret(
            "webhook_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookRetrieveSecretResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve_secret(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            await async_client.webhooks.with_raw_response.retrieve_secret(
                "",
            )

    def test_method_unwrap(self, client: DodoPayments) -> None:
        key = b"secret"
        hook = standardwebhooks.Webhook(key)

        data = """{"business_id":"business_id","data":{"amount":"amount","business_id":"business_id","created_at":"2019-12-27T18:11:19.117Z","currency":"currency","dispute_id":"dispute_id","dispute_stage":"pre_dispute","dispute_status":"dispute_opened","payment_id":"payment_id","remarks":"remarks","payload_type":"Dispute"},"timestamp":"2019-12-27T18:11:19.117Z","type":"dispute.accepted"}"""
        msg_id = "1"
        timestamp = datetime.now(tz=timezone.utc)
        sig = hook.sign(msg_id=msg_id, timestamp=timestamp, data=data)
        headers = {
            "webhook-id": msg_id,
            "webhook-timestamp": str(int(timestamp.timestamp())),
            "webhook-signature": sig,
        }

        try:
            _ = client.webhooks.unwrap(data, headers=headers, key=key)
        except standardwebhooks.WebhookVerificationError as e:
            raise AssertionError("Failed to unwrap valid webhook") from e

        bad_headers = [
            {**headers, "webhook-signature": hook.sign(msg_id=msg_id, timestamp=timestamp, data="xxx")},
            {**headers, "webhook-id": "bad"},
            {**headers, "webhook-timestamp": "0"},
        ]
        for bad_header in bad_headers:
            with pytest.raises(standardwebhooks.WebhookVerificationError):
                _ = client.webhooks.unwrap(data, headers=bad_header, key=key)
