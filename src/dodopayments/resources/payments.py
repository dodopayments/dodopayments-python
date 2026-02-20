# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing import Dict, List, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import Currency, payment_list_params, payment_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.payment import Payment
from ..types.currency import Currency
from ..types.payment_method_types import PaymentMethodTypes
from ..types.billing_address_param import BillingAddressParam
from ..types.payment_list_response import PaymentListResponse
from ..types.customer_request_param import CustomerRequestParam
from ..types.payment_create_response import PaymentCreateResponse
from ..types.one_time_product_cart_item_param import OneTimeProductCartItemParam
from ..types.payment_retrieve_line_items_response import PaymentRetrieveLineItemsResponse

__all__ = ["PaymentsResource", "AsyncPaymentsResource"]


class PaymentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PaymentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return PaymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PaymentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return PaymentsResourceWithStreamingResponse(self)

    @typing_extensions.deprecated("deprecated")
    def create(
        self,
        *,
        billing: BillingAddressParam,
        customer: CustomerRequestParam,
        product_cart: Iterable[OneTimeProductCartItemParam],
        allowed_payment_method_types: Optional[List[PaymentMethodTypes]] | Omit = omit,
        billing_currency: Optional[Currency] | Omit = omit,
        discount_code: Optional[str] | Omit = omit,
        force_3ds: Optional[bool] | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        payment_link: Optional[bool] | Omit = omit,
        payment_method_id: Optional[str] | Omit = omit,
        redirect_immediately: bool | Omit = omit,
        return_url: Optional[str] | Omit = omit,
        short_link: Optional[bool] | Omit = omit,
        show_saved_payment_methods: bool | Omit = omit,
        tax_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentCreateResponse:
        """
        Args:
          billing: Billing address details for the payment

          customer: Customer information for the payment

          product_cart: List of products in the cart. Must contain at least 1 and at most 100 items.

          allowed_payment_method_types: List of payment methods allowed during checkout.

              Customers will **never** see payment methods that are **not** in this list.
              However, adding a method here **does not guarantee** customers will see it.
              Availability still depends on other factors (e.g., customer location, merchant
              settings).

          billing_currency: Fix the currency in which the end customer is billed. If Dodo Payments cannot
              support that currency for this transaction, it will not proceed

          discount_code: Discount Code to apply to the transaction

          force_3ds: Override merchant default 3DS behaviour for this payment

          metadata: Additional metadata associated with the payment. Defaults to empty if not
              provided.

          payment_link: Whether to generate a payment link. Defaults to false if not specified.

          payment_method_id: Optional payment method ID to use for this payment. If provided, customer_id
              must also be provided. The payment method will be validated for eligibility with
              the payment's currency.

          redirect_immediately: If true, redirects the customer immediately after payment completion False by
              default

          return_url: Optional URL to redirect the customer after payment. Must be a valid URL if
              provided.

          short_link: If true, returns a shortened payment link. Defaults to false if not specified.

          show_saved_payment_methods: Display saved payment methods of a returning customer False by default

          tax_id: Tax ID in case the payment is B2B. If tax id validation fails the payment
              creation will fail

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/payments",
            body=maybe_transform(
                {
                    "billing": billing,
                    "customer": customer,
                    "product_cart": product_cart,
                    "allowed_payment_method_types": allowed_payment_method_types,
                    "billing_currency": billing_currency,
                    "discount_code": discount_code,
                    "force_3ds": force_3ds,
                    "metadata": metadata,
                    "payment_link": payment_link,
                    "payment_method_id": payment_method_id,
                    "redirect_immediately": redirect_immediately,
                    "return_url": return_url,
                    "short_link": short_link,
                    "show_saved_payment_methods": show_saved_payment_methods,
                    "tax_id": tax_id,
                },
                payment_create_params.PaymentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentCreateResponse,
        )

    def retrieve(
        self,
        payment_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Payment:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not payment_id:
            raise ValueError(f"Expected a non-empty value for `payment_id` but received {payment_id!r}")
        return self._get(
            f"/payments/{payment_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Payment,
        )

    def list(
        self,
        *,
        brand_id: str | Omit = omit,
        created_at_gte: Union[str, datetime] | Omit = omit,
        created_at_lte: Union[str, datetime] | Omit = omit,
        customer_id: str | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        product_id: str | Omit = omit,
        status: Literal[
            "succeeded",
            "failed",
            "cancelled",
            "processing",
            "requires_customer_action",
            "requires_merchant_action",
            "requires_payment_method",
            "requires_confirmation",
            "requires_capture",
            "partially_captured",
            "partially_captured_and_capturable",
        ]
        | Omit = omit,
        subscription_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultPageNumberPagination[PaymentListResponse]:
        """
        Args:
          brand_id: filter by Brand id

          created_at_gte: Get events after this created time

          created_at_lte: Get events created before this time

          customer_id: Filter by customer id

          page_number: Page number default is 0

          page_size: Page size default is 10 max is 100

          product_id: Filter by product id

          status: Filter by status

          subscription_id: Filter by subscription id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/payments",
            page=SyncDefaultPageNumberPagination[PaymentListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "brand_id": brand_id,
                        "created_at_gte": created_at_gte,
                        "created_at_lte": created_at_lte,
                        "customer_id": customer_id,
                        "page_number": page_number,
                        "page_size": page_size,
                        "product_id": product_id,
                        "status": status,
                        "subscription_id": subscription_id,
                    },
                    payment_list_params.PaymentListParams,
                ),
            ),
            model=PaymentListResponse,
        )

    def retrieve_line_items(
        self,
        payment_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentRetrieveLineItemsResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not payment_id:
            raise ValueError(f"Expected a non-empty value for `payment_id` but received {payment_id!r}")
        return self._get(
            f"/payments/{payment_id}/line-items",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentRetrieveLineItemsResponse,
        )


class AsyncPaymentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPaymentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPaymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPaymentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return AsyncPaymentsResourceWithStreamingResponse(self)

    @typing_extensions.deprecated("deprecated")
    async def create(
        self,
        *,
        billing: BillingAddressParam,
        customer: CustomerRequestParam,
        product_cart: Iterable[OneTimeProductCartItemParam],
        allowed_payment_method_types: Optional[List[PaymentMethodTypes]] | Omit = omit,
        billing_currency: Optional[Currency] | Omit = omit,
        discount_code: Optional[str] | Omit = omit,
        force_3ds: Optional[bool] | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        payment_link: Optional[bool] | Omit = omit,
        payment_method_id: Optional[str] | Omit = omit,
        redirect_immediately: bool | Omit = omit,
        return_url: Optional[str] | Omit = omit,
        short_link: Optional[bool] | Omit = omit,
        show_saved_payment_methods: bool | Omit = omit,
        tax_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentCreateResponse:
        """
        Args:
          billing: Billing address details for the payment

          customer: Customer information for the payment

          product_cart: List of products in the cart. Must contain at least 1 and at most 100 items.

          allowed_payment_method_types: List of payment methods allowed during checkout.

              Customers will **never** see payment methods that are **not** in this list.
              However, adding a method here **does not guarantee** customers will see it.
              Availability still depends on other factors (e.g., customer location, merchant
              settings).

          billing_currency: Fix the currency in which the end customer is billed. If Dodo Payments cannot
              support that currency for this transaction, it will not proceed

          discount_code: Discount Code to apply to the transaction

          force_3ds: Override merchant default 3DS behaviour for this payment

          metadata: Additional metadata associated with the payment. Defaults to empty if not
              provided.

          payment_link: Whether to generate a payment link. Defaults to false if not specified.

          payment_method_id: Optional payment method ID to use for this payment. If provided, customer_id
              must also be provided. The payment method will be validated for eligibility with
              the payment's currency.

          redirect_immediately: If true, redirects the customer immediately after payment completion False by
              default

          return_url: Optional URL to redirect the customer after payment. Must be a valid URL if
              provided.

          short_link: If true, returns a shortened payment link. Defaults to false if not specified.

          show_saved_payment_methods: Display saved payment methods of a returning customer False by default

          tax_id: Tax ID in case the payment is B2B. If tax id validation fails the payment
              creation will fail

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/payments",
            body=await async_maybe_transform(
                {
                    "billing": billing,
                    "customer": customer,
                    "product_cart": product_cart,
                    "allowed_payment_method_types": allowed_payment_method_types,
                    "billing_currency": billing_currency,
                    "discount_code": discount_code,
                    "force_3ds": force_3ds,
                    "metadata": metadata,
                    "payment_link": payment_link,
                    "payment_method_id": payment_method_id,
                    "redirect_immediately": redirect_immediately,
                    "return_url": return_url,
                    "short_link": short_link,
                    "show_saved_payment_methods": show_saved_payment_methods,
                    "tax_id": tax_id,
                },
                payment_create_params.PaymentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentCreateResponse,
        )

    async def retrieve(
        self,
        payment_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Payment:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not payment_id:
            raise ValueError(f"Expected a non-empty value for `payment_id` but received {payment_id!r}")
        return await self._get(
            f"/payments/{payment_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Payment,
        )

    def list(
        self,
        *,
        brand_id: str | Omit = omit,
        created_at_gte: Union[str, datetime] | Omit = omit,
        created_at_lte: Union[str, datetime] | Omit = omit,
        customer_id: str | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        product_id: str | Omit = omit,
        status: Literal[
            "succeeded",
            "failed",
            "cancelled",
            "processing",
            "requires_customer_action",
            "requires_merchant_action",
            "requires_payment_method",
            "requires_confirmation",
            "requires_capture",
            "partially_captured",
            "partially_captured_and_capturable",
        ]
        | Omit = omit,
        subscription_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PaymentListResponse, AsyncDefaultPageNumberPagination[PaymentListResponse]]:
        """
        Args:
          brand_id: filter by Brand id

          created_at_gte: Get events after this created time

          created_at_lte: Get events created before this time

          customer_id: Filter by customer id

          page_number: Page number default is 0

          page_size: Page size default is 10 max is 100

          product_id: Filter by product id

          status: Filter by status

          subscription_id: Filter by subscription id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/payments",
            page=AsyncDefaultPageNumberPagination[PaymentListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "brand_id": brand_id,
                        "created_at_gte": created_at_gte,
                        "created_at_lte": created_at_lte,
                        "customer_id": customer_id,
                        "page_number": page_number,
                        "page_size": page_size,
                        "product_id": product_id,
                        "status": status,
                        "subscription_id": subscription_id,
                    },
                    payment_list_params.PaymentListParams,
                ),
            ),
            model=PaymentListResponse,
        )

    async def retrieve_line_items(
        self,
        payment_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentRetrieveLineItemsResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not payment_id:
            raise ValueError(f"Expected a non-empty value for `payment_id` but received {payment_id!r}")
        return await self._get(
            f"/payments/{payment_id}/line-items",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentRetrieveLineItemsResponse,
        )


class PaymentsResourceWithRawResponse:
    def __init__(self, payments: PaymentsResource) -> None:
        self._payments = payments

        self.create = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                payments.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.retrieve = to_raw_response_wrapper(
            payments.retrieve,
        )
        self.list = to_raw_response_wrapper(
            payments.list,
        )
        self.retrieve_line_items = to_raw_response_wrapper(
            payments.retrieve_line_items,
        )


class AsyncPaymentsResourceWithRawResponse:
    def __init__(self, payments: AsyncPaymentsResource) -> None:
        self._payments = payments

        self.create = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                payments.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.retrieve = async_to_raw_response_wrapper(
            payments.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            payments.list,
        )
        self.retrieve_line_items = async_to_raw_response_wrapper(
            payments.retrieve_line_items,
        )


class PaymentsResourceWithStreamingResponse:
    def __init__(self, payments: PaymentsResource) -> None:
        self._payments = payments

        self.create = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                payments.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.retrieve = to_streamed_response_wrapper(
            payments.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            payments.list,
        )
        self.retrieve_line_items = to_streamed_response_wrapper(
            payments.retrieve_line_items,
        )


class AsyncPaymentsResourceWithStreamingResponse:
    def __init__(self, payments: AsyncPaymentsResource) -> None:
        self._payments = payments

        self.create = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                payments.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.retrieve = async_to_streamed_response_wrapper(
            payments.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            payments.list,
        )
        self.retrieve_line_items = async_to_streamed_response_wrapper(
            payments.retrieve_line_items,
        )
