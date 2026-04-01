# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .details import (
    DetailsResource,
    AsyncDetailsResource,
    DetailsResourceWithRawResponse,
    AsyncDetailsResourceWithRawResponse,
    DetailsResourceWithStreamingResponse,
    AsyncDetailsResourceWithStreamingResponse,
)
from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._utils import path_template
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.payouts.breakup_retrieve_response import BreakupRetrieveResponse

__all__ = ["BreakupResource", "AsyncBreakupResource"]


class BreakupResource(SyncAPIResource):
    @cached_property
    def details(self) -> DetailsResource:
        return DetailsResource(self._client)

    @cached_property
    def with_raw_response(self) -> BreakupResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return BreakupResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BreakupResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return BreakupResourceWithStreamingResponse(self)

    def retrieve(
        self,
        payout_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BreakupRetrieveResponse:
        """
        Returns the breakdown of a payout by event type (payments, refunds, disputes,
        fees, etc.) in the payout's currency. Each amount is proportionally allocated
        based on USD equivalent values, ensuring the total sums exactly to the payout
        amount.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not payout_id:
            raise ValueError(f"Expected a non-empty value for `payout_id` but received {payout_id!r}")
        return self._get(
            path_template("/payouts/{payout_id}/breakup", payout_id=payout_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BreakupRetrieveResponse,
        )


class AsyncBreakupResource(AsyncAPIResource):
    @cached_property
    def details(self) -> AsyncDetailsResource:
        return AsyncDetailsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBreakupResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBreakupResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBreakupResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return AsyncBreakupResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        payout_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BreakupRetrieveResponse:
        """
        Returns the breakdown of a payout by event type (payments, refunds, disputes,
        fees, etc.) in the payout's currency. Each amount is proportionally allocated
        based on USD equivalent values, ensuring the total sums exactly to the payout
        amount.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not payout_id:
            raise ValueError(f"Expected a non-empty value for `payout_id` but received {payout_id!r}")
        return await self._get(
            path_template("/payouts/{payout_id}/breakup", payout_id=payout_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BreakupRetrieveResponse,
        )


class BreakupResourceWithRawResponse:
    def __init__(self, breakup: BreakupResource) -> None:
        self._breakup = breakup

        self.retrieve = to_raw_response_wrapper(
            breakup.retrieve,
        )

    @cached_property
    def details(self) -> DetailsResourceWithRawResponse:
        return DetailsResourceWithRawResponse(self._breakup.details)


class AsyncBreakupResourceWithRawResponse:
    def __init__(self, breakup: AsyncBreakupResource) -> None:
        self._breakup = breakup

        self.retrieve = async_to_raw_response_wrapper(
            breakup.retrieve,
        )

    @cached_property
    def details(self) -> AsyncDetailsResourceWithRawResponse:
        return AsyncDetailsResourceWithRawResponse(self._breakup.details)


class BreakupResourceWithStreamingResponse:
    def __init__(self, breakup: BreakupResource) -> None:
        self._breakup = breakup

        self.retrieve = to_streamed_response_wrapper(
            breakup.retrieve,
        )

    @cached_property
    def details(self) -> DetailsResourceWithStreamingResponse:
        return DetailsResourceWithStreamingResponse(self._breakup.details)


class AsyncBreakupResourceWithStreamingResponse:
    def __init__(self, breakup: AsyncBreakupResource) -> None:
        self._breakup = breakup

        self.retrieve = async_to_streamed_response_wrapper(
            breakup.retrieve,
        )

    @cached_property
    def details(self) -> AsyncDetailsResourceWithStreamingResponse:
        return AsyncDetailsResourceWithStreamingResponse(self._breakup.details)
