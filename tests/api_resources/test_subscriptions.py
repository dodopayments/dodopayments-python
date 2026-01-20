# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from dodopayments import DodoPayments, AsyncDodoPayments
from dodopayments.types import (
    Subscription,
    SubscriptionListResponse,
    SubscriptionChargeResponse,
    SubscriptionCreateResponse,
    SubscriptionPreviewChangePlanResponse,
    SubscriptionUpdatePaymentMethodResponse,
    SubscriptionRetrieveUsageHistoryResponse,
)
from dodopayments._utils import parse_datetime
from dodopayments.pagination import SyncDefaultPageNumberPagination, AsyncDefaultPageNumberPagination

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSubscriptions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: DodoPayments) -> None:
        with pytest.warns(DeprecationWarning):
            subscription = client.subscriptions.create(
                billing={"country": "AF"},
                customer={"customer_id": "customer_id"},
                product_id="product_id",
                quantity=0,
            )

        assert_matches_type(SubscriptionCreateResponse, subscription, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: DodoPayments) -> None:
        with pytest.warns(DeprecationWarning):
            subscription = client.subscriptions.create(
                billing={
                    "country": "AF",
                    "city": "city",
                    "state": "state",
                    "street": "street",
                    "zipcode": "zipcode",
                },
                customer={"customer_id": "customer_id"},
                product_id="product_id",
                quantity=0,
                addons=[
                    {
                        "addon_id": "addon_id",
                        "quantity": 0,
                    }
                ],
                allowed_payment_method_types=["credit"],
                billing_currency="AED",
                discount_code="discount_code",
                force_3ds=True,
                metadata={"foo": "string"},
                on_demand={
                    "mandate_only": True,
                    "adaptive_currency_fees_inclusive": True,
                    "product_currency": "AED",
                    "product_description": "product_description",
                    "product_price": 0,
                },
                one_time_product_cart=[
                    {
                        "product_id": "product_id",
                        "quantity": 0,
                        "amount": 0,
                    }
                ],
                payment_link=True,
                payment_method_id="payment_method_id",
                redirect_immediately=True,
                return_url="return_url",
                short_link=True,
                show_saved_payment_methods=True,
                tax_id="tax_id",
                trial_period_days=0,
            )

        assert_matches_type(SubscriptionCreateResponse, subscription, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: DodoPayments) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.subscriptions.with_raw_response.create(
                billing={"country": "AF"},
                customer={"customer_id": "customer_id"},
                product_id="product_id",
                quantity=0,
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionCreateResponse, subscription, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: DodoPayments) -> None:
        with pytest.warns(DeprecationWarning):
            with client.subscriptions.with_streaming_response.create(
                billing={"country": "AF"},
                customer={"customer_id": "customer_id"},
                product_id="product_id",
                quantity=0,
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                subscription = response.parse()
                assert_matches_type(SubscriptionCreateResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: DodoPayments) -> None:
        subscription = client.subscriptions.retrieve(
            "subscription_id",
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: DodoPayments) -> None:
        response = client.subscriptions.with_raw_response.retrieve(
            "subscription_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: DodoPayments) -> None:
        with client.subscriptions.with_streaming_response.retrieve(
            "subscription_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(Subscription, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            client.subscriptions.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: DodoPayments) -> None:
        subscription = client.subscriptions.update(
            subscription_id="subscription_id",
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: DodoPayments) -> None:
        subscription = client.subscriptions.update(
            subscription_id="subscription_id",
            billing={
                "country": "AF",
                "city": "city",
                "state": "state",
                "street": "street",
                "zipcode": "zipcode",
            },
            cancel_at_next_billing_date=True,
            customer_name="customer_name",
            disable_on_demand={"next_billing_date": parse_datetime("2019-12-27T18:11:19.117Z")},
            metadata={"foo": "string"},
            next_billing_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="pending",
            tax_id="tax_id",
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: DodoPayments) -> None:
        response = client.subscriptions.with_raw_response.update(
            subscription_id="subscription_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: DodoPayments) -> None:
        with client.subscriptions.with_streaming_response.update(
            subscription_id="subscription_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(Subscription, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            client.subscriptions.with_raw_response.update(
                subscription_id="",
            )

    @parametrize
    def test_method_list(self, client: DodoPayments) -> None:
        subscription = client.subscriptions.list()
        assert_matches_type(SyncDefaultPageNumberPagination[SubscriptionListResponse], subscription, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: DodoPayments) -> None:
        subscription = client.subscriptions.list(
            brand_id="brand_id",
            created_at_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            customer_id="customer_id",
            page_number=0,
            page_size=0,
            status="pending",
        )
        assert_matches_type(SyncDefaultPageNumberPagination[SubscriptionListResponse], subscription, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: DodoPayments) -> None:
        response = client.subscriptions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SyncDefaultPageNumberPagination[SubscriptionListResponse], subscription, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: DodoPayments) -> None:
        with client.subscriptions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(
                SyncDefaultPageNumberPagination[SubscriptionListResponse], subscription, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_change_plan(self, client: DodoPayments) -> None:
        subscription = client.subscriptions.change_plan(
            subscription_id="subscription_id",
            product_id="product_id",
            proration_billing_mode="prorated_immediately",
            quantity=0,
        )
        assert subscription is None

    @parametrize
    def test_method_change_plan_with_all_params(self, client: DodoPayments) -> None:
        subscription = client.subscriptions.change_plan(
            subscription_id="subscription_id",
            product_id="product_id",
            proration_billing_mode="prorated_immediately",
            quantity=0,
            addons=[
                {
                    "addon_id": "addon_id",
                    "quantity": 0,
                }
            ],
            metadata={"foo": "string"},
        )
        assert subscription is None

    @parametrize
    def test_raw_response_change_plan(self, client: DodoPayments) -> None:
        response = client.subscriptions.with_raw_response.change_plan(
            subscription_id="subscription_id",
            product_id="product_id",
            proration_billing_mode="prorated_immediately",
            quantity=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert subscription is None

    @parametrize
    def test_streaming_response_change_plan(self, client: DodoPayments) -> None:
        with client.subscriptions.with_streaming_response.change_plan(
            subscription_id="subscription_id",
            product_id="product_id",
            proration_billing_mode="prorated_immediately",
            quantity=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert subscription is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_change_plan(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            client.subscriptions.with_raw_response.change_plan(
                subscription_id="",
                product_id="product_id",
                proration_billing_mode="prorated_immediately",
                quantity=0,
            )

    @parametrize
    def test_method_charge(self, client: DodoPayments) -> None:
        subscription = client.subscriptions.charge(
            subscription_id="subscription_id",
            product_price=0,
        )
        assert_matches_type(SubscriptionChargeResponse, subscription, path=["response"])

    @parametrize
    def test_method_charge_with_all_params(self, client: DodoPayments) -> None:
        subscription = client.subscriptions.charge(
            subscription_id="subscription_id",
            product_price=0,
            adaptive_currency_fees_inclusive=True,
            customer_balance_config={
                "allow_customer_credits_purchase": True,
                "allow_customer_credits_usage": True,
            },
            metadata={"foo": "string"},
            product_currency="AED",
            product_description="product_description",
        )
        assert_matches_type(SubscriptionChargeResponse, subscription, path=["response"])

    @parametrize
    def test_raw_response_charge(self, client: DodoPayments) -> None:
        response = client.subscriptions.with_raw_response.charge(
            subscription_id="subscription_id",
            product_price=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionChargeResponse, subscription, path=["response"])

    @parametrize
    def test_streaming_response_charge(self, client: DodoPayments) -> None:
        with client.subscriptions.with_streaming_response.charge(
            subscription_id="subscription_id",
            product_price=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(SubscriptionChargeResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_charge(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            client.subscriptions.with_raw_response.charge(
                subscription_id="",
                product_price=0,
            )

    @parametrize
    def test_method_preview_change_plan(self, client: DodoPayments) -> None:
        subscription = client.subscriptions.preview_change_plan(
            subscription_id="subscription_id",
            product_id="product_id",
            proration_billing_mode="prorated_immediately",
            quantity=0,
        )
        assert_matches_type(SubscriptionPreviewChangePlanResponse, subscription, path=["response"])

    @parametrize
    def test_method_preview_change_plan_with_all_params(self, client: DodoPayments) -> None:
        subscription = client.subscriptions.preview_change_plan(
            subscription_id="subscription_id",
            product_id="product_id",
            proration_billing_mode="prorated_immediately",
            quantity=0,
            addons=[
                {
                    "addon_id": "addon_id",
                    "quantity": 0,
                }
            ],
            metadata={"foo": "string"},
        )
        assert_matches_type(SubscriptionPreviewChangePlanResponse, subscription, path=["response"])

    @parametrize
    def test_raw_response_preview_change_plan(self, client: DodoPayments) -> None:
        response = client.subscriptions.with_raw_response.preview_change_plan(
            subscription_id="subscription_id",
            product_id="product_id",
            proration_billing_mode="prorated_immediately",
            quantity=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionPreviewChangePlanResponse, subscription, path=["response"])

    @parametrize
    def test_streaming_response_preview_change_plan(self, client: DodoPayments) -> None:
        with client.subscriptions.with_streaming_response.preview_change_plan(
            subscription_id="subscription_id",
            product_id="product_id",
            proration_billing_mode="prorated_immediately",
            quantity=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(SubscriptionPreviewChangePlanResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_preview_change_plan(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            client.subscriptions.with_raw_response.preview_change_plan(
                subscription_id="",
                product_id="product_id",
                proration_billing_mode="prorated_immediately",
                quantity=0,
            )

    @parametrize
    def test_method_retrieve_usage_history(self, client: DodoPayments) -> None:
        subscription = client.subscriptions.retrieve_usage_history(
            subscription_id="subscription_id",
        )
        assert_matches_type(
            SyncDefaultPageNumberPagination[SubscriptionRetrieveUsageHistoryResponse], subscription, path=["response"]
        )

    @parametrize
    def test_method_retrieve_usage_history_with_all_params(self, client: DodoPayments) -> None:
        subscription = client.subscriptions.retrieve_usage_history(
            subscription_id="subscription_id",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            meter_id="meter_id",
            page_number=0,
            page_size=0,
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(
            SyncDefaultPageNumberPagination[SubscriptionRetrieveUsageHistoryResponse], subscription, path=["response"]
        )

    @parametrize
    def test_raw_response_retrieve_usage_history(self, client: DodoPayments) -> None:
        response = client.subscriptions.with_raw_response.retrieve_usage_history(
            subscription_id="subscription_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(
            SyncDefaultPageNumberPagination[SubscriptionRetrieveUsageHistoryResponse], subscription, path=["response"]
        )

    @parametrize
    def test_streaming_response_retrieve_usage_history(self, client: DodoPayments) -> None:
        with client.subscriptions.with_streaming_response.retrieve_usage_history(
            subscription_id="subscription_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(
                SyncDefaultPageNumberPagination[SubscriptionRetrieveUsageHistoryResponse],
                subscription,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve_usage_history(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            client.subscriptions.with_raw_response.retrieve_usage_history(
                subscription_id="",
            )

    @parametrize
    def test_method_update_payment_method_overload_1(self, client: DodoPayments) -> None:
        subscription = client.subscriptions.update_payment_method(
            subscription_id="subscription_id",
            type="new",
        )
        assert_matches_type(SubscriptionUpdatePaymentMethodResponse, subscription, path=["response"])

    @parametrize
    def test_method_update_payment_method_with_all_params_overload_1(self, client: DodoPayments) -> None:
        subscription = client.subscriptions.update_payment_method(
            subscription_id="subscription_id",
            type="new",
            return_url="return_url",
        )
        assert_matches_type(SubscriptionUpdatePaymentMethodResponse, subscription, path=["response"])

    @parametrize
    def test_raw_response_update_payment_method_overload_1(self, client: DodoPayments) -> None:
        response = client.subscriptions.with_raw_response.update_payment_method(
            subscription_id="subscription_id",
            type="new",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionUpdatePaymentMethodResponse, subscription, path=["response"])

    @parametrize
    def test_streaming_response_update_payment_method_overload_1(self, client: DodoPayments) -> None:
        with client.subscriptions.with_streaming_response.update_payment_method(
            subscription_id="subscription_id",
            type="new",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(SubscriptionUpdatePaymentMethodResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_payment_method_overload_1(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            client.subscriptions.with_raw_response.update_payment_method(
                subscription_id="",
                type="new",
            )

    @parametrize
    def test_method_update_payment_method_overload_2(self, client: DodoPayments) -> None:
        subscription = client.subscriptions.update_payment_method(
            subscription_id="subscription_id",
            payment_method_id="payment_method_id",
            type="existing",
        )
        assert_matches_type(SubscriptionUpdatePaymentMethodResponse, subscription, path=["response"])

    @parametrize
    def test_raw_response_update_payment_method_overload_2(self, client: DodoPayments) -> None:
        response = client.subscriptions.with_raw_response.update_payment_method(
            subscription_id="subscription_id",
            payment_method_id="payment_method_id",
            type="existing",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionUpdatePaymentMethodResponse, subscription, path=["response"])

    @parametrize
    def test_streaming_response_update_payment_method_overload_2(self, client: DodoPayments) -> None:
        with client.subscriptions.with_streaming_response.update_payment_method(
            subscription_id="subscription_id",
            payment_method_id="payment_method_id",
            type="existing",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(SubscriptionUpdatePaymentMethodResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_payment_method_overload_2(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            client.subscriptions.with_raw_response.update_payment_method(
                subscription_id="",
                payment_method_id="payment_method_id",
                type="existing",
            )


class TestAsyncSubscriptions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncDodoPayments) -> None:
        with pytest.warns(DeprecationWarning):
            subscription = await async_client.subscriptions.create(
                billing={"country": "AF"},
                customer={"customer_id": "customer_id"},
                product_id="product_id",
                quantity=0,
            )

        assert_matches_type(SubscriptionCreateResponse, subscription, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDodoPayments) -> None:
        with pytest.warns(DeprecationWarning):
            subscription = await async_client.subscriptions.create(
                billing={
                    "country": "AF",
                    "city": "city",
                    "state": "state",
                    "street": "street",
                    "zipcode": "zipcode",
                },
                customer={"customer_id": "customer_id"},
                product_id="product_id",
                quantity=0,
                addons=[
                    {
                        "addon_id": "addon_id",
                        "quantity": 0,
                    }
                ],
                allowed_payment_method_types=["credit"],
                billing_currency="AED",
                discount_code="discount_code",
                force_3ds=True,
                metadata={"foo": "string"},
                on_demand={
                    "mandate_only": True,
                    "adaptive_currency_fees_inclusive": True,
                    "product_currency": "AED",
                    "product_description": "product_description",
                    "product_price": 0,
                },
                one_time_product_cart=[
                    {
                        "product_id": "product_id",
                        "quantity": 0,
                        "amount": 0,
                    }
                ],
                payment_link=True,
                payment_method_id="payment_method_id",
                redirect_immediately=True,
                return_url="return_url",
                short_link=True,
                show_saved_payment_methods=True,
                tax_id="tax_id",
                trial_period_days=0,
            )

        assert_matches_type(SubscriptionCreateResponse, subscription, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDodoPayments) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.subscriptions.with_raw_response.create(
                billing={"country": "AF"},
                customer={"customer_id": "customer_id"},
                product_id="product_id",
                quantity=0,
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(SubscriptionCreateResponse, subscription, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDodoPayments) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.subscriptions.with_streaming_response.create(
                billing={"country": "AF"},
                customer={"customer_id": "customer_id"},
                product_id="product_id",
                quantity=0,
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                subscription = await response.parse()
                assert_matches_type(SubscriptionCreateResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDodoPayments) -> None:
        subscription = await async_client.subscriptions.retrieve(
            "subscription_id",
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.subscriptions.with_raw_response.retrieve(
            "subscription_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.subscriptions.with_streaming_response.retrieve(
            "subscription_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(Subscription, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            await async_client.subscriptions.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncDodoPayments) -> None:
        subscription = await async_client.subscriptions.update(
            subscription_id="subscription_id",
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncDodoPayments) -> None:
        subscription = await async_client.subscriptions.update(
            subscription_id="subscription_id",
            billing={
                "country": "AF",
                "city": "city",
                "state": "state",
                "street": "street",
                "zipcode": "zipcode",
            },
            cancel_at_next_billing_date=True,
            customer_name="customer_name",
            disable_on_demand={"next_billing_date": parse_datetime("2019-12-27T18:11:19.117Z")},
            metadata={"foo": "string"},
            next_billing_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="pending",
            tax_id="tax_id",
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.subscriptions.with_raw_response.update(
            subscription_id="subscription_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(Subscription, subscription, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.subscriptions.with_streaming_response.update(
            subscription_id="subscription_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(Subscription, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            await async_client.subscriptions.with_raw_response.update(
                subscription_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncDodoPayments) -> None:
        subscription = await async_client.subscriptions.list()
        assert_matches_type(AsyncDefaultPageNumberPagination[SubscriptionListResponse], subscription, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDodoPayments) -> None:
        subscription = await async_client.subscriptions.list(
            brand_id="brand_id",
            created_at_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            customer_id="customer_id",
            page_number=0,
            page_size=0,
            status="pending",
        )
        assert_matches_type(AsyncDefaultPageNumberPagination[SubscriptionListResponse], subscription, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.subscriptions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(AsyncDefaultPageNumberPagination[SubscriptionListResponse], subscription, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.subscriptions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(
                AsyncDefaultPageNumberPagination[SubscriptionListResponse], subscription, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_change_plan(self, async_client: AsyncDodoPayments) -> None:
        subscription = await async_client.subscriptions.change_plan(
            subscription_id="subscription_id",
            product_id="product_id",
            proration_billing_mode="prorated_immediately",
            quantity=0,
        )
        assert subscription is None

    @parametrize
    async def test_method_change_plan_with_all_params(self, async_client: AsyncDodoPayments) -> None:
        subscription = await async_client.subscriptions.change_plan(
            subscription_id="subscription_id",
            product_id="product_id",
            proration_billing_mode="prorated_immediately",
            quantity=0,
            addons=[
                {
                    "addon_id": "addon_id",
                    "quantity": 0,
                }
            ],
            metadata={"foo": "string"},
        )
        assert subscription is None

    @parametrize
    async def test_raw_response_change_plan(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.subscriptions.with_raw_response.change_plan(
            subscription_id="subscription_id",
            product_id="product_id",
            proration_billing_mode="prorated_immediately",
            quantity=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert subscription is None

    @parametrize
    async def test_streaming_response_change_plan(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.subscriptions.with_streaming_response.change_plan(
            subscription_id="subscription_id",
            product_id="product_id",
            proration_billing_mode="prorated_immediately",
            quantity=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert subscription is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_change_plan(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            await async_client.subscriptions.with_raw_response.change_plan(
                subscription_id="",
                product_id="product_id",
                proration_billing_mode="prorated_immediately",
                quantity=0,
            )

    @parametrize
    async def test_method_charge(self, async_client: AsyncDodoPayments) -> None:
        subscription = await async_client.subscriptions.charge(
            subscription_id="subscription_id",
            product_price=0,
        )
        assert_matches_type(SubscriptionChargeResponse, subscription, path=["response"])

    @parametrize
    async def test_method_charge_with_all_params(self, async_client: AsyncDodoPayments) -> None:
        subscription = await async_client.subscriptions.charge(
            subscription_id="subscription_id",
            product_price=0,
            adaptive_currency_fees_inclusive=True,
            customer_balance_config={
                "allow_customer_credits_purchase": True,
                "allow_customer_credits_usage": True,
            },
            metadata={"foo": "string"},
            product_currency="AED",
            product_description="product_description",
        )
        assert_matches_type(SubscriptionChargeResponse, subscription, path=["response"])

    @parametrize
    async def test_raw_response_charge(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.subscriptions.with_raw_response.charge(
            subscription_id="subscription_id",
            product_price=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(SubscriptionChargeResponse, subscription, path=["response"])

    @parametrize
    async def test_streaming_response_charge(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.subscriptions.with_streaming_response.charge(
            subscription_id="subscription_id",
            product_price=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(SubscriptionChargeResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_charge(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            await async_client.subscriptions.with_raw_response.charge(
                subscription_id="",
                product_price=0,
            )

    @parametrize
    async def test_method_preview_change_plan(self, async_client: AsyncDodoPayments) -> None:
        subscription = await async_client.subscriptions.preview_change_plan(
            subscription_id="subscription_id",
            product_id="product_id",
            proration_billing_mode="prorated_immediately",
            quantity=0,
        )
        assert_matches_type(SubscriptionPreviewChangePlanResponse, subscription, path=["response"])

    @parametrize
    async def test_method_preview_change_plan_with_all_params(self, async_client: AsyncDodoPayments) -> None:
        subscription = await async_client.subscriptions.preview_change_plan(
            subscription_id="subscription_id",
            product_id="product_id",
            proration_billing_mode="prorated_immediately",
            quantity=0,
            addons=[
                {
                    "addon_id": "addon_id",
                    "quantity": 0,
                }
            ],
            metadata={"foo": "string"},
        )
        assert_matches_type(SubscriptionPreviewChangePlanResponse, subscription, path=["response"])

    @parametrize
    async def test_raw_response_preview_change_plan(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.subscriptions.with_raw_response.preview_change_plan(
            subscription_id="subscription_id",
            product_id="product_id",
            proration_billing_mode="prorated_immediately",
            quantity=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(SubscriptionPreviewChangePlanResponse, subscription, path=["response"])

    @parametrize
    async def test_streaming_response_preview_change_plan(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.subscriptions.with_streaming_response.preview_change_plan(
            subscription_id="subscription_id",
            product_id="product_id",
            proration_billing_mode="prorated_immediately",
            quantity=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(SubscriptionPreviewChangePlanResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_preview_change_plan(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            await async_client.subscriptions.with_raw_response.preview_change_plan(
                subscription_id="",
                product_id="product_id",
                proration_billing_mode="prorated_immediately",
                quantity=0,
            )

    @parametrize
    async def test_method_retrieve_usage_history(self, async_client: AsyncDodoPayments) -> None:
        subscription = await async_client.subscriptions.retrieve_usage_history(
            subscription_id="subscription_id",
        )
        assert_matches_type(
            AsyncDefaultPageNumberPagination[SubscriptionRetrieveUsageHistoryResponse], subscription, path=["response"]
        )

    @parametrize
    async def test_method_retrieve_usage_history_with_all_params(self, async_client: AsyncDodoPayments) -> None:
        subscription = await async_client.subscriptions.retrieve_usage_history(
            subscription_id="subscription_id",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            meter_id="meter_id",
            page_number=0,
            page_size=0,
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(
            AsyncDefaultPageNumberPagination[SubscriptionRetrieveUsageHistoryResponse], subscription, path=["response"]
        )

    @parametrize
    async def test_raw_response_retrieve_usage_history(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.subscriptions.with_raw_response.retrieve_usage_history(
            subscription_id="subscription_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(
            AsyncDefaultPageNumberPagination[SubscriptionRetrieveUsageHistoryResponse], subscription, path=["response"]
        )

    @parametrize
    async def test_streaming_response_retrieve_usage_history(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.subscriptions.with_streaming_response.retrieve_usage_history(
            subscription_id="subscription_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(
                AsyncDefaultPageNumberPagination[SubscriptionRetrieveUsageHistoryResponse],
                subscription,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve_usage_history(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            await async_client.subscriptions.with_raw_response.retrieve_usage_history(
                subscription_id="",
            )

    @parametrize
    async def test_method_update_payment_method_overload_1(self, async_client: AsyncDodoPayments) -> None:
        subscription = await async_client.subscriptions.update_payment_method(
            subscription_id="subscription_id",
            type="new",
        )
        assert_matches_type(SubscriptionUpdatePaymentMethodResponse, subscription, path=["response"])

    @parametrize
    async def test_method_update_payment_method_with_all_params_overload_1(
        self, async_client: AsyncDodoPayments
    ) -> None:
        subscription = await async_client.subscriptions.update_payment_method(
            subscription_id="subscription_id",
            type="new",
            return_url="return_url",
        )
        assert_matches_type(SubscriptionUpdatePaymentMethodResponse, subscription, path=["response"])

    @parametrize
    async def test_raw_response_update_payment_method_overload_1(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.subscriptions.with_raw_response.update_payment_method(
            subscription_id="subscription_id",
            type="new",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(SubscriptionUpdatePaymentMethodResponse, subscription, path=["response"])

    @parametrize
    async def test_streaming_response_update_payment_method_overload_1(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.subscriptions.with_streaming_response.update_payment_method(
            subscription_id="subscription_id",
            type="new",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(SubscriptionUpdatePaymentMethodResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_payment_method_overload_1(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            await async_client.subscriptions.with_raw_response.update_payment_method(
                subscription_id="",
                type="new",
            )

    @parametrize
    async def test_method_update_payment_method_overload_2(self, async_client: AsyncDodoPayments) -> None:
        subscription = await async_client.subscriptions.update_payment_method(
            subscription_id="subscription_id",
            payment_method_id="payment_method_id",
            type="existing",
        )
        assert_matches_type(SubscriptionUpdatePaymentMethodResponse, subscription, path=["response"])

    @parametrize
    async def test_raw_response_update_payment_method_overload_2(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.subscriptions.with_raw_response.update_payment_method(
            subscription_id="subscription_id",
            payment_method_id="payment_method_id",
            type="existing",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(SubscriptionUpdatePaymentMethodResponse, subscription, path=["response"])

    @parametrize
    async def test_streaming_response_update_payment_method_overload_2(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.subscriptions.with_streaming_response.update_payment_method(
            subscription_id="subscription_id",
            payment_method_id="payment_method_id",
            type="existing",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(SubscriptionUpdatePaymentMethodResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_payment_method_overload_2(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            await async_client.subscriptions.with_raw_response.update_payment_method(
                subscription_id="",
                payment_method_id="payment_method_id",
                type="existing",
            )
