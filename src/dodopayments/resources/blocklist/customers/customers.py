# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import overload

import httpx

from .notes import (
    NotesResource,
    AsyncNotesResource,
    NotesResourceWithRawResponse,
    AsyncNotesResourceWithRawResponse,
    NotesResourceWithStreamingResponse,
    AsyncNotesResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import path_template, required_args, maybe_transform, async_maybe_transform
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
from ....types.blocklist import BlockedCustomerSource, customer_list_params, customer_create_params
from ....types.blocklist.blocked_customer import BlockedCustomer
from ....types.blocklist.blocked_customer_source import BlockedCustomerSource

__all__ = ["CustomersResource", "AsyncCustomersResource"]


class CustomersResource(SyncAPIResource):
    @cached_property
    def notes(self) -> NotesResource:
        return NotesResource(self._client)

    @cached_property
    def with_raw_response(self) -> CustomersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return CustomersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return CustomersResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        customer_id: str,
        reason: Optional[str] | Omit = omit,
        source: Optional[BlockedCustomerSource] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BlockedCustomer:
        """Args:
          customer_id: Customer to block.

        The block still applies to that customer's email.

          reason: Why the merchant blocked this customer. The entry page shows it.

          source: Screen the merchant blocked from. Ignored for an API-key caller, whose entry
              always records `api`. A dashboard caller that omits it records `blocklist_page`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        email: str,
        reason: Optional[str] | Omit = omit,
        source: Optional[BlockedCustomerSource] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BlockedCustomer:
        """Args:
          email: Email to block.

        It must belong to an existing customer of this business.

          reason: Why the merchant blocked this customer. The entry page shows it.

          source: Screen the merchant blocked from. Ignored for an API-key caller, whose entry
              always records `api`. A dashboard caller that omits it records `blocklist_page`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["customer_id"], ["email"])
    def create(
        self,
        *,
        customer_id: str | Omit = omit,
        reason: Optional[str] | Omit = omit,
        source: Optional[BlockedCustomerSource] | Omit = omit,
        email: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BlockedCustomer:
        return self._post(
            "/blocklist/customers",
            body=maybe_transform(
                {
                    "customer_id": customer_id,
                    "reason": reason,
                    "source": source,
                    "email": email,
                },
                customer_create_params.CustomerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BlockedCustomer,
        )

    def retrieve(
        self,
        entry_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BlockedCustomer:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entry_id:
            raise ValueError(f"Expected a non-empty value for `entry_id` but received {entry_id!r}")
        return self._get(
            path_template("/blocklist/customers/{entry_id}", entry_id=entry_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BlockedCustomer,
        )

    def list(
        self,
        *,
        blocked_by_email: Optional[str] | Omit = omit,
        created_at_gte: Union[str, datetime, None] | Omit = omit,
        created_at_lte: Union[str, datetime, None] | Omit = omit,
        identifier: Optional[str] | Omit = omit,
        page_number: Optional[int] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultPageNumberPagination[BlockedCustomer]:
        """
        Args:
          blocked_by_email: Filter by the dashboard user who blocked the customer.

          created_at_gte: Blocked on or after this time.

          created_at_lte: Blocked on or before this time.

          identifier: Partial, case-insensitive match on the email and on the customer id.

          page_number: Page number. Default 0.

          page_size: Page size. Default 10, maximum 100.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/blocklist/customers",
            page=SyncDefaultPageNumberPagination[BlockedCustomer],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "blocked_by_email": blocked_by_email,
                        "created_at_gte": created_at_gte,
                        "created_at_lte": created_at_lte,
                        "identifier": identifier,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    customer_list_params.CustomerListParams,
                ),
            ),
            model=BlockedCustomer,
        )

    def delete(
        self,
        entry_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entry_id:
            raise ValueError(f"Expected a non-empty value for `entry_id` but received {entry_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/blocklist/customers/{entry_id}", entry_id=entry_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncCustomersResource(AsyncAPIResource):
    @cached_property
    def notes(self) -> AsyncNotesResource:
        return AsyncNotesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCustomersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCustomersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return AsyncCustomersResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        customer_id: str,
        reason: Optional[str] | Omit = omit,
        source: Optional[BlockedCustomerSource] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BlockedCustomer:
        """Args:
          customer_id: Customer to block.

        The block still applies to that customer's email.

          reason: Why the merchant blocked this customer. The entry page shows it.

          source: Screen the merchant blocked from. Ignored for an API-key caller, whose entry
              always records `api`. A dashboard caller that omits it records `blocklist_page`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        email: str,
        reason: Optional[str] | Omit = omit,
        source: Optional[BlockedCustomerSource] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BlockedCustomer:
        """Args:
          email: Email to block.

        It must belong to an existing customer of this business.

          reason: Why the merchant blocked this customer. The entry page shows it.

          source: Screen the merchant blocked from. Ignored for an API-key caller, whose entry
              always records `api`. A dashboard caller that omits it records `blocklist_page`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["customer_id"], ["email"])
    async def create(
        self,
        *,
        customer_id: str | Omit = omit,
        reason: Optional[str] | Omit = omit,
        source: Optional[BlockedCustomerSource] | Omit = omit,
        email: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BlockedCustomer:
        return await self._post(
            "/blocklist/customers",
            body=await async_maybe_transform(
                {
                    "customer_id": customer_id,
                    "reason": reason,
                    "source": source,
                    "email": email,
                },
                customer_create_params.CustomerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BlockedCustomer,
        )

    async def retrieve(
        self,
        entry_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BlockedCustomer:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entry_id:
            raise ValueError(f"Expected a non-empty value for `entry_id` but received {entry_id!r}")
        return await self._get(
            path_template("/blocklist/customers/{entry_id}", entry_id=entry_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BlockedCustomer,
        )

    def list(
        self,
        *,
        blocked_by_email: Optional[str] | Omit = omit,
        created_at_gte: Union[str, datetime, None] | Omit = omit,
        created_at_lte: Union[str, datetime, None] | Omit = omit,
        identifier: Optional[str] | Omit = omit,
        page_number: Optional[int] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[BlockedCustomer, AsyncDefaultPageNumberPagination[BlockedCustomer]]:
        """
        Args:
          blocked_by_email: Filter by the dashboard user who blocked the customer.

          created_at_gte: Blocked on or after this time.

          created_at_lte: Blocked on or before this time.

          identifier: Partial, case-insensitive match on the email and on the customer id.

          page_number: Page number. Default 0.

          page_size: Page size. Default 10, maximum 100.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/blocklist/customers",
            page=AsyncDefaultPageNumberPagination[BlockedCustomer],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "blocked_by_email": blocked_by_email,
                        "created_at_gte": created_at_gte,
                        "created_at_lte": created_at_lte,
                        "identifier": identifier,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    customer_list_params.CustomerListParams,
                ),
            ),
            model=BlockedCustomer,
        )

    async def delete(
        self,
        entry_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entry_id:
            raise ValueError(f"Expected a non-empty value for `entry_id` but received {entry_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/blocklist/customers/{entry_id}", entry_id=entry_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class CustomersResourceWithRawResponse:
    def __init__(self, customers: CustomersResource) -> None:
        self._customers = customers

        self.create = to_raw_response_wrapper(
            customers.create,
        )
        self.retrieve = to_raw_response_wrapper(
            customers.retrieve,
        )
        self.list = to_raw_response_wrapper(
            customers.list,
        )
        self.delete = to_raw_response_wrapper(
            customers.delete,
        )

    @cached_property
    def notes(self) -> NotesResourceWithRawResponse:
        return NotesResourceWithRawResponse(self._customers.notes)


class AsyncCustomersResourceWithRawResponse:
    def __init__(self, customers: AsyncCustomersResource) -> None:
        self._customers = customers

        self.create = async_to_raw_response_wrapper(
            customers.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            customers.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            customers.list,
        )
        self.delete = async_to_raw_response_wrapper(
            customers.delete,
        )

    @cached_property
    def notes(self) -> AsyncNotesResourceWithRawResponse:
        return AsyncNotesResourceWithRawResponse(self._customers.notes)


class CustomersResourceWithStreamingResponse:
    def __init__(self, customers: CustomersResource) -> None:
        self._customers = customers

        self.create = to_streamed_response_wrapper(
            customers.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            customers.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            customers.list,
        )
        self.delete = to_streamed_response_wrapper(
            customers.delete,
        )

    @cached_property
    def notes(self) -> NotesResourceWithStreamingResponse:
        return NotesResourceWithStreamingResponse(self._customers.notes)


class AsyncCustomersResourceWithStreamingResponse:
    def __init__(self, customers: AsyncCustomersResource) -> None:
        self._customers = customers

        self.create = async_to_streamed_response_wrapper(
            customers.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            customers.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            customers.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            customers.delete,
        )

    @cached_property
    def notes(self) -> AsyncNotesResourceWithStreamingResponse:
        return AsyncNotesResourceWithStreamingResponse(self._customers.notes)
