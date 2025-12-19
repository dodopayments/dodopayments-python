# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from dodopayments import DodoPayments, AsyncDodoPayments
from dodopayments.types import (
    Payment,
    PaymentListResponse,
    PaymentCreateResponse,
    PaymentRetrieveLineItemsResponse,
)
from dodopayments._utils import parse_datetime
from dodopayments.pagination import SyncDefaultPageNumberPagination, AsyncDefaultPageNumberPagination

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPayments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: DodoPayments) -> None:
        with pytest.warns(DeprecationWarning):
            payment = client.payments.create(
                billing={"country": "AF"},
                customer={"customer_id": "customer_id"},
                product_cart=[
                    {
                        "product_id": "product_id",
                        "quantity": 0,
                    }
                ],
            )

        assert_matches_type(PaymentCreateResponse, payment, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: DodoPayments) -> None:
        with pytest.warns(DeprecationWarning):
            payment = client.payments.create(
                billing={
                    "country": "AF",
                    "city": "city",
                    "state": "state",
                    "street": "street",
                    "zipcode": "zipcode",
                },
                customer={"customer_id": "customer_id"},
                product_cart=[
                    {
                        "product_id": "product_id",
                        "quantity": 0,
                        "amount": 0,
                    }
                ],
                allowed_payment_method_types=["credit"],
                billing_currency="AED",
                discount_code="discount_code",
                force_3ds=True,
                metadata={"foo": "string"},
                payment_link=True,
                redirect_immediately=True,
                return_url="return_url",
                short_link=True,
                show_saved_payment_methods=True,
                tax_id="tax_id",
            )

        assert_matches_type(PaymentCreateResponse, payment, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: DodoPayments) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.payments.with_raw_response.create(
                billing={"country": "AF"},
                customer={"customer_id": "customer_id"},
                product_cart=[
                    {
                        "product_id": "product_id",
                        "quantity": 0,
                    }
                ],
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(PaymentCreateResponse, payment, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: DodoPayments) -> None:
        with pytest.warns(DeprecationWarning):
            with client.payments.with_streaming_response.create(
                billing={"country": "AF"},
                customer={"customer_id": "customer_id"},
                product_cart=[
                    {
                        "product_id": "product_id",
                        "quantity": 0,
                    }
                ],
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                payment = response.parse()
                assert_matches_type(PaymentCreateResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: DodoPayments) -> None:
        payment = client.payments.retrieve(
            "payment_id",
        )
        assert_matches_type(Payment, payment, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: DodoPayments) -> None:
        response = client.payments.with_raw_response.retrieve(
            "payment_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(Payment, payment, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: DodoPayments) -> None:
        with client.payments.with_streaming_response.retrieve(
            "payment_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = response.parse()
            assert_matches_type(Payment, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `payment_id` but received ''"):
            client.payments.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: DodoPayments) -> None:
        payment = client.payments.list()
        assert_matches_type(SyncDefaultPageNumberPagination[PaymentListResponse], payment, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: DodoPayments) -> None:
        payment = client.payments.list(
            brand_id="brand_id",
            created_at_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            customer_id="customer_id",
            page_number=0,
            page_size=0,
            status="succeeded",
            subscription_id="subscription_id",
        )
        assert_matches_type(SyncDefaultPageNumberPagination[PaymentListResponse], payment, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: DodoPayments) -> None:
        response = client.payments.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(SyncDefaultPageNumberPagination[PaymentListResponse], payment, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: DodoPayments) -> None:
        with client.payments.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = response.parse()
            assert_matches_type(SyncDefaultPageNumberPagination[PaymentListResponse], payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve_line_items(self, client: DodoPayments) -> None:
        payment = client.payments.retrieve_line_items(
            "payment_id",
        )
        assert_matches_type(PaymentRetrieveLineItemsResponse, payment, path=["response"])

    @parametrize
    def test_raw_response_retrieve_line_items(self, client: DodoPayments) -> None:
        response = client.payments.with_raw_response.retrieve_line_items(
            "payment_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(PaymentRetrieveLineItemsResponse, payment, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_line_items(self, client: DodoPayments) -> None:
        with client.payments.with_streaming_response.retrieve_line_items(
            "payment_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = response.parse()
            assert_matches_type(PaymentRetrieveLineItemsResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve_line_items(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `payment_id` but received ''"):
            client.payments.with_raw_response.retrieve_line_items(
                "",
            )


class TestAsyncPayments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncDodoPayments) -> None:
        with pytest.warns(DeprecationWarning):
            payment = await async_client.payments.create(
                billing={"country": "AF"},
                customer={"customer_id": "customer_id"},
                product_cart=[
                    {
                        "product_id": "product_id",
                        "quantity": 0,
                    }
                ],
            )

        assert_matches_type(PaymentCreateResponse, payment, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDodoPayments) -> None:
        with pytest.warns(DeprecationWarning):
            payment = await async_client.payments.create(
                billing={
                    "country": "AF",
                    "city": "city",
                    "state": "state",
                    "street": "street",
                    "zipcode": "zipcode",
                },
                customer={"customer_id": "customer_id"},
                product_cart=[
                    {
                        "product_id": "product_id",
                        "quantity": 0,
                        "amount": 0,
                    }
                ],
                allowed_payment_method_types=["credit"],
                billing_currency="AED",
                discount_code="discount_code",
                force_3ds=True,
                metadata={"foo": "string"},
                payment_link=True,
                redirect_immediately=True,
                return_url="return_url",
                short_link=True,
                show_saved_payment_methods=True,
                tax_id="tax_id",
            )

        assert_matches_type(PaymentCreateResponse, payment, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDodoPayments) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.payments.with_raw_response.create(
                billing={"country": "AF"},
                customer={"customer_id": "customer_id"},
                product_cart=[
                    {
                        "product_id": "product_id",
                        "quantity": 0,
                    }
                ],
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = await response.parse()
        assert_matches_type(PaymentCreateResponse, payment, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDodoPayments) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.payments.with_streaming_response.create(
                billing={"country": "AF"},
                customer={"customer_id": "customer_id"},
                product_cart=[
                    {
                        "product_id": "product_id",
                        "quantity": 0,
                    }
                ],
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                payment = await response.parse()
                assert_matches_type(PaymentCreateResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDodoPayments) -> None:
        payment = await async_client.payments.retrieve(
            "payment_id",
        )
        assert_matches_type(Payment, payment, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.payments.with_raw_response.retrieve(
            "payment_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = await response.parse()
        assert_matches_type(Payment, payment, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.payments.with_streaming_response.retrieve(
            "payment_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert_matches_type(Payment, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `payment_id` but received ''"):
            await async_client.payments.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncDodoPayments) -> None:
        payment = await async_client.payments.list()
        assert_matches_type(AsyncDefaultPageNumberPagination[PaymentListResponse], payment, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDodoPayments) -> None:
        payment = await async_client.payments.list(
            brand_id="brand_id",
            created_at_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            customer_id="customer_id",
            page_number=0,
            page_size=0,
            status="succeeded",
            subscription_id="subscription_id",
        )
        assert_matches_type(AsyncDefaultPageNumberPagination[PaymentListResponse], payment, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.payments.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = await response.parse()
        assert_matches_type(AsyncDefaultPageNumberPagination[PaymentListResponse], payment, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.payments.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert_matches_type(AsyncDefaultPageNumberPagination[PaymentListResponse], payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve_line_items(self, async_client: AsyncDodoPayments) -> None:
        payment = await async_client.payments.retrieve_line_items(
            "payment_id",
        )
        assert_matches_type(PaymentRetrieveLineItemsResponse, payment, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_line_items(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.payments.with_raw_response.retrieve_line_items(
            "payment_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = await response.parse()
        assert_matches_type(PaymentRetrieveLineItemsResponse, payment, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_line_items(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.payments.with_streaming_response.retrieve_line_items(
            "payment_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert_matches_type(PaymentRetrieveLineItemsResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve_line_items(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `payment_id` but received ''"):
            await async_client.payments.with_raw_response.retrieve_line_items(
                "",
            )
