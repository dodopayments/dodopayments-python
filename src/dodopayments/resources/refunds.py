# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime

import httpx

from ..types import RefundStatus, refund_list_params, refund_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from .._base_client import AsyncPaginator, make_request_options
from ..types.refund import Refund
from ..types.refund_status import RefundStatus

__all__ = ["RefundsResource", "AsyncRefundsResource"]


class RefundsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RefundsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return RefundsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RefundsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return RefundsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        payment_id: str,
        items: Optional[Iterable[refund_create_params.Item]] | NotGiven = NOT_GIVEN,
        reason: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Refund:
        """
        Args:
          payment_id: The unique identifier of the payment to be refunded.

          items: Partially Refund an Individual Item

          reason: The reason for the refund, if any. Maximum length is 3000 characters. Optional.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/refunds",
            body=maybe_transform(
                {
                    "payment_id": payment_id,
                    "items": items,
                    "reason": reason,
                },
                refund_create_params.RefundCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Refund,
        )

    def retrieve(
        self,
        refund_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Refund:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not refund_id:
            raise ValueError(f"Expected a non-empty value for `refund_id` but received {refund_id!r}")
        return self._get(
            f"/refunds/{refund_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Refund,
        )

    def list(
        self,
        *,
        created_at_gte: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        created_at_lte: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        customer_id: Optional[str] | NotGiven = NOT_GIVEN,
        page_number: Optional[int] | NotGiven = NOT_GIVEN,
        page_size: Optional[int] | NotGiven = NOT_GIVEN,
        status: Optional[RefundStatus] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncDefaultPageNumberPagination[Refund]:
        """
        Args:
          created_at_gte: Get events after this created time

          created_at_lte: Get events created before this time

          customer_id: Filter by customer_id

          page_number: Page number default is 0

          page_size: Page size default is 10 max is 100

          status: Filter by status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/refunds",
            page=SyncDefaultPageNumberPagination[Refund],
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
                        "page_number": page_number,
                        "page_size": page_size,
                        "status": status,
                    },
                    refund_list_params.RefundListParams,
                ),
            ),
            model=Refund,
        )


class AsyncRefundsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRefundsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRefundsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRefundsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return AsyncRefundsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        payment_id: str,
        items: Optional[Iterable[refund_create_params.Item]] | NotGiven = NOT_GIVEN,
        reason: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Refund:
        """
        Args:
          payment_id: The unique identifier of the payment to be refunded.

          items: Partially Refund an Individual Item

          reason: The reason for the refund, if any. Maximum length is 3000 characters. Optional.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/refunds",
            body=await async_maybe_transform(
                {
                    "payment_id": payment_id,
                    "items": items,
                    "reason": reason,
                },
                refund_create_params.RefundCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Refund,
        )

    async def retrieve(
        self,
        refund_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Refund:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not refund_id:
            raise ValueError(f"Expected a non-empty value for `refund_id` but received {refund_id!r}")
        return await self._get(
            f"/refunds/{refund_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Refund,
        )

    def list(
        self,
        *,
        created_at_gte: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        created_at_lte: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        customer_id: Optional[str] | NotGiven = NOT_GIVEN,
        page_number: Optional[int] | NotGiven = NOT_GIVEN,
        page_size: Optional[int] | NotGiven = NOT_GIVEN,
        status: Optional[RefundStatus] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Refund, AsyncDefaultPageNumberPagination[Refund]]:
        """
        Args:
          created_at_gte: Get events after this created time

          created_at_lte: Get events created before this time

          customer_id: Filter by customer_id

          page_number: Page number default is 0

          page_size: Page size default is 10 max is 100

          status: Filter by status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/refunds",
            page=AsyncDefaultPageNumberPagination[Refund],
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
                        "page_number": page_number,
                        "page_size": page_size,
                        "status": status,
                    },
                    refund_list_params.RefundListParams,
                ),
            ),
            model=Refund,
        )


class RefundsResourceWithRawResponse:
    def __init__(self, refunds: RefundsResource) -> None:
        self._refunds = refunds

        self.create = to_raw_response_wrapper(
            refunds.create,
        )
        self.retrieve = to_raw_response_wrapper(
            refunds.retrieve,
        )
        self.list = to_raw_response_wrapper(
            refunds.list,
        )


class AsyncRefundsResourceWithRawResponse:
    def __init__(self, refunds: AsyncRefundsResource) -> None:
        self._refunds = refunds

        self.create = async_to_raw_response_wrapper(
            refunds.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            refunds.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            refunds.list,
        )


class RefundsResourceWithStreamingResponse:
    def __init__(self, refunds: RefundsResource) -> None:
        self._refunds = refunds

        self.create = to_streamed_response_wrapper(
            refunds.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            refunds.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            refunds.list,
        )


class AsyncRefundsResourceWithStreamingResponse:
    def __init__(self, refunds: AsyncRefundsResource) -> None:
        self._refunds = refunds

        self.create = async_to_streamed_response_wrapper(
            refunds.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            refunds.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            refunds.list,
        )
