# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from dodopayments import DodoPayments, AsyncDodoPayments
from dodopayments.types.webhooks import HeaderRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHeaders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: DodoPayments) -> None:
        header = client.webhooks.headers.retrieve(
            "webhook_id",
        )
        assert_matches_type(HeaderRetrieveResponse, header, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: DodoPayments) -> None:
        response = client.webhooks.headers.with_raw_response.retrieve(
            "webhook_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        header = response.parse()
        assert_matches_type(HeaderRetrieveResponse, header, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: DodoPayments) -> None:
        with client.webhooks.headers.with_streaming_response.retrieve(
            "webhook_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            header = response.parse()
            assert_matches_type(HeaderRetrieveResponse, header, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            client.webhooks.headers.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: DodoPayments) -> None:
        header = client.webhooks.headers.update(
            webhook_id="webhook_id",
            headers={"foo": "string"},
        )
        assert header is None

    @parametrize
    def test_raw_response_update(self, client: DodoPayments) -> None:
        response = client.webhooks.headers.with_raw_response.update(
            webhook_id="webhook_id",
            headers={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        header = response.parse()
        assert header is None

    @parametrize
    def test_streaming_response_update(self, client: DodoPayments) -> None:
        with client.webhooks.headers.with_streaming_response.update(
            webhook_id="webhook_id",
            headers={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            header = response.parse()
            assert header is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            client.webhooks.headers.with_raw_response.update(
                webhook_id="",
                headers={"foo": "string"},
            )


class TestAsyncHeaders:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDodoPayments) -> None:
        header = await async_client.webhooks.headers.retrieve(
            "webhook_id",
        )
        assert_matches_type(HeaderRetrieveResponse, header, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.webhooks.headers.with_raw_response.retrieve(
            "webhook_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        header = await response.parse()
        assert_matches_type(HeaderRetrieveResponse, header, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.webhooks.headers.with_streaming_response.retrieve(
            "webhook_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            header = await response.parse()
            assert_matches_type(HeaderRetrieveResponse, header, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            await async_client.webhooks.headers.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncDodoPayments) -> None:
        header = await async_client.webhooks.headers.update(
            webhook_id="webhook_id",
            headers={"foo": "string"},
        )
        assert header is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.webhooks.headers.with_raw_response.update(
            webhook_id="webhook_id",
            headers={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        header = await response.parse()
        assert header is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.webhooks.headers.with_streaming_response.update(
            webhook_id="webhook_id",
            headers={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            header = await response.parse()
            assert header is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            await async_client.webhooks.headers.with_raw_response.update(
                webhook_id="",
                headers={"foo": "string"},
            )
