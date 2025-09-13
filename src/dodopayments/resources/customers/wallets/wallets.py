# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .ledger_entries import (
    LedgerEntriesResource,
    AsyncLedgerEntriesResource,
    LedgerEntriesResourceWithRawResponse,
    AsyncLedgerEntriesResourceWithRawResponse,
    LedgerEntriesResourceWithStreamingResponse,
    AsyncLedgerEntriesResourceWithStreamingResponse,
)
from ...._base_client import make_request_options
from ....types.customers.wallet_list_response import WalletListResponse

__all__ = ["WalletsResource", "AsyncWalletsResource"]


class WalletsResource(SyncAPIResource):
    @cached_property
    def ledger_entries(self) -> LedgerEntriesResource:
        return LedgerEntriesResource(self._client)

    @cached_property
    def with_raw_response(self) -> WalletsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return WalletsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WalletsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return WalletsResourceWithStreamingResponse(self)

    def list(
        self,
        customer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WalletListResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return self._get(
            f"/customers/{customer_id}/wallets",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WalletListResponse,
        )


class AsyncWalletsResource(AsyncAPIResource):
    @cached_property
    def ledger_entries(self) -> AsyncLedgerEntriesResource:
        return AsyncLedgerEntriesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncWalletsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWalletsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWalletsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return AsyncWalletsResourceWithStreamingResponse(self)

    async def list(
        self,
        customer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WalletListResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return await self._get(
            f"/customers/{customer_id}/wallets",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WalletListResponse,
        )


class WalletsResourceWithRawResponse:
    def __init__(self, wallets: WalletsResource) -> None:
        self._wallets = wallets

        self.list = to_raw_response_wrapper(
            wallets.list,
        )

    @cached_property
    def ledger_entries(self) -> LedgerEntriesResourceWithRawResponse:
        return LedgerEntriesResourceWithRawResponse(self._wallets.ledger_entries)


class AsyncWalletsResourceWithRawResponse:
    def __init__(self, wallets: AsyncWalletsResource) -> None:
        self._wallets = wallets

        self.list = async_to_raw_response_wrapper(
            wallets.list,
        )

    @cached_property
    def ledger_entries(self) -> AsyncLedgerEntriesResourceWithRawResponse:
        return AsyncLedgerEntriesResourceWithRawResponse(self._wallets.ledger_entries)


class WalletsResourceWithStreamingResponse:
    def __init__(self, wallets: WalletsResource) -> None:
        self._wallets = wallets

        self.list = to_streamed_response_wrapper(
            wallets.list,
        )

    @cached_property
    def ledger_entries(self) -> LedgerEntriesResourceWithStreamingResponse:
        return LedgerEntriesResourceWithStreamingResponse(self._wallets.ledger_entries)


class AsyncWalletsResourceWithStreamingResponse:
    def __init__(self, wallets: AsyncWalletsResource) -> None:
        self._wallets = wallets

        self.list = async_to_streamed_response_wrapper(
            wallets.list,
        )

    @cached_property
    def ledger_entries(self) -> AsyncLedgerEntriesResourceWithStreamingResponse:
        return AsyncLedgerEntriesResourceWithStreamingResponse(self._wallets.ledger_entries)
