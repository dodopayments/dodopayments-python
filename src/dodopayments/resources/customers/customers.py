# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime

import httpx

from ...types import customer_list_params, customer_create_params, customer_update_params
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
from .customer_portal import (
    CustomerPortalResource,
    AsyncCustomerPortalResource,
    CustomerPortalResourceWithRawResponse,
    AsyncCustomerPortalResourceWithRawResponse,
    CustomerPortalResourceWithStreamingResponse,
    AsyncCustomerPortalResourceWithStreamingResponse,
)
from .wallets.wallets import (
    WalletsResource,
    AsyncWalletsResource,
    WalletsResourceWithRawResponse,
    AsyncWalletsResourceWithRawResponse,
    WalletsResourceWithStreamingResponse,
    AsyncWalletsResourceWithStreamingResponse,
)
from ...types.customer import Customer
from ...types.customer_retrieve_payment_methods_response import CustomerRetrievePaymentMethodsResponse

__all__ = ["CustomersResource", "AsyncCustomersResource"]


class CustomersResource(SyncAPIResource):
    @cached_property
    def customer_portal(self) -> CustomerPortalResource:
        return CustomerPortalResource(self._client)

    @cached_property
    def wallets(self) -> WalletsResource:
        return WalletsResource(self._client)

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

    def create(
        self,
        *,
        email: str,
        name: str,
        metadata: Dict[str, str] | Omit = omit,
        phone_number: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Customer:
        """
        Args:
          metadata: Additional metadata for the customer

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/customers",
            body=maybe_transform(
                {
                    "email": email,
                    "name": name,
                    "metadata": metadata,
                    "phone_number": phone_number,
                },
                customer_create_params.CustomerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Customer,
        )

    def retrieve(
        self,
        customer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Customer:
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
            f"/customers/{customer_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Customer,
        )

    def update(
        self,
        customer_id: str,
        *,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        name: Optional[str] | Omit = omit,
        phone_number: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Customer:
        """
        Args:
          metadata: Additional metadata for the customer

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return self._patch(
            f"/customers/{customer_id}",
            body=maybe_transform(
                {
                    "metadata": metadata,
                    "name": name,
                    "phone_number": phone_number,
                },
                customer_update_params.CustomerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Customer,
        )

    def list(
        self,
        *,
        created_at_gte: Union[str, datetime] | Omit = omit,
        created_at_lte: Union[str, datetime] | Omit = omit,
        email: str | Omit = omit,
        name: str | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultPageNumberPagination[Customer]:
        """
        Args:
          created_at_gte: Filter customers created on or after this timestamp

          created_at_lte: Filter customers created on or before this timestamp

          email: Filter by customer email

          name: Filter by customer name (partial match, case-insensitive)

          page_number: Page number default is 0

          page_size: Page size default is 10 max is 100

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/customers",
            page=SyncDefaultPageNumberPagination[Customer],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_at_gte": created_at_gte,
                        "created_at_lte": created_at_lte,
                        "email": email,
                        "name": name,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    customer_list_params.CustomerListParams,
                ),
            ),
            model=Customer,
        )

    def retrieve_payment_methods(
        self,
        customer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerRetrievePaymentMethodsResponse:
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
            f"/customers/{customer_id}/payment-methods",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerRetrievePaymentMethodsResponse,
        )


class AsyncCustomersResource(AsyncAPIResource):
    @cached_property
    def customer_portal(self) -> AsyncCustomerPortalResource:
        return AsyncCustomerPortalResource(self._client)

    @cached_property
    def wallets(self) -> AsyncWalletsResource:
        return AsyncWalletsResource(self._client)

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

    async def create(
        self,
        *,
        email: str,
        name: str,
        metadata: Dict[str, str] | Omit = omit,
        phone_number: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Customer:
        """
        Args:
          metadata: Additional metadata for the customer

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/customers",
            body=await async_maybe_transform(
                {
                    "email": email,
                    "name": name,
                    "metadata": metadata,
                    "phone_number": phone_number,
                },
                customer_create_params.CustomerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Customer,
        )

    async def retrieve(
        self,
        customer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Customer:
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
            f"/customers/{customer_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Customer,
        )

    async def update(
        self,
        customer_id: str,
        *,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        name: Optional[str] | Omit = omit,
        phone_number: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Customer:
        """
        Args:
          metadata: Additional metadata for the customer

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return await self._patch(
            f"/customers/{customer_id}",
            body=await async_maybe_transform(
                {
                    "metadata": metadata,
                    "name": name,
                    "phone_number": phone_number,
                },
                customer_update_params.CustomerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Customer,
        )

    def list(
        self,
        *,
        created_at_gte: Union[str, datetime] | Omit = omit,
        created_at_lte: Union[str, datetime] | Omit = omit,
        email: str | Omit = omit,
        name: str | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Customer, AsyncDefaultPageNumberPagination[Customer]]:
        """
        Args:
          created_at_gte: Filter customers created on or after this timestamp

          created_at_lte: Filter customers created on or before this timestamp

          email: Filter by customer email

          name: Filter by customer name (partial match, case-insensitive)

          page_number: Page number default is 0

          page_size: Page size default is 10 max is 100

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/customers",
            page=AsyncDefaultPageNumberPagination[Customer],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_at_gte": created_at_gte,
                        "created_at_lte": created_at_lte,
                        "email": email,
                        "name": name,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    customer_list_params.CustomerListParams,
                ),
            ),
            model=Customer,
        )

    async def retrieve_payment_methods(
        self,
        customer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerRetrievePaymentMethodsResponse:
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
            f"/customers/{customer_id}/payment-methods",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerRetrievePaymentMethodsResponse,
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
        self.update = to_raw_response_wrapper(
            customers.update,
        )
        self.list = to_raw_response_wrapper(
            customers.list,
        )
        self.retrieve_payment_methods = to_raw_response_wrapper(
            customers.retrieve_payment_methods,
        )

    @cached_property
    def customer_portal(self) -> CustomerPortalResourceWithRawResponse:
        return CustomerPortalResourceWithRawResponse(self._customers.customer_portal)

    @cached_property
    def wallets(self) -> WalletsResourceWithRawResponse:
        return WalletsResourceWithRawResponse(self._customers.wallets)


class AsyncCustomersResourceWithRawResponse:
    def __init__(self, customers: AsyncCustomersResource) -> None:
        self._customers = customers

        self.create = async_to_raw_response_wrapper(
            customers.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            customers.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            customers.update,
        )
        self.list = async_to_raw_response_wrapper(
            customers.list,
        )
        self.retrieve_payment_methods = async_to_raw_response_wrapper(
            customers.retrieve_payment_methods,
        )

    @cached_property
    def customer_portal(self) -> AsyncCustomerPortalResourceWithRawResponse:
        return AsyncCustomerPortalResourceWithRawResponse(self._customers.customer_portal)

    @cached_property
    def wallets(self) -> AsyncWalletsResourceWithRawResponse:
        return AsyncWalletsResourceWithRawResponse(self._customers.wallets)


class CustomersResourceWithStreamingResponse:
    def __init__(self, customers: CustomersResource) -> None:
        self._customers = customers

        self.create = to_streamed_response_wrapper(
            customers.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            customers.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            customers.update,
        )
        self.list = to_streamed_response_wrapper(
            customers.list,
        )
        self.retrieve_payment_methods = to_streamed_response_wrapper(
            customers.retrieve_payment_methods,
        )

    @cached_property
    def customer_portal(self) -> CustomerPortalResourceWithStreamingResponse:
        return CustomerPortalResourceWithStreamingResponse(self._customers.customer_portal)

    @cached_property
    def wallets(self) -> WalletsResourceWithStreamingResponse:
        return WalletsResourceWithStreamingResponse(self._customers.wallets)


class AsyncCustomersResourceWithStreamingResponse:
    def __init__(self, customers: AsyncCustomersResource) -> None:
        self._customers = customers

        self.create = async_to_streamed_response_wrapper(
            customers.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            customers.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            customers.update,
        )
        self.list = async_to_streamed_response_wrapper(
            customers.list,
        )
        self.retrieve_payment_methods = async_to_streamed_response_wrapper(
            customers.retrieve_payment_methods,
        )

    @cached_property
    def customer_portal(self) -> AsyncCustomerPortalResourceWithStreamingResponse:
        return AsyncCustomerPortalResourceWithStreamingResponse(self._customers.customer_portal)

    @cached_property
    def wallets(self) -> AsyncWalletsResourceWithStreamingResponse:
        return AsyncWalletsResourceWithStreamingResponse(self._customers.wallets)
