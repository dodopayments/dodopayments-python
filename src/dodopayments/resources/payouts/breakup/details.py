# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncDefaultPageNumberPagination, AsyncDefaultPageNumberPagination
from ...._base_client import AsyncPaginator, make_request_options
from ....types.payouts.breakup import detail_list_params
from ....types.payouts.breakup.detail_list_response import DetailListResponse

__all__ = ["DetailsResource", "AsyncDetailsResource"]


class DetailsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DetailsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return DetailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DetailsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return DetailsResourceWithStreamingResponse(self)

    def list(
        self,
        payout_id: str,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultPageNumberPagination[DetailListResponse]:
        """
        Returns paginated individual balance ledger entries for a payout, with each
        entry's amount pro-rated into the payout's currency. Supports pagination via
        `page_size` (default 10, max 100) and `page_number` (default 0) query
        parameters.

        Args:
          page_number: Page number (0-indexed). Default: 0.

          page_size: Number of items per page. Default: 10, Max: 100.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not payout_id:
            raise ValueError(f"Expected a non-empty value for `payout_id` but received {payout_id!r}")
        return self._get_api_list(
            path_template("/payouts/{payout_id}/breakup/details", payout_id=payout_id),
            page=SyncDefaultPageNumberPagination[DetailListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    detail_list_params.DetailListParams,
                ),
            ),
            model=DetailListResponse,
        )

    def download_csv(
        self,
        payout_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Downloads the complete payout breakup as a CSV file.

        Each row represents a
        balance ledger entry with columns: Ledger ID, Event Type, Original Amount,
        Original Currency, Reference Object ID, Description, Created At, USD Equivalent
        Amount, and Payout Currency Amount.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not payout_id:
            raise ValueError(f"Expected a non-empty value for `payout_id` but received {payout_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            path_template("/payouts/{payout_id}/breakup/details/csv", payout_id=payout_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncDetailsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDetailsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDetailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDetailsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return AsyncDetailsResourceWithStreamingResponse(self)

    def list(
        self,
        payout_id: str,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[DetailListResponse, AsyncDefaultPageNumberPagination[DetailListResponse]]:
        """
        Returns paginated individual balance ledger entries for a payout, with each
        entry's amount pro-rated into the payout's currency. Supports pagination via
        `page_size` (default 10, max 100) and `page_number` (default 0) query
        parameters.

        Args:
          page_number: Page number (0-indexed). Default: 0.

          page_size: Number of items per page. Default: 10, Max: 100.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not payout_id:
            raise ValueError(f"Expected a non-empty value for `payout_id` but received {payout_id!r}")
        return self._get_api_list(
            path_template("/payouts/{payout_id}/breakup/details", payout_id=payout_id),
            page=AsyncDefaultPageNumberPagination[DetailListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    detail_list_params.DetailListParams,
                ),
            ),
            model=DetailListResponse,
        )

    async def download_csv(
        self,
        payout_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Downloads the complete payout breakup as a CSV file.

        Each row represents a
        balance ledger entry with columns: Ledger ID, Event Type, Original Amount,
        Original Currency, Reference Object ID, Description, Created At, USD Equivalent
        Amount, and Payout Currency Amount.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not payout_id:
            raise ValueError(f"Expected a non-empty value for `payout_id` but received {payout_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            path_template("/payouts/{payout_id}/breakup/details/csv", payout_id=payout_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class DetailsResourceWithRawResponse:
    def __init__(self, details: DetailsResource) -> None:
        self._details = details

        self.list = to_raw_response_wrapper(
            details.list,
        )
        self.download_csv = to_raw_response_wrapper(
            details.download_csv,
        )


class AsyncDetailsResourceWithRawResponse:
    def __init__(self, details: AsyncDetailsResource) -> None:
        self._details = details

        self.list = async_to_raw_response_wrapper(
            details.list,
        )
        self.download_csv = async_to_raw_response_wrapper(
            details.download_csv,
        )


class DetailsResourceWithStreamingResponse:
    def __init__(self, details: DetailsResource) -> None:
        self._details = details

        self.list = to_streamed_response_wrapper(
            details.list,
        )
        self.download_csv = to_streamed_response_wrapper(
            details.download_csv,
        )


class AsyncDetailsResourceWithStreamingResponse:
    def __init__(self, details: AsyncDetailsResource) -> None:
        self._details = details

        self.list = async_to_streamed_response_wrapper(
            details.list,
        )
        self.download_csv = async_to_streamed_response_wrapper(
            details.download_csv,
        )
