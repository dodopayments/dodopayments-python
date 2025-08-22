# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable, Optional

import httpx

from ..types import Currency, checkout_session_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.currency import Currency
from ..types.payment_method_types import PaymentMethodTypes
from ..types.customer_request_param import CustomerRequestParam
from ..types.checkout_session_response import CheckoutSessionResponse

__all__ = ["CheckoutSessionsResource", "AsyncCheckoutSessionsResource"]


class CheckoutSessionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CheckoutSessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return CheckoutSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CheckoutSessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return CheckoutSessionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        product_cart: Iterable[checkout_session_create_params.ProductCart],
        allowed_payment_method_types: Optional[List[PaymentMethodTypes]] | NotGiven = NOT_GIVEN,
        billing_address: Optional[checkout_session_create_params.BillingAddress] | NotGiven = NOT_GIVEN,
        billing_currency: Optional[Currency] | NotGiven = NOT_GIVEN,
        confirm: bool | NotGiven = NOT_GIVEN,
        customer: Optional[CustomerRequestParam] | NotGiven = NOT_GIVEN,
        customization: checkout_session_create_params.Customization | NotGiven = NOT_GIVEN,
        discount_code: Optional[str] | NotGiven = NOT_GIVEN,
        feature_flags: checkout_session_create_params.FeatureFlags | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        return_url: Optional[str] | NotGiven = NOT_GIVEN,
        show_saved_payment_methods: bool | NotGiven = NOT_GIVEN,
        subscription_data: Optional[checkout_session_create_params.SubscriptionData] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CheckoutSessionResponse:
        """
        Args:
          allowed_payment_method_types: Customers will never see payment methods that are not in this list. However,
              adding a method here does not guarantee customers will see it. Availability
              still depends on other factors (e.g., customer location, merchant settings).

              Disclaimar: Always provide 'credit' and 'debit' as a fallback. If all payment
              methods are unavailable, checkout session will fail.

          billing_address: Billing address information for the session

          billing_currency: This field is ingored if adaptive pricing is disabled

          confirm: If confirm is true, all the details will be finalized. If required data is
              missing, an API error is thrown.

          customer: Customer details for the session

          customization: Customization for the checkout session page

          metadata: Additional metadata associated with the payment. Defaults to empty if not
              provided.

          return_url: The url to redirect after payment failure or success.

          show_saved_payment_methods: Display saved payment methods of a returning customer False by default

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/checkouts",
            body=maybe_transform(
                {
                    "product_cart": product_cart,
                    "allowed_payment_method_types": allowed_payment_method_types,
                    "billing_address": billing_address,
                    "billing_currency": billing_currency,
                    "confirm": confirm,
                    "customer": customer,
                    "customization": customization,
                    "discount_code": discount_code,
                    "feature_flags": feature_flags,
                    "metadata": metadata,
                    "return_url": return_url,
                    "show_saved_payment_methods": show_saved_payment_methods,
                    "subscription_data": subscription_data,
                },
                checkout_session_create_params.CheckoutSessionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CheckoutSessionResponse,
        )


class AsyncCheckoutSessionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCheckoutSessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCheckoutSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCheckoutSessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return AsyncCheckoutSessionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        product_cart: Iterable[checkout_session_create_params.ProductCart],
        allowed_payment_method_types: Optional[List[PaymentMethodTypes]] | NotGiven = NOT_GIVEN,
        billing_address: Optional[checkout_session_create_params.BillingAddress] | NotGiven = NOT_GIVEN,
        billing_currency: Optional[Currency] | NotGiven = NOT_GIVEN,
        confirm: bool | NotGiven = NOT_GIVEN,
        customer: Optional[CustomerRequestParam] | NotGiven = NOT_GIVEN,
        customization: checkout_session_create_params.Customization | NotGiven = NOT_GIVEN,
        discount_code: Optional[str] | NotGiven = NOT_GIVEN,
        feature_flags: checkout_session_create_params.FeatureFlags | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        return_url: Optional[str] | NotGiven = NOT_GIVEN,
        show_saved_payment_methods: bool | NotGiven = NOT_GIVEN,
        subscription_data: Optional[checkout_session_create_params.SubscriptionData] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CheckoutSessionResponse:
        """
        Args:
          allowed_payment_method_types: Customers will never see payment methods that are not in this list. However,
              adding a method here does not guarantee customers will see it. Availability
              still depends on other factors (e.g., customer location, merchant settings).

              Disclaimar: Always provide 'credit' and 'debit' as a fallback. If all payment
              methods are unavailable, checkout session will fail.

          billing_address: Billing address information for the session

          billing_currency: This field is ingored if adaptive pricing is disabled

          confirm: If confirm is true, all the details will be finalized. If required data is
              missing, an API error is thrown.

          customer: Customer details for the session

          customization: Customization for the checkout session page

          metadata: Additional metadata associated with the payment. Defaults to empty if not
              provided.

          return_url: The url to redirect after payment failure or success.

          show_saved_payment_methods: Display saved payment methods of a returning customer False by default

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/checkouts",
            body=await async_maybe_transform(
                {
                    "product_cart": product_cart,
                    "allowed_payment_method_types": allowed_payment_method_types,
                    "billing_address": billing_address,
                    "billing_currency": billing_currency,
                    "confirm": confirm,
                    "customer": customer,
                    "customization": customization,
                    "discount_code": discount_code,
                    "feature_flags": feature_flags,
                    "metadata": metadata,
                    "return_url": return_url,
                    "show_saved_payment_methods": show_saved_payment_methods,
                    "subscription_data": subscription_data,
                },
                checkout_session_create_params.CheckoutSessionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CheckoutSessionResponse,
        )


class CheckoutSessionsResourceWithRawResponse:
    def __init__(self, checkout_sessions: CheckoutSessionsResource) -> None:
        self._checkout_sessions = checkout_sessions

        self.create = to_raw_response_wrapper(
            checkout_sessions.create,
        )


class AsyncCheckoutSessionsResourceWithRawResponse:
    def __init__(self, checkout_sessions: AsyncCheckoutSessionsResource) -> None:
        self._checkout_sessions = checkout_sessions

        self.create = async_to_raw_response_wrapper(
            checkout_sessions.create,
        )


class CheckoutSessionsResourceWithStreamingResponse:
    def __init__(self, checkout_sessions: CheckoutSessionsResource) -> None:
        self._checkout_sessions = checkout_sessions

        self.create = to_streamed_response_wrapper(
            checkout_sessions.create,
        )


class AsyncCheckoutSessionsResourceWithStreamingResponse:
    def __init__(self, checkout_sessions: AsyncCheckoutSessionsResource) -> None:
        self._checkout_sessions = checkout_sessions

        self.create = async_to_streamed_response_wrapper(
            checkout_sessions.create,
        )
