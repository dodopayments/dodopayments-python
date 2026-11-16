# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from dodopayments import DodoPayments, AsyncDodoPayments
from dodopayments.types import AppInstallationRetrieveSettingsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAppInstallation:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve_settings(self, client: DodoPayments) -> None:
        app_installation = client.app_installation.retrieve_settings()
        assert_matches_type(AppInstallationRetrieveSettingsResponse, app_installation, path=["response"])

    @parametrize
    def test_raw_response_retrieve_settings(self, client: DodoPayments) -> None:
        response = client.app_installation.with_raw_response.retrieve_settings()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app_installation = response.parse()
        assert_matches_type(AppInstallationRetrieveSettingsResponse, app_installation, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_settings(self, client: DodoPayments) -> None:
        with client.app_installation.with_streaming_response.retrieve_settings() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app_installation = response.parse()
            assert_matches_type(AppInstallationRetrieveSettingsResponse, app_installation, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAppInstallation:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve_settings(self, async_client: AsyncDodoPayments) -> None:
        app_installation = await async_client.app_installation.retrieve_settings()
        assert_matches_type(AppInstallationRetrieveSettingsResponse, app_installation, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_settings(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.app_installation.with_raw_response.retrieve_settings()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app_installation = await response.parse()
        assert_matches_type(AppInstallationRetrieveSettingsResponse, app_installation, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_settings(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.app_installation.with_streaming_response.retrieve_settings() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app_installation = await response.parse()
            assert_matches_type(AppInstallationRetrieveSettingsResponse, app_installation, path=["response"])

        assert cast(Any, response.is_closed) is True
