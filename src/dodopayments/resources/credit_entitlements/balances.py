# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncDefaultPageNumberPagination, AsyncDefaultPageNumberPagination
from ..._base_client import AsyncPaginator, make_request_options
from ...types.credit_entitlements import (
    LedgerEntryType,
    balance_list_params,
    balance_list_grants_params,
    balance_list_ledger_params,
    balance_create_ledger_entry_params,
)
from ...types.credit_entitlements.ledger_entry_type import LedgerEntryType
from ...types.credit_entitlements.credit_ledger_entry import CreditLedgerEntry
from ...types.credit_entitlements.customer_credit_balance import CustomerCreditBalance
from ...types.credit_entitlements.balance_list_grants_response import BalanceListGrantsResponse
from ...types.credit_entitlements.balance_create_ledger_entry_response import BalanceCreateLedgerEntryResponse

__all__ = ["BalancesResource", "AsyncBalancesResource"]


class BalancesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BalancesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return BalancesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BalancesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return BalancesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        customer_id: str,
        *,
        credit_entitlement_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerCreditBalance:
        """
        Returns the credit balance details for a specific customer and credit
        entitlement.

        # Authentication

        Requires an API key with `Viewer` role or higher.

        # Path Parameters

        - `credit_entitlement_id` - The unique identifier of the credit entitlement
        - `customer_id` - The unique identifier of the customer

        # Responses

        - `200 OK` - Returns the customer's balance
        - `404 Not Found` - Credit entitlement or customer balance not found
        - `500 Internal Server Error` - Database or server error

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not credit_entitlement_id:
            raise ValueError(
                f"Expected a non-empty value for `credit_entitlement_id` but received {credit_entitlement_id!r}"
            )
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return self._get(
            f"/credit-entitlements/{credit_entitlement_id}/balances/{customer_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerCreditBalance,
        )

    def list(
        self,
        credit_entitlement_id: str,
        *,
        customer_id: str | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultPageNumberPagination[CustomerCreditBalance]:
        """
        Returns a paginated list of customer credit balances for the given credit
        entitlement.

        # Authentication

        Requires an API key with `Viewer` role or higher.

        # Path Parameters

        - `credit_entitlement_id` - The unique identifier of the credit entitlement

        # Query Parameters

        - `page_size` - Number of items per page (default: 10, max: 100)
        - `page_number` - Zero-based page number (default: 0)
        - `customer_id` - Optional filter by specific customer

        # Responses

        - `200 OK` - Returns list of customer balances
        - `404 Not Found` - Credit entitlement not found
        - `500 Internal Server Error` - Database or server error

        Args:
          customer_id: Filter by specific customer ID

          page_number: Page number default is 0

          page_size: Page size default is 10 max is 100

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not credit_entitlement_id:
            raise ValueError(
                f"Expected a non-empty value for `credit_entitlement_id` but received {credit_entitlement_id!r}"
            )
        return self._get_api_list(
            f"/credit-entitlements/{credit_entitlement_id}/balances",
            page=SyncDefaultPageNumberPagination[CustomerCreditBalance],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "customer_id": customer_id,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    balance_list_params.BalanceListParams,
                ),
            ),
            model=CustomerCreditBalance,
        )

    def create_ledger_entry(
        self,
        customer_id: str,
        *,
        credit_entitlement_id: str,
        amount: str,
        entry_type: LedgerEntryType,
        expires_at: Union[str, datetime, None] | Omit = omit,
        idempotency_key: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        reason: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BalanceCreateLedgerEntryResponse:
        """For credit entries, a new grant is created.

        For debit entries, credits are
        deducted from existing grants using FIFO (oldest first).

        # Authentication

        Requires an API key with `Editor` role.

        # Path Parameters

        - `credit_entitlement_id` - The unique identifier of the credit entitlement
        - `customer_id` - The unique identifier of the customer

        # Request Body

        - `entry_type` - "credit" or "debit"
        - `amount` - Amount to credit or debit
        - `reason` - Optional human-readable reason
        - `expires_at` - Optional expiration for credited amount (only for credit type)
        - `idempotency_key` - Optional key to prevent duplicate entries

        # Responses

        - `201 Created` - Ledger entry created successfully
        - `400 Bad Request` - Invalid request (e.g., debit with insufficient balance)
        - `404 Not Found` - Credit entitlement or customer not found
        - `409 Conflict` - Idempotency key already exists
        - `500 Internal Server Error` - Database or server error

        Args:
          amount: Amount to credit or debit

          entry_type: Entry type: credit or debit

          expires_at: Expiration for credited amount (only for credit type)

          idempotency_key: Idempotency key to prevent duplicate entries

          metadata: Optional metadata (max 50 key-value pairs, key max 40 chars, value max 500
              chars)

          reason: Human-readable reason for the entry

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not credit_entitlement_id:
            raise ValueError(
                f"Expected a non-empty value for `credit_entitlement_id` but received {credit_entitlement_id!r}"
            )
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return self._post(
            f"/credit-entitlements/{credit_entitlement_id}/balances/{customer_id}/ledger-entries",
            body=maybe_transform(
                {
                    "amount": amount,
                    "entry_type": entry_type,
                    "expires_at": expires_at,
                    "idempotency_key": idempotency_key,
                    "metadata": metadata,
                    "reason": reason,
                },
                balance_create_ledger_entry_params.BalanceCreateLedgerEntryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BalanceCreateLedgerEntryResponse,
        )

    def list_grants(
        self,
        customer_id: str,
        *,
        credit_entitlement_id: str,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        status: Literal["active", "expired", "depleted"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultPageNumberPagination[BalanceListGrantsResponse]:
        """
        Returns a paginated list of credit grants with optional filtering by status.

        # Authentication

        Requires an API key with `Viewer` role or higher.

        # Path Parameters

        - `credit_entitlement_id` - The unique identifier of the credit entitlement
        - `customer_id` - The unique identifier of the customer

        # Query Parameters

        - `page_size` - Number of items per page (default: 10, max: 100)
        - `page_number` - Zero-based page number (default: 0)
        - `status` - Filter by status: active, expired, depleted

        # Responses

        - `200 OK` - Returns list of grants
        - `404 Not Found` - Credit entitlement not found
        - `500 Internal Server Error` - Database or server error

        Args:
          page_number: Page number default is 0

          page_size: Page size default is 10 max is 100

          status: Filter by grant status: active, expired, depleted

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not credit_entitlement_id:
            raise ValueError(
                f"Expected a non-empty value for `credit_entitlement_id` but received {credit_entitlement_id!r}"
            )
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return self._get_api_list(
            f"/credit-entitlements/{credit_entitlement_id}/balances/{customer_id}/grants",
            page=SyncDefaultPageNumberPagination[BalanceListGrantsResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                        "status": status,
                    },
                    balance_list_grants_params.BalanceListGrantsParams,
                ),
            ),
            model=BalanceListGrantsResponse,
        )

    def list_ledger(
        self,
        customer_id: str,
        *,
        credit_entitlement_id: str,
        end_date: Union[str, datetime] | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        start_date: Union[str, datetime] | Omit = omit,
        transaction_type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultPageNumberPagination[CreditLedgerEntry]:
        """
        Returns a paginated list of credit transaction history with optional filtering.

        # Authentication

        Requires an API key with `Viewer` role or higher.

        # Path Parameters

        - `credit_entitlement_id` - The unique identifier of the credit entitlement
        - `customer_id` - The unique identifier of the customer

        # Query Parameters

        - `page_size` - Number of items per page (default: 10, max: 100)
        - `page_number` - Zero-based page number (default: 0)
        - `transaction_type` - Filter by transaction type
        - `start_date` - Filter entries from this date
        - `end_date` - Filter entries until this date

        # Responses

        - `200 OK` - Returns list of ledger entries
        - `404 Not Found` - Credit entitlement not found
        - `500 Internal Server Error` - Database or server error

        Args:
          end_date: Filter by end date

          page_number: Page number default is 0

          page_size: Page size default is 10 max is 100

          start_date: Filter by start date

          transaction_type: Filter by transaction type (snake_case: credit_added, credit_deducted,
              credit_expired, etc.)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not credit_entitlement_id:
            raise ValueError(
                f"Expected a non-empty value for `credit_entitlement_id` but received {credit_entitlement_id!r}"
            )
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return self._get_api_list(
            f"/credit-entitlements/{credit_entitlement_id}/balances/{customer_id}/ledger",
            page=SyncDefaultPageNumberPagination[CreditLedgerEntry],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_date": end_date,
                        "page_number": page_number,
                        "page_size": page_size,
                        "start_date": start_date,
                        "transaction_type": transaction_type,
                    },
                    balance_list_ledger_params.BalanceListLedgerParams,
                ),
            ),
            model=CreditLedgerEntry,
        )


class AsyncBalancesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBalancesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBalancesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBalancesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return AsyncBalancesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        customer_id: str,
        *,
        credit_entitlement_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerCreditBalance:
        """
        Returns the credit balance details for a specific customer and credit
        entitlement.

        # Authentication

        Requires an API key with `Viewer` role or higher.

        # Path Parameters

        - `credit_entitlement_id` - The unique identifier of the credit entitlement
        - `customer_id` - The unique identifier of the customer

        # Responses

        - `200 OK` - Returns the customer's balance
        - `404 Not Found` - Credit entitlement or customer balance not found
        - `500 Internal Server Error` - Database or server error

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not credit_entitlement_id:
            raise ValueError(
                f"Expected a non-empty value for `credit_entitlement_id` but received {credit_entitlement_id!r}"
            )
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return await self._get(
            f"/credit-entitlements/{credit_entitlement_id}/balances/{customer_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerCreditBalance,
        )

    def list(
        self,
        credit_entitlement_id: str,
        *,
        customer_id: str | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[CustomerCreditBalance, AsyncDefaultPageNumberPagination[CustomerCreditBalance]]:
        """
        Returns a paginated list of customer credit balances for the given credit
        entitlement.

        # Authentication

        Requires an API key with `Viewer` role or higher.

        # Path Parameters

        - `credit_entitlement_id` - The unique identifier of the credit entitlement

        # Query Parameters

        - `page_size` - Number of items per page (default: 10, max: 100)
        - `page_number` - Zero-based page number (default: 0)
        - `customer_id` - Optional filter by specific customer

        # Responses

        - `200 OK` - Returns list of customer balances
        - `404 Not Found` - Credit entitlement not found
        - `500 Internal Server Error` - Database or server error

        Args:
          customer_id: Filter by specific customer ID

          page_number: Page number default is 0

          page_size: Page size default is 10 max is 100

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not credit_entitlement_id:
            raise ValueError(
                f"Expected a non-empty value for `credit_entitlement_id` but received {credit_entitlement_id!r}"
            )
        return self._get_api_list(
            f"/credit-entitlements/{credit_entitlement_id}/balances",
            page=AsyncDefaultPageNumberPagination[CustomerCreditBalance],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "customer_id": customer_id,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    balance_list_params.BalanceListParams,
                ),
            ),
            model=CustomerCreditBalance,
        )

    async def create_ledger_entry(
        self,
        customer_id: str,
        *,
        credit_entitlement_id: str,
        amount: str,
        entry_type: LedgerEntryType,
        expires_at: Union[str, datetime, None] | Omit = omit,
        idempotency_key: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        reason: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BalanceCreateLedgerEntryResponse:
        """For credit entries, a new grant is created.

        For debit entries, credits are
        deducted from existing grants using FIFO (oldest first).

        # Authentication

        Requires an API key with `Editor` role.

        # Path Parameters

        - `credit_entitlement_id` - The unique identifier of the credit entitlement
        - `customer_id` - The unique identifier of the customer

        # Request Body

        - `entry_type` - "credit" or "debit"
        - `amount` - Amount to credit or debit
        - `reason` - Optional human-readable reason
        - `expires_at` - Optional expiration for credited amount (only for credit type)
        - `idempotency_key` - Optional key to prevent duplicate entries

        # Responses

        - `201 Created` - Ledger entry created successfully
        - `400 Bad Request` - Invalid request (e.g., debit with insufficient balance)
        - `404 Not Found` - Credit entitlement or customer not found
        - `409 Conflict` - Idempotency key already exists
        - `500 Internal Server Error` - Database or server error

        Args:
          amount: Amount to credit or debit

          entry_type: Entry type: credit or debit

          expires_at: Expiration for credited amount (only for credit type)

          idempotency_key: Idempotency key to prevent duplicate entries

          metadata: Optional metadata (max 50 key-value pairs, key max 40 chars, value max 500
              chars)

          reason: Human-readable reason for the entry

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not credit_entitlement_id:
            raise ValueError(
                f"Expected a non-empty value for `credit_entitlement_id` but received {credit_entitlement_id!r}"
            )
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return await self._post(
            f"/credit-entitlements/{credit_entitlement_id}/balances/{customer_id}/ledger-entries",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "entry_type": entry_type,
                    "expires_at": expires_at,
                    "idempotency_key": idempotency_key,
                    "metadata": metadata,
                    "reason": reason,
                },
                balance_create_ledger_entry_params.BalanceCreateLedgerEntryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BalanceCreateLedgerEntryResponse,
        )

    def list_grants(
        self,
        customer_id: str,
        *,
        credit_entitlement_id: str,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        status: Literal["active", "expired", "depleted"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[BalanceListGrantsResponse, AsyncDefaultPageNumberPagination[BalanceListGrantsResponse]]:
        """
        Returns a paginated list of credit grants with optional filtering by status.

        # Authentication

        Requires an API key with `Viewer` role or higher.

        # Path Parameters

        - `credit_entitlement_id` - The unique identifier of the credit entitlement
        - `customer_id` - The unique identifier of the customer

        # Query Parameters

        - `page_size` - Number of items per page (default: 10, max: 100)
        - `page_number` - Zero-based page number (default: 0)
        - `status` - Filter by status: active, expired, depleted

        # Responses

        - `200 OK` - Returns list of grants
        - `404 Not Found` - Credit entitlement not found
        - `500 Internal Server Error` - Database or server error

        Args:
          page_number: Page number default is 0

          page_size: Page size default is 10 max is 100

          status: Filter by grant status: active, expired, depleted

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not credit_entitlement_id:
            raise ValueError(
                f"Expected a non-empty value for `credit_entitlement_id` but received {credit_entitlement_id!r}"
            )
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return self._get_api_list(
            f"/credit-entitlements/{credit_entitlement_id}/balances/{customer_id}/grants",
            page=AsyncDefaultPageNumberPagination[BalanceListGrantsResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                        "status": status,
                    },
                    balance_list_grants_params.BalanceListGrantsParams,
                ),
            ),
            model=BalanceListGrantsResponse,
        )

    def list_ledger(
        self,
        customer_id: str,
        *,
        credit_entitlement_id: str,
        end_date: Union[str, datetime] | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        start_date: Union[str, datetime] | Omit = omit,
        transaction_type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[CreditLedgerEntry, AsyncDefaultPageNumberPagination[CreditLedgerEntry]]:
        """
        Returns a paginated list of credit transaction history with optional filtering.

        # Authentication

        Requires an API key with `Viewer` role or higher.

        # Path Parameters

        - `credit_entitlement_id` - The unique identifier of the credit entitlement
        - `customer_id` - The unique identifier of the customer

        # Query Parameters

        - `page_size` - Number of items per page (default: 10, max: 100)
        - `page_number` - Zero-based page number (default: 0)
        - `transaction_type` - Filter by transaction type
        - `start_date` - Filter entries from this date
        - `end_date` - Filter entries until this date

        # Responses

        - `200 OK` - Returns list of ledger entries
        - `404 Not Found` - Credit entitlement not found
        - `500 Internal Server Error` - Database or server error

        Args:
          end_date: Filter by end date

          page_number: Page number default is 0

          page_size: Page size default is 10 max is 100

          start_date: Filter by start date

          transaction_type: Filter by transaction type (snake_case: credit_added, credit_deducted,
              credit_expired, etc.)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not credit_entitlement_id:
            raise ValueError(
                f"Expected a non-empty value for `credit_entitlement_id` but received {credit_entitlement_id!r}"
            )
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return self._get_api_list(
            f"/credit-entitlements/{credit_entitlement_id}/balances/{customer_id}/ledger",
            page=AsyncDefaultPageNumberPagination[CreditLedgerEntry],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_date": end_date,
                        "page_number": page_number,
                        "page_size": page_size,
                        "start_date": start_date,
                        "transaction_type": transaction_type,
                    },
                    balance_list_ledger_params.BalanceListLedgerParams,
                ),
            ),
            model=CreditLedgerEntry,
        )


