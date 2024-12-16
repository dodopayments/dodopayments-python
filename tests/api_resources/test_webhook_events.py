# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from dodopayments import DodoPayments, AsyncDodoPayments
from dodopayments.types import WebhookEvent
from dodopayments._utils import parse_datetime
from dodopayments.pagination import SyncDefaultPageNumberPagination, AsyncDefaultPageNumberPagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebhookEvents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: DodoPayments) -> None:
        webhook_event = client.webhook_events.retrieve(
            "webhook_event_id",
        )
        assert_matches_type(WebhookEvent, webhook_event, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: DodoPayments) -> None:
        response = client.webhook_events.with_raw_response.retrieve(
            "webhook_event_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_event = response.parse()
        assert_matches_type(WebhookEvent, webhook_event, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: DodoPayments) -> None:
        with client.webhook_events.with_streaming_response.retrieve(
            "webhook_event_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_event = response.parse()
            assert_matches_type(WebhookEvent, webhook_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_event_id` but received ''"):
            client.webhook_events.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: DodoPayments) -> None:
        webhook_event = client.webhook_events.list()
        assert_matches_type(SyncDefaultPageNumberPagination[WebhookEvent], webhook_event, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: DodoPayments) -> None:
        webhook_event = client.webhook_events.list(
            created_at_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=0,
            object_id="object_id",
            page_number=0,
            page_size=0,
        )
        assert_matches_type(SyncDefaultPageNumberPagination[WebhookEvent], webhook_event, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: DodoPayments) -> None:
        response = client.webhook_events.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_event = response.parse()
        assert_matches_type(SyncDefaultPageNumberPagination[WebhookEvent], webhook_event, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: DodoPayments) -> None:
        with client.webhook_events.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_event = response.parse()
            assert_matches_type(SyncDefaultPageNumberPagination[WebhookEvent], webhook_event, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWebhookEvents:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDodoPayments) -> None:
        webhook_event = await async_client.webhook_events.retrieve(
            "webhook_event_id",
        )
        assert_matches_type(WebhookEvent, webhook_event, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.webhook_events.with_raw_response.retrieve(
            "webhook_event_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_event = await response.parse()
        assert_matches_type(WebhookEvent, webhook_event, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.webhook_events.with_streaming_response.retrieve(
            "webhook_event_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_event = await response.parse()
            assert_matches_type(WebhookEvent, webhook_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_event_id` but received ''"):
            await async_client.webhook_events.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncDodoPayments) -> None:
        webhook_event = await async_client.webhook_events.list()
        assert_matches_type(AsyncDefaultPageNumberPagination[WebhookEvent], webhook_event, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDodoPayments) -> None:
        webhook_event = await async_client.webhook_events.list(
            created_at_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=0,
            object_id="object_id",
            page_number=0,
            page_size=0,
        )
        assert_matches_type(AsyncDefaultPageNumberPagination[WebhookEvent], webhook_event, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.webhook_events.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_event = await response.parse()
        assert_matches_type(AsyncDefaultPageNumberPagination[WebhookEvent], webhook_event, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.webhook_events.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_event = await response.parse()
            assert_matches_type(AsyncDefaultPageNumberPagination[WebhookEvent], webhook_event, path=["response"])

        assert cast(Any, response.is_closed) is True
