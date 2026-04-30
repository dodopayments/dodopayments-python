# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from dodopayments import DodoPayments, AsyncDodoPayments
from dodopayments.types.entitlements import FileUploadResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_delete(self, client: DodoPayments) -> None:
        file = client.entitlements.files.delete(
            file_id="file_id",
            id="id",
        )
        assert file is None

    @parametrize
    def test_raw_response_delete(self, client: DodoPayments) -> None:
        response = client.entitlements.files.with_raw_response.delete(
            file_id="file_id",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert file is None

    @parametrize
    def test_streaming_response_delete(self, client: DodoPayments) -> None:
        with client.entitlements.files.with_streaming_response.delete(
            file_id="file_id",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert file is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.entitlements.files.with_raw_response.delete(
                file_id="file_id",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.entitlements.files.with_raw_response.delete(
                file_id="",
                id="id",
            )

    @parametrize
    def test_method_upload(self, client: DodoPayments) -> None:
        file = client.entitlements.files.upload(
            "id",
        )
        assert_matches_type(FileUploadResponse, file, path=["response"])

    @parametrize
    def test_raw_response_upload(self, client: DodoPayments) -> None:
        response = client.entitlements.files.with_raw_response.upload(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileUploadResponse, file, path=["response"])

    @parametrize
    def test_streaming_response_upload(self, client: DodoPayments) -> None:
        with client.entitlements.files.with_streaming_response.upload(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileUploadResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_upload(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.entitlements.files.with_raw_response.upload(
                "",
            )


class TestAsyncFiles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_delete(self, async_client: AsyncDodoPayments) -> None:
        file = await async_client.entitlements.files.delete(
            file_id="file_id",
            id="id",
        )
        assert file is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.entitlements.files.with_raw_response.delete(
            file_id="file_id",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert file is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.entitlements.files.with_streaming_response.delete(
            file_id="file_id",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert file is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.entitlements.files.with_raw_response.delete(
                file_id="file_id",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.entitlements.files.with_raw_response.delete(
                file_id="",
                id="id",
            )

    @parametrize
    async def test_method_upload(self, async_client: AsyncDodoPayments) -> None:
        file = await async_client.entitlements.files.upload(
            "id",
        )
        assert_matches_type(FileUploadResponse, file, path=["response"])

    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.entitlements.files.with_raw_response.upload(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileUploadResponse, file, path=["response"])

    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.entitlements.files.with_streaming_response.upload(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileUploadResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_upload(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.entitlements.files.with_raw_response.upload(
                "",
            )
