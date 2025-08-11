# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from dodopayments import DodoPayments, AsyncDodoPayments
from dodopayments._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestYourWebhookURL:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: DodoPayments) -> None:
        your_webhook_url = client.your_webhook_url.create(
            business_id="business_id",
            data={
                "billing": {
                    "city": "city",
                    "country": "AF",
                    "state": "state",
                    "street": "street",
                    "zipcode": "zipcode",
                },
                "brand_id": "brand_id",
                "business_id": "business_id",
                "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "currency": "AED",
                "customer": {
                    "customer_id": "customer_id",
                    "email": "email",
                    "name": "name",
                },
                "digital_products_delivered": True,
                "disputes": [
                    {
                        "amount": "amount",
                        "business_id": "business_id",
                        "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "currency": "currency",
                        "dispute_id": "dispute_id",
                        "dispute_stage": "pre_dispute",
                        "dispute_status": "dispute_opened",
                        "payment_id": "payment_id",
                    }
                ],
                "metadata": {"foo": "string"},
                "payment_id": "payment_id",
                "refunds": [
                    {
                        "business_id": "business_id",
                        "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "is_partial": True,
                        "payment_id": "payment_id",
                        "refund_id": "refund_id",
                        "status": "succeeded",
                    }
                ],
                "settlement_amount": 0,
                "settlement_currency": "AED",
                "total_amount": 0,
                "payload_type": "Payment",
            },
            timestamp=parse_datetime("2019-12-27T18:11:19.117Z"),
            type="payment.succeeded",
            webhook_id="webhook-id",
            webhook_signature="webhook-signature",
            webhook_timestamp="webhook-timestamp",
        )
        assert your_webhook_url is None

    @parametrize
    def test_raw_response_create(self, client: DodoPayments) -> None:
        response = client.your_webhook_url.with_raw_response.create(
            business_id="business_id",
            data={
                "billing": {
                    "city": "city",
                    "country": "AF",
                    "state": "state",
                    "street": "street",
                    "zipcode": "zipcode",
                },
                "brand_id": "brand_id",
                "business_id": "business_id",
                "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "currency": "AED",
                "customer": {
                    "customer_id": "customer_id",
                    "email": "email",
                    "name": "name",
                },
                "digital_products_delivered": True,
                "disputes": [
                    {
                        "amount": "amount",
                        "business_id": "business_id",
                        "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "currency": "currency",
                        "dispute_id": "dispute_id",
                        "dispute_stage": "pre_dispute",
                        "dispute_status": "dispute_opened",
                        "payment_id": "payment_id",
                    }
                ],
                "metadata": {"foo": "string"},
                "payment_id": "payment_id",
                "refunds": [
                    {
                        "business_id": "business_id",
                        "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "is_partial": True,
                        "payment_id": "payment_id",
                        "refund_id": "refund_id",
                        "status": "succeeded",
                    }
                ],
                "settlement_amount": 0,
                "settlement_currency": "AED",
                "total_amount": 0,
                "payload_type": "Payment",
            },
            timestamp=parse_datetime("2019-12-27T18:11:19.117Z"),
            type="payment.succeeded",
            webhook_id="webhook-id",
            webhook_signature="webhook-signature",
            webhook_timestamp="webhook-timestamp",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        your_webhook_url = response.parse()
        assert your_webhook_url is None

    @parametrize
    def test_streaming_response_create(self, client: DodoPayments) -> None:
        with client.your_webhook_url.with_streaming_response.create(
            business_id="business_id",
            data={
                "billing": {
                    "city": "city",
                    "country": "AF",
                    "state": "state",
                    "street": "street",
                    "zipcode": "zipcode",
                },
                "brand_id": "brand_id",
                "business_id": "business_id",
                "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "currency": "AED",
                "customer": {
                    "customer_id": "customer_id",
                    "email": "email",
                    "name": "name",
                },
                "digital_products_delivered": True,
                "disputes": [
                    {
                        "amount": "amount",
                        "business_id": "business_id",
                        "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "currency": "currency",
                        "dispute_id": "dispute_id",
                        "dispute_stage": "pre_dispute",
                        "dispute_status": "dispute_opened",
                        "payment_id": "payment_id",
                    }
                ],
                "metadata": {"foo": "string"},
                "payment_id": "payment_id",
                "refunds": [
                    {
                        "business_id": "business_id",
                        "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "is_partial": True,
                        "payment_id": "payment_id",
                        "refund_id": "refund_id",
                        "status": "succeeded",
                    }
                ],
                "settlement_amount": 0,
                "settlement_currency": "AED",
                "total_amount": 0,
                "payload_type": "Payment",
            },
            timestamp=parse_datetime("2019-12-27T18:11:19.117Z"),
            type="payment.succeeded",
            webhook_id="webhook-id",
            webhook_signature="webhook-signature",
            webhook_timestamp="webhook-timestamp",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            your_webhook_url = response.parse()
            assert your_webhook_url is None

        assert cast(Any, response.is_closed) is True


class TestAsyncYourWebhookURL:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncDodoPayments) -> None:
        your_webhook_url = await async_client.your_webhook_url.create(
            business_id="business_id",
            data={
                "billing": {
                    "city": "city",
                    "country": "AF",
                    "state": "state",
                    "street": "street",
                    "zipcode": "zipcode",
                },
                "brand_id": "brand_id",
                "business_id": "business_id",
                "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "currency": "AED",
                "customer": {
                    "customer_id": "customer_id",
                    "email": "email",
                    "name": "name",
                },
                "digital_products_delivered": True,
                "disputes": [
                    {
                        "amount": "amount",
                        "business_id": "business_id",
                        "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "currency": "currency",
                        "dispute_id": "dispute_id",
                        "dispute_stage": "pre_dispute",
                        "dispute_status": "dispute_opened",
                        "payment_id": "payment_id",
                    }
                ],
                "metadata": {"foo": "string"},
                "payment_id": "payment_id",
                "refunds": [
                    {
                        "business_id": "business_id",
                        "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "is_partial": True,
                        "payment_id": "payment_id",
                        "refund_id": "refund_id",
                        "status": "succeeded",
                    }
                ],
                "settlement_amount": 0,
                "settlement_currency": "AED",
                "total_amount": 0,
                "payload_type": "Payment",
            },
            timestamp=parse_datetime("2019-12-27T18:11:19.117Z"),
            type="payment.succeeded",
            webhook_id="webhook-id",
            webhook_signature="webhook-signature",
            webhook_timestamp="webhook-timestamp",
        )
        assert your_webhook_url is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.your_webhook_url.with_raw_response.create(
            business_id="business_id",
            data={
                "billing": {
                    "city": "city",
                    "country": "AF",
                    "state": "state",
                    "street": "street",
                    "zipcode": "zipcode",
                },
                "brand_id": "brand_id",
                "business_id": "business_id",
                "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "currency": "AED",
                "customer": {
                    "customer_id": "customer_id",
                    "email": "email",
                    "name": "name",
                },
                "digital_products_delivered": True,
                "disputes": [
                    {
                        "amount": "amount",
                        "business_id": "business_id",
                        "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "currency": "currency",
                        "dispute_id": "dispute_id",
                        "dispute_stage": "pre_dispute",
                        "dispute_status": "dispute_opened",
                        "payment_id": "payment_id",
                    }
                ],
                "metadata": {"foo": "string"},
                "payment_id": "payment_id",
                "refunds": [
                    {
                        "business_id": "business_id",
                        "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "is_partial": True,
                        "payment_id": "payment_id",
                        "refund_id": "refund_id",
                        "status": "succeeded",
                    }
                ],
                "settlement_amount": 0,
                "settlement_currency": "AED",
                "total_amount": 0,
                "payload_type": "Payment",
            },
            timestamp=parse_datetime("2019-12-27T18:11:19.117Z"),
            type="payment.succeeded",
            webhook_id="webhook-id",
            webhook_signature="webhook-signature",
            webhook_timestamp="webhook-timestamp",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        your_webhook_url = await response.parse()
        assert your_webhook_url is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.your_webhook_url.with_streaming_response.create(
            business_id="business_id",
            data={
                "billing": {
                    "city": "city",
                    "country": "AF",
                    "state": "state",
                    "street": "street",
                    "zipcode": "zipcode",
                },
                "brand_id": "brand_id",
                "business_id": "business_id",
                "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "currency": "AED",
                "customer": {
                    "customer_id": "customer_id",
                    "email": "email",
                    "name": "name",
                },
                "digital_products_delivered": True,
                "disputes": [
                    {
                        "amount": "amount",
                        "business_id": "business_id",
                        "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "currency": "currency",
                        "dispute_id": "dispute_id",
                        "dispute_stage": "pre_dispute",
                        "dispute_status": "dispute_opened",
                        "payment_id": "payment_id",
                    }
                ],
                "metadata": {"foo": "string"},
                "payment_id": "payment_id",
                "refunds": [
                    {
                        "business_id": "business_id",
                        "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "is_partial": True,
                        "payment_id": "payment_id",
                        "refund_id": "refund_id",
                        "status": "succeeded",
                    }
                ],
                "settlement_amount": 0,
                "settlement_currency": "AED",
                "total_amount": 0,
                "payload_type": "Payment",
            },
            timestamp=parse_datetime("2019-12-27T18:11:19.117Z"),
            type="payment.succeeded",
            webhook_id="webhook-id",
            webhook_signature="webhook-signature",
            webhook_timestamp="webhook-timestamp",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            your_webhook_url = await response.parse()
            assert your_webhook_url is None

        assert cast(Any, response.is_closed) is True
