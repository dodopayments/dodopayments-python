# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from dodopayments import DodoPayments, AsyncDodoPayments
from dodopayments.types import (
    Discount,
)
from dodopayments._utils import parse_datetime
from dodopayments.pagination import SyncDefaultPageNumberPagination, AsyncDefaultPageNumberPagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDiscounts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: DodoPayments) -> None:
        discount = client.discounts.create(
            amount=0,
            type="flat",
        )
        assert_matches_type(Discount, discount, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: DodoPayments) -> None:
        discount = client.discounts.create(
            amount=0,
            type="flat",
            code="code",
            currency_options=[
                {
                    "currency": "AED",
                    "is_default": True,
                    "max_amount_possible": 0,
                    "minimum_subtotal": 0,
                }
            ],
            customer_eligibility="any",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            metadata={"foo": "string"},
            name="name",
            per_customer_usage_limit=0,
            preserve_on_plan_change=True,
            restricted_to=["string"],
            starts_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            subscription_cycles=0,
            usage_limit=0,
        )
        assert_matches_type(Discount, discount, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: DodoPayments) -> None:
        response = client.discounts.with_raw_response.create(
            amount=0,
            type="flat",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        discount = response.parse()
        assert_matches_type(Discount, discount, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: DodoPayments) -> None:
        with client.discounts.with_streaming_response.create(
            amount=0,
            type="flat",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            discount = response.parse()
            assert_matches_type(Discount, discount, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: DodoPayments) -> None:
        discount = client.discounts.retrieve(
            "dsc_qxxEmg5PuM1uNTE0LgkP9",
        )
        assert_matches_type(Discount, discount, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: DodoPayments) -> None:
        response = client.discounts.with_raw_response.retrieve(
            "dsc_qxxEmg5PuM1uNTE0LgkP9",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        discount = response.parse()
        assert_matches_type(Discount, discount, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: DodoPayments) -> None:
        with client.discounts.with_streaming_response.retrieve(
            "dsc_qxxEmg5PuM1uNTE0LgkP9",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            discount = response.parse()
            assert_matches_type(Discount, discount, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `discount_id` but received ''"):
            client.discounts.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: DodoPayments) -> None:
        discount = client.discounts.update(
            discount_id="dsc_qxxEmg5PuM1uNTE0LgkP9",
        )
        assert_matches_type(Discount, discount, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: DodoPayments) -> None:
        discount = client.discounts.update(
            discount_id="dsc_qxxEmg5PuM1uNTE0LgkP9",
            amount=0,
            code="code",
            currency_options=[
                {
                    "currency": "AED",
                    "is_default": True,
                    "max_amount_possible": 0,
                    "minimum_subtotal": 0,
                }
            ],
            customer_eligibility="any",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            metadata={"foo": "string"},
            name="name",
            per_customer_usage_limit=0,
            preserve_on_plan_change=True,
            restricted_to=["string"],
            starts_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            subscription_cycles=0,
            type="flat",
            usage_limit=0,
        )
        assert_matches_type(Discount, discount, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: DodoPayments) -> None:
        response = client.discounts.with_raw_response.update(
            discount_id="dsc_qxxEmg5PuM1uNTE0LgkP9",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        discount = response.parse()
        assert_matches_type(Discount, discount, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: DodoPayments) -> None:
        with client.discounts.with_streaming_response.update(
            discount_id="dsc_qxxEmg5PuM1uNTE0LgkP9",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            discount = response.parse()
            assert_matches_type(Discount, discount, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `discount_id` but received ''"):
            client.discounts.with_raw_response.update(
                discount_id="",
            )

    @parametrize
    def test_method_list(self, client: DodoPayments) -> None:
        discount = client.discounts.list()
        assert_matches_type(SyncDefaultPageNumberPagination[Discount], discount, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: DodoPayments) -> None:
        discount = client.discounts.list(
            active=True,
            code="code",
            discount_type="flat",
            page_number=0,
            page_size=0,
            product_id="product_id",
        )
        assert_matches_type(SyncDefaultPageNumberPagination[Discount], discount, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: DodoPayments) -> None:
        response = client.discounts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        discount = response.parse()
        assert_matches_type(SyncDefaultPageNumberPagination[Discount], discount, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: DodoPayments) -> None:
        with client.discounts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            discount = response.parse()
            assert_matches_type(SyncDefaultPageNumberPagination[Discount], discount, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: DodoPayments) -> None:
        discount = client.discounts.delete(
            "dsc_qxxEmg5PuM1uNTE0LgkP9",
        )
        assert discount is None

    @parametrize
    def test_raw_response_delete(self, client: DodoPayments) -> None:
        response = client.discounts.with_raw_response.delete(
            "dsc_qxxEmg5PuM1uNTE0LgkP9",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        discount = response.parse()
        assert discount is None

    @parametrize
    def test_streaming_response_delete(self, client: DodoPayments) -> None:
        with client.discounts.with_streaming_response.delete(
            "dsc_qxxEmg5PuM1uNTE0LgkP9",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            discount = response.parse()
            assert discount is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `discount_id` but received ''"):
            client.discounts.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_retrieve_by_code(self, client: DodoPayments) -> None:
        discount = client.discounts.retrieve_by_code(
            "code",
        )
        assert_matches_type(Discount, discount, path=["response"])

    @parametrize
    def test_raw_response_retrieve_by_code(self, client: DodoPayments) -> None:
        response = client.discounts.with_raw_response.retrieve_by_code(
            "code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        discount = response.parse()
        assert_matches_type(Discount, discount, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_by_code(self, client: DodoPayments) -> None:
        with client.discounts.with_streaming_response.retrieve_by_code(
            "code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            discount = response.parse()
            assert_matches_type(Discount, discount, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve_by_code(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            client.discounts.with_raw_response.retrieve_by_code(
                "",
            )


class TestAsyncDiscounts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncDodoPayments) -> None:
        discount = await async_client.discounts.create(
            amount=0,
            type="flat",
        )
        assert_matches_type(Discount, discount, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDodoPayments) -> None:
        discount = await async_client.discounts.create(
            amount=0,
            type="flat",
            code="code",
            currency_options=[
                {
                    "currency": "AED",
                    "is_default": True,
                    "max_amount_possible": 0,
                    "minimum_subtotal": 0,
                }
            ],
            customer_eligibility="any",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            metadata={"foo": "string"},
            name="name",
            per_customer_usage_limit=0,
            preserve_on_plan_change=True,
            restricted_to=["string"],
            starts_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            subscription_cycles=0,
            usage_limit=0,
        )
        assert_matches_type(Discount, discount, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.discounts.with_raw_response.create(
            amount=0,
            type="flat",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        discount = await response.parse()
        assert_matches_type(Discount, discount, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.discounts.with_streaming_response.create(
            amount=0,
            type="flat",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            discount = await response.parse()
            assert_matches_type(Discount, discount, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDodoPayments) -> None:
        discount = await async_client.discounts.retrieve(
            "dsc_qxxEmg5PuM1uNTE0LgkP9",
        )
        assert_matches_type(Discount, discount, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.discounts.with_raw_response.retrieve(
            "dsc_qxxEmg5PuM1uNTE0LgkP9",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        discount = await response.parse()
        assert_matches_type(Discount, discount, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.discounts.with_streaming_response.retrieve(
            "dsc_qxxEmg5PuM1uNTE0LgkP9",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            discount = await response.parse()
            assert_matches_type(Discount, discount, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `discount_id` but received ''"):
            await async_client.discounts.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncDodoPayments) -> None:
        discount = await async_client.discounts.update(
            discount_id="dsc_qxxEmg5PuM1uNTE0LgkP9",
        )
        assert_matches_type(Discount, discount, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncDodoPayments) -> None:
        discount = await async_client.discounts.update(
            discount_id="dsc_qxxEmg5PuM1uNTE0LgkP9",
            amount=0,
            code="code",
            currency_options=[
                {
                    "currency": "AED",
                    "is_default": True,
                    "max_amount_possible": 0,
                    "minimum_subtotal": 0,
                }
            ],
            customer_eligibility="any",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            metadata={"foo": "string"},
            name="name",
            per_customer_usage_limit=0,
            preserve_on_plan_change=True,
            restricted_to=["string"],
            starts_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            subscription_cycles=0,
            type="flat",
            usage_limit=0,
        )
        assert_matches_type(Discount, discount, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.discounts.with_raw_response.update(
            discount_id="dsc_qxxEmg5PuM1uNTE0LgkP9",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        discount = await response.parse()
        assert_matches_type(Discount, discount, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.discounts.with_streaming_response.update(
            discount_id="dsc_qxxEmg5PuM1uNTE0LgkP9",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            discount = await response.parse()
            assert_matches_type(Discount, discount, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `discount_id` but received ''"):
            await async_client.discounts.with_raw_response.update(
                discount_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncDodoPayments) -> None:
        discount = await async_client.discounts.list()
        assert_matches_type(AsyncDefaultPageNumberPagination[Discount], discount, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDodoPayments) -> None:
        discount = await async_client.discounts.list(
            active=True,
            code="code",
            discount_type="flat",
            page_number=0,
            page_size=0,
            product_id="product_id",
        )
        assert_matches_type(AsyncDefaultPageNumberPagination[Discount], discount, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.discounts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        discount = await response.parse()
        assert_matches_type(AsyncDefaultPageNumberPagination[Discount], discount, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.discounts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            discount = await response.parse()
            assert_matches_type(AsyncDefaultPageNumberPagination[Discount], discount, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncDodoPayments) -> None:
        discount = await async_client.discounts.delete(
            "dsc_qxxEmg5PuM1uNTE0LgkP9",
        )
        assert discount is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.discounts.with_raw_response.delete(
            "dsc_qxxEmg5PuM1uNTE0LgkP9",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        discount = await response.parse()
        assert discount is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.discounts.with_streaming_response.delete(
            "dsc_qxxEmg5PuM1uNTE0LgkP9",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            discount = await response.parse()
            assert discount is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `discount_id` but received ''"):
            await async_client.discounts.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_retrieve_by_code(self, async_client: AsyncDodoPayments) -> None:
        discount = await async_client.discounts.retrieve_by_code(
            "code",
        )
        assert_matches_type(Discount, discount, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_by_code(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.discounts.with_raw_response.retrieve_by_code(
            "code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        discount = await response.parse()
        assert_matches_type(Discount, discount, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_by_code(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.discounts.with_streaming_response.retrieve_by_code(
            "code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            discount = await response.parse()
            assert_matches_type(Discount, discount, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve_by_code(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            await async_client.discounts.with_raw_response.retrieve_by_code(
                "",
            )
