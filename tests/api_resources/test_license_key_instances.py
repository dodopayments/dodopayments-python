# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from dodopayments import DodoPayments, AsyncDodoPayments
from dodopayments.types import (
    LicenseKeyInstance,
    LicenseKeyInstanceListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLicenseKeyInstances:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: DodoPayments) -> None:
        license_key_instance = client.license_key_instances.retrieve(
            "id",
        )
        assert_matches_type(LicenseKeyInstance, license_key_instance, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: DodoPayments) -> None:
        response = client.license_key_instances.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        license_key_instance = response.parse()
        assert_matches_type(LicenseKeyInstance, license_key_instance, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: DodoPayments) -> None:
        with client.license_key_instances.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            license_key_instance = response.parse()
            assert_matches_type(LicenseKeyInstance, license_key_instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.license_key_instances.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: DodoPayments) -> None:
        license_key_instance = client.license_key_instances.update(
            id="lki_123",
            name="name",
        )
        assert_matches_type(LicenseKeyInstance, license_key_instance, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: DodoPayments) -> None:
        response = client.license_key_instances.with_raw_response.update(
            id="lki_123",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        license_key_instance = response.parse()
        assert_matches_type(LicenseKeyInstance, license_key_instance, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: DodoPayments) -> None:
        with client.license_key_instances.with_streaming_response.update(
            id="lki_123",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            license_key_instance = response.parse()
            assert_matches_type(LicenseKeyInstance, license_key_instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.license_key_instances.with_raw_response.update(
                id="",
                name="name",
            )

    @parametrize
    def test_method_list(self, client: DodoPayments) -> None:
        license_key_instance = client.license_key_instances.list()
        assert_matches_type(LicenseKeyInstanceListResponse, license_key_instance, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: DodoPayments) -> None:
        license_key_instance = client.license_key_instances.list(
            license_key_id="license_key_id",
            page_number=0,
            page_size=0,
        )
        assert_matches_type(LicenseKeyInstanceListResponse, license_key_instance, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: DodoPayments) -> None:
        response = client.license_key_instances.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        license_key_instance = response.parse()
        assert_matches_type(LicenseKeyInstanceListResponse, license_key_instance, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: DodoPayments) -> None:
        with client.license_key_instances.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            license_key_instance = response.parse()
            assert_matches_type(LicenseKeyInstanceListResponse, license_key_instance, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLicenseKeyInstances:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDodoPayments) -> None:
        license_key_instance = await async_client.license_key_instances.retrieve(
            "id",
        )
        assert_matches_type(LicenseKeyInstance, license_key_instance, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.license_key_instances.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        license_key_instance = await response.parse()
        assert_matches_type(LicenseKeyInstance, license_key_instance, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.license_key_instances.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            license_key_instance = await response.parse()
            assert_matches_type(LicenseKeyInstance, license_key_instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.license_key_instances.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncDodoPayments) -> None:
        license_key_instance = await async_client.license_key_instances.update(
            id="lki_123",
            name="name",
        )
        assert_matches_type(LicenseKeyInstance, license_key_instance, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.license_key_instances.with_raw_response.update(
            id="lki_123",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        license_key_instance = await response.parse()
        assert_matches_type(LicenseKeyInstance, license_key_instance, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.license_key_instances.with_streaming_response.update(
            id="lki_123",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            license_key_instance = await response.parse()
            assert_matches_type(LicenseKeyInstance, license_key_instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.license_key_instances.with_raw_response.update(
                id="",
                name="name",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncDodoPayments) -> None:
        license_key_instance = await async_client.license_key_instances.list()
        assert_matches_type(LicenseKeyInstanceListResponse, license_key_instance, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDodoPayments) -> None:
        license_key_instance = await async_client.license_key_instances.list(
            license_key_id="license_key_id",
            page_number=0,
            page_size=0,
        )
        assert_matches_type(LicenseKeyInstanceListResponse, license_key_instance, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.license_key_instances.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        license_key_instance = await response.parse()
        assert_matches_type(LicenseKeyInstanceListResponse, license_key_instance, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.license_key_instances.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            license_key_instance = await response.parse()
            assert_matches_type(LicenseKeyInstanceListResponse, license_key_instance, path=["response"])

        assert cast(Any, response.is_closed) is True
