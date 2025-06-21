# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from dodopayments import DodoPayments, AsyncDodoPayments
from dodopayments._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPayments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_retrieve(self, client: DodoPayments, respx_mock: MockRouter) -> None:
        respx_mock.get("/invoices/payments/payment_id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        payment = client.invoices.payments.retrieve(
            "payment_id",
        )
        assert payment.is_closed
        assert payment.json() == {"foo": "bar"}
        assert cast(Any, payment.is_closed) is True
        assert isinstance(payment, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_retrieve(self, client: DodoPayments, respx_mock: MockRouter) -> None:
        respx_mock.get("/invoices/payments/payment_id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        payment = client.invoices.payments.with_raw_response.retrieve(
            "payment_id",
        )

        assert payment.is_closed is True
        assert payment.http_request.headers.get("X-Stainless-Lang") == "python"
        assert payment.json() == {"foo": "bar"}
        assert isinstance(payment, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_retrieve(self, client: DodoPayments, respx_mock: MockRouter) -> None:
        respx_mock.get("/invoices/payments/payment_id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.invoices.payments.with_streaming_response.retrieve(
            "payment_id",
        ) as payment:
            assert not payment.is_closed
            assert payment.http_request.headers.get("X-Stainless-Lang") == "python"

            assert payment.json() == {"foo": "bar"}
            assert cast(Any, payment.is_closed) is True
            assert isinstance(payment, StreamedBinaryAPIResponse)

        assert cast(Any, payment.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_retrieve(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `payment_id` but received ''"):
            client.invoices.payments.with_raw_response.retrieve(
                "",
            )


class TestAsyncPayments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_retrieve(self, async_client: AsyncDodoPayments, respx_mock: MockRouter) -> None:
        respx_mock.get("/invoices/payments/payment_id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        payment = await async_client.invoices.payments.retrieve(
            "payment_id",
        )
        assert payment.is_closed
        assert await payment.json() == {"foo": "bar"}
        assert cast(Any, payment.is_closed) is True
        assert isinstance(payment, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_retrieve(self, async_client: AsyncDodoPayments, respx_mock: MockRouter) -> None:
        respx_mock.get("/invoices/payments/payment_id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        payment = await async_client.invoices.payments.with_raw_response.retrieve(
            "payment_id",
        )

        assert payment.is_closed is True
        assert payment.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await payment.json() == {"foo": "bar"}
        assert isinstance(payment, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_retrieve(self, async_client: AsyncDodoPayments, respx_mock: MockRouter) -> None:
        respx_mock.get("/invoices/payments/payment_id").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.invoices.payments.with_streaming_response.retrieve(
            "payment_id",
        ) as payment:
            assert not payment.is_closed
            assert payment.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await payment.json() == {"foo": "bar"}
            assert cast(Any, payment.is_closed) is True
            assert isinstance(payment, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, payment.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_retrieve(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `payment_id` but received ''"):
            await async_client.invoices.payments.with_raw_response.retrieve(
                "",
            )
