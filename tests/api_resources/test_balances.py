# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from dodopayments import DodoPayments, AsyncDodoPayments
from dodopayments.types import BalanceLedgerEntry
from dodopayments._utils import parse_datetime
from dodopayments.pagination import SyncDefaultPageNumberPagination, AsyncDefaultPageNumberPagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBalances:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve_ledger(self, client: DodoPayments) -> None:
        balance = client.balances.retrieve_ledger()
        assert_matches_type(SyncDefaultPageNumberPagination[BalanceLedgerEntry], balance, path=["response"])

    @parametrize
    def test_method_retrieve_ledger_with_all_params(self, client: DodoPayments) -> None:
        balance = client.balances.retrieve_ledger(
            created_at_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            currency="AED",
            event_type="payment",
            limit=0,
            page_number=0,
            page_size=0,
            reference_object_id="reference_object_id",
        )
        assert_matches_type(SyncDefaultPageNumberPagination[BalanceLedgerEntry], balance, path=["response"])

    @parametrize
    def test_raw_response_retrieve_ledger(self, client: DodoPayments) -> None:
        response = client.balances.with_raw_response.retrieve_ledger()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        balance = response.parse()
        assert_matches_type(SyncDefaultPageNumberPagination[BalanceLedgerEntry], balance, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_ledger(self, client: DodoPayments) -> None:
        with client.balances.with_streaming_response.retrieve_ledger() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            balance = response.parse()
            assert_matches_type(SyncDefaultPageNumberPagination[BalanceLedgerEntry], balance, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBalances:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve_ledger(self, async_client: AsyncDodoPayments) -> None:
        balance = await async_client.balances.retrieve_ledger()
        assert_matches_type(AsyncDefaultPageNumberPagination[BalanceLedgerEntry], balance, path=["response"])

    @parametrize
    async def test_method_retrieve_ledger_with_all_params(self, async_client: AsyncDodoPayments) -> None:
        balance = await async_client.balances.retrieve_ledger(
            created_at_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            currency="AED",
            event_type="payment",
            limit=0,
            page_number=0,
            page_size=0,
            reference_object_id="reference_object_id",
        )
        assert_matches_type(AsyncDefaultPageNumberPagination[BalanceLedgerEntry], balance, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_ledger(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.balances.with_raw_response.retrieve_ledger()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        balance = await response.parse()
        assert_matches_type(AsyncDefaultPageNumberPagination[BalanceLedgerEntry], balance, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_ledger(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.balances.with_streaming_response.retrieve_ledger() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            balance = await response.parse()
            assert_matches_type(AsyncDefaultPageNumberPagination[BalanceLedgerEntry], balance, path=["response"])

        assert cast(Any, response.is_closed) is True
