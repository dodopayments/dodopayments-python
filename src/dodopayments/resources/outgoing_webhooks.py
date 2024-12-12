# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import outgoing_webhook_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options

__all__ = ["OutgoingWebhooksResource", "AsyncOutgoingWebhooksResource"]


class OutgoingWebhooksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OutgoingWebhooksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/dodo-payments-python#accessing-raw-response-data-eg-headers
        """
        return OutgoingWebhooksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OutgoingWebhooksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/dodo-payments-python#with_streaming_response
        """
        return OutgoingWebhooksResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        business_id: str,
        data: Union[
            outgoing_webhook_create_params.DataPayment,
            outgoing_webhook_create_params.DataSubscription,
            outgoing_webhook_create_params.DataRefund,
            outgoing_webhook_create_params.DataDispute,
        ],
        timestamp: Union[str, datetime],
        type: Literal[
            "payment.succeeded",
            "payment.failed",
            "payment.processing",
            "payment.cancelled",
            "refund.succeeded",
            "refund.failed",
            "dispute.opened",
            "dispute.expired",
            "dispute.accepted",
            "dispute.cancelled",
            "dispute.challenged",
            "dispute.won",
            "dispute.lost",
            "subscription.active",
            "subscription.on_hold",
            "subscription.paused",
            "subscription.cancelled",
            "subscription.failed",
            "subscription.expired",
        ],
        webhook_id: str,
        webhook_signature: str,
        webhook_timestamp: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Args:
          timestamp: The timestamp of when the event occurred (not necessarily the same of when it
              was delivered)

          type: Event types for Dodo events

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers.update(
            {"webhook-id": webhook_id, "webhook-signature": webhook_signature, "webhook-timestamp": webhook_timestamp}
        )
        return self._post(
            "/your-webhook-url",
            body=maybe_transform(
                {
                    "business_id": business_id,
                    "data": data,
                    "timestamp": timestamp,
                    "type": type,
                },
                outgoing_webhook_create_params.OutgoingWebhookCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncOutgoingWebhooksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOutgoingWebhooksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/dodo-payments-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOutgoingWebhooksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOutgoingWebhooksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/dodo-payments-python#with_streaming_response
        """
        return AsyncOutgoingWebhooksResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        business_id: str,
        data: Union[
            outgoing_webhook_create_params.DataPayment,
            outgoing_webhook_create_params.DataSubscription,
            outgoing_webhook_create_params.DataRefund,
            outgoing_webhook_create_params.DataDispute,
        ],
        timestamp: Union[str, datetime],
        type: Literal[
            "payment.succeeded",
            "payment.failed",
            "payment.processing",
            "payment.cancelled",
            "refund.succeeded",
            "refund.failed",
            "dispute.opened",
            "dispute.expired",
            "dispute.accepted",
            "dispute.cancelled",
            "dispute.challenged",
            "dispute.won",
            "dispute.lost",
            "subscription.active",
            "subscription.on_hold",
            "subscription.paused",
            "subscription.cancelled",
            "subscription.failed",
            "subscription.expired",
        ],
        webhook_id: str,
        webhook_signature: str,
        webhook_timestamp: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Args:
          timestamp: The timestamp of when the event occurred (not necessarily the same of when it
              was delivered)

          type: Event types for Dodo events

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers.update(
            {"webhook-id": webhook_id, "webhook-signature": webhook_signature, "webhook-timestamp": webhook_timestamp}
        )
        return await self._post(
            "/your-webhook-url",
            body=await async_maybe_transform(
                {
                    "business_id": business_id,
                    "data": data,
                    "timestamp": timestamp,
                    "type": type,
                },
                outgoing_webhook_create_params.OutgoingWebhookCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class OutgoingWebhooksResourceWithRawResponse:
    def __init__(self, outgoing_webhooks: OutgoingWebhooksResource) -> None:
        self._outgoing_webhooks = outgoing_webhooks

        self.create = to_raw_response_wrapper(
            outgoing_webhooks.create,
        )


class AsyncOutgoingWebhooksResourceWithRawResponse:
    def __init__(self, outgoing_webhooks: AsyncOutgoingWebhooksResource) -> None:
        self._outgoing_webhooks = outgoing_webhooks

        self.create = async_to_raw_response_wrapper(
            outgoing_webhooks.create,
        )


class OutgoingWebhooksResourceWithStreamingResponse:
    def __init__(self, outgoing_webhooks: OutgoingWebhooksResource) -> None:
        self._outgoing_webhooks = outgoing_webhooks

        self.create = to_streamed_response_wrapper(
            outgoing_webhooks.create,
        )


class AsyncOutgoingWebhooksResourceWithStreamingResponse:
    def __init__(self, outgoing_webhooks: AsyncOutgoingWebhooksResource) -> None:
        self._outgoing_webhooks = outgoing_webhooks

        self.create = async_to_streamed_response_wrapper(
            outgoing_webhooks.create,
        )
