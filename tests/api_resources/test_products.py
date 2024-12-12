# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from dodo_payments import DodoPayments, AsyncDodoPayments
from dodo_payments.types import (
    Product,
    ProductListResponse,
    ProductCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProducts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: DodoPayments) -> None:
        product = client.products.create(
            price={
                "currency": "AED",
                "discount": 0,
                "price": 0,
                "purchasing_power_parity": True,
                "type": "one_time_price",
            },
            tax_category="digital_products",
        )
        assert_matches_type(ProductCreateResponse, product, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: DodoPayments) -> None:
        product = client.products.create(
            price={
                "currency": "AED",
                "discount": 0,
                "price": 0,
                "purchasing_power_parity": True,
                "type": "one_time_price",
            },
            tax_category="digital_products",
            description="description",
            name="name",
        )
        assert_matches_type(ProductCreateResponse, product, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: DodoPayments) -> None:
        response = client.products.with_raw_response.create(
            price={
                "currency": "AED",
                "discount": 0,
                "price": 0,
                "purchasing_power_parity": True,
                "type": "one_time_price",
            },
            tax_category="digital_products",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = response.parse()
        assert_matches_type(ProductCreateResponse, product, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: DodoPayments) -> None:
        with client.products.with_streaming_response.create(
            price={
                "currency": "AED",
                "discount": 0,
                "price": 0,
                "purchasing_power_parity": True,
                "type": "one_time_price",
            },
            tax_category="digital_products",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = response.parse()
            assert_matches_type(ProductCreateResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: DodoPayments) -> None:
        product = client.products.retrieve(
            "id",
        )
        assert_matches_type(Product, product, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: DodoPayments) -> None:
        response = client.products.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = response.parse()
        assert_matches_type(Product, product, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: DodoPayments) -> None:
        with client.products.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = response.parse()
            assert_matches_type(Product, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.products.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: DodoPayments) -> None:
        product = client.products.update(
            id="id",
        )
        assert product is None

    @parametrize
    def test_method_update_with_all_params(self, client: DodoPayments) -> None:
        product = client.products.update(
            id="id",
            description="description",
            name="name",
            price={
                "currency": "AED",
                "discount": 0,
                "price": 0,
                "purchasing_power_parity": True,
                "type": "one_time_price",
            },
            tax_category="digital_products",
        )
        assert product is None

    @parametrize
    def test_raw_response_update(self, client: DodoPayments) -> None:
        response = client.products.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = response.parse()
        assert product is None

    @parametrize
    def test_streaming_response_update(self, client: DodoPayments) -> None:
        with client.products.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = response.parse()
            assert product is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.products.with_raw_response.update(
                id="",
            )

    @parametrize
    def test_method_list(self, client: DodoPayments) -> None:
        product = client.products.list()
        assert_matches_type(ProductListResponse, product, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: DodoPayments) -> None:
        product = client.products.list(
            page_number=0,
            page_size=0,
        )
        assert_matches_type(ProductListResponse, product, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: DodoPayments) -> None:
        response = client.products.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = response.parse()
        assert_matches_type(ProductListResponse, product, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: DodoPayments) -> None:
        with client.products.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = response.parse()
            assert_matches_type(ProductListResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncProducts:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncDodoPayments) -> None:
        product = await async_client.products.create(
            price={
                "currency": "AED",
                "discount": 0,
                "price": 0,
                "purchasing_power_parity": True,
                "type": "one_time_price",
            },
            tax_category="digital_products",
        )
        assert_matches_type(ProductCreateResponse, product, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDodoPayments) -> None:
        product = await async_client.products.create(
            price={
                "currency": "AED",
                "discount": 0,
                "price": 0,
                "purchasing_power_parity": True,
                "type": "one_time_price",
            },
            tax_category="digital_products",
            description="description",
            name="name",
        )
        assert_matches_type(ProductCreateResponse, product, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.products.with_raw_response.create(
            price={
                "currency": "AED",
                "discount": 0,
                "price": 0,
                "purchasing_power_parity": True,
                "type": "one_time_price",
            },
            tax_category="digital_products",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = await response.parse()
        assert_matches_type(ProductCreateResponse, product, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.products.with_streaming_response.create(
            price={
                "currency": "AED",
                "discount": 0,
                "price": 0,
                "purchasing_power_parity": True,
                "type": "one_time_price",
            },
            tax_category="digital_products",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = await response.parse()
            assert_matches_type(ProductCreateResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDodoPayments) -> None:
        product = await async_client.products.retrieve(
            "id",
        )
        assert_matches_type(Product, product, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.products.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = await response.parse()
        assert_matches_type(Product, product, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.products.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = await response.parse()
            assert_matches_type(Product, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.products.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncDodoPayments) -> None:
        product = await async_client.products.update(
            id="id",
        )
        assert product is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncDodoPayments) -> None:
        product = await async_client.products.update(
            id="id",
            description="description",
            name="name",
            price={
                "currency": "AED",
                "discount": 0,
                "price": 0,
                "purchasing_power_parity": True,
                "type": "one_time_price",
            },
            tax_category="digital_products",
        )
        assert product is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.products.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = await response.parse()
        assert product is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.products.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = await response.parse()
            assert product is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.products.with_raw_response.update(
                id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncDodoPayments) -> None:
        product = await async_client.products.list()
        assert_matches_type(ProductListResponse, product, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDodoPayments) -> None:
        product = await async_client.products.list(
            page_number=0,
            page_size=0,
        )
        assert_matches_type(ProductListResponse, product, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.products.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = await response.parse()
        assert_matches_type(ProductListResponse, product, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.products.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = await response.parse()
            assert_matches_type(ProductListResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True
