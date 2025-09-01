# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from dodopayments import DodoPayments, AsyncDodoPayments
from dodopayments.types import Event, UsageEventIngestResponse
from dodopayments._utils import parse_datetime
from dodopayments.pagination import SyncDefaultPageNumberPagination, AsyncDefaultPageNumberPagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsageEvents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: DodoPayments) -> None:
        usage_event = client.usage_events.retrieve(
            "event_id",
        )
        assert_matches_type(Event, usage_event, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: DodoPayments) -> None:
        response = client.usage_events.with_raw_response.retrieve(
            "event_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage_event = response.parse()
        assert_matches_type(Event, usage_event, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: DodoPayments) -> None:
        with client.usage_events.with_streaming_response.retrieve(
            "event_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage_event = response.parse()
            assert_matches_type(Event, usage_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            client.usage_events.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: DodoPayments) -> None:
        usage_event = client.usage_events.list()
        assert_matches_type(SyncDefaultPageNumberPagination[Event], usage_event, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: DodoPayments) -> None:
        usage_event = client.usage_events.list(
            customer_id="customer_id",
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            event_name="event_name",
            meter_id="meter_id",
            page_number=0,
            page_size=0,
            start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncDefaultPageNumberPagination[Event], usage_event, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: DodoPayments) -> None:
        response = client.usage_events.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage_event = response.parse()
        assert_matches_type(SyncDefaultPageNumberPagination[Event], usage_event, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: DodoPayments) -> None:
        with client.usage_events.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage_event = response.parse()
            assert_matches_type(SyncDefaultPageNumberPagination[Event], usage_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_ingest(self, client: DodoPayments) -> None:
        usage_event = client.usage_events.ingest(
            events=[
                {
                    "customer_id": "customer_id",
                    "event_id": "event_id",
                    "event_name": "event_name",
                }
            ],
        )
        assert_matches_type(UsageEventIngestResponse, usage_event, path=["response"])

    @parametrize
    def test_raw_response_ingest(self, client: DodoPayments) -> None:
        response = client.usage_events.with_raw_response.ingest(
            events=[
                {
                    "customer_id": "customer_id",
                    "event_id": "event_id",
                    "event_name": "event_name",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage_event = response.parse()
        assert_matches_type(UsageEventIngestResponse, usage_event, path=["response"])

    @parametrize
    def test_streaming_response_ingest(self, client: DodoPayments) -> None:
        with client.usage_events.with_streaming_response.ingest(
            events=[
                {
                    "customer_id": "customer_id",
                    "event_id": "event_id",
                    "event_name": "event_name",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage_event = response.parse()
            assert_matches_type(UsageEventIngestResponse, usage_event, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUsageEvents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDodoPayments) -> None:
        usage_event = await async_client.usage_events.retrieve(
            "event_id",
        )
        assert_matches_type(Event, usage_event, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.usage_events.with_raw_response.retrieve(
            "event_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage_event = await response.parse()
        assert_matches_type(Event, usage_event, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.usage_events.with_streaming_response.retrieve(
            "event_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage_event = await response.parse()
            assert_matches_type(Event, usage_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            await async_client.usage_events.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncDodoPayments) -> None:
        usage_event = await async_client.usage_events.list()
        assert_matches_type(AsyncDefaultPageNumberPagination[Event], usage_event, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDodoPayments) -> None:
        usage_event = await async_client.usage_events.list(
            customer_id="customer_id",
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            event_name="event_name",
            meter_id="meter_id",
            page_number=0,
            page_size=0,
            start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncDefaultPageNumberPagination[Event], usage_event, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.usage_events.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage_event = await response.parse()
        assert_matches_type(AsyncDefaultPageNumberPagination[Event], usage_event, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.usage_events.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage_event = await response.parse()
            assert_matches_type(AsyncDefaultPageNumberPagination[Event], usage_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_ingest(self, async_client: AsyncDodoPayments) -> None:
        usage_event = await async_client.usage_events.ingest(
            events=[
                {
                    "customer_id": "customer_id",
                    "event_id": "event_id",
                    "event_name": "event_name",
                }
            ],
        )
        assert_matches_type(UsageEventIngestResponse, usage_event, path=["response"])

    @parametrize
    async def test_raw_response_ingest(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.usage_events.with_raw_response.ingest(
            events=[
                {
                    "customer_id": "customer_id",
                    "event_id": "event_id",
                    "event_name": "event_name",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage_event = await response.parse()
        assert_matches_type(UsageEventIngestResponse, usage_event, path=["response"])

    @parametrize
    async def test_streaming_response_ingest(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.usage_events.with_streaming_response.ingest(
            events=[
                {
                    "customer_id": "customer_id",
                    "event_id": "event_id",
                    "event_name": "event_name",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage_event = await response.parse()
            assert_matches_type(UsageEventIngestResponse, usage_event, path=["response"])

        assert cast(Any, response.is_closed) is True
