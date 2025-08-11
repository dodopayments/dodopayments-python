# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime

import httpx

from ..types import WebhookEventType, your_webhook_url_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.webhook_event_type import WebhookEventType

__all__ = ["YourWebhookURLResource", "AsyncYourWebhookURLResource"]


class YourWebhookURLResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> YourWebhookURLResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return YourWebhookURLResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> YourWebhookURLResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return YourWebhookURLResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        business_id: str,
        data: Union[
            your_webhook_url_create_params.DataPayment,
            your_webhook_url_create_params.DataSubscription,
            your_webhook_url_create_params.DataRefund,
            your_webhook_url_create_params.DataDispute,
            your_webhook_url_create_params.DataLicenseKey,
        ],
        timestamp: Union[str, datetime],
        type: WebhookEventType,
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
          data: The latest data at the time of delivery attempt

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
                your_webhook_url_create_params.YourWebhookURLCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncYourWebhookURLResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncYourWebhookURLResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return AsyncYourWebhookURLResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncYourWebhookURLResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return AsyncYourWebhookURLResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        business_id: str,
        data: Union[
            your_webhook_url_create_params.DataPayment,
            your_webhook_url_create_params.DataSubscription,
            your_webhook_url_create_params.DataRefund,
            your_webhook_url_create_params.DataDispute,
            your_webhook_url_create_params.DataLicenseKey,
        ],
        timestamp: Union[str, datetime],
        type: WebhookEventType,
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
          data: The latest data at the time of delivery attempt

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
                your_webhook_url_create_params.YourWebhookURLCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class YourWebhookURLResourceWithRawResponse:
    def __init__(self, your_webhook_url: YourWebhookURLResource) -> None:
        self._your_webhook_url = your_webhook_url

        self.create = to_raw_response_wrapper(
            your_webhook_url.create,
        )


class AsyncYourWebhookURLResourceWithRawResponse:
    def __init__(self, your_webhook_url: AsyncYourWebhookURLResource) -> None:
        self._your_webhook_url = your_webhook_url

        self.create = async_to_raw_response_wrapper(
            your_webhook_url.create,
        )


class YourWebhookURLResourceWithStreamingResponse:
    def __init__(self, your_webhook_url: YourWebhookURLResource) -> None:
        self._your_webhook_url = your_webhook_url

        self.create = to_streamed_response_wrapper(
            your_webhook_url.create,
        )


class AsyncYourWebhookURLResourceWithStreamingResponse:
    def __init__(self, your_webhook_url: AsyncYourWebhookURLResource) -> None:
        self._your_webhook_url = your_webhook_url

        self.create = async_to_streamed_response_wrapper(
            your_webhook_url.create,
        )
