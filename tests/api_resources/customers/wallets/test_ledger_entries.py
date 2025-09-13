# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from dodopayments import DodoPayments, AsyncDodoPayments
from dodopayments.pagination import SyncDefaultPageNumberPagination, AsyncDefaultPageNumberPagination
from dodopayments.types.customers import CustomerWallet
from dodopayments.types.customers.wallets import (
    CustomerWalletTransaction,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLedgerEntries:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: DodoPayments) -> None:
        ledger_entry = client.customers.wallets.ledger_entries.create(
            customer_id="customer_id",
            amount=0,
            currency="AED",
            entry_type="credit",
        )
        assert_matches_type(CustomerWallet, ledger_entry, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: DodoPayments) -> None:
        ledger_entry = client.customers.wallets.ledger_entries.create(
            customer_id="customer_id",
            amount=0,
            currency="AED",
            entry_type="credit",
            idempotency_key="idempotency_key",
            reason="reason",
        )
        assert_matches_type(CustomerWallet, ledger_entry, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: DodoPayments) -> None:
        response = client.customers.wallets.ledger_entries.with_raw_response.create(
            customer_id="customer_id",
            amount=0,
            currency="AED",
            entry_type="credit",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_entry = response.parse()
        assert_matches_type(CustomerWallet, ledger_entry, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: DodoPayments) -> None:
        with client.customers.wallets.ledger_entries.with_streaming_response.create(
            customer_id="customer_id",
            amount=0,
            currency="AED",
            entry_type="credit",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_entry = response.parse()
            assert_matches_type(CustomerWallet, ledger_entry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.customers.wallets.ledger_entries.with_raw_response.create(
                customer_id="",
                amount=0,
                currency="AED",
                entry_type="credit",
            )

    @parametrize
    def test_method_list(self, client: DodoPayments) -> None:
        ledger_entry = client.customers.wallets.ledger_entries.list(
            customer_id="customer_id",
        )
        assert_matches_type(SyncDefaultPageNumberPagination[CustomerWalletTransaction], ledger_entry, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: DodoPayments) -> None:
        ledger_entry = client.customers.wallets.ledger_entries.list(
            customer_id="customer_id",
            currency="AED",
            page_number=0,
            page_size=0,
        )
        assert_matches_type(SyncDefaultPageNumberPagination[CustomerWalletTransaction], ledger_entry, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: DodoPayments) -> None:
        response = client.customers.wallets.ledger_entries.with_raw_response.list(
            customer_id="customer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_entry = response.parse()
        assert_matches_type(SyncDefaultPageNumberPagination[CustomerWalletTransaction], ledger_entry, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: DodoPayments) -> None:
        with client.customers.wallets.ledger_entries.with_streaming_response.list(
            customer_id="customer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_entry = response.parse()
            assert_matches_type(
                SyncDefaultPageNumberPagination[CustomerWalletTransaction], ledger_entry, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.customers.wallets.ledger_entries.with_raw_response.list(
                customer_id="",
            )


class TestAsyncLedgerEntries:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncDodoPayments) -> None:
        ledger_entry = await async_client.customers.wallets.ledger_entries.create(
            customer_id="customer_id",
            amount=0,
            currency="AED",
            entry_type="credit",
        )
        assert_matches_type(CustomerWallet, ledger_entry, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDodoPayments) -> None:
        ledger_entry = await async_client.customers.wallets.ledger_entries.create(
            customer_id="customer_id",
            amount=0,
            currency="AED",
            entry_type="credit",
            idempotency_key="idempotency_key",
            reason="reason",
        )
        assert_matches_type(CustomerWallet, ledger_entry, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.customers.wallets.ledger_entries.with_raw_response.create(
            customer_id="customer_id",
            amount=0,
            currency="AED",
            entry_type="credit",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_entry = await response.parse()
        assert_matches_type(CustomerWallet, ledger_entry, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.customers.wallets.ledger_entries.with_streaming_response.create(
            customer_id="customer_id",
            amount=0,
            currency="AED",
            entry_type="credit",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_entry = await response.parse()
            assert_matches_type(CustomerWallet, ledger_entry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.customers.wallets.ledger_entries.with_raw_response.create(
                customer_id="",
                amount=0,
                currency="AED",
                entry_type="credit",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncDodoPayments) -> None:
        ledger_entry = await async_client.customers.wallets.ledger_entries.list(
            customer_id="customer_id",
        )
        assert_matches_type(
            AsyncDefaultPageNumberPagination[CustomerWalletTransaction], ledger_entry, path=["response"]
        )

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDodoPayments) -> None:
        ledger_entry = await async_client.customers.wallets.ledger_entries.list(
            customer_id="customer_id",
            currency="AED",
            page_number=0,
            page_size=0,
        )
        assert_matches_type(
            AsyncDefaultPageNumberPagination[CustomerWalletTransaction], ledger_entry, path=["response"]
        )

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.customers.wallets.ledger_entries.with_raw_response.list(
            customer_id="customer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_entry = await response.parse()
        assert_matches_type(
            AsyncDefaultPageNumberPagination[CustomerWalletTransaction], ledger_entry, path=["response"]
        )

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.customers.wallets.ledger_entries.with_streaming_response.list(
            customer_id="customer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_entry = await response.parse()
            assert_matches_type(
                AsyncDefaultPageNumberPagination[CustomerWalletTransaction], ledger_entry, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.customers.wallets.ledger_entries.with_raw_response.list(
                customer_id="",
            )
