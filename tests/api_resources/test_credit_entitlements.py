# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from dodopayments import DodoPayments, AsyncDodoPayments
from dodopayments.types import (
    CreditEntitlement,
)
from dodopayments.pagination import SyncDefaultPageNumberPagination, AsyncDefaultPageNumberPagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCreditEntitlements:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: DodoPayments) -> None:
        credit_entitlement = client.credit_entitlements.create(
            name="name",
            overage_enabled=True,
            precision=0,
            rollover_enabled=True,
            unit="unit",
        )
        assert_matches_type(CreditEntitlement, credit_entitlement, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: DodoPayments) -> None:
        credit_entitlement = client.credit_entitlements.create(
            name="name",
            overage_enabled=True,
            precision=0,
            rollover_enabled=True,
            unit="unit",
            currency="AED",
            description="description",
            expires_after_days=0,
            max_rollover_count=0,
            overage_behavior="forgive_at_reset",
            overage_limit=0,
            price_per_unit="price_per_unit",
            rollover_percentage=0,
            rollover_timeframe_count=0,
            rollover_timeframe_interval="Day",
        )
        assert_matches_type(CreditEntitlement, credit_entitlement, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: DodoPayments) -> None:
        response = client.credit_entitlements.with_raw_response.create(
            name="name",
            overage_enabled=True,
            precision=0,
            rollover_enabled=True,
            unit="unit",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_entitlement = response.parse()
        assert_matches_type(CreditEntitlement, credit_entitlement, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: DodoPayments) -> None:
        with client.credit_entitlements.with_streaming_response.create(
            name="name",
            overage_enabled=True,
            precision=0,
            rollover_enabled=True,
            unit="unit",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_entitlement = response.parse()
            assert_matches_type(CreditEntitlement, credit_entitlement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: DodoPayments) -> None:
        credit_entitlement = client.credit_entitlements.retrieve(
            "id",
        )
        assert_matches_type(CreditEntitlement, credit_entitlement, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: DodoPayments) -> None:
        response = client.credit_entitlements.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_entitlement = response.parse()
        assert_matches_type(CreditEntitlement, credit_entitlement, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: DodoPayments) -> None:
        with client.credit_entitlements.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_entitlement = response.parse()
            assert_matches_type(CreditEntitlement, credit_entitlement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.credit_entitlements.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: DodoPayments) -> None:
        credit_entitlement = client.credit_entitlements.update(
            id="id",
        )
        assert credit_entitlement is None

    @parametrize
    def test_method_update_with_all_params(self, client: DodoPayments) -> None:
        credit_entitlement = client.credit_entitlements.update(
            id="id",
            currency="AED",
            description="description",
            expires_after_days=0,
            max_rollover_count=0,
            name="name",
            overage_behavior="forgive_at_reset",
            overage_enabled=True,
            overage_limit=0,
            price_per_unit="price_per_unit",
            rollover_enabled=True,
            rollover_percentage=0,
            rollover_timeframe_count=0,
            rollover_timeframe_interval="Day",
            unit="unit",
        )
        assert credit_entitlement is None

    @parametrize
    def test_raw_response_update(self, client: DodoPayments) -> None:
        response = client.credit_entitlements.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_entitlement = response.parse()
        assert credit_entitlement is None

    @parametrize
    def test_streaming_response_update(self, client: DodoPayments) -> None:
        with client.credit_entitlements.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_entitlement = response.parse()
            assert credit_entitlement is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.credit_entitlements.with_raw_response.update(
                id="",
            )

    @parametrize
    def test_method_list(self, client: DodoPayments) -> None:
        credit_entitlement = client.credit_entitlements.list()
        assert_matches_type(SyncDefaultPageNumberPagination[CreditEntitlement], credit_entitlement, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: DodoPayments) -> None:
        credit_entitlement = client.credit_entitlements.list(
            deleted=True,
            page_number=0,
            page_size=0,
        )
        assert_matches_type(SyncDefaultPageNumberPagination[CreditEntitlement], credit_entitlement, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: DodoPayments) -> None:
        response = client.credit_entitlements.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_entitlement = response.parse()
        assert_matches_type(SyncDefaultPageNumberPagination[CreditEntitlement], credit_entitlement, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: DodoPayments) -> None:
        with client.credit_entitlements.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_entitlement = response.parse()
            assert_matches_type(
                SyncDefaultPageNumberPagination[CreditEntitlement], credit_entitlement, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: DodoPayments) -> None:
        credit_entitlement = client.credit_entitlements.delete(
            "id",
        )
        assert credit_entitlement is None

    @parametrize
    def test_raw_response_delete(self, client: DodoPayments) -> None:
        response = client.credit_entitlements.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_entitlement = response.parse()
        assert credit_entitlement is None

    @parametrize
    def test_streaming_response_delete(self, client: DodoPayments) -> None:
        with client.credit_entitlements.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_entitlement = response.parse()
            assert credit_entitlement is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.credit_entitlements.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_undelete(self, client: DodoPayments) -> None:
        credit_entitlement = client.credit_entitlements.undelete(
            "id",
        )
        assert credit_entitlement is None

    @parametrize
    def test_raw_response_undelete(self, client: DodoPayments) -> None:
        response = client.credit_entitlements.with_raw_response.undelete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_entitlement = response.parse()
        assert credit_entitlement is None

    @parametrize
    def test_streaming_response_undelete(self, client: DodoPayments) -> None:
        with client.credit_entitlements.with_streaming_response.undelete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_entitlement = response.parse()
            assert credit_entitlement is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_undelete(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.credit_entitlements.with_raw_response.undelete(
                "",
            )


class TestAsyncCreditEntitlements:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncDodoPayments) -> None:
        credit_entitlement = await async_client.credit_entitlements.create(
            name="name",
            overage_enabled=True,
            precision=0,
            rollover_enabled=True,
            unit="unit",
        )
        assert_matches_type(CreditEntitlement, credit_entitlement, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDodoPayments) -> None:
        credit_entitlement = await async_client.credit_entitlements.create(
            name="name",
            overage_enabled=True,
            precision=0,
            rollover_enabled=True,
            unit="unit",
            currency="AED",
            description="description",
            expires_after_days=0,
            max_rollover_count=0,
            overage_behavior="forgive_at_reset",
            overage_limit=0,
            price_per_unit="price_per_unit",
            rollover_percentage=0,
            rollover_timeframe_count=0,
            rollover_timeframe_interval="Day",
        )
        assert_matches_type(CreditEntitlement, credit_entitlement, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.credit_entitlements.with_raw_response.create(
            name="name",
            overage_enabled=True,
            precision=0,
            rollover_enabled=True,
            unit="unit",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_entitlement = await response.parse()
        assert_matches_type(CreditEntitlement, credit_entitlement, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.credit_entitlements.with_streaming_response.create(
            name="name",
            overage_enabled=True,
            precision=0,
            rollover_enabled=True,
            unit="unit",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_entitlement = await response.parse()
            assert_matches_type(CreditEntitlement, credit_entitlement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDodoPayments) -> None:
        credit_entitlement = await async_client.credit_entitlements.retrieve(
            "id",
        )
        assert_matches_type(CreditEntitlement, credit_entitlement, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.credit_entitlements.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_entitlement = await response.parse()
        assert_matches_type(CreditEntitlement, credit_entitlement, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.credit_entitlements.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_entitlement = await response.parse()
            assert_matches_type(CreditEntitlement, credit_entitlement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.credit_entitlements.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncDodoPayments) -> None:
        credit_entitlement = await async_client.credit_entitlements.update(
            id="id",
        )
        assert credit_entitlement is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncDodoPayments) -> None:
        credit_entitlement = await async_client.credit_entitlements.update(
            id="id",
            currency="AED",
            description="description",
            expires_after_days=0,
            max_rollover_count=0,
            name="name",
            overage_behavior="forgive_at_reset",
            overage_enabled=True,
            overage_limit=0,
            price_per_unit="price_per_unit",
            rollover_enabled=True,
            rollover_percentage=0,
            rollover_timeframe_count=0,
            rollover_timeframe_interval="Day",
            unit="unit",
        )
        assert credit_entitlement is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.credit_entitlements.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_entitlement = await response.parse()
        assert credit_entitlement is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.credit_entitlements.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_entitlement = await response.parse()
            assert credit_entitlement is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.credit_entitlements.with_raw_response.update(
                id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncDodoPayments) -> None:
        credit_entitlement = await async_client.credit_entitlements.list()
        assert_matches_type(AsyncDefaultPageNumberPagination[CreditEntitlement], credit_entitlement, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDodoPayments) -> None:
        credit_entitlement = await async_client.credit_entitlements.list(
            deleted=True,
            page_number=0,
            page_size=0,
        )
        assert_matches_type(AsyncDefaultPageNumberPagination[CreditEntitlement], credit_entitlement, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.credit_entitlements.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_entitlement = await response.parse()
        assert_matches_type(AsyncDefaultPageNumberPagination[CreditEntitlement], credit_entitlement, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.credit_entitlements.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_entitlement = await response.parse()
            assert_matches_type(
                AsyncDefaultPageNumberPagination[CreditEntitlement], credit_entitlement, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncDodoPayments) -> None:
        credit_entitlement = await async_client.credit_entitlements.delete(
            "id",
        )
        assert credit_entitlement is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.credit_entitlements.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_entitlement = await response.parse()
        assert credit_entitlement is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.credit_entitlements.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_entitlement = await response.parse()
            assert credit_entitlement is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.credit_entitlements.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_undelete(self, async_client: AsyncDodoPayments) -> None:
        credit_entitlement = await async_client.credit_entitlements.undelete(
            "id",
        )
        assert credit_entitlement is None

    @parametrize
    async def test_raw_response_undelete(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.credit_entitlements.with_raw_response.undelete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_entitlement = await response.parse()
        assert credit_entitlement is None

    @parametrize
    async def test_streaming_response_undelete(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.credit_entitlements.with_streaming_response.undelete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_entitlement = await response.parse()
            assert credit_entitlement is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_undelete(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.credit_entitlements.with_raw_response.undelete(
                "",
            )
