# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import dispute_list_params
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
from ..types.dispute_list_response import DisputeListResponse
from ..types.dispute_retrieve_response import DisputeRetrieveResponse

__all__ = ["DisputesResource", "AsyncDisputesResource"]


class DisputesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DisputesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return DisputesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DisputesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return DisputesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        dispute_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DisputeRetrieveResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dispute_id:
            raise ValueError(f"Expected a non-empty value for `dispute_id` but received {dispute_id!r}")
        return self._get(
            f"/disputes/{dispute_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DisputeRetrieveResponse,
        )

    def list(
        self,
        *,
        created_at_gte: Union[str, datetime] | NotGiven = NOT_GIVEN,
        created_at_lte: Union[str, datetime] | NotGiven = NOT_GIVEN,
        customer_id: str | NotGiven = NOT_GIVEN,
        dispute_stage: Literal["pre_dispute", "dispute", "pre_arbitration"] | NotGiven = NOT_GIVEN,
        dispute_status: Literal[
            "dispute_opened",
            "dispute_expired",
            "dispute_accepted",
            "dispute_cancelled",
            "dispute_challenged",
            "dispute_won",
            "dispute_lost",
        ]
        | NotGiven = NOT_GIVEN,
        page_number: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncDefaultPageNumberPagination[DisputeListResponse]:
        """
        Args:
          created_at_gte: Get events after this created time

          created_at_lte: Get events created before this time

          customer_id: Filter by customer_id

          dispute_stage: Filter by dispute stage

          dispute_status: Filter by dispute status

          page_number: Page number default is 0

          page_size: Page size default is 10 max is 100

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/disputes",
            page=SyncDefaultPageNumberPagination[DisputeListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_at_gte": created_at_gte,
                        "created_at_lte": created_at_lte,
                        "customer_id": customer_id,
                        "dispute_stage": dispute_stage,
                        "dispute_status": dispute_status,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    dispute_list_params.DisputeListParams,
                ),
            ),
            model=DisputeListResponse,
        )


class AsyncDisputesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDisputesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDisputesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDisputesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return AsyncDisputesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        dispute_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DisputeRetrieveResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dispute_id:
            raise ValueError(f"Expected a non-empty value for `dispute_id` but received {dispute_id!r}")
        return await self._get(
            f"/disputes/{dispute_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DisputeRetrieveResponse,
        )

    def list(
        self,
        *,
        created_at_gte: Union[str, datetime] | NotGiven = NOT_GIVEN,
        created_at_lte: Union[str, datetime] | NotGiven = NOT_GIVEN,
        customer_id: str | NotGiven = NOT_GIVEN,
        dispute_stage: Literal["pre_dispute", "dispute", "pre_arbitration"] | NotGiven = NOT_GIVEN,
        dispute_status: Literal[
            "dispute_opened",
            "dispute_expired",
            "dispute_accepted",
            "dispute_cancelled",
            "dispute_challenged",
            "dispute_won",
            "dispute_lost",
        ]
        | NotGiven = NOT_GIVEN,
        page_number: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[DisputeListResponse, AsyncDefaultPageNumberPagination[DisputeListResponse]]:
        """
        Args:
          created_at_gte: Get events after this created time

          created_at_lte: Get events created before this time

          customer_id: Filter by customer_id

          dispute_stage: Filter by dispute stage

          dispute_status: Filter by dispute status

          page_number: Page number default is 0

          page_size: Page size default is 10 max is 100

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/disputes",
            page=AsyncDefaultPageNumberPagination[DisputeListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_at_gte": created_at_gte,
                        "created_at_lte": created_at_lte,
                        "customer_id": customer_id,
                        "dispute_stage": dispute_stage,
                        "dispute_status": dispute_status,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    dispute_list_params.DisputeListParams,
                ),
            ),
            model=DisputeListResponse,
        )


class DisputesResourceWithRawResponse:
    def __init__(self, disputes: DisputesResource) -> None:
        self._disputes = disputes

        self.retrieve = to_raw_response_wrapper(
            disputes.retrieve,
        )
        self.list = to_raw_response_wrapper(
            disputes.list,
        )


class AsyncDisputesResourceWithRawResponse:
    def __init__(self, disputes: AsyncDisputesResource) -> None:
        self._disputes = disputes

        self.retrieve = async_to_raw_response_wrapper(
            disputes.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            disputes.list,
        )


class DisputesResourceWithStreamingResponse:
    def __init__(self, disputes: DisputesResource) -> None:
        self._disputes = disputes

        self.retrieve = to_streamed_response_wrapper(
            disputes.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            disputes.list,
        )


class AsyncDisputesResourceWithStreamingResponse:
    def __init__(self, disputes: AsyncDisputesResource) -> None:
        self._disputes = disputes

        self.retrieve = async_to_streamed_response_wrapper(
            disputes.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            disputes.list,
        )
