# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from dodopayments import DodoPayments, AsyncDodoPayments
from dodopayments.types.products import (
    LocalizedPrice,
    ListLocalizedPricesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLocalizedPrices:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: DodoPayments) -> None:
        localized_price = client.products.localized_prices.create(
            product_id="pdt_R8AWMPiV8RyJElcCKvAID",
            amount=0,
            currency="AED",
        )
        assert_matches_type(LocalizedPrice, localized_price, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: DodoPayments) -> None:
        localized_price = client.products.localized_prices.create(
            product_id="pdt_R8AWMPiV8RyJElcCKvAID",
            amount=0,
            currency="AED",
            country_code="AF",
        )
        assert_matches_type(LocalizedPrice, localized_price, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: DodoPayments) -> None:
        response = client.products.localized_prices.with_raw_response.create(
            product_id="pdt_R8AWMPiV8RyJElcCKvAID",
            amount=0,
            currency="AED",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        localized_price = response.parse()
        assert_matches_type(LocalizedPrice, localized_price, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: DodoPayments) -> None:
        with client.products.localized_prices.with_streaming_response.create(
            product_id="pdt_R8AWMPiV8RyJElcCKvAID",
            amount=0,
            currency="AED",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            localized_price = response.parse()
            assert_matches_type(LocalizedPrice, localized_price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `product_id` but received ''"):
            client.products.localized_prices.with_raw_response.create(
                product_id="",
                amount=0,
                currency="AED",
            )

    @parametrize
    def test_method_retrieve(self, client: DodoPayments) -> None:
        localized_price = client.products.localized_prices.retrieve(
            id="lcp_3aOOT7ebrzBOV41yL2V6s",
            product_id="pdt_R8AWMPiV8RyJElcCKvAID",
        )
        assert_matches_type(LocalizedPrice, localized_price, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: DodoPayments) -> None:
        response = client.products.localized_prices.with_raw_response.retrieve(
            id="lcp_3aOOT7ebrzBOV41yL2V6s",
            product_id="pdt_R8AWMPiV8RyJElcCKvAID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        localized_price = response.parse()
        assert_matches_type(LocalizedPrice, localized_price, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: DodoPayments) -> None:
        with client.products.localized_prices.with_streaming_response.retrieve(
            id="lcp_3aOOT7ebrzBOV41yL2V6s",
            product_id="pdt_R8AWMPiV8RyJElcCKvAID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            localized_price = response.parse()
            assert_matches_type(LocalizedPrice, localized_price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `product_id` but received ''"):
            client.products.localized_prices.with_raw_response.retrieve(
                id="lcp_3aOOT7ebrzBOV41yL2V6s",
                product_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.products.localized_prices.with_raw_response.retrieve(
                id="",
                product_id="pdt_R8AWMPiV8RyJElcCKvAID",
            )

    @parametrize
    def test_method_update(self, client: DodoPayments) -> None:
        localized_price = client.products.localized_prices.update(
            id="lcp_3aOOT7ebrzBOV41yL2V6s",
            product_id="pdt_R8AWMPiV8RyJElcCKvAID",
        )
        assert_matches_type(LocalizedPrice, localized_price, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: DodoPayments) -> None:
        localized_price = client.products.localized_prices.update(
            id="lcp_3aOOT7ebrzBOV41yL2V6s",
            product_id="pdt_R8AWMPiV8RyJElcCKvAID",
            amount=0,
        )
        assert_matches_type(LocalizedPrice, localized_price, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: DodoPayments) -> None:
        response = client.products.localized_prices.with_raw_response.update(
            id="lcp_3aOOT7ebrzBOV41yL2V6s",
            product_id="pdt_R8AWMPiV8RyJElcCKvAID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        localized_price = response.parse()
        assert_matches_type(LocalizedPrice, localized_price, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: DodoPayments) -> None:
        with client.products.localized_prices.with_streaming_response.update(
            id="lcp_3aOOT7ebrzBOV41yL2V6s",
            product_id="pdt_R8AWMPiV8RyJElcCKvAID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            localized_price = response.parse()
            assert_matches_type(LocalizedPrice, localized_price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `product_id` but received ''"):
            client.products.localized_prices.with_raw_response.update(
                id="lcp_3aOOT7ebrzBOV41yL2V6s",
                product_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.products.localized_prices.with_raw_response.update(
                id="",
                product_id="pdt_R8AWMPiV8RyJElcCKvAID",
            )

    @parametrize
    def test_method_list(self, client: DodoPayments) -> None:
        localized_price = client.products.localized_prices.list(
            "pdt_R8AWMPiV8RyJElcCKvAID",
        )
        assert_matches_type(ListLocalizedPricesResponse, localized_price, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: DodoPayments) -> None:
        response = client.products.localized_prices.with_raw_response.list(
            "pdt_R8AWMPiV8RyJElcCKvAID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        localized_price = response.parse()
        assert_matches_type(ListLocalizedPricesResponse, localized_price, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: DodoPayments) -> None:
        with client.products.localized_prices.with_streaming_response.list(
            "pdt_R8AWMPiV8RyJElcCKvAID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            localized_price = response.parse()
            assert_matches_type(ListLocalizedPricesResponse, localized_price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `product_id` but received ''"):
            client.products.localized_prices.with_raw_response.list(
                "",
            )

    @parametrize
    def test_method_archive(self, client: DodoPayments) -> None:
        localized_price = client.products.localized_prices.archive(
            id="lcp_3aOOT7ebrzBOV41yL2V6s",
            product_id="pdt_R8AWMPiV8RyJElcCKvAID",
        )
        assert localized_price is None

    @parametrize
    def test_raw_response_archive(self, client: DodoPayments) -> None:
        response = client.products.localized_prices.with_raw_response.archive(
            id="lcp_3aOOT7ebrzBOV41yL2V6s",
            product_id="pdt_R8AWMPiV8RyJElcCKvAID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        localized_price = response.parse()
        assert localized_price is None

    @parametrize
    def test_streaming_response_archive(self, client: DodoPayments) -> None:
        with client.products.localized_prices.with_streaming_response.archive(
            id="lcp_3aOOT7ebrzBOV41yL2V6s",
            product_id="pdt_R8AWMPiV8RyJElcCKvAID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            localized_price = response.parse()
            assert localized_price is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_archive(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `product_id` but received ''"):
            client.products.localized_prices.with_raw_response.archive(
                id="lcp_3aOOT7ebrzBOV41yL2V6s",
                product_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.products.localized_prices.with_raw_response.archive(
                id="",
                product_id="pdt_R8AWMPiV8RyJElcCKvAID",
            )


class TestAsyncLocalizedPrices:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncDodoPayments) -> None:
        localized_price = await async_client.products.localized_prices.create(
            product_id="pdt_R8AWMPiV8RyJElcCKvAID",
            amount=0,
            currency="AED",
        )
        assert_matches_type(LocalizedPrice, localized_price, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDodoPayments) -> None:
        localized_price = await async_client.products.localized_prices.create(
            product_id="pdt_R8AWMPiV8RyJElcCKvAID",
            amount=0,
            currency="AED",
            country_code="AF",
        )
        assert_matches_type(LocalizedPrice, localized_price, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.products.localized_prices.with_raw_response.create(
            product_id="pdt_R8AWMPiV8RyJElcCKvAID",
            amount=0,
            currency="AED",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        localized_price = await response.parse()
        assert_matches_type(LocalizedPrice, localized_price, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.products.localized_prices.with_streaming_response.create(
            product_id="pdt_R8AWMPiV8RyJElcCKvAID",
            amount=0,
            currency="AED",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            localized_price = await response.parse()
            assert_matches_type(LocalizedPrice, localized_price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `product_id` but received ''"):
            await async_client.products.localized_prices.with_raw_response.create(
                product_id="",
                amount=0,
                currency="AED",
            )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDodoPayments) -> None:
        localized_price = await async_client.products.localized_prices.retrieve(
            id="lcp_3aOOT7ebrzBOV41yL2V6s",
            product_id="pdt_R8AWMPiV8RyJElcCKvAID",
        )
        assert_matches_type(LocalizedPrice, localized_price, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.products.localized_prices.with_raw_response.retrieve(
            id="lcp_3aOOT7ebrzBOV41yL2V6s",
            product_id="pdt_R8AWMPiV8RyJElcCKvAID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        localized_price = await response.parse()
        assert_matches_type(LocalizedPrice, localized_price, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.products.localized_prices.with_streaming_response.retrieve(
            id="lcp_3aOOT7ebrzBOV41yL2V6s",
            product_id="pdt_R8AWMPiV8RyJElcCKvAID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            localized_price = await response.parse()
            assert_matches_type(LocalizedPrice, localized_price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `product_id` but received ''"):
            await async_client.products.localized_prices.with_raw_response.retrieve(
                id="lcp_3aOOT7ebrzBOV41yL2V6s",
                product_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.products.localized_prices.with_raw_response.retrieve(
                id="",
                product_id="pdt_R8AWMPiV8RyJElcCKvAID",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncDodoPayments) -> None:
        localized_price = await async_client.products.localized_prices.update(
            id="lcp_3aOOT7ebrzBOV41yL2V6s",
            product_id="pdt_R8AWMPiV8RyJElcCKvAID",
        )
        assert_matches_type(LocalizedPrice, localized_price, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncDodoPayments) -> None:
        localized_price = await async_client.products.localized_prices.update(
            id="lcp_3aOOT7ebrzBOV41yL2V6s",
            product_id="pdt_R8AWMPiV8RyJElcCKvAID",
            amount=0,
        )
        assert_matches_type(LocalizedPrice, localized_price, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.products.localized_prices.with_raw_response.update(
            id="lcp_3aOOT7ebrzBOV41yL2V6s",
            product_id="pdt_R8AWMPiV8RyJElcCKvAID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        localized_price = await response.parse()
        assert_matches_type(LocalizedPrice, localized_price, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.products.localized_prices.with_streaming_response.update(
            id="lcp_3aOOT7ebrzBOV41yL2V6s",
            product_id="pdt_R8AWMPiV8RyJElcCKvAID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            localized_price = await response.parse()
            assert_matches_type(LocalizedPrice, localized_price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `product_id` but received ''"):
            await async_client.products.localized_prices.with_raw_response.update(
                id="lcp_3aOOT7ebrzBOV41yL2V6s",
                product_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.products.localized_prices.with_raw_response.update(
                id="",
                product_id="pdt_R8AWMPiV8RyJElcCKvAID",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncDodoPayments) -> None:
        localized_price = await async_client.products.localized_prices.list(
            "pdt_R8AWMPiV8RyJElcCKvAID",
        )
        assert_matches_type(ListLocalizedPricesResponse, localized_price, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.products.localized_prices.with_raw_response.list(
            "pdt_R8AWMPiV8RyJElcCKvAID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        localized_price = await response.parse()
        assert_matches_type(ListLocalizedPricesResponse, localized_price, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.products.localized_prices.with_streaming_response.list(
            "pdt_R8AWMPiV8RyJElcCKvAID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            localized_price = await response.parse()
            assert_matches_type(ListLocalizedPricesResponse, localized_price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `product_id` but received ''"):
            await async_client.products.localized_prices.with_raw_response.list(
                "",
            )

    @parametrize
    async def test_method_archive(self, async_client: AsyncDodoPayments) -> None:
        localized_price = await async_client.products.localized_prices.archive(
            id="lcp_3aOOT7ebrzBOV41yL2V6s",
            product_id="pdt_R8AWMPiV8RyJElcCKvAID",
        )
        assert localized_price is None

    @parametrize
    async def test_raw_response_archive(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.products.localized_prices.with_raw_response.archive(
            id="lcp_3aOOT7ebrzBOV41yL2V6s",
            product_id="pdt_R8AWMPiV8RyJElcCKvAID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        localized_price = await response.parse()
        assert localized_price is None

    @parametrize
    async def test_streaming_response_archive(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.products.localized_prices.with_streaming_response.archive(
            id="lcp_3aOOT7ebrzBOV41yL2V6s",
            product_id="pdt_R8AWMPiV8RyJElcCKvAID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            localized_price = await response.parse()
            assert localized_price is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_archive(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `product_id` but received ''"):
            await async_client.products.localized_prices.with_raw_response.archive(
                id="lcp_3aOOT7ebrzBOV41yL2V6s",
                product_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.products.localized_prices.with_raw_response.archive(
                id="",
                product_id="pdt_R8AWMPiV8RyJElcCKvAID",
            )
