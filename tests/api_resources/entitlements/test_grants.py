# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from dodopayments import DodoPayments, AsyncDodoPayments
from dodopayments.pagination import SyncDefaultPageNumberPagination, AsyncDefaultPageNumberPagination
from dodopayments.types.entitlements import EntitlementGrant

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGrants:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: DodoPayments) -> None:
        grant = client.entitlements.grants.list(
            id="id",
        )
        assert_matches_type(SyncDefaultPageNumberPagination[EntitlementGrant], grant, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: DodoPayments) -> None:
        grant = client.entitlements.grants.list(
            id="id",
            customer_id="customer_id",
            page_number=0,
            page_size=0,
            status="Pending",
        )
        assert_matches_type(SyncDefaultPageNumberPagination[EntitlementGrant], grant, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: DodoPayments) -> None:
        response = client.entitlements.grants.with_raw_response.list(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        grant = response.parse()
        assert_matches_type(SyncDefaultPageNumberPagination[EntitlementGrant], grant, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: DodoPayments) -> None:
        with client.entitlements.grants.with_streaming_response.list(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            grant = response.parse()
            assert_matches_type(SyncDefaultPageNumberPagination[EntitlementGrant], grant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.entitlements.grants.with_raw_response.list(
                id="",
            )

    @parametrize
    def test_method_revoke(self, client: DodoPayments) -> None:
        grant = client.entitlements.grants.revoke(
            grant_id="grant_id",
            id="id",
        )
        assert_matches_type(EntitlementGrant, grant, path=["response"])

    @parametrize
    def test_raw_response_revoke(self, client: DodoPayments) -> None:
        response = client.entitlements.grants.with_raw_response.revoke(
            grant_id="grant_id",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        grant = response.parse()
        assert_matches_type(EntitlementGrant, grant, path=["response"])

    @parametrize
    def test_streaming_response_revoke(self, client: DodoPayments) -> None:
        with client.entitlements.grants.with_streaming_response.revoke(
            grant_id="grant_id",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            grant = response.parse()
            assert_matches_type(EntitlementGrant, grant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_revoke(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.entitlements.grants.with_raw_response.revoke(
                grant_id="grant_id",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `grant_id` but received ''"):
            client.entitlements.grants.with_raw_response.revoke(
                grant_id="",
                id="id",
            )


class TestAsyncGrants:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncDodoPayments) -> None:
        grant = await async_client.entitlements.grants.list(
            id="id",
        )
        assert_matches_type(AsyncDefaultPageNumberPagination[EntitlementGrant], grant, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDodoPayments) -> None:
        grant = await async_client.entitlements.grants.list(
            id="id",
            customer_id="customer_id",
            page_number=0,
            page_size=0,
            status="Pending",
        )
        assert_matches_type(AsyncDefaultPageNumberPagination[EntitlementGrant], grant, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.entitlements.grants.with_raw_response.list(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        grant = await response.parse()
        assert_matches_type(AsyncDefaultPageNumberPagination[EntitlementGrant], grant, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.entitlements.grants.with_streaming_response.list(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            grant = await response.parse()
            assert_matches_type(AsyncDefaultPageNumberPagination[EntitlementGrant], grant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.entitlements.grants.with_raw_response.list(
                id="",
            )

    @parametrize
    async def test_method_revoke(self, async_client: AsyncDodoPayments) -> None:
        grant = await async_client.entitlements.grants.revoke(
            grant_id="grant_id",
            id="id",
        )
        assert_matches_type(EntitlementGrant, grant, path=["response"])

    @parametrize
    async def test_raw_response_revoke(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.entitlements.grants.with_raw_response.revoke(
            grant_id="grant_id",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        grant = await response.parse()
        assert_matches_type(EntitlementGrant, grant, path=["response"])

    @parametrize
    async def test_streaming_response_revoke(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.entitlements.grants.with_streaming_response.revoke(
            grant_id="grant_id",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            grant = await response.parse()
            assert_matches_type(EntitlementGrant, grant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_revoke(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.entitlements.grants.with_raw_response.revoke(
                grant_id="grant_id",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `grant_id` but received ''"):
            await async_client.entitlements.grants.with_raw_response.revoke(
                grant_id="",
                id="id",
            )
