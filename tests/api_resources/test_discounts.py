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
            type="percentage",
        )
        assert_matches_type(Discount, discount, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: DodoPayments) -> None:
        discount = client.discounts.create(
            amount=0,
            type="percentage",
            code="code",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            name="name",
            restricted_to=["string"],
            usage_limit=0,
        )
        assert_matches_type(Discount, discount, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: DodoPayments) -> None:
        response = client.discounts.with_raw_response.create(
            amount=0,
            type="percentage",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        discount = response.parse()
        assert_matches_type(Discount, discount, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: DodoPayments) -> None:
        with client.discounts.with_streaming_response.create(
            amount=0,
            type="percentage",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            discount = response.parse()
            assert_matches_type(Discount, discount, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: DodoPayments) -> None:
        discount = client.discounts.retrieve(
            "discount_id",
        )
        assert_matches_type(Discount, discount, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: DodoPayments) -> None:
        response = client.discounts.with_raw_response.retrieve(
            "discount_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        discount = response.parse()
        assert_matches_type(Discount, discount, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: DodoPayments) -> None:
        with client.discounts.with_streaming_response.retrieve(
            "discount_id",
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
            discount_id="discount_id",
        )
        assert_matches_type(Discount, discount, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: DodoPayments) -> None:
        discount = client.discounts.update(
            discount_id="discount_id",
            amount=0,
            code="code",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            name="name",
            restricted_to=["string"],
            type="percentage",
            usage_limit=0,
        )
        assert_matches_type(Discount, discount, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: DodoPayments) -> None:
        response = client.discounts.with_raw_response.update(
            discount_id="discount_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        discount = response.parse()
        assert_matches_type(Discount, discount, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: DodoPayments) -> None:
        with client.discounts.with_streaming_response.update(
            discount_id="discount_id",
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
            page_number=0,
            page_size=0,
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
            "discount_id",
        )
        assert discount is None

    @parametrize
    def test_raw_response_delete(self, client: DodoPayments) -> None:
        response = client.discounts.with_raw_response.delete(
            "discount_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        discount = response.parse()
        assert discount is None

    @parametrize
    def test_streaming_response_delete(self, client: DodoPayments) -> None:
        with client.discounts.with_streaming_response.delete(
            "discount_id",
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


class TestAsyncDiscounts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncDodoPayments) -> None:
        discount = await async_client.discounts.create(
            amount=0,
            type="percentage",
        )
        assert_matches_type(Discount, discount, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDodoPayments) -> None:
        discount = await async_client.discounts.create(
            amount=0,
            type="percentage",
            code="code",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            name="name",
            restricted_to=["string"],
            usage_limit=0,
        )
        assert_matches_type(Discount, discount, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.discounts.with_raw_response.create(
            amount=0,
            type="percentage",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        discount = await response.parse()
        assert_matches_type(Discount, discount, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.discounts.with_streaming_response.create(
            amount=0,
            type="percentage",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            discount = await response.parse()
            assert_matches_type(Discount, discount, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDodoPayments) -> None:
        discount = await async_client.discounts.retrieve(
            "discount_id",
        )
        assert_matches_type(Discount, discount, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.discounts.with_raw_response.retrieve(
            "discount_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        discount = await response.parse()
        assert_matches_type(Discount, discount, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.discounts.with_streaming_response.retrieve(
            "discount_id",
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
            discount_id="discount_id",
        )
        assert_matches_type(Discount, discount, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncDodoPayments) -> None:
        discount = await async_client.discounts.update(
            discount_id="discount_id",
            amount=0,
            code="code",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            name="name",
            restricted_to=["string"],
            type="percentage",
            usage_limit=0,
        )
        assert_matches_type(Discount, discount, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.discounts.with_raw_response.update(
            discount_id="discount_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        discount = await response.parse()
        assert_matches_type(Discount, discount, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.discounts.with_streaming_response.update(
            discount_id="discount_id",
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
            page_number=0,
            page_size=0,
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
            "discount_id",
        )
        assert discount is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.discounts.with_raw_response.delete(
            "discount_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        discount = await response.parse()
        assert discount is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.discounts.with_streaming_response.delete(
            "discount_id",
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
