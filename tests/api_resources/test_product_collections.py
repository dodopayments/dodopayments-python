# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from dodopayments import DodoPayments, AsyncDodoPayments
from dodopayments.types import (
    ProductCollectionListResponse,
    ProductCollectionCreateResponse,
    ProductCollectionRetrieveResponse,
    ProductCollectionUnarchiveResponse,
    ProductCollectionUpdateImagesResponse,
)
from dodopayments.pagination import SyncDefaultPageNumberPagination, AsyncDefaultPageNumberPagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProductCollections:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: DodoPayments) -> None:
        product_collection = client.product_collections.create(
            groups=[{"products": [{"product_id": "product_id"}]}],
            name="name",
        )
        assert_matches_type(ProductCollectionCreateResponse, product_collection, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: DodoPayments) -> None:
        product_collection = client.product_collections.create(
            groups=[
                {
                    "products": [
                        {
                            "product_id": "product_id",
                            "status": True,
                        }
                    ],
                    "group_name": "group_name",
                    "status": True,
                }
            ],
            name="name",
            brand_id="brand_id",
            description="description",
        )
        assert_matches_type(ProductCollectionCreateResponse, product_collection, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: DodoPayments) -> None:
        response = client.product_collections.with_raw_response.create(
            groups=[{"products": [{"product_id": "product_id"}]}],
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product_collection = response.parse()
        assert_matches_type(ProductCollectionCreateResponse, product_collection, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: DodoPayments) -> None:
        with client.product_collections.with_streaming_response.create(
            groups=[{"products": [{"product_id": "product_id"}]}],
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product_collection = response.parse()
            assert_matches_type(ProductCollectionCreateResponse, product_collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: DodoPayments) -> None:
        product_collection = client.product_collections.retrieve(
            "id",
        )
        assert_matches_type(ProductCollectionRetrieveResponse, product_collection, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: DodoPayments) -> None:
        response = client.product_collections.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product_collection = response.parse()
        assert_matches_type(ProductCollectionRetrieveResponse, product_collection, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: DodoPayments) -> None:
        with client.product_collections.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product_collection = response.parse()
            assert_matches_type(ProductCollectionRetrieveResponse, product_collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.product_collections.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: DodoPayments) -> None:
        product_collection = client.product_collections.update(
            id="id",
        )
        assert product_collection is None

    @parametrize
    def test_method_update_with_all_params(self, client: DodoPayments) -> None:
        product_collection = client.product_collections.update(
            id="id",
            brand_id="brand_id",
            description="description",
            group_order=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            image_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        )
        assert product_collection is None

    @parametrize
    def test_raw_response_update(self, client: DodoPayments) -> None:
        response = client.product_collections.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product_collection = response.parse()
        assert product_collection is None

    @parametrize
    def test_streaming_response_update(self, client: DodoPayments) -> None:
        with client.product_collections.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product_collection = response.parse()
            assert product_collection is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.product_collections.with_raw_response.update(
                id="",
            )

    @parametrize
    def test_method_list(self, client: DodoPayments) -> None:
        product_collection = client.product_collections.list()
        assert_matches_type(
            SyncDefaultPageNumberPagination[ProductCollectionListResponse], product_collection, path=["response"]
        )

    @parametrize
    def test_method_list_with_all_params(self, client: DodoPayments) -> None:
        product_collection = client.product_collections.list(
            archived=True,
            brand_id="brand_id",
            page_number=0,
            page_size=0,
        )
        assert_matches_type(
            SyncDefaultPageNumberPagination[ProductCollectionListResponse], product_collection, path=["response"]
        )

    @parametrize
    def test_raw_response_list(self, client: DodoPayments) -> None:
        response = client.product_collections.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product_collection = response.parse()
        assert_matches_type(
            SyncDefaultPageNumberPagination[ProductCollectionListResponse], product_collection, path=["response"]
        )

    @parametrize
    def test_streaming_response_list(self, client: DodoPayments) -> None:
        with client.product_collections.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product_collection = response.parse()
            assert_matches_type(
                SyncDefaultPageNumberPagination[ProductCollectionListResponse], product_collection, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: DodoPayments) -> None:
        product_collection = client.product_collections.delete(
            "id",
        )
        assert product_collection is None

    @parametrize
    def test_raw_response_delete(self, client: DodoPayments) -> None:
        response = client.product_collections.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product_collection = response.parse()
        assert product_collection is None

    @parametrize
    def test_streaming_response_delete(self, client: DodoPayments) -> None:
        with client.product_collections.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product_collection = response.parse()
            assert product_collection is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.product_collections.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_unarchive(self, client: DodoPayments) -> None:
        product_collection = client.product_collections.unarchive(
            "id",
        )
        assert_matches_type(ProductCollectionUnarchiveResponse, product_collection, path=["response"])

    @parametrize
    def test_raw_response_unarchive(self, client: DodoPayments) -> None:
        response = client.product_collections.with_raw_response.unarchive(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product_collection = response.parse()
        assert_matches_type(ProductCollectionUnarchiveResponse, product_collection, path=["response"])

    @parametrize
    def test_streaming_response_unarchive(self, client: DodoPayments) -> None:
        with client.product_collections.with_streaming_response.unarchive(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product_collection = response.parse()
            assert_matches_type(ProductCollectionUnarchiveResponse, product_collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_unarchive(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.product_collections.with_raw_response.unarchive(
                "",
            )

    @parametrize
    def test_method_update_images(self, client: DodoPayments) -> None:
        product_collection = client.product_collections.update_images(
            id="id",
        )
        assert_matches_type(ProductCollectionUpdateImagesResponse, product_collection, path=["response"])

    @parametrize
    def test_method_update_images_with_all_params(self, client: DodoPayments) -> None:
        product_collection = client.product_collections.update_images(
            id="id",
            force_update=True,
        )
        assert_matches_type(ProductCollectionUpdateImagesResponse, product_collection, path=["response"])

    @parametrize
    def test_raw_response_update_images(self, client: DodoPayments) -> None:
        response = client.product_collections.with_raw_response.update_images(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product_collection = response.parse()
        assert_matches_type(ProductCollectionUpdateImagesResponse, product_collection, path=["response"])

    @parametrize
    def test_streaming_response_update_images(self, client: DodoPayments) -> None:
        with client.product_collections.with_streaming_response.update_images(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product_collection = response.parse()
            assert_matches_type(ProductCollectionUpdateImagesResponse, product_collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_images(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.product_collections.with_raw_response.update_images(
                id="",
            )


class TestAsyncProductCollections:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncDodoPayments) -> None:
        product_collection = await async_client.product_collections.create(
            groups=[{"products": [{"product_id": "product_id"}]}],
            name="name",
        )
        assert_matches_type(ProductCollectionCreateResponse, product_collection, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDodoPayments) -> None:
        product_collection = await async_client.product_collections.create(
            groups=[
                {
                    "products": [
                        {
                            "product_id": "product_id",
                            "status": True,
                        }
                    ],
                    "group_name": "group_name",
                    "status": True,
                }
            ],
            name="name",
            brand_id="brand_id",
            description="description",
        )
        assert_matches_type(ProductCollectionCreateResponse, product_collection, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.product_collections.with_raw_response.create(
            groups=[{"products": [{"product_id": "product_id"}]}],
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product_collection = await response.parse()
        assert_matches_type(ProductCollectionCreateResponse, product_collection, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.product_collections.with_streaming_response.create(
            groups=[{"products": [{"product_id": "product_id"}]}],
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product_collection = await response.parse()
            assert_matches_type(ProductCollectionCreateResponse, product_collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDodoPayments) -> None:
        product_collection = await async_client.product_collections.retrieve(
            "id",
        )
        assert_matches_type(ProductCollectionRetrieveResponse, product_collection, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.product_collections.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product_collection = await response.parse()
        assert_matches_type(ProductCollectionRetrieveResponse, product_collection, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.product_collections.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product_collection = await response.parse()
            assert_matches_type(ProductCollectionRetrieveResponse, product_collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.product_collections.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncDodoPayments) -> None:
        product_collection = await async_client.product_collections.update(
            id="id",
        )
        assert product_collection is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncDodoPayments) -> None:
        product_collection = await async_client.product_collections.update(
            id="id",
            brand_id="brand_id",
            description="description",
            group_order=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            image_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        )
        assert product_collection is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.product_collections.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product_collection = await response.parse()
        assert product_collection is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.product_collections.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product_collection = await response.parse()
            assert product_collection is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.product_collections.with_raw_response.update(
                id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncDodoPayments) -> None:
        product_collection = await async_client.product_collections.list()
        assert_matches_type(
            AsyncDefaultPageNumberPagination[ProductCollectionListResponse], product_collection, path=["response"]
        )

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDodoPayments) -> None:
        product_collection = await async_client.product_collections.list(
            archived=True,
            brand_id="brand_id",
            page_number=0,
            page_size=0,
        )
        assert_matches_type(
            AsyncDefaultPageNumberPagination[ProductCollectionListResponse], product_collection, path=["response"]
        )

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.product_collections.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product_collection = await response.parse()
        assert_matches_type(
            AsyncDefaultPageNumberPagination[ProductCollectionListResponse], product_collection, path=["response"]
        )

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.product_collections.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product_collection = await response.parse()
            assert_matches_type(
                AsyncDefaultPageNumberPagination[ProductCollectionListResponse], product_collection, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncDodoPayments) -> None:
        product_collection = await async_client.product_collections.delete(
            "id",
        )
        assert product_collection is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.product_collections.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product_collection = await response.parse()
        assert product_collection is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.product_collections.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product_collection = await response.parse()
            assert product_collection is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.product_collections.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_unarchive(self, async_client: AsyncDodoPayments) -> None:
        product_collection = await async_client.product_collections.unarchive(
            "id",
        )
        assert_matches_type(ProductCollectionUnarchiveResponse, product_collection, path=["response"])

    @parametrize
    async def test_raw_response_unarchive(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.product_collections.with_raw_response.unarchive(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product_collection = await response.parse()
        assert_matches_type(ProductCollectionUnarchiveResponse, product_collection, path=["response"])

    @parametrize
    async def test_streaming_response_unarchive(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.product_collections.with_streaming_response.unarchive(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product_collection = await response.parse()
            assert_matches_type(ProductCollectionUnarchiveResponse, product_collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_unarchive(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.product_collections.with_raw_response.unarchive(
                "",
            )

    @parametrize
    async def test_method_update_images(self, async_client: AsyncDodoPayments) -> None:
        product_collection = await async_client.product_collections.update_images(
            id="id",
        )
        assert_matches_type(ProductCollectionUpdateImagesResponse, product_collection, path=["response"])

    @parametrize
    async def test_method_update_images_with_all_params(self, async_client: AsyncDodoPayments) -> None:
        product_collection = await async_client.product_collections.update_images(
            id="id",
            force_update=True,
        )
        assert_matches_type(ProductCollectionUpdateImagesResponse, product_collection, path=["response"])

    @parametrize
    async def test_raw_response_update_images(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.product_collections.with_raw_response.update_images(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product_collection = await response.parse()
        assert_matches_type(ProductCollectionUpdateImagesResponse, product_collection, path=["response"])

    @parametrize
    async def test_streaming_response_update_images(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.product_collections.with_streaming_response.update_images(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product_collection = await response.parse()
            assert_matches_type(ProductCollectionUpdateImagesResponse, product_collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_images(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.product_collections.with_raw_response.update_images(
                id="",
            )
