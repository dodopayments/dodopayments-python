# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import (
    SubscriptionStatus,
    subscription_list_params,
    subscription_charge_params,
    subscription_create_params,
    subscription_update_params,
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
from ..types.subscription import Subscription
from ..types.subscription_status import SubscriptionStatus
from ..types.billing_address_param import BillingAddressParam
from ..types.customer_request_param import CustomerRequestParam
from ..types.subscription_charge_response import SubscriptionChargeResponse
from ..types.subscription_create_response import SubscriptionCreateResponse

__all__ = ["SubscriptionsResource", "AsyncSubscriptionsResource"]


class SubscriptionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SubscriptionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return SubscriptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SubscriptionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return SubscriptionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        billing: BillingAddressParam,
        customer: CustomerRequestParam,
        product_id: str,
        quantity: int,
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
        on_demand: Optional[subscription_create_params.OnDemand] | NotGiven = NOT_GIVEN,
        payment_link: Optional[bool] | NotGiven = NOT_GIVEN,
        return_url: Optional[str] | NotGiven = NOT_GIVEN,
        show_saved_payment_methods: bool | NotGiven = NOT_GIVEN,
        tax_id: Optional[str] | NotGiven = NOT_GIVEN,
        trial_period_days: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubscriptionCreateResponse:
        """
        Args:
          product_id: Unique identifier of the product to subscribe to

          quantity: Number of units to subscribe for. Must be at least 1.

          allowed_payment_method_types: List of payment methods allowed during checkout.

              Customers will **never** see payment methods that are **not** in this list.
              However, adding a method here **does not guarantee** customers will see it.
              Availability still depends on other factors (e.g., customer location, merchant
              settings).

          discount_code: Discount Code to apply to the subscription

          payment_link: If true, generates a payment link. Defaults to false if not specified.

          return_url: Optional URL to redirect after successful subscription creation

          show_saved_payment_methods: Display saved payment methods of a returning customer False by default

          tax_id: Tax ID in case the payment is B2B. If tax id validation fails the payment
              creation will fail

          trial_period_days: Optional trial period in days If specified, this value overrides the trial
              period set in the product's price Must be between 0 and 10000 days

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/subscriptions",
            body=maybe_transform(
                {
                    "billing": billing,
                    "customer": customer,
                    "product_id": product_id,
                    "quantity": quantity,
                    "allowed_payment_method_types": allowed_payment_method_types,
                    "billing_currency": billing_currency,
                    "discount_code": discount_code,
                    "metadata": metadata,
                    "on_demand": on_demand,
                    "payment_link": payment_link,
                    "return_url": return_url,
                    "show_saved_payment_methods": show_saved_payment_methods,
                    "tax_id": tax_id,
                    "trial_period_days": trial_period_days,
                },
                subscription_create_params.SubscriptionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionCreateResponse,
        )

    def retrieve(
        self,
        subscription_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Subscription:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
        return self._get(
            f"/subscriptions/{subscription_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Subscription,
        )

    def update(
        self,
        subscription_id: str,
        *,
        billing: Optional[BillingAddressParam] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        status: Optional[SubscriptionStatus] | NotGiven = NOT_GIVEN,
        tax_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Subscription:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
        return self._patch(
            f"/subscriptions/{subscription_id}",
            body=maybe_transform(
                {
                    "billing": billing,
                    "metadata": metadata,
                    "status": status,
                    "tax_id": tax_id,
                },
                subscription_update_params.SubscriptionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Subscription,
        )

    def list(
        self,
        *,
        created_at_gte: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        created_at_lte: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        customer_id: Optional[str] | NotGiven = NOT_GIVEN,
        page_number: Optional[int] | NotGiven = NOT_GIVEN,
        page_size: Optional[int] | NotGiven = NOT_GIVEN,
        status: Optional[SubscriptionStatus] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncDefaultPageNumberPagination[Subscription]:
        """
        Args:
          created_at_gte: Get events after this created time

          created_at_lte: Get events created before this time

          customer_id: Filter by customer id

          page_number: Page number default is 0

          page_size: Page size default is 10 max is 100

          status: Filter by status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/subscriptions",
            page=SyncDefaultPageNumberPagination[Subscription],
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
                    subscription_list_params.SubscriptionListParams,
                ),
            ),
            model=Subscription,
        )

    def charge(
        self,
        subscription_id: str,
        *,
        product_price: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubscriptionChargeResponse:
        """Args:
          product_price: The product price.

        Represented in the lowest denomination of the currency (e.g.,
              cents for USD). For example, to charge $1.00, pass `100`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
        return self._post(
            f"/subscriptions/{subscription_id}/charge",
            body=maybe_transform({"product_price": product_price}, subscription_charge_params.SubscriptionChargeParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionChargeResponse,
        )


class AsyncSubscriptionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSubscriptionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSubscriptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSubscriptionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return AsyncSubscriptionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        billing: BillingAddressParam,
        customer: CustomerRequestParam,
        product_id: str,
        quantity: int,
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
        on_demand: Optional[subscription_create_params.OnDemand] | NotGiven = NOT_GIVEN,
        payment_link: Optional[bool] | NotGiven = NOT_GIVEN,
        return_url: Optional[str] | NotGiven = NOT_GIVEN,
        show_saved_payment_methods: bool | NotGiven = NOT_GIVEN,
        tax_id: Optional[str] | NotGiven = NOT_GIVEN,
        trial_period_days: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubscriptionCreateResponse:
        """
        Args:
          product_id: Unique identifier of the product to subscribe to

          quantity: Number of units to subscribe for. Must be at least 1.

          allowed_payment_method_types: List of payment methods allowed during checkout.

              Customers will **never** see payment methods that are **not** in this list.
              However, adding a method here **does not guarantee** customers will see it.
              Availability still depends on other factors (e.g., customer location, merchant
              settings).

          discount_code: Discount Code to apply to the subscription

          payment_link: If true, generates a payment link. Defaults to false if not specified.

          return_url: Optional URL to redirect after successful subscription creation

          show_saved_payment_methods: Display saved payment methods of a returning customer False by default

          tax_id: Tax ID in case the payment is B2B. If tax id validation fails the payment
              creation will fail

          trial_period_days: Optional trial period in days If specified, this value overrides the trial
              period set in the product's price Must be between 0 and 10000 days

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/subscriptions",
            body=await async_maybe_transform(
                {
                    "billing": billing,
                    "customer": customer,
                    "product_id": product_id,
                    "quantity": quantity,
                    "allowed_payment_method_types": allowed_payment_method_types,
                    "billing_currency": billing_currency,
                    "discount_code": discount_code,
                    "metadata": metadata,
                    "on_demand": on_demand,
                    "payment_link": payment_link,
                    "return_url": return_url,
                    "show_saved_payment_methods": show_saved_payment_methods,
                    "tax_id": tax_id,
                    "trial_period_days": trial_period_days,
                },
                subscription_create_params.SubscriptionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionCreateResponse,
        )

    async def retrieve(
        self,
        subscription_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Subscription:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
        return await self._get(
            f"/subscriptions/{subscription_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Subscription,
        )

    async def update(
        self,
        subscription_id: str,
        *,
        billing: Optional[BillingAddressParam] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        status: Optional[SubscriptionStatus] | NotGiven = NOT_GIVEN,
        tax_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Subscription:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
        return await self._patch(
            f"/subscriptions/{subscription_id}",
            body=await async_maybe_transform(
                {
                    "billing": billing,
                    "metadata": metadata,
                    "status": status,
                    "tax_id": tax_id,
                },
                subscription_update_params.SubscriptionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Subscription,
        )

    def list(
        self,
        *,
        created_at_gte: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        created_at_lte: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        customer_id: Optional[str] | NotGiven = NOT_GIVEN,
        page_number: Optional[int] | NotGiven = NOT_GIVEN,
        page_size: Optional[int] | NotGiven = NOT_GIVEN,
        status: Optional[SubscriptionStatus] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Subscription, AsyncDefaultPageNumberPagination[Subscription]]:
        """
        Args:
          created_at_gte: Get events after this created time

          created_at_lte: Get events created before this time

          customer_id: Filter by customer id

          page_number: Page number default is 0

          page_size: Page size default is 10 max is 100

          status: Filter by status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/subscriptions",
            page=AsyncDefaultPageNumberPagination[Subscription],
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
                    subscription_list_params.SubscriptionListParams,
                ),
            ),
            model=Subscription,
        )

    async def charge(
        self,
        subscription_id: str,
        *,
        product_price: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubscriptionChargeResponse:
        """Args:
          product_price: The product price.

        Represented in the lowest denomination of the currency (e.g.,
              cents for USD). For example, to charge $1.00, pass `100`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
        return await self._post(
            f"/subscriptions/{subscription_id}/charge",
            body=await async_maybe_transform(
                {"product_price": product_price}, subscription_charge_params.SubscriptionChargeParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionChargeResponse,
        )


class SubscriptionsResourceWithRawResponse:
    def __init__(self, subscriptions: SubscriptionsResource) -> None:
        self._subscriptions = subscriptions

        self.create = to_raw_response_wrapper(
            subscriptions.create,
        )
        self.retrieve = to_raw_response_wrapper(
            subscriptions.retrieve,
        )
        self.update = to_raw_response_wrapper(
            subscriptions.update,
        )
        self.list = to_raw_response_wrapper(
            subscriptions.list,
        )
        self.charge = to_raw_response_wrapper(
            subscriptions.charge,
        )


class AsyncSubscriptionsResourceWithRawResponse:
    def __init__(self, subscriptions: AsyncSubscriptionsResource) -> None:
        self._subscriptions = subscriptions

        self.create = async_to_raw_response_wrapper(
            subscriptions.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            subscriptions.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            subscriptions.update,
        )
        self.list = async_to_raw_response_wrapper(
            subscriptions.list,
        )
        self.charge = async_to_raw_response_wrapper(
            subscriptions.charge,
        )


class SubscriptionsResourceWithStreamingResponse:
    def __init__(self, subscriptions: SubscriptionsResource) -> None:
        self._subscriptions = subscriptions

        self.create = to_streamed_response_wrapper(
            subscriptions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            subscriptions.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            subscriptions.update,
        )
        self.list = to_streamed_response_wrapper(
            subscriptions.list,
        )
        self.charge = to_streamed_response_wrapper(
            subscriptions.charge,
        )


class AsyncSubscriptionsResourceWithStreamingResponse:
    def __init__(self, subscriptions: AsyncSubscriptionsResource) -> None:
        self._subscriptions = subscriptions

        self.create = async_to_streamed_response_wrapper(
            subscriptions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            subscriptions.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            subscriptions.update,
        )
        self.list = async_to_streamed_response_wrapper(
            subscriptions.list,
        )
        self.charge = async_to_streamed_response_wrapper(
            subscriptions.charge,
        )
