# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from dodopayments import DodoPayments, AsyncDodoPayments
from dodopayments._utils import parse_datetime
from dodopayments.pagination import SyncDefaultPageNumberPagination, AsyncDefaultPageNumberPagination
from dodopayments.types.blocklist import (
    BlockedCustomer,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCustomers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_overload_1(self, client: DodoPayments) -> None:
        customer = client.blocklist.customers.create(
            customer_id="customer_id",
        )
        assert_matches_type(BlockedCustomer, customer, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: DodoPayments) -> None:
        customer = client.blocklist.customers.create(
            customer_id="customer_id",
            reason="reason",
            source="blocklist_page",
        )
        assert_matches_type(BlockedCustomer, customer, path=["response"])

    @parametrize
    def test_raw_response_create_overload_1(self, client: DodoPayments) -> None:
        response = client.blocklist.customers.with_raw_response.create(
            customer_id="customer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(BlockedCustomer, customer, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_1(self, client: DodoPayments) -> None:
        with client.blocklist.customers.with_streaming_response.create(
            customer_id="customer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(BlockedCustomer, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_2(self, client: DodoPayments) -> None:
        customer = client.blocklist.customers.create(
            email="email",
        )
        assert_matches_type(BlockedCustomer, customer, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: DodoPayments) -> None:
        customer = client.blocklist.customers.create(
            email="email",
            reason="reason",
            source="blocklist_page",
        )
        assert_matches_type(BlockedCustomer, customer, path=["response"])

    @parametrize
    def test_raw_response_create_overload_2(self, client: DodoPayments) -> None:
        response = client.blocklist.customers.with_raw_response.create(
            email="email",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(BlockedCustomer, customer, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_2(self, client: DodoPayments) -> None:
        with client.blocklist.customers.with_streaming_response.create(
            email="email",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(BlockedCustomer, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: DodoPayments) -> None:
        customer = client.blocklist.customers.retrieve(
            "entry_id",
        )
        assert_matches_type(BlockedCustomer, customer, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: DodoPayments) -> None:
        response = client.blocklist.customers.with_raw_response.retrieve(
            "entry_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(BlockedCustomer, customer, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: DodoPayments) -> None:
        with client.blocklist.customers.with_streaming_response.retrieve(
            "entry_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(BlockedCustomer, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entry_id` but received ''"):
            client.blocklist.customers.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: DodoPayments) -> None:
        customer = client.blocklist.customers.list()
        assert_matches_type(SyncDefaultPageNumberPagination[BlockedCustomer], customer, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: DodoPayments) -> None:
        customer = client.blocklist.customers.list(
            blocked_by_email="blocked_by_email",
            created_at_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            identifier="identifier",
            page_number=0,
            page_size=0,
        )
        assert_matches_type(SyncDefaultPageNumberPagination[BlockedCustomer], customer, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: DodoPayments) -> None:
        response = client.blocklist.customers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(SyncDefaultPageNumberPagination[BlockedCustomer], customer, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: DodoPayments) -> None:
        with client.blocklist.customers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(SyncDefaultPageNumberPagination[BlockedCustomer], customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: DodoPayments) -> None:
        customer = client.blocklist.customers.delete(
            "entry_id",
        )
        assert customer is None

    @parametrize
    def test_raw_response_delete(self, client: DodoPayments) -> None:
        response = client.blocklist.customers.with_raw_response.delete(
            "entry_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert customer is None

    @parametrize
    def test_streaming_response_delete(self, client: DodoPayments) -> None:
        with client.blocklist.customers.with_streaming_response.delete(
            "entry_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert customer is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entry_id` but received ''"):
            client.blocklist.customers.with_raw_response.delete(
                "",
            )


class TestAsyncCustomers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncDodoPayments) -> None:
        customer = await async_client.blocklist.customers.create(
            customer_id="customer_id",
        )
        assert_matches_type(BlockedCustomer, customer, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncDodoPayments) -> None:
        customer = await async_client.blocklist.customers.create(
            customer_id="customer_id",
            reason="reason",
            source="blocklist_page",
        )
        assert_matches_type(BlockedCustomer, customer, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.blocklist.customers.with_raw_response.create(
            customer_id="customer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert_matches_type(BlockedCustomer, customer, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.blocklist.customers.with_streaming_response.create(
            customer_id="customer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(BlockedCustomer, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncDodoPayments) -> None:
        customer = await async_client.blocklist.customers.create(
            email="email",
        )
        assert_matches_type(BlockedCustomer, customer, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncDodoPayments) -> None:
        customer = await async_client.blocklist.customers.create(
            email="email",
            reason="reason",
            source="blocklist_page",
        )
        assert_matches_type(BlockedCustomer, customer, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.blocklist.customers.with_raw_response.create(
            email="email",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert_matches_type(BlockedCustomer, customer, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.blocklist.customers.with_streaming_response.create(
            email="email",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(BlockedCustomer, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDodoPayments) -> None:
        customer = await async_client.blocklist.customers.retrieve(
            "entry_id",
        )
        assert_matches_type(BlockedCustomer, customer, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.blocklist.customers.with_raw_response.retrieve(
            "entry_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert_matches_type(BlockedCustomer, customer, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.blocklist.customers.with_streaming_response.retrieve(
            "entry_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(BlockedCustomer, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entry_id` but received ''"):
            await async_client.blocklist.customers.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncDodoPayments) -> None:
        customer = await async_client.blocklist.customers.list()
        assert_matches_type(AsyncDefaultPageNumberPagination[BlockedCustomer], customer, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDodoPayments) -> None:
        customer = await async_client.blocklist.customers.list(
            blocked_by_email="blocked_by_email",
            created_at_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            identifier="identifier",
            page_number=0,
            page_size=0,
        )
        assert_matches_type(AsyncDefaultPageNumberPagination[BlockedCustomer], customer, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.blocklist.customers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert_matches_type(AsyncDefaultPageNumberPagination[BlockedCustomer], customer, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.blocklist.customers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(AsyncDefaultPageNumberPagination[BlockedCustomer], customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncDodoPayments) -> None:
        customer = await async_client.blocklist.customers.delete(
            "entry_id",
        )
        assert customer is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.blocklist.customers.with_raw_response.delete(
            "entry_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert customer is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.blocklist.customers.with_streaming_response.delete(
            "entry_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert customer is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entry_id` but received ''"):
            await async_client.blocklist.customers.with_raw_response.delete(
                "",
            )
