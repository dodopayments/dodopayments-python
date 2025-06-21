# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from dodopayments import DodoPayments, AsyncDodoPayments
from dodopayments.types import (
    LicenseKeyInstance,
    LicenseValidateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLicenses:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_activate(self, client: DodoPayments) -> None:
        license = client.licenses.activate(
            license_key="license_key",
            name="name",
        )
        assert_matches_type(LicenseKeyInstance, license, path=["response"])

    @parametrize
    def test_raw_response_activate(self, client: DodoPayments) -> None:
        response = client.licenses.with_raw_response.activate(
            license_key="license_key",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        license = response.parse()
        assert_matches_type(LicenseKeyInstance, license, path=["response"])

    @parametrize
    def test_streaming_response_activate(self, client: DodoPayments) -> None:
        with client.licenses.with_streaming_response.activate(
            license_key="license_key",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            license = response.parse()
            assert_matches_type(LicenseKeyInstance, license, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_deactivate(self, client: DodoPayments) -> None:
        license = client.licenses.deactivate(
            license_key="license_key",
            license_key_instance_id="license_key_instance_id",
        )
        assert license is None

    @parametrize
    def test_raw_response_deactivate(self, client: DodoPayments) -> None:
        response = client.licenses.with_raw_response.deactivate(
            license_key="license_key",
            license_key_instance_id="license_key_instance_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        license = response.parse()
        assert license is None

    @parametrize
    def test_streaming_response_deactivate(self, client: DodoPayments) -> None:
        with client.licenses.with_streaming_response.deactivate(
            license_key="license_key",
            license_key_instance_id="license_key_instance_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            license = response.parse()
            assert license is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_validate(self, client: DodoPayments) -> None:
        license = client.licenses.validate(
            license_key="2b1f8e2d-c41e-4e8f-b2d3-d9fd61c38f43",
        )
        assert_matches_type(LicenseValidateResponse, license, path=["response"])

    @parametrize
    def test_method_validate_with_all_params(self, client: DodoPayments) -> None:
        license = client.licenses.validate(
            license_key="2b1f8e2d-c41e-4e8f-b2d3-d9fd61c38f43",
            license_key_instance_id="lki_123",
        )
        assert_matches_type(LicenseValidateResponse, license, path=["response"])

    @parametrize
    def test_raw_response_validate(self, client: DodoPayments) -> None:
        response = client.licenses.with_raw_response.validate(
            license_key="2b1f8e2d-c41e-4e8f-b2d3-d9fd61c38f43",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        license = response.parse()
        assert_matches_type(LicenseValidateResponse, license, path=["response"])

    @parametrize
    def test_streaming_response_validate(self, client: DodoPayments) -> None:
        with client.licenses.with_streaming_response.validate(
            license_key="2b1f8e2d-c41e-4e8f-b2d3-d9fd61c38f43",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            license = response.parse()
            assert_matches_type(LicenseValidateResponse, license, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLicenses:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_activate(self, async_client: AsyncDodoPayments) -> None:
        license = await async_client.licenses.activate(
            license_key="license_key",
            name="name",
        )
        assert_matches_type(LicenseKeyInstance, license, path=["response"])

    @parametrize
    async def test_raw_response_activate(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.licenses.with_raw_response.activate(
            license_key="license_key",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        license = await response.parse()
        assert_matches_type(LicenseKeyInstance, license, path=["response"])

    @parametrize
    async def test_streaming_response_activate(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.licenses.with_streaming_response.activate(
            license_key="license_key",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            license = await response.parse()
            assert_matches_type(LicenseKeyInstance, license, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_deactivate(self, async_client: AsyncDodoPayments) -> None:
        license = await async_client.licenses.deactivate(
            license_key="license_key",
            license_key_instance_id="license_key_instance_id",
        )
        assert license is None

    @parametrize
    async def test_raw_response_deactivate(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.licenses.with_raw_response.deactivate(
            license_key="license_key",
            license_key_instance_id="license_key_instance_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        license = await response.parse()
        assert license is None

    @parametrize
    async def test_streaming_response_deactivate(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.licenses.with_streaming_response.deactivate(
            license_key="license_key",
            license_key_instance_id="license_key_instance_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            license = await response.parse()
            assert license is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_validate(self, async_client: AsyncDodoPayments) -> None:
        license = await async_client.licenses.validate(
            license_key="2b1f8e2d-c41e-4e8f-b2d3-d9fd61c38f43",
        )
        assert_matches_type(LicenseValidateResponse, license, path=["response"])

    @parametrize
    async def test_method_validate_with_all_params(self, async_client: AsyncDodoPayments) -> None:
        license = await async_client.licenses.validate(
            license_key="2b1f8e2d-c41e-4e8f-b2d3-d9fd61c38f43",
            license_key_instance_id="lki_123",
        )
        assert_matches_type(LicenseValidateResponse, license, path=["response"])

    @parametrize
    async def test_raw_response_validate(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.licenses.with_raw_response.validate(
            license_key="2b1f8e2d-c41e-4e8f-b2d3-d9fd61c38f43",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        license = await response.parse()
        assert_matches_type(LicenseValidateResponse, license, path=["response"])

    @parametrize
    async def test_streaming_response_validate(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.licenses.with_streaming_response.validate(
            license_key="2b1f8e2d-c41e-4e8f-b2d3-d9fd61c38f43",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            license = await response.parse()
            assert_matches_type(LicenseValidateResponse, license, path=["response"])

        assert cast(Any, response.is_closed) is True
