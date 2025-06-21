# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from dodopayments import DodoPayments, AsyncDodoPayments
from dodopayments.types import MiscListSupportedCountriesResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMisc:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list_supported_countries(self, client: DodoPayments) -> None:
        misc = client.misc.list_supported_countries()
        assert_matches_type(MiscListSupportedCountriesResponse, misc, path=["response"])

    @parametrize
    def test_raw_response_list_supported_countries(self, client: DodoPayments) -> None:
        response = client.misc.with_raw_response.list_supported_countries()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        misc = response.parse()
        assert_matches_type(MiscListSupportedCountriesResponse, misc, path=["response"])

    @parametrize
    def test_streaming_response_list_supported_countries(self, client: DodoPayments) -> None:
        with client.misc.with_streaming_response.list_supported_countries() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            misc = response.parse()
            assert_matches_type(MiscListSupportedCountriesResponse, misc, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMisc:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list_supported_countries(self, async_client: AsyncDodoPayments) -> None:
        misc = await async_client.misc.list_supported_countries()
        assert_matches_type(MiscListSupportedCountriesResponse, misc, path=["response"])

    @parametrize
    async def test_raw_response_list_supported_countries(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.misc.with_raw_response.list_supported_countries()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        misc = await response.parse()
        assert_matches_type(MiscListSupportedCountriesResponse, misc, path=["response"])

    @parametrize
    async def test_streaming_response_list_supported_countries(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.misc.with_streaming_response.list_supported_countries() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            misc = await response.parse()
            assert_matches_type(MiscListSupportedCountriesResponse, misc, path=["response"])

        assert cast(Any, response.is_closed) is True
