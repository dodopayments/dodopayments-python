# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from dodopayments import DodoPayments, AsyncDodoPayments
from dodopayments.types import CustomerPortalSession

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCustomerPortal:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: DodoPayments) -> None:
        customer_portal = client.customers.customer_portal.create(
            customer_id="customer_id",
        )
        assert_matches_type(CustomerPortalSession, customer_portal, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: DodoPayments) -> None:
        customer_portal = client.customers.customer_portal.create(
            customer_id="customer_id",
            send_email=True,
        )
        assert_matches_type(CustomerPortalSession, customer_portal, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: DodoPayments) -> None:
        response = client.customers.customer_portal.with_raw_response.create(
            customer_id="customer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_portal = response.parse()
        assert_matches_type(CustomerPortalSession, customer_portal, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: DodoPayments) -> None:
        with client.customers.customer_portal.with_streaming_response.create(
            customer_id="customer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer_portal = response.parse()
            assert_matches_type(CustomerPortalSession, customer_portal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.customers.customer_portal.with_raw_response.create(
                customer_id="",
            )


class TestAsyncCustomerPortal:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncDodoPayments) -> None:
        customer_portal = await async_client.customers.customer_portal.create(
            customer_id="customer_id",
        )
        assert_matches_type(CustomerPortalSession, customer_portal, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDodoPayments) -> None:
        customer_portal = await async_client.customers.customer_portal.create(
            customer_id="customer_id",
            send_email=True,
        )
        assert_matches_type(CustomerPortalSession, customer_portal, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.customers.customer_portal.with_raw_response.create(
            customer_id="customer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_portal = await response.parse()
        assert_matches_type(CustomerPortalSession, customer_portal, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.customers.customer_portal.with_streaming_response.create(
            customer_id="customer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer_portal = await response.parse()
            assert_matches_type(CustomerPortalSession, customer_portal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.customers.customer_portal.with_raw_response.create(
                customer_id="",
            )
