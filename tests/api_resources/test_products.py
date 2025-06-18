# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from dodopayments import DodoPayments, AsyncDodoPayments
from dodopayments.types import (
    Product,
    ProductListResponse,
    ProductUpdateFilesResponse,
)
from dodopayments.pagination import SyncDefaultPageNumberPagination, AsyncDefaultPageNumberPagination

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
        assert_matches_type(Product, product, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: DodoPayments) -> None:
        product = client.products.create(
            price={
                "currency": "AED",
                "discount": 0,
                "price": 0,
                "purchasing_power_parity": True,
                "type": "one_time_price",
                "pay_what_you_want": True,
                "suggested_price": 0,
                "tax_inclusive": True,
            },
            tax_category="digital_products",
            addons=["string"],
            brand_id="brand_id",
            description="description",
            digital_product_delivery={
                "external_url": "external_url",
                "instructions": "instructions",
            },
            license_key_activation_message="license_key_activation_message",
            license_key_activations_limit=0,
            license_key_duration={
                "count": 0,
                "interval": "Day",
            },
            license_key_enabled=True,
            name="name",
        )
        assert_matches_type(Product, product, path=["response"])

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
        assert_matches_type(Product, product, path=["response"])

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
            assert_matches_type(Product, product, path=["response"])

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
            addons=["string"],
            brand_id="brand_id",
            description="description",
            digital_product_delivery={
                "external_url": "external_url",
                "files": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                "instructions": "instructions",
            },
            image_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            license_key_activation_message="license_key_activation_message",
            license_key_activations_limit=0,
            license_key_duration={
                "count": 0,
                "interval": "Day",
            },
            license_key_enabled=True,
            name="name",
            price={
                "currency": "AED",
                "discount": 0,
                "price": 0,
                "purchasing_power_parity": True,
                "type": "one_time_price",
                "pay_what_you_want": True,
                "suggested_price": 0,
                "tax_inclusive": True,
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
        assert_matches_type(SyncDefaultPageNumberPagination[ProductListResponse], product, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: DodoPayments) -> None:
        product = client.products.list(
            archived=True,
            brand_id="brand_id",
            page_number=0,
            page_size=0,
            recurring=True,
        )
        assert_matches_type(SyncDefaultPageNumberPagination[ProductListResponse], product, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: DodoPayments) -> None:
        response = client.products.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = response.parse()
        assert_matches_type(SyncDefaultPageNumberPagination[ProductListResponse], product, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: DodoPayments) -> None:
        with client.products.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = response.parse()
            assert_matches_type(SyncDefaultPageNumberPagination[ProductListResponse], product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: DodoPayments) -> None:
        product = client.products.delete(
            "id",
        )
        assert product is None

    @parametrize
    def test_raw_response_delete(self, client: DodoPayments) -> None:
        response = client.products.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = response.parse()
        assert product is None

    @parametrize
    def test_streaming_response_delete(self, client: DodoPayments) -> None:
        with client.products.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = response.parse()
            assert product is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.products.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_unarchive(self, client: DodoPayments) -> None:
        product = client.products.unarchive(
            "id",
        )
        assert product is None

    @parametrize
    def test_raw_response_unarchive(self, client: DodoPayments) -> None:
        response = client.products.with_raw_response.unarchive(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = response.parse()
        assert product is None

    @parametrize
    def test_streaming_response_unarchive(self, client: DodoPayments) -> None:
        with client.products.with_streaming_response.unarchive(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = response.parse()
            assert product is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_unarchive(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.products.with_raw_response.unarchive(
                "",
            )

    @parametrize
    def test_method_update_files(self, client: DodoPayments) -> None:
        product = client.products.update_files(
            id="id",
            file_name="file_name",
        )
        assert_matches_type(ProductUpdateFilesResponse, product, path=["response"])

    @parametrize
    def test_raw_response_update_files(self, client: DodoPayments) -> None:
        response = client.products.with_raw_response.update_files(
            id="id",
            file_name="file_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = response.parse()
        assert_matches_type(ProductUpdateFilesResponse, product, path=["response"])

    @parametrize
    def test_streaming_response_update_files(self, client: DodoPayments) -> None:
        with client.products.with_streaming_response.update_files(
            id="id",
            file_name="file_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = response.parse()
            assert_matches_type(ProductUpdateFilesResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_files(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.products.with_raw_response.update_files(
                id="",
                file_name="file_name",
            )


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
        assert_matches_type(Product, product, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDodoPayments) -> None:
        product = await async_client.products.create(
            price={
                "currency": "AED",
                "discount": 0,
                "price": 0,
                "purchasing_power_parity": True,
                "type": "one_time_price",
                "pay_what_you_want": True,
                "suggested_price": 0,
                "tax_inclusive": True,
            },
            tax_category="digital_products",
            addons=["string"],
            brand_id="brand_id",
            description="description",
            digital_product_delivery={
                "external_url": "external_url",
                "instructions": "instructions",
            },
            license_key_activation_message="license_key_activation_message",
            license_key_activations_limit=0,
            license_key_duration={
                "count": 0,
                "interval": "Day",
            },
            license_key_enabled=True,
            name="name",
        )
        assert_matches_type(Product, product, path=["response"])

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
        assert_matches_type(Product, product, path=["response"])

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
            assert_matches_type(Product, product, path=["response"])

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
            addons=["string"],
            brand_id="brand_id",
            description="description",
            digital_product_delivery={
                "external_url": "external_url",
                "files": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                "instructions": "instructions",
            },
            image_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            license_key_activation_message="license_key_activation_message",
            license_key_activations_limit=0,
            license_key_duration={
                "count": 0,
                "interval": "Day",
            },
            license_key_enabled=True,
            name="name",
            price={
                "currency": "AED",
                "discount": 0,
                "price": 0,
                "purchasing_power_parity": True,
                "type": "one_time_price",
                "pay_what_you_want": True,
                "suggested_price": 0,
                "tax_inclusive": True,
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
        assert_matches_type(AsyncDefaultPageNumberPagination[ProductListResponse], product, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDodoPayments) -> None:
        product = await async_client.products.list(
            archived=True,
            brand_id="brand_id",
            page_number=0,
            page_size=0,
            recurring=True,
        )
        assert_matches_type(AsyncDefaultPageNumberPagination[ProductListResponse], product, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.products.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = await response.parse()
        assert_matches_type(AsyncDefaultPageNumberPagination[ProductListResponse], product, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.products.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = await response.parse()
            assert_matches_type(AsyncDefaultPageNumberPagination[ProductListResponse], product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncDodoPayments) -> None:
        product = await async_client.products.delete(
            "id",
        )
        assert product is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.products.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = await response.parse()
        assert product is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.products.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = await response.parse()
            assert product is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.products.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_unarchive(self, async_client: AsyncDodoPayments) -> None:
        product = await async_client.products.unarchive(
            "id",
        )
        assert product is None

    @parametrize
    async def test_raw_response_unarchive(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.products.with_raw_response.unarchive(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = await response.parse()
        assert product is None

    @parametrize
    async def test_streaming_response_unarchive(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.products.with_streaming_response.unarchive(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = await response.parse()
            assert product is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_unarchive(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.products.with_raw_response.unarchive(
                "",
            )

    @parametrize
    async def test_method_update_files(self, async_client: AsyncDodoPayments) -> None:
        product = await async_client.products.update_files(
            id="id",
            file_name="file_name",
        )
        assert_matches_type(ProductUpdateFilesResponse, product, path=["response"])

    @parametrize
    async def test_raw_response_update_files(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.products.with_raw_response.update_files(
            id="id",
            file_name="file_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = await response.parse()
        assert_matches_type(ProductUpdateFilesResponse, product, path=["response"])

    @parametrize
    async def test_streaming_response_update_files(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.products.with_streaming_response.update_files(
            id="id",
            file_name="file_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = await response.parse()
            assert_matches_type(ProductUpdateFilesResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_files(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.products.with_raw_response.update_files(
                id="",
                file_name="file_name",
            )
