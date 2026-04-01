# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from dodopayments import DodoPayments, AsyncDodoPayments
from dodopayments.pagination import SyncDefaultPageNumberPagination, AsyncDefaultPageNumberPagination
from dodopayments.types.payouts.breakup import DetailListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDetails:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: DodoPayments) -> None:
        detail = client.payouts.breakup.details.list(
            payout_id="payout_id",
        )
        assert_matches_type(SyncDefaultPageNumberPagination[DetailListResponse], detail, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: DodoPayments) -> None:
        detail = client.payouts.breakup.details.list(
            payout_id="payout_id",
            page_number=0,
            page_size=0,
        )
        assert_matches_type(SyncDefaultPageNumberPagination[DetailListResponse], detail, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: DodoPayments) -> None:
        response = client.payouts.breakup.details.with_raw_response.list(
            payout_id="payout_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        detail = response.parse()
        assert_matches_type(SyncDefaultPageNumberPagination[DetailListResponse], detail, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: DodoPayments) -> None:
        with client.payouts.breakup.details.with_streaming_response.list(
            payout_id="payout_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            detail = response.parse()
            assert_matches_type(SyncDefaultPageNumberPagination[DetailListResponse], detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `payout_id` but received ''"):
            client.payouts.breakup.details.with_raw_response.list(
                payout_id="",
            )

    @parametrize
    def test_method_download_csv(self, client: DodoPayments) -> None:
        detail = client.payouts.breakup.details.download_csv(
            "payout_id",
        )
        assert detail is None

    @parametrize
    def test_raw_response_download_csv(self, client: DodoPayments) -> None:
        response = client.payouts.breakup.details.with_raw_response.download_csv(
            "payout_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        detail = response.parse()
        assert detail is None

    @parametrize
    def test_streaming_response_download_csv(self, client: DodoPayments) -> None:
        with client.payouts.breakup.details.with_streaming_response.download_csv(
            "payout_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            detail = response.parse()
            assert detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_download_csv(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `payout_id` but received ''"):
            client.payouts.breakup.details.with_raw_response.download_csv(
                "",
            )


class TestAsyncDetails:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncDodoPayments) -> None:
        detail = await async_client.payouts.breakup.details.list(
            payout_id="payout_id",
        )
        assert_matches_type(AsyncDefaultPageNumberPagination[DetailListResponse], detail, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDodoPayments) -> None:
        detail = await async_client.payouts.breakup.details.list(
            payout_id="payout_id",
            page_number=0,
            page_size=0,
        )
        assert_matches_type(AsyncDefaultPageNumberPagination[DetailListResponse], detail, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.payouts.breakup.details.with_raw_response.list(
            payout_id="payout_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        detail = await response.parse()
        assert_matches_type(AsyncDefaultPageNumberPagination[DetailListResponse], detail, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.payouts.breakup.details.with_streaming_response.list(
            payout_id="payout_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            detail = await response.parse()
            assert_matches_type(AsyncDefaultPageNumberPagination[DetailListResponse], detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `payout_id` but received ''"):
            await async_client.payouts.breakup.details.with_raw_response.list(
                payout_id="",
            )

    @parametrize
    async def test_method_download_csv(self, async_client: AsyncDodoPayments) -> None:
        detail = await async_client.payouts.breakup.details.download_csv(
            "payout_id",
        )
        assert detail is None

    @parametrize
    async def test_raw_response_download_csv(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.payouts.breakup.details.with_raw_response.download_csv(
            "payout_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        detail = await response.parse()
        assert detail is None

    @parametrize
    async def test_streaming_response_download_csv(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.payouts.breakup.details.with_streaming_response.download_csv(
            "payout_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            detail = await response.parse()
            assert detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_download_csv(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `payout_id` but received ''"):
            await async_client.payouts.breakup.details.with_raw_response.download_csv(
                "",
            )
