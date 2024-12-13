# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from dodopayments import Dodopayments, AsyncDodopayments
from dodopayments.types import PayoutListResponse
from dodopayments.pagination import SyncPageNumberPage, AsyncPageNumberPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPayouts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Dodopayments) -> None:
        payout = client.payouts.list()
        assert_matches_type(SyncPageNumberPage[PayoutListResponse], payout, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Dodopayments) -> None:
        payout = client.payouts.list(
            page_number=0,
            page_size=0,
        )
        assert_matches_type(SyncPageNumberPage[PayoutListResponse], payout, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Dodopayments) -> None:
        response = client.payouts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payout = response.parse()
        assert_matches_type(SyncPageNumberPage[PayoutListResponse], payout, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Dodopayments) -> None:
        with client.payouts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payout = response.parse()
            assert_matches_type(SyncPageNumberPage[PayoutListResponse], payout, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPayouts:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncDodopayments) -> None:
        payout = await async_client.payouts.list()
        assert_matches_type(AsyncPageNumberPage[PayoutListResponse], payout, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDodopayments) -> None:
        payout = await async_client.payouts.list(
            page_number=0,
            page_size=0,
        )
        assert_matches_type(AsyncPageNumberPage[PayoutListResponse], payout, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDodopayments) -> None:
        response = await async_client.payouts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payout = await response.parse()
        assert_matches_type(AsyncPageNumberPage[PayoutListResponse], payout, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDodopayments) -> None:
        async with async_client.payouts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payout = await response.parse()
            assert_matches_type(AsyncPageNumberPage[PayoutListResponse], payout, path=["response"])

        assert cast(Any, response.is_closed) is True
