# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from dodopayments import DodoPayments, AsyncDodoPayments
from dodopayments.types.product_collections import GroupCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGroups:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: DodoPayments) -> None:
        group = client.product_collections.groups.create(
            id="id",
            products=[{"product_id": "product_id"}],
        )
        assert_matches_type(GroupCreateResponse, group, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: DodoPayments) -> None:
        group = client.product_collections.groups.create(
            id="id",
            products=[
                {
                    "product_id": "product_id",
                    "status": True,
                }
            ],
            group_name="group_name",
            status=True,
        )
        assert_matches_type(GroupCreateResponse, group, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: DodoPayments) -> None:
        response = client.product_collections.groups.with_raw_response.create(
            id="id",
            products=[{"product_id": "product_id"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = response.parse()
        assert_matches_type(GroupCreateResponse, group, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: DodoPayments) -> None:
        with client.product_collections.groups.with_streaming_response.create(
            id="id",
            products=[{"product_id": "product_id"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = response.parse()
            assert_matches_type(GroupCreateResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.product_collections.groups.with_raw_response.create(
                id="",
                products=[{"product_id": "product_id"}],
            )

    @parametrize
    def test_method_update(self, client: DodoPayments) -> None:
        group = client.product_collections.groups.update(
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="id",
        )
        assert group is None

    @parametrize
    def test_method_update_with_all_params(self, client: DodoPayments) -> None:
        group = client.product_collections.groups.update(
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="id",
            group_name="group_name",
            product_order=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            status=True,
        )
        assert group is None

    @parametrize
    def test_raw_response_update(self, client: DodoPayments) -> None:
        response = client.product_collections.groups.with_raw_response.update(
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = response.parse()
        assert group is None

    @parametrize
    def test_streaming_response_update(self, client: DodoPayments) -> None:
        with client.product_collections.groups.with_streaming_response.update(
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = response.parse()
            assert group is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.product_collections.groups.with_raw_response.update(
                group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            client.product_collections.groups.with_raw_response.update(
                group_id="",
                id="id",
            )

    @parametrize
    def test_method_delete(self, client: DodoPayments) -> None:
        group = client.product_collections.groups.delete(
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="id",
        )
        assert group is None

    @parametrize
    def test_raw_response_delete(self, client: DodoPayments) -> None:
        response = client.product_collections.groups.with_raw_response.delete(
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = response.parse()
        assert group is None

    @parametrize
    def test_streaming_response_delete(self, client: DodoPayments) -> None:
        with client.product_collections.groups.with_streaming_response.delete(
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = response.parse()
            assert group is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.product_collections.groups.with_raw_response.delete(
                group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            client.product_collections.groups.with_raw_response.delete(
                group_id="",
                id="id",
            )


class TestAsyncGroups:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncDodoPayments) -> None:
        group = await async_client.product_collections.groups.create(
            id="id",
            products=[{"product_id": "product_id"}],
        )
        assert_matches_type(GroupCreateResponse, group, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDodoPayments) -> None:
        group = await async_client.product_collections.groups.create(
            id="id",
            products=[
                {
                    "product_id": "product_id",
                    "status": True,
                }
            ],
            group_name="group_name",
            status=True,
        )
        assert_matches_type(GroupCreateResponse, group, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.product_collections.groups.with_raw_response.create(
            id="id",
            products=[{"product_id": "product_id"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = await response.parse()
        assert_matches_type(GroupCreateResponse, group, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.product_collections.groups.with_streaming_response.create(
            id="id",
            products=[{"product_id": "product_id"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = await response.parse()
            assert_matches_type(GroupCreateResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.product_collections.groups.with_raw_response.create(
                id="",
                products=[{"product_id": "product_id"}],
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncDodoPayments) -> None:
        group = await async_client.product_collections.groups.update(
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="id",
        )
        assert group is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncDodoPayments) -> None:
        group = await async_client.product_collections.groups.update(
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="id",
            group_name="group_name",
            product_order=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            status=True,
        )
        assert group is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.product_collections.groups.with_raw_response.update(
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = await response.parse()
        assert group is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.product_collections.groups.with_streaming_response.update(
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = await response.parse()
            assert group is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.product_collections.groups.with_raw_response.update(
                group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            await async_client.product_collections.groups.with_raw_response.update(
                group_id="",
                id="id",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncDodoPayments) -> None:
        group = await async_client.product_collections.groups.delete(
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="id",
        )
        assert group is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.product_collections.groups.with_raw_response.delete(
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = await response.parse()
        assert group is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.product_collections.groups.with_streaming_response.delete(
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = await response.parse()
            assert group is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.product_collections.groups.with_raw_response.delete(
                group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            await async_client.product_collections.groups.with_raw_response.delete(
                group_id="",
                id="id",
            )
