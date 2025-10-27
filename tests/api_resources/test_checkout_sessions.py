# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from dodopayments import DodoPayments, AsyncDodoPayments
from dodopayments.types import (
    CheckoutSessionStatus,
    CheckoutSessionResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCheckoutSessions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: DodoPayments) -> None:
        checkout_session = client.checkout_sessions.create(
            product_cart=[
                {
                    "product_id": "product_id",
                    "quantity": 0,
                }
            ],
        )
        assert_matches_type(CheckoutSessionResponse, checkout_session, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: DodoPayments) -> None:
        checkout_session = client.checkout_sessions.create(
            product_cart=[
                {
                    "product_id": "product_id",
                    "quantity": 0,
                    "addons": [
                        {
                            "addon_id": "addon_id",
                            "quantity": 0,
                        }
                    ],
                    "amount": 0,
                }
            ],
            allowed_payment_method_types=["credit"],
            billing_address={
                "country": "AF",
                "city": "city",
                "state": "state",
                "street": "street",
                "zipcode": "zipcode",
            },
            billing_currency="AED",
            confirm=True,
            customer={"customer_id": "customer_id"},
            customization={
                "force_language": "force_language",
                "show_on_demand_tag": True,
                "show_order_details": True,
                "theme": "dark",
            },
            discount_code="discount_code",
            feature_flags={
                "allow_currency_selection": True,
                "allow_discount_code": True,
                "allow_phone_number_collection": True,
                "allow_tax_id": True,
                "always_create_new_customer": True,
            },
            force_3ds=True,
            metadata={"foo": "string"},
            return_url="return_url",
            show_saved_payment_methods=True,
            subscription_data={
                "on_demand": {
                    "mandate_only": True,
                    "adaptive_currency_fees_inclusive": True,
                    "product_currency": "AED",
                    "product_description": "product_description",
                    "product_price": 0,
                },
                "trial_period_days": 0,
            },
        )
        assert_matches_type(CheckoutSessionResponse, checkout_session, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: DodoPayments) -> None:
        response = client.checkout_sessions.with_raw_response.create(
            product_cart=[
                {
                    "product_id": "product_id",
                    "quantity": 0,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        checkout_session = response.parse()
        assert_matches_type(CheckoutSessionResponse, checkout_session, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: DodoPayments) -> None:
        with client.checkout_sessions.with_streaming_response.create(
            product_cart=[
                {
                    "product_id": "product_id",
                    "quantity": 0,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            checkout_session = response.parse()
            assert_matches_type(CheckoutSessionResponse, checkout_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: DodoPayments) -> None:
        checkout_session = client.checkout_sessions.retrieve(
            "id",
        )
        assert_matches_type(CheckoutSessionStatus, checkout_session, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: DodoPayments) -> None:
        response = client.checkout_sessions.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        checkout_session = response.parse()
        assert_matches_type(CheckoutSessionStatus, checkout_session, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: DodoPayments) -> None:
        with client.checkout_sessions.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            checkout_session = response.parse()
            assert_matches_type(CheckoutSessionStatus, checkout_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.checkout_sessions.with_raw_response.retrieve(
                "",
            )


class TestAsyncCheckoutSessions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncDodoPayments) -> None:
        checkout_session = await async_client.checkout_sessions.create(
            product_cart=[
                {
                    "product_id": "product_id",
                    "quantity": 0,
                }
            ],
        )
        assert_matches_type(CheckoutSessionResponse, checkout_session, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDodoPayments) -> None:
        checkout_session = await async_client.checkout_sessions.create(
            product_cart=[
                {
                    "product_id": "product_id",
                    "quantity": 0,
                    "addons": [
                        {
                            "addon_id": "addon_id",
                            "quantity": 0,
                        }
                    ],
                    "amount": 0,
                }
            ],
            allowed_payment_method_types=["credit"],
            billing_address={
                "country": "AF",
                "city": "city",
                "state": "state",
                "street": "street",
                "zipcode": "zipcode",
            },
            billing_currency="AED",
            confirm=True,
            customer={"customer_id": "customer_id"},
            customization={
                "force_language": "force_language",
                "show_on_demand_tag": True,
                "show_order_details": True,
                "theme": "dark",
            },
            discount_code="discount_code",
            feature_flags={
                "allow_currency_selection": True,
                "allow_discount_code": True,
                "allow_phone_number_collection": True,
                "allow_tax_id": True,
                "always_create_new_customer": True,
            },
            force_3ds=True,
            metadata={"foo": "string"},
            return_url="return_url",
            show_saved_payment_methods=True,
            subscription_data={
                "on_demand": {
                    "mandate_only": True,
                    "adaptive_currency_fees_inclusive": True,
                    "product_currency": "AED",
                    "product_description": "product_description",
                    "product_price": 0,
                },
                "trial_period_days": 0,
            },
        )
        assert_matches_type(CheckoutSessionResponse, checkout_session, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.checkout_sessions.with_raw_response.create(
            product_cart=[
                {
                    "product_id": "product_id",
                    "quantity": 0,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        checkout_session = await response.parse()
        assert_matches_type(CheckoutSessionResponse, checkout_session, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.checkout_sessions.with_streaming_response.create(
            product_cart=[
                {
                    "product_id": "product_id",
                    "quantity": 0,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            checkout_session = await response.parse()
            assert_matches_type(CheckoutSessionResponse, checkout_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDodoPayments) -> None:
        checkout_session = await async_client.checkout_sessions.retrieve(
            "id",
        )
        assert_matches_type(CheckoutSessionStatus, checkout_session, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.checkout_sessions.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        checkout_session = await response.parse()
        assert_matches_type(CheckoutSessionStatus, checkout_session, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.checkout_sessions.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            checkout_session = await response.parse()
            assert_matches_type(CheckoutSessionStatus, checkout_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.checkout_sessions.with_raw_response.retrieve(
                "",
            )
