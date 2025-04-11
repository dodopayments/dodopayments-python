# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from dodopayments import DodoPayments, AsyncDodoPayments
from dodopayments.types import LicenseKey
from dodopayments._utils import parse_datetime
from dodopayments.pagination import SyncDefaultPageNumberPagination, AsyncDefaultPageNumberPagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLicenseKeys:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: DodoPayments) -> None:
        license_key = client.license_keys.retrieve(
            "id",
        )
        assert_matches_type(LicenseKey, license_key, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: DodoPayments) -> None:
        response = client.license_keys.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        license_key = response.parse()
        assert_matches_type(LicenseKey, license_key, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: DodoPayments) -> None:
        with client.license_keys.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            license_key = response.parse()
            assert_matches_type(LicenseKey, license_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.license_keys.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: DodoPayments) -> None:
        license_key = client.license_keys.update(
            id="lic_123",
        )
        assert_matches_type(LicenseKey, license_key, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: DodoPayments) -> None:
        license_key = client.license_keys.update(
            id="lic_123",
            activations_limit=0,
            disabled=True,
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(LicenseKey, license_key, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: DodoPayments) -> None:
        response = client.license_keys.with_raw_response.update(
            id="lic_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        license_key = response.parse()
        assert_matches_type(LicenseKey, license_key, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: DodoPayments) -> None:
        with client.license_keys.with_streaming_response.update(
            id="lic_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            license_key = response.parse()
            assert_matches_type(LicenseKey, license_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.license_keys.with_raw_response.update(
                id="",
            )

    @parametrize
    def test_method_list(self, client: DodoPayments) -> None:
        license_key = client.license_keys.list()
        assert_matches_type(SyncDefaultPageNumberPagination[LicenseKey], license_key, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: DodoPayments) -> None:
        license_key = client.license_keys.list(
            customer_id="customer_id",
            page_number=0,
            page_size=0,
            product_id="product_id",
            status="active",
        )
        assert_matches_type(SyncDefaultPageNumberPagination[LicenseKey], license_key, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: DodoPayments) -> None:
        response = client.license_keys.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        license_key = response.parse()
        assert_matches_type(SyncDefaultPageNumberPagination[LicenseKey], license_key, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: DodoPayments) -> None:
        with client.license_keys.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            license_key = response.parse()
            assert_matches_type(SyncDefaultPageNumberPagination[LicenseKey], license_key, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLicenseKeys:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDodoPayments) -> None:
        license_key = await async_client.license_keys.retrieve(
            "id",
        )
        assert_matches_type(LicenseKey, license_key, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.license_keys.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        license_key = await response.parse()
        assert_matches_type(LicenseKey, license_key, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.license_keys.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            license_key = await response.parse()
            assert_matches_type(LicenseKey, license_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.license_keys.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncDodoPayments) -> None:
        license_key = await async_client.license_keys.update(
            id="lic_123",
        )
        assert_matches_type(LicenseKey, license_key, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncDodoPayments) -> None:
        license_key = await async_client.license_keys.update(
            id="lic_123",
            activations_limit=0,
            disabled=True,
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(LicenseKey, license_key, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.license_keys.with_raw_response.update(
            id="lic_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        license_key = await response.parse()
        assert_matches_type(LicenseKey, license_key, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.license_keys.with_streaming_response.update(
            id="lic_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            license_key = await response.parse()
            assert_matches_type(LicenseKey, license_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.license_keys.with_raw_response.update(
                id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncDodoPayments) -> None:
        license_key = await async_client.license_keys.list()
        assert_matches_type(AsyncDefaultPageNumberPagination[LicenseKey], license_key, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDodoPayments) -> None:
        license_key = await async_client.license_keys.list(
            customer_id="customer_id",
            page_number=0,
            page_size=0,
            product_id="product_id",
            status="active",
        )
        assert_matches_type(AsyncDefaultPageNumberPagination[LicenseKey], license_key, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.license_keys.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        license_key = await response.parse()
        assert_matches_type(AsyncDefaultPageNumberPagination[LicenseKey], license_key, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.license_keys.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            license_key = await response.parse()
            assert_matches_type(AsyncDefaultPageNumberPagination[LicenseKey], license_key, path=["response"])

        assert cast(Any, response.is_closed) is True
