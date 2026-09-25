# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from dodopayments import DodoPayments, AsyncDodoPayments
from dodopayments.types import ModerationScreenResponse, ModerationRetrieveUsageResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestModeration:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve_usage(self, client: DodoPayments) -> None:
        moderation = client.moderation.retrieve_usage()
        assert_matches_type(ModerationRetrieveUsageResponse, moderation, path=["response"])

    @parametrize
    def test_raw_response_retrieve_usage(self, client: DodoPayments) -> None:
        response = client.moderation.with_raw_response.retrieve_usage()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        moderation = response.parse()
        assert_matches_type(ModerationRetrieveUsageResponse, moderation, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_usage(self, client: DodoPayments) -> None:
        with client.moderation.with_streaming_response.retrieve_usage() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            moderation = response.parse()
            assert_matches_type(ModerationRetrieveUsageResponse, moderation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_screen(self, client: DodoPayments) -> None:
        moderation = client.moderation.screen()
        assert_matches_type(ModerationScreenResponse, moderation, path=["response"])

    @parametrize
    def test_method_screen_with_all_params(self, client: DodoPayments) -> None:
        moderation = client.moderation.screen(
            image="image",
            request_id="request_id",
            text="text",
        )
        assert_matches_type(ModerationScreenResponse, moderation, path=["response"])

    @parametrize
    def test_raw_response_screen(self, client: DodoPayments) -> None:
        response = client.moderation.with_raw_response.screen()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        moderation = response.parse()
        assert_matches_type(ModerationScreenResponse, moderation, path=["response"])

    @parametrize
    def test_streaming_response_screen(self, client: DodoPayments) -> None:
        with client.moderation.with_streaming_response.screen() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            moderation = response.parse()
            assert_matches_type(ModerationScreenResponse, moderation, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncModeration:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve_usage(self, async_client: AsyncDodoPayments) -> None:
        moderation = await async_client.moderation.retrieve_usage()
        assert_matches_type(ModerationRetrieveUsageResponse, moderation, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_usage(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.moderation.with_raw_response.retrieve_usage()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        moderation = await response.parse()
        assert_matches_type(ModerationRetrieveUsageResponse, moderation, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_usage(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.moderation.with_streaming_response.retrieve_usage() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            moderation = await response.parse()
            assert_matches_type(ModerationRetrieveUsageResponse, moderation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_screen(self, async_client: AsyncDodoPayments) -> None:
        moderation = await async_client.moderation.screen()
        assert_matches_type(ModerationScreenResponse, moderation, path=["response"])

    @parametrize
    async def test_method_screen_with_all_params(self, async_client: AsyncDodoPayments) -> None:
        moderation = await async_client.moderation.screen(
            image="image",
            request_id="request_id",
            text="text",
        )
        assert_matches_type(ModerationScreenResponse, moderation, path=["response"])

    @parametrize
    async def test_raw_response_screen(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.moderation.with_raw_response.screen()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        moderation = await response.parse()
        assert_matches_type(ModerationScreenResponse, moderation, path=["response"])

    @parametrize
    async def test_streaming_response_screen(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.moderation.with_streaming_response.screen() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            moderation = await response.parse()
            assert_matches_type(ModerationScreenResponse, moderation, path=["response"])

        assert cast(Any, response.is_closed) is True
