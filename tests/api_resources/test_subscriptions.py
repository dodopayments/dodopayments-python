# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from dodopayments import DodoPayments, AsyncDodoPayments
from dodopayments.types import (
    Subscription,
    SubscriptionChargeResponse,
    SubscriptionCreateResponse,
)
from dodopayments._utils import parse_datetime
from dodopayments.pagination import SyncDefaultPageNumberPagination, AsyncDefaultPageNumberPagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSubscriptions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: DodoPayments) -> None:
        subscription = client.subscriptions.create(
            billing={
                "city": "city",
                "country": "AF",
                "state": "state",
                "street": "street",
                "zipcode": "zipcode",
            },
            customer={"customer_id": "customer_id"},
            product_id="product_id",
            quantity=0,
        )
        assert_matches_type(SubscriptionCreateResponse, subscription, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: DodoPayments) -> None:
        subscription = client.subscriptions.create(
            billing={
                "city": "city",
                "country": "AF",
                "state": "state",
                "street": "street",
                "zipcode": "zipcode",
            },
            customer={"customer_id": "customer_id"},
            product_id="product_id",
            quantity=0,
            allowed_payment_method_types=["credit"],
            discount_code="discount_code",
            metadata={"foo": "string"},
            on_demand={
                "mandate_only": True,
                "product_price": 0,
            },
            payment_link=True,
            return_url="return_url",
            tax_id="tax_id",
            trial_period_days=0,
        )
        assert_matches_type(SubscriptionCreateResponse, subscription, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: DodoPayments) -> None:
        response = client.subscriptions.with_raw_response.create(
            billing={
                "city": "city",
                "country": "AF",
                "state": "state",
                "street": "street",
                "zipcode": "zipcode",
            },
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
        with client.subscriptions.with_streaming_response.create(
            billing={
                "city": "city",
                "country": "AF",
                "state": "state",
                "street": "street",
                "zipcode": "zipcode",
            },
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
            metadata={"foo": "string"},
            status="pending",
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
        assert_matches_type(SyncDefaultPageNumberPagination[Subscription], subscription, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: DodoPayments) -> None:
        subscription = client.subscriptions.list(
            created_at_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            customer_id="customer_id",
            page_number=0,
            page_size=0,
            status="pending",
        )
        assert_matches_type(SyncDefaultPageNumberPagination[Subscription], subscription, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: DodoPayments) -> None:
        response = client.subscriptions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SyncDefaultPageNumberPagination[Subscription], subscription, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: DodoPayments) -> None:
        with client.subscriptions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(SyncDefaultPageNumberPagination[Subscription], subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_charge(self, client: DodoPayments) -> None:
        subscription = client.subscriptions.charge(
            subscription_id="subscription_id",
            product_price=0,
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


class TestAsyncSubscriptions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncDodoPayments) -> None:
        subscription = await async_client.subscriptions.create(
            billing={
                "city": "city",
                "country": "AF",
                "state": "state",
                "street": "street",
                "zipcode": "zipcode",
            },
            customer={"customer_id": "customer_id"},
            product_id="product_id",
            quantity=0,
        )
        assert_matches_type(SubscriptionCreateResponse, subscription, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDodoPayments) -> None:
        subscription = await async_client.subscriptions.create(
            billing={
                "city": "city",
                "country": "AF",
                "state": "state",
                "street": "street",
                "zipcode": "zipcode",
            },
            customer={"customer_id": "customer_id"},
            product_id="product_id",
            quantity=0,
            allowed_payment_method_types=["credit"],
            discount_code="discount_code",
            metadata={"foo": "string"},
            on_demand={
                "mandate_only": True,
                "product_price": 0,
            },
            payment_link=True,
            return_url="return_url",
            tax_id="tax_id",
            trial_period_days=0,
        )
        assert_matches_type(SubscriptionCreateResponse, subscription, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.subscriptions.with_raw_response.create(
            billing={
                "city": "city",
                "country": "AF",
                "state": "state",
                "street": "street",
                "zipcode": "zipcode",
            },
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
        async with async_client.subscriptions.with_streaming_response.create(
            billing={
                "city": "city",
                "country": "AF",
                "state": "state",
                "street": "street",
                "zipcode": "zipcode",
            },
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
            metadata={"foo": "string"},
            status="pending",
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
        assert_matches_type(AsyncDefaultPageNumberPagination[Subscription], subscription, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDodoPayments) -> None:
        subscription = await async_client.subscriptions.list(
            created_at_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            customer_id="customer_id",
            page_number=0,
            page_size=0,
            status="pending",
        )
        assert_matches_type(AsyncDefaultPageNumberPagination[Subscription], subscription, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.subscriptions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(AsyncDefaultPageNumberPagination[Subscription], subscription, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.subscriptions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(AsyncDefaultPageNumberPagination[Subscription], subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_charge(self, async_client: AsyncDodoPayments) -> None:
        subscription = await async_client.subscriptions.charge(
            subscription_id="subscription_id",
            product_price=0,
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
