# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import (
    IntentStatus,
    payment_list_params,
    payment_create_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
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
from ..types.intent_status import IntentStatus
from ..types.billing_address_param import BillingAddressParam
from ..types.payment_list_response import PaymentListResponse
from ..types.customer_request_param import CustomerRequestParam
from ..types.payment_create_response import PaymentCreateResponse
from ..types.one_time_product_cart_item_param import OneTimeProductCartItemParam

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

    def create(
        self,
        *,
        billing: BillingAddressParam,
        customer: CustomerRequestParam,
        product_cart: Iterable[OneTimeProductCartItemParam],
        allowed_payment_method_types: Optional[
            List[
                Literal[
                    "credit",
                    "debit",
                    "upi_collect",
                    "upi_intent",
                    "apple_pay",
                    "cashapp",
                    "google_pay",
                    "multibanco",
                    "bancontact_card",
                    "eps",
                    "ideal",
                    "przelewy24",
                    "affirm",
                    "klarna",
                    "sepa",
                    "ach",
                    "amazon_pay",
                    "afterpay_clearpay",
                ]
            ]
        ]
        | NotGiven = NOT_GIVEN,
        billing_currency: Optional[
            Literal[
                "AED",
                "ALL",
                "AMD",
                "ANG",
                "AOA",
                "ARS",
                "AUD",
                "AWG",
                "AZN",
                "BAM",
                "BBD",
                "BDT",
                "BGN",
                "BHD",
                "BIF",
                "BMD",
                "BND",
                "BOB",
                "BRL",
                "BSD",
                "BWP",
                "BYN",
                "BZD",
                "CAD",
                "CHF",
                "CLP",
                "CNY",
                "COP",
                "CRC",
                "CUP",
                "CVE",
                "CZK",
                "DJF",
                "DKK",
                "DOP",
                "DZD",
                "EGP",
                "ETB",
                "EUR",
                "FJD",
                "FKP",
                "GBP",
                "GEL",
                "GHS",
                "GIP",
                "GMD",
                "GNF",
                "GTQ",
                "GYD",
                "HKD",
                "HNL",
                "HRK",
                "HTG",
                "HUF",
                "IDR",
                "ILS",
                "INR",
                "IQD",
                "JMD",
                "JOD",
                "JPY",
                "KES",
                "KGS",
                "KHR",
                "KMF",
                "KRW",
                "KWD",
                "KYD",
                "KZT",
                "LAK",
                "LBP",
                "LKR",
                "LRD",
                "LSL",
                "LYD",
                "MAD",
                "MDL",
                "MGA",
                "MKD",
                "MMK",
                "MNT",
                "MOP",
                "MRU",
                "MUR",
                "MVR",
                "MWK",
                "MXN",
                "MYR",
                "MZN",
                "NAD",
                "NGN",
                "NIO",
                "NOK",
                "NPR",
                "NZD",
                "OMR",
                "PAB",
                "PEN",
                "PGK",
                "PHP",
                "PKR",
                "PLN",
                "PYG",
                "QAR",
                "RON",
                "RSD",
                "RUB",
                "RWF",
                "SAR",
                "SBD",
                "SCR",
                "SEK",
                "SGD",
                "SHP",
                "SLE",
                "SLL",
                "SOS",
                "SRD",
                "SSP",
                "STN",
                "SVC",
                "SZL",
                "THB",
                "TND",
                "TOP",
                "TRY",
                "TTD",
                "TWD",
                "TZS",
                "UAH",
                "UGX",
                "USD",
                "UYU",
                "UZS",
                "VES",
                "VND",
                "VUV",
                "WST",
                "XAF",
                "XCD",
                "XOF",
                "XPF",
                "YER",
                "ZAR",
                "ZMW",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        discount_code: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        payment_link: Optional[bool] | NotGiven = NOT_GIVEN,
        return_url: Optional[str] | NotGiven = NOT_GIVEN,
        show_saved_payment_methods: bool | NotGiven = NOT_GIVEN,
        tax_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentCreateResponse:
        """Args:
          product_cart: List of products in the cart.

        Must contain at least 1 and at most 100 items.

          allowed_payment_method_types: List of payment methods allowed during checkout.

              Customers will **never** see payment methods that are **not** in this list.
              However, adding a method here **does not guarantee** customers will see it.
              Availability still depends on other factors (e.g., customer location, merchant
              settings).

          discount_code: Discount Code to apply to the transaction

          payment_link: Whether to generate a payment link. Defaults to false if not specified.

          return_url: Optional URL to redirect the customer after payment. Must be a valid URL if
              provided.

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
                    "metadata": metadata,
                    "payment_link": payment_link,
                    "return_url": return_url,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        created_at_gte: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        created_at_lte: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        customer_id: Optional[str] | NotGiven = NOT_GIVEN,
        page_number: Optional[int] | NotGiven = NOT_GIVEN,
        page_size: Optional[int] | NotGiven = NOT_GIVEN,
        status: Optional[IntentStatus] | NotGiven = NOT_GIVEN,
        subscription_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncDefaultPageNumberPagination[PaymentListResponse]:
        """
        Args:
          created_at_gte: Get events after this created time

          created_at_lte: Get events created before this time

          customer_id: Filter by customer id

          page_number: Page number default is 0

          page_size: Page size default is 10 max is 100

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
                        "created_at_gte": created_at_gte,
                        "created_at_lte": created_at_lte,
                        "customer_id": customer_id,
                        "page_number": page_number,
                        "page_size": page_size,
                        "status": status,
                        "subscription_id": subscription_id,
                    },
                    payment_list_params.PaymentListParams,
                ),
            ),
            model=PaymentListResponse,
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

    async def create(
        self,
        *,
        billing: BillingAddressParam,
        customer: CustomerRequestParam,
        product_cart: Iterable[OneTimeProductCartItemParam],
        allowed_payment_method_types: Optional[
            List[
                Literal[
                    "credit",
                    "debit",
                    "upi_collect",
                    "upi_intent",
                    "apple_pay",
                    "cashapp",
                    "google_pay",
                    "multibanco",
                    "bancontact_card",
                    "eps",
                    "ideal",
                    "przelewy24",
                    "affirm",
                    "klarna",
                    "sepa",
                    "ach",
                    "amazon_pay",
                    "afterpay_clearpay",
                ]
            ]
        ]
        | NotGiven = NOT_GIVEN,
        billing_currency: Optional[
            Literal[
                "AED",
                "ALL",
                "AMD",
                "ANG",
                "AOA",
                "ARS",
                "AUD",
                "AWG",
                "AZN",
                "BAM",
                "BBD",
                "BDT",
                "BGN",
                "BHD",
                "BIF",
                "BMD",
                "BND",
                "BOB",
                "BRL",
                "BSD",
                "BWP",
                "BYN",
                "BZD",
                "CAD",
                "CHF",
                "CLP",
                "CNY",
                "COP",
                "CRC",
                "CUP",
                "CVE",
                "CZK",
                "DJF",
                "DKK",
                "DOP",
                "DZD",
                "EGP",
                "ETB",
                "EUR",
                "FJD",
                "FKP",
                "GBP",
                "GEL",
                "GHS",
                "GIP",
                "GMD",
                "GNF",
                "GTQ",
                "GYD",
                "HKD",
                "HNL",
                "HRK",
                "HTG",
                "HUF",
                "IDR",
                "ILS",
                "INR",
                "IQD",
                "JMD",
                "JOD",
                "JPY",
                "KES",
                "KGS",
                "KHR",
                "KMF",
                "KRW",
                "KWD",
                "KYD",
                "KZT",
                "LAK",
                "LBP",
                "LKR",
                "LRD",
                "LSL",
                "LYD",
                "MAD",
                "MDL",
                "MGA",
                "MKD",
                "MMK",
                "MNT",
                "MOP",
                "MRU",
                "MUR",
                "MVR",
                "MWK",
                "MXN",
                "MYR",
                "MZN",
                "NAD",
                "NGN",
                "NIO",
                "NOK",
                "NPR",
                "NZD",
                "OMR",
                "PAB",
                "PEN",
                "PGK",
                "PHP",
                "PKR",
                "PLN",
                "PYG",
                "QAR",
                "RON",
                "RSD",
                "RUB",
                "RWF",
                "SAR",
                "SBD",
                "SCR",
                "SEK",
                "SGD",
                "SHP",
                "SLE",
                "SLL",
                "SOS",
                "SRD",
                "SSP",
                "STN",
                "SVC",
                "SZL",
                "THB",
                "TND",
                "TOP",
                "TRY",
                "TTD",
                "TWD",
                "TZS",
                "UAH",
                "UGX",
                "USD",
                "UYU",
                "UZS",
                "VES",
                "VND",
                "VUV",
                "WST",
                "XAF",
                "XCD",
                "XOF",
                "XPF",
                "YER",
                "ZAR",
                "ZMW",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        discount_code: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        payment_link: Optional[bool] | NotGiven = NOT_GIVEN,
        return_url: Optional[str] | NotGiven = NOT_GIVEN,
        show_saved_payment_methods: bool | NotGiven = NOT_GIVEN,
        tax_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentCreateResponse:
        """Args:
          product_cart: List of products in the cart.

        Must contain at least 1 and at most 100 items.

          allowed_payment_method_types: List of payment methods allowed during checkout.

              Customers will **never** see payment methods that are **not** in this list.
              However, adding a method here **does not guarantee** customers will see it.
              Availability still depends on other factors (e.g., customer location, merchant
              settings).

          discount_code: Discount Code to apply to the transaction

          payment_link: Whether to generate a payment link. Defaults to false if not specified.

          return_url: Optional URL to redirect the customer after payment. Must be a valid URL if
              provided.

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
                    "metadata": metadata,
                    "payment_link": payment_link,
                    "return_url": return_url,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        created_at_gte: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        created_at_lte: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        customer_id: Optional[str] | NotGiven = NOT_GIVEN,
        page_number: Optional[int] | NotGiven = NOT_GIVEN,
        page_size: Optional[int] | NotGiven = NOT_GIVEN,
        status: Optional[IntentStatus] | NotGiven = NOT_GIVEN,
        subscription_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[PaymentListResponse, AsyncDefaultPageNumberPagination[PaymentListResponse]]:
        """
        Args:
          created_at_gte: Get events after this created time

          created_at_lte: Get events created before this time

          customer_id: Filter by customer id

          page_number: Page number default is 0

          page_size: Page size default is 10 max is 100

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
                        "created_at_gte": created_at_gte,
                        "created_at_lte": created_at_lte,
                        "customer_id": customer_id,
                        "page_number": page_number,
                        "page_size": page_size,
                        "status": status,
                        "subscription_id": subscription_id,
                    },
                    payment_list_params.PaymentListParams,
                ),
            ),
            model=PaymentListResponse,
        )


class PaymentsResourceWithRawResponse:
    def __init__(self, payments: PaymentsResource) -> None:
        self._payments = payments

        self.create = to_raw_response_wrapper(
            payments.create,
        )
        self.retrieve = to_raw_response_wrapper(
            payments.retrieve,
        )
        self.list = to_raw_response_wrapper(
            payments.list,
        )


class AsyncPaymentsResourceWithRawResponse:
    def __init__(self, payments: AsyncPaymentsResource) -> None:
        self._payments = payments

        self.create = async_to_raw_response_wrapper(
            payments.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            payments.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            payments.list,
        )


class PaymentsResourceWithStreamingResponse:
    def __init__(self, payments: PaymentsResource) -> None:
        self._payments = payments

        self.create = to_streamed_response_wrapper(
            payments.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            payments.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            payments.list,
        )


class AsyncPaymentsResourceWithStreamingResponse:
    def __init__(self, payments: AsyncPaymentsResource) -> None:
        self._payments = payments

        self.create = async_to_streamed_response_wrapper(
            payments.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            payments.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            payments.list,
        )
