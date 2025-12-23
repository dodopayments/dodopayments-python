# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from dodopayments import DodoPayments, AsyncDodoPayments
from dodopayments.pagination import SyncDefaultPageNumberPagination, AsyncDefaultPageNumberPagination
from dodopayments.types.products import (
    ShortLinkListResponse,
    ShortLinkCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestShortLinks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: DodoPayments) -> None:
        short_link = client.products.short_links.create(
            id="id",
            slug="slug",
        )
        assert_matches_type(ShortLinkCreateResponse, short_link, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: DodoPayments) -> None:
        short_link = client.products.short_links.create(
            id="id",
            slug="slug",
            static_checkout_params={"foo": "string"},
        )
        assert_matches_type(ShortLinkCreateResponse, short_link, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: DodoPayments) -> None:
        response = client.products.short_links.with_raw_response.create(
            id="id",
            slug="slug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        short_link = response.parse()
        assert_matches_type(ShortLinkCreateResponse, short_link, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: DodoPayments) -> None:
        with client.products.short_links.with_streaming_response.create(
            id="id",
            slug="slug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            short_link = response.parse()
            assert_matches_type(ShortLinkCreateResponse, short_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.products.short_links.with_raw_response.create(
                id="",
                slug="slug",
            )

    @parametrize
    def test_method_list(self, client: DodoPayments) -> None:
        short_link = client.products.short_links.list()
        assert_matches_type(SyncDefaultPageNumberPagination[ShortLinkListResponse], short_link, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: DodoPayments) -> None:
        short_link = client.products.short_links.list(
            page_number=0,
            page_size=0,
            product_id="product_id",
        )
        assert_matches_type(SyncDefaultPageNumberPagination[ShortLinkListResponse], short_link, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: DodoPayments) -> None:
        response = client.products.short_links.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        short_link = response.parse()
        assert_matches_type(SyncDefaultPageNumberPagination[ShortLinkListResponse], short_link, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: DodoPayments) -> None:
        with client.products.short_links.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            short_link = response.parse()
            assert_matches_type(SyncDefaultPageNumberPagination[ShortLinkListResponse], short_link, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncShortLinks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncDodoPayments) -> None:
        short_link = await async_client.products.short_links.create(
            id="id",
            slug="slug",
        )
        assert_matches_type(ShortLinkCreateResponse, short_link, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDodoPayments) -> None:
        short_link = await async_client.products.short_links.create(
            id="id",
            slug="slug",
            static_checkout_params={"foo": "string"},
        )
        assert_matches_type(ShortLinkCreateResponse, short_link, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.products.short_links.with_raw_response.create(
            id="id",
            slug="slug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        short_link = await response.parse()
        assert_matches_type(ShortLinkCreateResponse, short_link, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.products.short_links.with_streaming_response.create(
            id="id",
            slug="slug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            short_link = await response.parse()
            assert_matches_type(ShortLinkCreateResponse, short_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.products.short_links.with_raw_response.create(
                id="",
                slug="slug",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncDodoPayments) -> None:
        short_link = await async_client.products.short_links.list()
        assert_matches_type(AsyncDefaultPageNumberPagination[ShortLinkListResponse], short_link, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDodoPayments) -> None:
        short_link = await async_client.products.short_links.list(
            page_number=0,
            page_size=0,
            product_id="product_id",
        )
        assert_matches_type(AsyncDefaultPageNumberPagination[ShortLinkListResponse], short_link, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.products.short_links.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        short_link = await response.parse()
        assert_matches_type(AsyncDefaultPageNumberPagination[ShortLinkListResponse], short_link, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.products.short_links.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            short_link = await response.parse()
            assert_matches_type(AsyncDefaultPageNumberPagination[ShortLinkListResponse], short_link, path=["response"])

        assert cast(Any, response.is_closed) is True