class BalancesResourceWithRawResponse:
    def __init__(self, balances: BalancesResource) -> None:
        self._balances = balances

        self.retrieve = to_raw_response_wrapper(
            balances.retrieve,
        )
        self.list = to_raw_response_wrapper(
            balances.list,
        )
        self.create_ledger_entry = to_raw_response_wrapper(
            balances.create_ledger_entry,
        )
        self.list_grants = to_raw_response_wrapper(
            balances.list_grants,
        )
        self.list_ledger = to_raw_response_wrapper(
            balances.list_ledger,
        )


class AsyncBalancesResourceWithRawResponse:
    def __init__(self, balances: AsyncBalancesResource) -> None:
        self._balances = balances

        self.retrieve = async_to_raw_response_wrapper(
            balances.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            balances.list,
        )
        self.create_ledger_entry = async_to_raw_response_wrapper(
            balances.create_ledger_entry,
        )
        self.list_grants = async_to_raw_response_wrapper(
            balances.list_grants,
        )
        self.list_ledger = async_to_raw_response_wrapper(
            balances.list_ledger,
        )


class BalancesResourceWithStreamingResponse:
    def __init__(self, balances: BalancesResource) -> None:
        self._balances = balances

        self.retrieve = to_streamed_response_wrapper(
            balances.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            balances.list,
        )
        self.create_ledger_entry = to_streamed_response_wrapper(
            balances.create_ledger_entry,
        )
        self.list_grants = to_streamed_response_wrapper(
            balances.list_grants,
        )
        self.list_ledger = to_streamed_response_wrapper(
            balances.list_ledger,
        )


class AsyncBalancesResourceWithStreamingResponse:
    def __init__(self, balances: AsyncBalancesResource) -> None:
        self._balances = balances

        self.retrieve = async_to_streamed_response_wrapper(
            balances.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            balances.list,
        )
        self.create_ledger_entry = async_to_streamed_response_wrapper(
            balances.create_ledger_entry,
        )
        self.list_grants = async_to_streamed_response_wrapper(
            balances.list_grants,
        )
        self.list_ledger = async_to_streamed_response_wrapper(
            balances.list_ledger,
        )
