# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from dodopayments import Dodopayments, AsyncDodopayments
from dodopayments.types import Dispute, DisputeListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDisputes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Dodopayments) -> None:
        dispute = client.disputes.retrieve(
            "dispute_id",
        )
        assert_matches_type(Dispute, dispute, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Dodopayments) -> None:
        response = client.disputes.with_raw_response.retrieve(
            "dispute_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dispute = response.parse()
        assert_matches_type(Dispute, dispute, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Dodopayments) -> None:
        with client.disputes.with_streaming_response.retrieve(
            "dispute_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dispute = response.parse()
            assert_matches_type(Dispute, dispute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Dodopayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dispute_id` but received ''"):
            client.disputes.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Dodopayments) -> None:
        dispute = client.disputes.list()
        assert_matches_type(DisputeListResponse, dispute, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Dodopayments) -> None:
        dispute = client.disputes.list(
            page_number=0,
            page_size=0,
        )
        assert_matches_type(DisputeListResponse, dispute, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Dodopayments) -> None:
        response = client.disputes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dispute = response.parse()
        assert_matches_type(DisputeListResponse, dispute, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Dodopayments) -> None:
        with client.disputes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dispute = response.parse()
            assert_matches_type(DisputeListResponse, dispute, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDisputes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDodopayments) -> None:
        dispute = await async_client.disputes.retrieve(
            "dispute_id",
        )
        assert_matches_type(Dispute, dispute, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDodopayments) -> None:
        response = await async_client.disputes.with_raw_response.retrieve(
            "dispute_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dispute = await response.parse()
        assert_matches_type(Dispute, dispute, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDodopayments) -> None:
        async with async_client.disputes.with_streaming_response.retrieve(
            "dispute_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dispute = await response.parse()
            assert_matches_type(Dispute, dispute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDodopayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dispute_id` but received ''"):
            await async_client.disputes.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncDodopayments) -> None:
        dispute = await async_client.disputes.list()
        assert_matches_type(DisputeListResponse, dispute, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDodopayments) -> None:
        dispute = await async_client.disputes.list(
            page_number=0,
            page_size=0,
        )
        assert_matches_type(DisputeListResponse, dispute, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDodopayments) -> None:
        response = await async_client.disputes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dispute = await response.parse()
        assert_matches_type(DisputeListResponse, dispute, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDodopayments) -> None:
        async with async_client.disputes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dispute = await response.parse()
            assert_matches_type(DisputeListResponse, dispute, path=["response"])

        assert cast(Any, response.is_closed) is True
