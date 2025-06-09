# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime

import httpx

from ..types import webhook_event_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncDefaultPageNumberPagination, AsyncDefaultPageNumberPagination
from .._base_client import AsyncPaginator, make_request_options
from ..types.webhook_event import WebhookEvent

__all__ = ["WebhookEventsResource", "AsyncWebhookEventsResource"]


class WebhookEventsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WebhookEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return WebhookEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WebhookEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return WebhookEventsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        webhook_event_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WebhookEvent:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not webhook_event_id:
            raise ValueError(f"Expected a non-empty value for `webhook_event_id` but received {webhook_event_id!r}")
        return self._get(
            f"/webhook_events/{webhook_event_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookEvent,
        )

    def list(
        self,
        *,
        created_at_gte: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        created_at_lte: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        object_id: Optional[str] | NotGiven = NOT_GIVEN,
        page_number: Optional[int] | NotGiven = NOT_GIVEN,
        page_size: Optional[int] | NotGiven = NOT_GIVEN,
        webhook_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncDefaultPageNumberPagination[WebhookEvent]:
        """
        Args:
          created_at_gte: Get events after this created time

          created_at_lte: Get events created before this time

          limit: Min : 1, Max : 100, default 10

          object_id: Get events history of a specific object like payment/subscription/refund/dispute

          page_number: Page number default is 0

          page_size: Page size default is 10 max is 100

          webhook_id: Filter by webhook destination

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/webhook_events",
            page=SyncDefaultPageNumberPagination[WebhookEvent],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_at_gte": created_at_gte,
                        "created_at_lte": created_at_lte,
                        "limit": limit,
                        "object_id": object_id,
                        "page_number": page_number,
                        "page_size": page_size,
                        "webhook_id": webhook_id,
                    },
                    webhook_event_list_params.WebhookEventListParams,
                ),
            ),
            model=WebhookEvent,
        )


class AsyncWebhookEventsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWebhookEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWebhookEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWebhookEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return AsyncWebhookEventsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        webhook_event_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WebhookEvent:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not webhook_event_id:
            raise ValueError(f"Expected a non-empty value for `webhook_event_id` but received {webhook_event_id!r}")
        return await self._get(
            f"/webhook_events/{webhook_event_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookEvent,
        )

    def list(
        self,
        *,
        created_at_gte: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        created_at_lte: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        object_id: Optional[str] | NotGiven = NOT_GIVEN,
        page_number: Optional[int] | NotGiven = NOT_GIVEN,
        page_size: Optional[int] | NotGiven = NOT_GIVEN,
        webhook_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[WebhookEvent, AsyncDefaultPageNumberPagination[WebhookEvent]]:
        """
        Args:
          created_at_gte: Get events after this created time

          created_at_lte: Get events created before this time

          limit: Min : 1, Max : 100, default 10

          object_id: Get events history of a specific object like payment/subscription/refund/dispute

          page_number: Page number default is 0

          page_size: Page size default is 10 max is 100

          webhook_id: Filter by webhook destination

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/webhook_events",
            page=AsyncDefaultPageNumberPagination[WebhookEvent],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_at_gte": created_at_gte,
                        "created_at_lte": created_at_lte,
                        "limit": limit,
                        "object_id": object_id,
                        "page_number": page_number,
                        "page_size": page_size,
                        "webhook_id": webhook_id,
                    },
                    webhook_event_list_params.WebhookEventListParams,
                ),
            ),
            model=WebhookEvent,
        )


class WebhookEventsResourceWithRawResponse:
    def __init__(self, webhook_events: WebhookEventsResource) -> None:
        self._webhook_events = webhook_events

        self.retrieve = to_raw_response_wrapper(
            webhook_events.retrieve,
        )
        self.list = to_raw_response_wrapper(
            webhook_events.list,
        )


class AsyncWebhookEventsResourceWithRawResponse:
    def __init__(self, webhook_events: AsyncWebhookEventsResource) -> None:
        self._webhook_events = webhook_events

        self.retrieve = async_to_raw_response_wrapper(
            webhook_events.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            webhook_events.list,
        )


class WebhookEventsResourceWithStreamingResponse:
    def __init__(self, webhook_events: WebhookEventsResource) -> None:
        self._webhook_events = webhook_events

        self.retrieve = to_streamed_response_wrapper(
            webhook_events.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            webhook_events.list,
        )


class AsyncWebhookEventsResourceWithStreamingResponse:
    def __init__(self, webhook_events: AsyncWebhookEventsResource) -> None:
        self._webhook_events = webhook_events

        self.retrieve = async_to_streamed_response_wrapper(
            webhook_events.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            webhook_events.list,
        )
