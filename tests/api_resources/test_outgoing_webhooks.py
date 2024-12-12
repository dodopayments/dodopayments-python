# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from dodopayments import Dodopayments, AsyncDodopayments
from dodopayments._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOutgoingWebhooks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Dodopayments) -> None:
        outgoing_webhook = client.outgoing_webhooks.create(
            business_id="business_id",
            data={
                "business_id": "business_id",
                "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "currency": "AED",
                "customer": {
                    "customer_id": "customer_id",
                    "email": "email",
                    "name": "name",
                },
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
                "payment_id": "payment_id",
                "refunds": [
                    {
                        "business_id": "business_id",
                        "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "payment_id": "payment_id",
                        "refund_id": "refund_id",
                        "status": "succeeded",
                    }
                ],
                "total_amount": 0,
                "payload_type": "Payment",
            },
            timestamp=parse_datetime("2019-12-27T18:11:19.117Z"),
            type="payment.succeeded",
            webhook_id="webhook-id",
            webhook_signature="webhook-signature",
            webhook_timestamp="webhook-timestamp",
        )
        assert outgoing_webhook is None

    @parametrize
    def test_raw_response_create(self, client: Dodopayments) -> None:
        response = client.outgoing_webhooks.with_raw_response.create(
            business_id="business_id",
            data={
                "business_id": "business_id",
                "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "currency": "AED",
                "customer": {
                    "customer_id": "customer_id",
                    "email": "email",
                    "name": "name",
                },
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
                "payment_id": "payment_id",
                "refunds": [
                    {
                        "business_id": "business_id",
                        "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "payment_id": "payment_id",
                        "refund_id": "refund_id",
                        "status": "succeeded",
                    }
                ],
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
        outgoing_webhook = response.parse()
        assert outgoing_webhook is None

    @parametrize
    def test_streaming_response_create(self, client: Dodopayments) -> None:
        with client.outgoing_webhooks.with_streaming_response.create(
            business_id="business_id",
            data={
                "business_id": "business_id",
                "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "currency": "AED",
                "customer": {
                    "customer_id": "customer_id",
                    "email": "email",
                    "name": "name",
                },
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
                "payment_id": "payment_id",
                "refunds": [
                    {
                        "business_id": "business_id",
                        "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "payment_id": "payment_id",
                        "refund_id": "refund_id",
                        "status": "succeeded",
                    }
                ],
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

            outgoing_webhook = response.parse()
            assert outgoing_webhook is None

        assert cast(Any, response.is_closed) is True


class TestAsyncOutgoingWebhooks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncDodopayments) -> None:
        outgoing_webhook = await async_client.outgoing_webhooks.create(
            business_id="business_id",
            data={
                "business_id": "business_id",
                "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "currency": "AED",
                "customer": {
                    "customer_id": "customer_id",
                    "email": "email",
                    "name": "name",
                },
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
                "payment_id": "payment_id",
                "refunds": [
                    {
                        "business_id": "business_id",
                        "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "payment_id": "payment_id",
                        "refund_id": "refund_id",
                        "status": "succeeded",
                    }
                ],
                "total_amount": 0,
                "payload_type": "Payment",
            },
            timestamp=parse_datetime("2019-12-27T18:11:19.117Z"),
            type="payment.succeeded",
            webhook_id="webhook-id",
            webhook_signature="webhook-signature",
            webhook_timestamp="webhook-timestamp",
        )
        assert outgoing_webhook is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDodopayments) -> None:
        response = await async_client.outgoing_webhooks.with_raw_response.create(
            business_id="business_id",
            data={
                "business_id": "business_id",
                "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "currency": "AED",
                "customer": {
                    "customer_id": "customer_id",
                    "email": "email",
                    "name": "name",
                },
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
                "payment_id": "payment_id",
                "refunds": [
                    {
                        "business_id": "business_id",
                        "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "payment_id": "payment_id",
                        "refund_id": "refund_id",
                        "status": "succeeded",
                    }
                ],
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
        outgoing_webhook = await response.parse()
        assert outgoing_webhook is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDodopayments) -> None:
        async with async_client.outgoing_webhooks.with_streaming_response.create(
            business_id="business_id",
            data={
                "business_id": "business_id",
                "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "currency": "AED",
                "customer": {
                    "customer_id": "customer_id",
                    "email": "email",
                    "name": "name",
                },
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
                "payment_id": "payment_id",
                "refunds": [
                    {
                        "business_id": "business_id",
                        "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "payment_id": "payment_id",
                        "refund_id": "refund_id",
                        "status": "succeeded",
                    }
                ],
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

            outgoing_webhook = await response.parse()
            assert outgoing_webhook is None

        assert cast(Any, response.is_closed) is True
