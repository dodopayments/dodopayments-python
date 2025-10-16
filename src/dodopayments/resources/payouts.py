# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime

import httpx

from ..types import payout_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.payout_list_response import PayoutListResponse

__all__ = ["PayoutsResource", "AsyncPayoutsResource"]


class PayoutsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PayoutsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return PayoutsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PayoutsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return PayoutsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        created_at_gte: Union[str, datetime] | Omit = omit,
        created_at_lte: Union[str, datetime] | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultPageNumberPagination[PayoutListResponse]:
        """
        Args:
          created_at_gte: Get payouts created after this time (inclusive)

          created_at_lte: Get payouts created before this time (inclusive)

          page_number: Page number default is 0

          page_size: Page size default is 10 max is 100

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/payouts",
            page=SyncDefaultPageNumberPagination[PayoutListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_at_gte": created_at_gte,
                        "created_at_lte": created_at_lte,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    payout_list_params.PayoutListParams,
                ),
            ),
            model=PayoutListResponse,
        )


class AsyncPayoutsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPayoutsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPayoutsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPayoutsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return AsyncPayoutsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        created_at_gte: Union[str, datetime] | Omit = omit,
        created_at_lte: Union[str, datetime] | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PayoutListResponse, AsyncDefaultPageNumberPagination[PayoutListResponse]]:
        """
        Args:
          created_at_gte: Get payouts created after this time (inclusive)

          created_at_lte: Get payouts created before this time (inclusive)

          page_number: Page number default is 0

          page_size: Page size default is 10 max is 100

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/payouts",
            page=AsyncDefaultPageNumberPagination[PayoutListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_at_gte": created_at_gte,
                        "created_at_lte": created_at_lte,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    payout_list_params.PayoutListParams,
                ),
            ),
            model=PayoutListResponse,
        )


class PayoutsResourceWithRawResponse:
    def __init__(self, payouts: PayoutsResource) -> None:
        self._payouts = payouts

        self.list = to_raw_response_wrapper(
            payouts.list,
        )


class AsyncPayoutsResourceWithRawResponse:
    def __init__(self, payouts: AsyncPayoutsResource) -> None:
        self._payouts = payouts

        self.list = async_to_raw_response_wrapper(
            payouts.list,
        )


class PayoutsResourceWithStreamingResponse:
    def __init__(self, payouts: PayoutsResource) -> None:
        self._payouts = payouts

        self.list = to_streamed_response_wrapper(
            payouts.list,
        )


class AsyncPayoutsResourceWithStreamingResponse:
    def __init__(self, payouts: AsyncPayoutsResource) -> None:
        self._payouts = payouts

        self.list = async_to_streamed_response_wrapper(
            payouts.list,
        )
