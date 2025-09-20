# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime

import httpx

from ..types import usage_event_list_params, usage_event_ingest_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncDefaultPageNumberPagination, AsyncDefaultPageNumberPagination
from ..types.event import Event
from .._base_client import AsyncPaginator, make_request_options
from ..types.event_input_param import EventInputParam
from ..types.usage_event_ingest_response import UsageEventIngestResponse

__all__ = ["UsageEventsResource", "AsyncUsageEventsResource"]


class UsageEventsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UsageEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return UsageEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsageEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return UsageEventsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        event_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Event:
        """Fetch detailed information about a single event using its unique event ID.

        This
        endpoint is useful for:

        - Debugging specific event ingestion issues
        - Retrieving event details for customer support
        - Validating that events were processed correctly
        - Getting the complete metadata for an event

        ## Event ID Format:

        The event ID should be the same value that was provided during event ingestion
        via the `/events/ingest` endpoint. Event IDs are case-sensitive and must match
        exactly.

        ## Response Details:

        The response includes all event data including:

        - Complete metadata key-value pairs
        - Original timestamp (preserved from ingestion)
        - Customer and business association
        - Event name and processing information

        ## Example Usage:

        ```text
        GET /events/api_call_12345
        ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return self._get(
            f"/events/{event_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Event,
        )

    def list(
        self,
        *,
        customer_id: str | Omit = omit,
        end: Union[str, datetime] | Omit = omit,
        event_name: str | Omit = omit,
        meter_id: str | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        start: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultPageNumberPagination[Event]:
        """Fetch events from your account with powerful filtering capabilities.

        This
        endpoint is ideal for:

        - Debugging event ingestion issues
        - Analyzing customer usage patterns
        - Building custom analytics dashboards
        - Auditing billing-related events

        ## Filtering Options:

        - **Customer filtering**: Filter by specific customer ID
        - **Event name filtering**: Filter by event type/name
        - **Meter-based filtering**: Use a meter ID to apply the meter's event name and
          filter criteria automatically
        - **Time range filtering**: Filter events within a specific date range
        - **Pagination**: Navigate through large result sets

        ## Meter Integration:

        When using `meter_id`, the endpoint automatically applies:

        - The meter's configured `event_name` filter
        - The meter's custom filter criteria (if any)
        - If you also provide `event_name`, it must match the meter's event name

        ## Example Queries:

        - Get all events for a customer: `?customer_id=cus_abc123`
        - Get API request events: `?event_name=api_request`
        - Get events from last 24 hours:
          `?start=2024-01-14T10:30:00Z&end=2024-01-15T10:30:00Z`
        - Get events with meter filtering: `?meter_id=mtr_xyz789`
        - Paginate results: `?page_size=50&page_number=2`

        Args:
          customer_id: Filter events by customer ID

          end: Filter events created before this timestamp

          event_name: Filter events by event name. If both event_name and meter_id are provided, they
              must match the meter's configured event_name

          meter_id: Filter events by meter ID. When provided, only events that match the meter's
              event_name and filter criteria will be returned

          page_number: Page number (0-based, default: 0)

          page_size: Number of events to return per page (default: 10)

          start: Filter events created after this timestamp

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/events",
            page=SyncDefaultPageNumberPagination[Event],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "customer_id": customer_id,
                        "end": end,
                        "event_name": event_name,
                        "meter_id": meter_id,
                        "page_number": page_number,
                        "page_size": page_size,
                        "start": start,
                    },
                    usage_event_list_params.UsageEventListParams,
                ),
            ),
            model=Event,
        )

    def ingest(
        self,
        *,
        events: Iterable[EventInputParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageEventIngestResponse:
        """
        This endpoint allows you to ingest custom events that can be used for:

        - Usage-based billing and metering
        - Analytics and reporting
        - Customer behavior tracking

        ## Important Notes:

        - **Duplicate Prevention**:
          - Duplicate `event_id` values within the same request are rejected (entire
            request fails)
          - Subsequent requests with existing `event_id` values are ignored (idempotent
            behavior)
        - **Rate Limiting**: Maximum 1000 events per request
        - **Time Validation**: Events with timestamps older than 1 hour or more than 5
          minutes in the future will be rejected
        - **Metadata Limits**: Maximum 50 key-value pairs per event, keys max 100 chars,
          values max 500 chars

        ## Example Usage:

        ```json
        {
          "events": [
            {
              "event_id": "api_call_12345",
              "customer_id": "cus_abc123",
              "event_name": "api_request",
              "timestamp": "2024-01-15T10:30:00Z",
              "metadata": {
                "endpoint": "/api/v1/users",
                "method": "GET",
                "tokens_used": "150"
              }
            }
          ]
        }
        ```

        Args:
          events: List of events to be pushed

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/events/ingest",
            body=maybe_transform({"events": events}, usage_event_ingest_params.UsageEventIngestParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UsageEventIngestResponse,
        )


class AsyncUsageEventsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUsageEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUsageEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsageEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return AsyncUsageEventsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        event_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Event:
        """Fetch detailed information about a single event using its unique event ID.

        This
        endpoint is useful for:

        - Debugging specific event ingestion issues
        - Retrieving event details for customer support
        - Validating that events were processed correctly
        - Getting the complete metadata for an event

        ## Event ID Format:

        The event ID should be the same value that was provided during event ingestion
        via the `/events/ingest` endpoint. Event IDs are case-sensitive and must match
        exactly.

        ## Response Details:

        The response includes all event data including:

        - Complete metadata key-value pairs
        - Original timestamp (preserved from ingestion)
        - Customer and business association
        - Event name and processing information

        ## Example Usage:

        ```text
        GET /events/api_call_12345
        ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return await self._get(
            f"/events/{event_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Event,
        )

    def list(
        self,
        *,
        customer_id: str | Omit = omit,
        end: Union[str, datetime] | Omit = omit,
        event_name: str | Omit = omit,
        meter_id: str | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        start: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Event, AsyncDefaultPageNumberPagination[Event]]:
        """Fetch events from your account with powerful filtering capabilities.

        This
        endpoint is ideal for:

        - Debugging event ingestion issues
        - Analyzing customer usage patterns
        - Building custom analytics dashboards
        - Auditing billing-related events

        ## Filtering Options:

        - **Customer filtering**: Filter by specific customer ID
        - **Event name filtering**: Filter by event type/name
        - **Meter-based filtering**: Use a meter ID to apply the meter's event name and
          filter criteria automatically
        - **Time range filtering**: Filter events within a specific date range
        - **Pagination**: Navigate through large result sets

        ## Meter Integration:

        When using `meter_id`, the endpoint automatically applies:

        - The meter's configured `event_name` filter
        - The meter's custom filter criteria (if any)
        - If you also provide `event_name`, it must match the meter's event name

        ## Example Queries:

        - Get all events for a customer: `?customer_id=cus_abc123`
        - Get API request events: `?event_name=api_request`
        - Get events from last 24 hours:
          `?start=2024-01-14T10:30:00Z&end=2024-01-15T10:30:00Z`
        - Get events with meter filtering: `?meter_id=mtr_xyz789`
        - Paginate results: `?page_size=50&page_number=2`

        Args:
          customer_id: Filter events by customer ID

          end: Filter events created before this timestamp

          event_name: Filter events by event name. If both event_name and meter_id are provided, they
              must match the meter's configured event_name

          meter_id: Filter events by meter ID. When provided, only events that match the meter's
              event_name and filter criteria will be returned

          page_number: Page number (0-based, default: 0)

          page_size: Number of events to return per page (default: 10)

          start: Filter events created after this timestamp

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/events",
            page=AsyncDefaultPageNumberPagination[Event],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "customer_id": customer_id,
                        "end": end,
                        "event_name": event_name,
                        "meter_id": meter_id,
                        "page_number": page_number,
                        "page_size": page_size,
                        "start": start,
                    },
                    usage_event_list_params.UsageEventListParams,
                ),
            ),
            model=Event,
        )

    async def ingest(
        self,
        *,
        events: Iterable[EventInputParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageEventIngestResponse:
        """
        This endpoint allows you to ingest custom events that can be used for:

        - Usage-based billing and metering
        - Analytics and reporting
        - Customer behavior tracking

        ## Important Notes:

        - **Duplicate Prevention**:
          - Duplicate `event_id` values within the same request are rejected (entire
            request fails)
          - Subsequent requests with existing `event_id` values are ignored (idempotent
            behavior)
        - **Rate Limiting**: Maximum 1000 events per request
        - **Time Validation**: Events with timestamps older than 1 hour or more than 5
          minutes in the future will be rejected
        - **Metadata Limits**: Maximum 50 key-value pairs per event, keys max 100 chars,
          values max 500 chars

        ## Example Usage:

        ```json
        {
          "events": [
            {
              "event_id": "api_call_12345",
              "customer_id": "cus_abc123",
              "event_name": "api_request",
              "timestamp": "2024-01-15T10:30:00Z",
              "metadata": {
                "endpoint": "/api/v1/users",
                "method": "GET",
                "tokens_used": "150"
              }
            }
          ]
        }
        ```

        Args:
          events: List of events to be pushed

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/events/ingest",
            body=await async_maybe_transform({"events": events}, usage_event_ingest_params.UsageEventIngestParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UsageEventIngestResponse,
        )


class UsageEventsResourceWithRawResponse:
    def __init__(self, usage_events: UsageEventsResource) -> None:
        self._usage_events = usage_events

        self.retrieve = to_raw_response_wrapper(
            usage_events.retrieve,
        )
        self.list = to_raw_response_wrapper(
            usage_events.list,
        )
        self.ingest = to_raw_response_wrapper(
            usage_events.ingest,
        )


class AsyncUsageEventsResourceWithRawResponse:
    def __init__(self, usage_events: AsyncUsageEventsResource) -> None:
        self._usage_events = usage_events

        self.retrieve = async_to_raw_response_wrapper(
            usage_events.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            usage_events.list,
        )
        self.ingest = async_to_raw_response_wrapper(
            usage_events.ingest,
        )


class UsageEventsResourceWithStreamingResponse:
    def __init__(self, usage_events: UsageEventsResource) -> None:
        self._usage_events = usage_events

        self.retrieve = to_streamed_response_wrapper(
            usage_events.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            usage_events.list,
        )
        self.ingest = to_streamed_response_wrapper(
            usage_events.ingest,
        )


class AsyncUsageEventsResourceWithStreamingResponse:
    def __init__(self, usage_events: AsyncUsageEventsResource) -> None:
        self._usage_events = usage_events

        self.retrieve = async_to_streamed_response_wrapper(
            usage_events.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            usage_events.list,
        )
        self.ingest = async_to_streamed_response_wrapper(
            usage_events.ingest,
        )
