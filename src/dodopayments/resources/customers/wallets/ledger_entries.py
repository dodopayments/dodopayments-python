# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ....types import Currency
from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
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
from ....types.currency import Currency
from ....types.customers.wallets import ledger_entry_list_params, ledger_entry_create_params
from ....types.customers.customer_wallet import CustomerWallet
from ....types.customers.wallets.customer_wallet_transaction import CustomerWalletTransaction

__all__ = ["LedgerEntriesResource", "AsyncLedgerEntriesResource"]


class LedgerEntriesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LedgerEntriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return LedgerEntriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LedgerEntriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return LedgerEntriesResourceWithStreamingResponse(self)

    def create(
        self,
        customer_id: str,
        *,
        amount: int,
        currency: Currency,
        entry_type: Literal["credit", "debit"],
        idempotency_key: Optional[str] | Omit = omit,
        reason: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerWallet:
        """
        Args:
          currency: Currency of the wallet to adjust

          entry_type: Type of ledger entry - credit or debit

          idempotency_key: Optional idempotency key to prevent duplicate entries

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return self._post(
            f"/customers/{customer_id}/wallets/ledger-entries",
            body=maybe_transform(
                {
                    "amount": amount,
                    "currency": currency,
                    "entry_type": entry_type,
                    "idempotency_key": idempotency_key,
                    "reason": reason,
                },
                ledger_entry_create_params.LedgerEntryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerWallet,
        )

    def list(
        self,
        customer_id: str,
        *,
        currency: Currency | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultPageNumberPagination[CustomerWalletTransaction]:
        """
        Args:
          currency: Optional currency filter

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return self._get_api_list(
            f"/customers/{customer_id}/wallets/ledger-entries",
            page=SyncDefaultPageNumberPagination[CustomerWalletTransaction],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "currency": currency,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    ledger_entry_list_params.LedgerEntryListParams,
                ),
            ),
            model=CustomerWalletTransaction,
        )


class AsyncLedgerEntriesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLedgerEntriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLedgerEntriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLedgerEntriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return AsyncLedgerEntriesResourceWithStreamingResponse(self)

    async def create(
        self,
        customer_id: str,
        *,
        amount: int,
        currency: Currency,
        entry_type: Literal["credit", "debit"],
        idempotency_key: Optional[str] | Omit = omit,
        reason: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerWallet:
        """
        Args:
          currency: Currency of the wallet to adjust

          entry_type: Type of ledger entry - credit or debit

          idempotency_key: Optional idempotency key to prevent duplicate entries

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return await self._post(
            f"/customers/{customer_id}/wallets/ledger-entries",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "currency": currency,
                    "entry_type": entry_type,
                    "idempotency_key": idempotency_key,
                    "reason": reason,
                },
                ledger_entry_create_params.LedgerEntryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerWallet,
        )

    def list(
        self,
        customer_id: str,
        *,
        currency: Currency | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[CustomerWalletTransaction, AsyncDefaultPageNumberPagination[CustomerWalletTransaction]]:
        """
        Args:
          currency: Optional currency filter

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return self._get_api_list(
            f"/customers/{customer_id}/wallets/ledger-entries",
            page=AsyncDefaultPageNumberPagination[CustomerWalletTransaction],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "currency": currency,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    ledger_entry_list_params.LedgerEntryListParams,
                ),
            ),
            model=CustomerWalletTransaction,
        )


class LedgerEntriesResourceWithRawResponse:
    def __init__(self, ledger_entries: LedgerEntriesResource) -> None:
        self._ledger_entries = ledger_entries

        self.create = to_raw_response_wrapper(
            ledger_entries.create,
        )
        self.list = to_raw_response_wrapper(
            ledger_entries.list,
        )


class AsyncLedgerEntriesResourceWithRawResponse:
    def __init__(self, ledger_entries: AsyncLedgerEntriesResource) -> None:
        self._ledger_entries = ledger_entries

        self.create = async_to_raw_response_wrapper(
            ledger_entries.create,
        )
        self.list = async_to_raw_response_wrapper(
            ledger_entries.list,
        )


class LedgerEntriesResourceWithStreamingResponse:
    def __init__(self, ledger_entries: LedgerEntriesResource) -> None:
        self._ledger_entries = ledger_entries

        self.create = to_streamed_response_wrapper(
            ledger_entries.create,
        )
        self.list = to_streamed_response_wrapper(
            ledger_entries.list,
        )


class AsyncLedgerEntriesResourceWithStreamingResponse:
    def __init__(self, ledger_entries: AsyncLedgerEntriesResource) -> None:
        self._ledger_entries = ledger_entries

        self.create = async_to_streamed_response_wrapper(
            ledger_entries.create,
        )
        self.list = async_to_streamed_response_wrapper(
            ledger_entries.list,
        )
