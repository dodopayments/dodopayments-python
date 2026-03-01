# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from dodopayments import DodoPayments, AsyncDodoPayments
from dodopayments._utils import parse_datetime
from dodopayments.pagination import SyncDefaultPageNumberPagination, AsyncDefaultPageNumberPagination
from dodopayments.types.credit_entitlements import (
    CreditLedgerEntry,
    CustomerCreditBalance,
    BalanceListGrantsResponse,
    BalanceCreateLedgerEntryResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBalances:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: DodoPayments) -> None:
        balance = client.credit_entitlements.balances.retrieve(
            customer_id="customer_id",
            credit_entitlement_id="credit_entitlement_id",
        )
        assert_matches_type(CustomerCreditBalance, balance, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: DodoPayments) -> None:
        response = client.credit_entitlements.balances.with_raw_response.retrieve(
            customer_id="customer_id",
            credit_entitlement_id="credit_entitlement_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        balance = response.parse()
        assert_matches_type(CustomerCreditBalance, balance, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: DodoPayments) -> None:
        with client.credit_entitlements.balances.with_streaming_response.retrieve(
            customer_id="customer_id",
            credit_entitlement_id="credit_entitlement_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            balance = response.parse()
            assert_matches_type(CustomerCreditBalance, balance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `credit_entitlement_id` but received ''"):
            client.credit_entitlements.balances.with_raw_response.retrieve(
                customer_id="customer_id",
                credit_entitlement_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.credit_entitlements.balances.with_raw_response.retrieve(
                customer_id="",
                credit_entitlement_id="credit_entitlement_id",
            )

    @parametrize
    def test_method_list(self, client: DodoPayments) -> None:
        balance = client.credit_entitlements.balances.list(
            credit_entitlement_id="credit_entitlement_id",
        )
        assert_matches_type(SyncDefaultPageNumberPagination[CustomerCreditBalance], balance, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: DodoPayments) -> None:
        balance = client.credit_entitlements.balances.list(
            credit_entitlement_id="credit_entitlement_id",
            customer_id="customer_id",
            page_number=0,
            page_size=0,
        )
        assert_matches_type(SyncDefaultPageNumberPagination[CustomerCreditBalance], balance, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: DodoPayments) -> None:
        response = client.credit_entitlements.balances.with_raw_response.list(
            credit_entitlement_id="credit_entitlement_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        balance = response.parse()
        assert_matches_type(SyncDefaultPageNumberPagination[CustomerCreditBalance], balance, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: DodoPayments) -> None:
        with client.credit_entitlements.balances.with_streaming_response.list(
            credit_entitlement_id="credit_entitlement_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            balance = response.parse()
            assert_matches_type(SyncDefaultPageNumberPagination[CustomerCreditBalance], balance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `credit_entitlement_id` but received ''"):
            client.credit_entitlements.balances.with_raw_response.list(
                credit_entitlement_id="",
            )

    @parametrize
    def test_method_create_ledger_entry(self, client: DodoPayments) -> None:
        balance = client.credit_entitlements.balances.create_ledger_entry(
            customer_id="customer_id",
            credit_entitlement_id="credit_entitlement_id",
            amount="amount",
            entry_type="credit",
        )
        assert_matches_type(BalanceCreateLedgerEntryResponse, balance, path=["response"])

    @parametrize
    def test_method_create_ledger_entry_with_all_params(self, client: DodoPayments) -> None:
        balance = client.credit_entitlements.balances.create_ledger_entry(
            customer_id="customer_id",
            credit_entitlement_id="credit_entitlement_id",
            amount="amount",
            entry_type="credit",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            idempotency_key="idempotency_key",
            metadata={"foo": "string"},
            reason="reason",
        )
        assert_matches_type(BalanceCreateLedgerEntryResponse, balance, path=["response"])

    @parametrize
    def test_raw_response_create_ledger_entry(self, client: DodoPayments) -> None:
        response = client.credit_entitlements.balances.with_raw_response.create_ledger_entry(
            customer_id="customer_id",
            credit_entitlement_id="credit_entitlement_id",
            amount="amount",
            entry_type="credit",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        balance = response.parse()
        assert_matches_type(BalanceCreateLedgerEntryResponse, balance, path=["response"])

    @parametrize
    def test_streaming_response_create_ledger_entry(self, client: DodoPayments) -> None:
        with client.credit_entitlements.balances.with_streaming_response.create_ledger_entry(
            customer_id="customer_id",
            credit_entitlement_id="credit_entitlement_id",
            amount="amount",
            entry_type="credit",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            balance = response.parse()
            assert_matches_type(BalanceCreateLedgerEntryResponse, balance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_ledger_entry(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `credit_entitlement_id` but received ''"):
            client.credit_entitlements.balances.with_raw_response.create_ledger_entry(
                customer_id="customer_id",
                credit_entitlement_id="",
                amount="amount",
                entry_type="credit",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.credit_entitlements.balances.with_raw_response.create_ledger_entry(
                customer_id="",
                credit_entitlement_id="credit_entitlement_id",
                amount="amount",
                entry_type="credit",
            )

    @parametrize
    def test_method_list_grants(self, client: DodoPayments) -> None:
        balance = client.credit_entitlements.balances.list_grants(
            customer_id="customer_id",
            credit_entitlement_id="credit_entitlement_id",
        )
        assert_matches_type(SyncDefaultPageNumberPagination[BalanceListGrantsResponse], balance, path=["response"])

    @parametrize
    def test_method_list_grants_with_all_params(self, client: DodoPayments) -> None:
        balance = client.credit_entitlements.balances.list_grants(
            customer_id="customer_id",
            credit_entitlement_id="credit_entitlement_id",
            page_number=0,
            page_size=0,
            status="active",
        )
        assert_matches_type(SyncDefaultPageNumberPagination[BalanceListGrantsResponse], balance, path=["response"])

    @parametrize
    def test_raw_response_list_grants(self, client: DodoPayments) -> None:
        response = client.credit_entitlements.balances.with_raw_response.list_grants(
            customer_id="customer_id",
            credit_entitlement_id="credit_entitlement_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        balance = response.parse()
        assert_matches_type(SyncDefaultPageNumberPagination[BalanceListGrantsResponse], balance, path=["response"])

    @parametrize
    def test_streaming_response_list_grants(self, client: DodoPayments) -> None:
        with client.credit_entitlements.balances.with_streaming_response.list_grants(
            customer_id="customer_id",
            credit_entitlement_id="credit_entitlement_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            balance = response.parse()
            assert_matches_type(SyncDefaultPageNumberPagination[BalanceListGrantsResponse], balance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_grants(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `credit_entitlement_id` but received ''"):
            client.credit_entitlements.balances.with_raw_response.list_grants(
                customer_id="customer_id",
                credit_entitlement_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.credit_entitlements.balances.with_raw_response.list_grants(
                customer_id="",
                credit_entitlement_id="credit_entitlement_id",
            )

    @parametrize
    def test_method_list_ledger(self, client: DodoPayments) -> None:
        balance = client.credit_entitlements.balances.list_ledger(
            customer_id="customer_id",
            credit_entitlement_id="credit_entitlement_id",
        )
        assert_matches_type(SyncDefaultPageNumberPagination[CreditLedgerEntry], balance, path=["response"])

    @parametrize
    def test_method_list_ledger_with_all_params(self, client: DodoPayments) -> None:
        balance = client.credit_entitlements.balances.list_ledger(
            customer_id="customer_id",
            credit_entitlement_id="credit_entitlement_id",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            page_number=0,
            page_size=0,
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            transaction_type="transaction_type",
        )
        assert_matches_type(SyncDefaultPageNumberPagination[CreditLedgerEntry], balance, path=["response"])

    @parametrize
    def test_raw_response_list_ledger(self, client: DodoPayments) -> None:
        response = client.credit_entitlements.balances.with_raw_response.list_ledger(
            customer_id="customer_id",
            credit_entitlement_id="credit_entitlement_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        balance = response.parse()
        assert_matches_type(SyncDefaultPageNumberPagination[CreditLedgerEntry], balance, path=["response"])

    @parametrize
    def test_streaming_response_list_ledger(self, client: DodoPayments) -> None:
        with client.credit_entitlements.balances.with_streaming_response.list_ledger(
            customer_id="customer_id",
            credit_entitlement_id="credit_entitlement_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            balance = response.parse()
            assert_matches_type(SyncDefaultPageNumberPagination[CreditLedgerEntry], balance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_ledger(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `credit_entitlement_id` but received ''"):
            client.credit_entitlements.balances.with_raw_response.list_ledger(
                customer_id="customer_id",
                credit_entitlement_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.credit_entitlements.balances.with_raw_response.list_ledger(
                customer_id="",
                credit_entitlement_id="credit_entitlement_id",
            )


class TestAsyncBalances:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDodoPayments) -> None:
        balance = await async_client.credit_entitlements.balances.retrieve(
            customer_id="customer_id",
            credit_entitlement_id="credit_entitlement_id",
        )
        assert_matches_type(CustomerCreditBalance, balance, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.credit_entitlements.balances.with_raw_response.retrieve(
            customer_id="customer_id",
            credit_entitlement_id="credit_entitlement_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        balance = await response.parse()
        assert_matches_type(CustomerCreditBalance, balance, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.credit_entitlements.balances.with_streaming_response.retrieve(
            customer_id="customer_id",
            credit_entitlement_id="credit_entitlement_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            balance = await response.parse()
            assert_matches_type(CustomerCreditBalance, balance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `credit_entitlement_id` but received ''"):
            await async_client.credit_entitlements.balances.with_raw_response.retrieve(
                customer_id="customer_id",
                credit_entitlement_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.credit_entitlements.balances.with_raw_response.retrieve(
                customer_id="",
                credit_entitlement_id="credit_entitlement_id",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncDodoPayments) -> None:
        balance = await async_client.credit_entitlements.balances.list(
            credit_entitlement_id="credit_entitlement_id",
        )
        assert_matches_type(AsyncDefaultPageNumberPagination[CustomerCreditBalance], balance, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDodoPayments) -> None:
        balance = await async_client.credit_entitlements.balances.list(
            credit_entitlement_id="credit_entitlement_id",
            customer_id="customer_id",
            page_number=0,
            page_size=0,
        )
        assert_matches_type(AsyncDefaultPageNumberPagination[CustomerCreditBalance], balance, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.credit_entitlements.balances.with_raw_response.list(
            credit_entitlement_id="credit_entitlement_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        balance = await response.parse()
        assert_matches_type(AsyncDefaultPageNumberPagination[CustomerCreditBalance], balance, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.credit_entitlements.balances.with_streaming_response.list(
            credit_entitlement_id="credit_entitlement_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            balance = await response.parse()
            assert_matches_type(AsyncDefaultPageNumberPagination[CustomerCreditBalance], balance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `credit_entitlement_id` but received ''"):
            await async_client.credit_entitlements.balances.with_raw_response.list(
                credit_entitlement_id="",
            )

    @parametrize
    async def test_method_create_ledger_entry(self, async_client: AsyncDodoPayments) -> None:
        balance = await async_client.credit_entitlements.balances.create_ledger_entry(
            customer_id="customer_id",
            credit_entitlement_id="credit_entitlement_id",
            amount="amount",
            entry_type="credit",
        )
        assert_matches_type(BalanceCreateLedgerEntryResponse, balance, path=["response"])

    @parametrize
    async def test_method_create_ledger_entry_with_all_params(self, async_client: AsyncDodoPayments) -> None:
        balance = await async_client.credit_entitlements.balances.create_ledger_entry(
            customer_id="customer_id",
            credit_entitlement_id="credit_entitlement_id",
            amount="amount",
            entry_type="credit",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            idempotency_key="idempotency_key",
            metadata={"foo": "string"},
            reason="reason",
        )
        assert_matches_type(BalanceCreateLedgerEntryResponse, balance, path=["response"])

    @parametrize
    async def test_raw_response_create_ledger_entry(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.credit_entitlements.balances.with_raw_response.create_ledger_entry(
            customer_id="customer_id",
            credit_entitlement_id="credit_entitlement_id",
            amount="amount",
            entry_type="credit",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        balance = await response.parse()
        assert_matches_type(BalanceCreateLedgerEntryResponse, balance, path=["response"])

    @parametrize
    async def test_streaming_response_create_ledger_entry(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.credit_entitlements.balances.with_streaming_response.create_ledger_entry(
            customer_id="customer_id",
            credit_entitlement_id="credit_entitlement_id",
            amount="amount",
            entry_type="credit",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            balance = await response.parse()
            assert_matches_type(BalanceCreateLedgerEntryResponse, balance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_ledger_entry(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `credit_entitlement_id` but received ''"):
            await async_client.credit_entitlements.balances.with_raw_response.create_ledger_entry(
                customer_id="customer_id",
                credit_entitlement_id="",
                amount="amount",
                entry_type="credit",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.credit_entitlements.balances.with_raw_response.create_ledger_entry(
                customer_id="",
                credit_entitlement_id="credit_entitlement_id",
                amount="amount",
                entry_type="credit",
            )

    @parametrize
    async def test_method_list_grants(self, async_client: AsyncDodoPayments) -> None:
        balance = await async_client.credit_entitlements.balances.list_grants(
            customer_id="customer_id",
            credit_entitlement_id="credit_entitlement_id",
        )
        assert_matches_type(AsyncDefaultPageNumberPagination[BalanceListGrantsResponse], balance, path=["response"])

    @parametrize
    async def test_method_list_grants_with_all_params(self, async_client: AsyncDodoPayments) -> None:
        balance = await async_client.credit_entitlements.balances.list_grants(
            customer_id="customer_id",
            credit_entitlement_id="credit_entitlement_id",
            page_number=0,
            page_size=0,
            status="active",
        )
        assert_matches_type(AsyncDefaultPageNumberPagination[BalanceListGrantsResponse], balance, path=["response"])

    @parametrize
    async def test_raw_response_list_grants(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.credit_entitlements.balances.with_raw_response.list_grants(
            customer_id="customer_id",
            credit_entitlement_id="credit_entitlement_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        balance = await response.parse()
        assert_matches_type(AsyncDefaultPageNumberPagination[BalanceListGrantsResponse], balance, path=["response"])

    @parametrize
    async def test_streaming_response_list_grants(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.credit_entitlements.balances.with_streaming_response.list_grants(
            customer_id="customer_id",
            credit_entitlement_id="credit_entitlement_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            balance = await response.parse()
            assert_matches_type(AsyncDefaultPageNumberPagination[BalanceListGrantsResponse], balance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_grants(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `credit_entitlement_id` but received ''"):
            await async_client.credit_entitlements.balances.with_raw_response.list_grants(
                customer_id="customer_id",
                credit_entitlement_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.credit_entitlements.balances.with_raw_response.list_grants(
                customer_id="",
                credit_entitlement_id="credit_entitlement_id",
            )

    @parametrize
    async def test_method_list_ledger(self, async_client: AsyncDodoPayments) -> None:
        balance = await async_client.credit_entitlements.balances.list_ledger(
            customer_id="customer_id",
            credit_entitlement_id="credit_entitlement_id",
        )
        assert_matches_type(AsyncDefaultPageNumberPagination[CreditLedgerEntry], balance, path=["response"])

    @parametrize
    async def test_method_list_ledger_with_all_params(self, async_client: AsyncDodoPayments) -> None:
        balance = await async_client.credit_entitlements.balances.list_ledger(
            customer_id="customer_id",
            credit_entitlement_id="credit_entitlement_id",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            page_number=0,
            page_size=0,
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            transaction_type="transaction_type",
        )
        assert_matches_type(AsyncDefaultPageNumberPagination[CreditLedgerEntry], balance, path=["response"])

    @parametrize
    async def test_raw_response_list_ledger(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.credit_entitlements.balances.with_raw_response.list_ledger(
            customer_id="customer_id",
            credit_entitlement_id="credit_entitlement_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        balance = await response.parse()
        assert_matches_type(AsyncDefaultPageNumberPagination[CreditLedgerEntry], balance, path=["response"])

    @parametrize
    async def test_streaming_response_list_ledger(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.credit_entitlements.balances.with_streaming_response.list_ledger(
            customer_id="customer_id",
            credit_entitlement_id="credit_entitlement_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            balance = await response.parse()
            assert_matches_type(AsyncDefaultPageNumberPagination[CreditLedgerEntry], balance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_ledger(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `credit_entitlement_id` but received ''"):
            await async_client.credit_entitlements.balances.with_raw_response.list_ledger(
                customer_id="customer_id",
                credit_entitlement_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.credit_entitlements.balances.with_raw_response.list_ledger(
                customer_id="",
                credit_entitlement_id="credit_entitlement_id",
            )
