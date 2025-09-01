# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import meter_list_params, meter_create_params
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
from ..pagination import SyncDefaultPageNumberPagination, AsyncDefaultPageNumberPagination
from ..types.meter import Meter
from .._base_client import AsyncPaginator, make_request_options
from ..types.meter_filter_param import MeterFilterParam
from ..types.meter_aggregation_param import MeterAggregationParam

__all__ = ["MetersResource", "AsyncMetersResource"]


class MetersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MetersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return MetersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MetersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return MetersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        aggregation: MeterAggregationParam,
        event_name: str,
        measurement_unit: str,
        name: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        filter: Optional[MeterFilterParam] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Meter:
        """
        Args:
          aggregation: Aggregation configuration for the meter

          event_name: Event name to track

          measurement_unit: measurement unit

          name: Name of the meter

          description: Optional description of the meter

          filter: Optional filter to apply to the meter

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/meters",
            body=maybe_transform(
                {
                    "aggregation": aggregation,
                    "event_name": event_name,
                    "measurement_unit": measurement_unit,
                    "name": name,
                    "description": description,
                    "filter": filter,
                },
                meter_create_params.MeterCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Meter,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Meter:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/meters/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Meter,
        )

    def list(
        self,
        *,
        archived: bool | NotGiven = NOT_GIVEN,
        page_number: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncDefaultPageNumberPagination[Meter]:
        """
        Args:
          archived: List archived meters

          page_number: Page number default is 0

          page_size: Page size default is 10 max is 100

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/meters",
            page=SyncDefaultPageNumberPagination[Meter],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "archived": archived,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    meter_list_params.MeterListParams,
                ),
            ),
            model=Meter,
        )

    def archive(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/meters/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def unarchive(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/meters/{id}/unarchive",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncMetersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMetersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMetersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMetersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return AsyncMetersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        aggregation: MeterAggregationParam,
        event_name: str,
        measurement_unit: str,
        name: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        filter: Optional[MeterFilterParam] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Meter:
        """
        Args:
          aggregation: Aggregation configuration for the meter

          event_name: Event name to track

          measurement_unit: measurement unit

          name: Name of the meter

          description: Optional description of the meter

          filter: Optional filter to apply to the meter

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/meters",
            body=await async_maybe_transform(
                {
                    "aggregation": aggregation,
                    "event_name": event_name,
                    "measurement_unit": measurement_unit,
                    "name": name,
                    "description": description,
                    "filter": filter,
                },
                meter_create_params.MeterCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Meter,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Meter:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/meters/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Meter,
        )

    def list(
        self,
        *,
        archived: bool | NotGiven = NOT_GIVEN,
        page_number: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Meter, AsyncDefaultPageNumberPagination[Meter]]:
        """
        Args:
          archived: List archived meters

          page_number: Page number default is 0

          page_size: Page size default is 10 max is 100

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/meters",
            page=AsyncDefaultPageNumberPagination[Meter],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "archived": archived,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    meter_list_params.MeterListParams,
                ),
            ),
            model=Meter,
        )

    async def archive(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/meters/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def unarchive(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/meters/{id}/unarchive",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class MetersResourceWithRawResponse:
    def __init__(self, meters: MetersResource) -> None:
        self._meters = meters

        self.create = to_raw_response_wrapper(
            meters.create,
        )
        self.retrieve = to_raw_response_wrapper(
            meters.retrieve,
        )
        self.list = to_raw_response_wrapper(
            meters.list,
        )
        self.archive = to_raw_response_wrapper(
            meters.archive,
        )
        self.unarchive = to_raw_response_wrapper(
            meters.unarchive,
        )


class AsyncMetersResourceWithRawResponse:
    def __init__(self, meters: AsyncMetersResource) -> None:
        self._meters = meters

        self.create = async_to_raw_response_wrapper(
            meters.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            meters.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            meters.list,
        )
        self.archive = async_to_raw_response_wrapper(
            meters.archive,
        )
        self.unarchive = async_to_raw_response_wrapper(
            meters.unarchive,
        )


class MetersResourceWithStreamingResponse:
    def __init__(self, meters: MetersResource) -> None:
        self._meters = meters

        self.create = to_streamed_response_wrapper(
            meters.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            meters.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            meters.list,
        )
        self.archive = to_streamed_response_wrapper(
            meters.archive,
        )
        self.unarchive = to_streamed_response_wrapper(
            meters.unarchive,
        )


class AsyncMetersResourceWithStreamingResponse:
    def __init__(self, meters: AsyncMetersResource) -> None:
        self._meters = meters

        self.create = async_to_streamed_response_wrapper(
            meters.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            meters.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            meters.list,
        )
        self.archive = async_to_streamed_response_wrapper(
            meters.archive,
        )
        self.unarchive = async_to_streamed_response_wrapper(
            meters.unarchive,
        )
