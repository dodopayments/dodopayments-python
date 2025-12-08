# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, overload

import httpx

from ..types import (
    Currency,
    SubscriptionStatus,
    subscription_list_params,
    subscription_charge_params,
    subscription_create_params,
    subscription_update_params,
    subscription_change_plan_params,
    subscription_preview_change_plan_params,
    subscription_update_payment_method_params,
    subscription_retrieve_usage_history_params,
)
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import required_args, maybe_transform, async_maybe_transform
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
from ..types.currency import Currency
from ..types.subscription import Subscription
from ..types.attach_addon_param import AttachAddonParam
from ..types.subscription_status import SubscriptionStatus
from ..types.payment_method_types import PaymentMethodTypes
from ..types.billing_address_param import BillingAddressParam
from ..types.customer_request_param import CustomerRequestParam
from ..types.subscription_list_response import SubscriptionListResponse
from ..types.on_demand_subscription_param import OnDemandSubscriptionParam
from ..types.subscription_charge_response import SubscriptionChargeResponse
from ..types.subscription_create_response import SubscriptionCreateResponse
from ..types.subscription_preview_change_plan_response import SubscriptionPreviewChangePlanResponse
from ..types.subscription_update_payment_method_response import SubscriptionUpdatePaymentMethodResponse
from ..types.subscription_retrieve_usage_history_response import SubscriptionRetrieveUsageHistoryResponse

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
        addons: Optional[Iterable[AttachAddonParam]] | Omit = omit,
        allowed_payment_method_types: Optional[List[PaymentMethodTypes]] | Omit = omit,
        billing_currency: Optional[Currency] | Omit = omit,
        discount_code: Optional[str] | Omit = omit,
        force_3ds: Optional[bool] | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        on_demand: Optional[OnDemandSubscriptionParam] | Omit = omit,
        payment_link: Optional[bool] | Omit = omit,
        return_url: Optional[str] | Omit = omit,
        show_saved_payment_methods: bool | Omit = omit,
        tax_id: Optional[str] | Omit = omit,
        trial_period_days: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionCreateResponse:
        """
        Args:
          billing: Billing address information for the subscription

          customer: Customer details for the subscription

          product_id: Unique identifier of the product to subscribe to

          quantity: Number of units to subscribe for. Must be at least 1.

          addons: Attach addons to this subscription

          allowed_payment_method_types: List of payment methods allowed during checkout.

              Customers will **never** see payment methods that are **not** in this list.
              However, adding a method here **does not guarantee** customers will see it.
              Availability still depends on other factors (e.g., customer location, merchant
              settings).

          billing_currency: Fix the currency in which the end customer is billed. If Dodo Payments cannot
              support that currency for this transaction, it will not proceed

          discount_code: Discount Code to apply to the subscription

          force_3ds: Override merchant default 3DS behaviour for this subscription

          metadata: Additional metadata for the subscription Defaults to empty if not specified

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
                    "addons": addons,
                    "allowed_payment_method_types": allowed_payment_method_types,
                    "billing_currency": billing_currency,
                    "discount_code": discount_code,
                    "force_3ds": force_3ds,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        billing: Optional[BillingAddressParam] | Omit = omit,
        cancel_at_next_billing_date: Optional[bool] | Omit = omit,
        customer_name: Optional[str] | Omit = omit,
        disable_on_demand: Optional[subscription_update_params.DisableOnDemand] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        next_billing_date: Union[str, datetime, None] | Omit = omit,
        status: Optional[SubscriptionStatus] | Omit = omit,
        tax_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Subscription:
        """
        Args:
          cancel_at_next_billing_date: When set, the subscription will remain active until the end of billing period

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
                    "cancel_at_next_billing_date": cancel_at_next_billing_date,
                    "customer_name": customer_name,
                    "disable_on_demand": disable_on_demand,
                    "metadata": metadata,
                    "next_billing_date": next_billing_date,
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
        brand_id: str | Omit = omit,
        created_at_gte: Union[str, datetime] | Omit = omit,
        created_at_lte: Union[str, datetime] | Omit = omit,
        customer_id: str | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        status: Literal["pending", "active", "on_hold", "cancelled", "failed", "expired"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultPageNumberPagination[SubscriptionListResponse]:
        """
        Args:
          brand_id: filter by Brand id

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
            page=SyncDefaultPageNumberPagination[SubscriptionListResponse],
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
                        "status": status,
                    },
                    subscription_list_params.SubscriptionListParams,
                ),
            ),
            model=SubscriptionListResponse,
        )

    def change_plan(
        self,
        subscription_id: str,
        *,
        product_id: str,
        proration_billing_mode: Literal["prorated_immediately", "full_immediately", "difference_immediately"],
        quantity: int,
        addons: Optional[Iterable[AttachAddonParam]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          product_id: Unique identifier of the product to subscribe to

          proration_billing_mode: Proration Billing Mode

          quantity: Number of units to subscribe for. Must be at least 1.

          addons: Addons for the new plan. Note : Leaving this empty would remove any existing
              addons

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/subscriptions/{subscription_id}/change-plan",
            body=maybe_transform(
                {
                    "product_id": product_id,
                    "proration_billing_mode": proration_billing_mode,
                    "quantity": quantity,
                    "addons": addons,
                },
                subscription_change_plan_params.SubscriptionChangePlanParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def charge(
        self,
        subscription_id: str,
        *,
        product_price: int,
        adaptive_currency_fees_inclusive: Optional[bool] | Omit = omit,
        customer_balance_config: Optional[subscription_charge_params.CustomerBalanceConfig] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        product_currency: Optional[Currency] | Omit = omit,
        product_description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionChargeResponse:
        """Args:
          product_price: The product price.

        Represented in the lowest denomination of the currency (e.g.,
              cents for USD). For example, to charge $1.00, pass `100`.

          adaptive_currency_fees_inclusive: Whether adaptive currency fees should be included in the product_price (true) or
              added on top (false). This field is ignored if adaptive pricing is not enabled
              for the business.

          customer_balance_config: Specify how customer balance is used for the payment

          metadata: Metadata for the payment. If not passed, the metadata of the subscription will
              be taken

          product_currency: Optional currency of the product price. If not specified, defaults to the
              currency of the product.

          product_description: Optional product description override for billing and line items. If not
              specified, the stored description of the product will be used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
        return self._post(
            f"/subscriptions/{subscription_id}/charge",
            body=maybe_transform(
                {
                    "product_price": product_price,
                    "adaptive_currency_fees_inclusive": adaptive_currency_fees_inclusive,
                    "customer_balance_config": customer_balance_config,
                    "metadata": metadata,
                    "product_currency": product_currency,
                    "product_description": product_description,
                },
                subscription_charge_params.SubscriptionChargeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionChargeResponse,
        )

    def preview_change_plan(
        self,
        subscription_id: str,
        *,
        product_id: str,
        proration_billing_mode: Literal["prorated_immediately", "full_immediately", "difference_immediately"],
        quantity: int,
        addons: Optional[Iterable[AttachAddonParam]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionPreviewChangePlanResponse:
        """
        Args:
          product_id: Unique identifier of the product to subscribe to

          proration_billing_mode: Proration Billing Mode

          quantity: Number of units to subscribe for. Must be at least 1.

          addons: Addons for the new plan. Note : Leaving this empty would remove any existing
              addons

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
        return self._post(
            f"/subscriptions/{subscription_id}/change-plan/preview",
            body=maybe_transform(
                {
                    "product_id": product_id,
                    "proration_billing_mode": proration_billing_mode,
                    "quantity": quantity,
                    "addons": addons,
                },
                subscription_preview_change_plan_params.SubscriptionPreviewChangePlanParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionPreviewChangePlanResponse,
        )

    def retrieve_usage_history(
        self,
        subscription_id: str,
        *,
        end_date: Union[str, datetime, None] | Omit = omit,
        meter_id: Optional[str] | Omit = omit,
        page_number: Optional[int] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        start_date: Union[str, datetime, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultPageNumberPagination[SubscriptionRetrieveUsageHistoryResponse]:
        """
        Get detailed usage history for a subscription that includes usage-based billing
        (metered components). This endpoint provides insights into customer usage
        patterns and billing calculations over time.

        ## What You'll Get:

        - **Billing periods**: Each item represents a billing cycle with start and end
          dates
        - **Meter usage**: Detailed breakdown of usage for each meter configured on the
          subscription
        - **Usage calculations**: Total units consumed, free threshold units, and
          chargeable units
        - **Historical tracking**: Complete audit trail of usage-based charges

        ## Use Cases:

        - **Customer support**: Investigate billing questions and usage discrepancies
        - **Usage analytics**: Analyze customer consumption patterns over time
        - **Billing transparency**: Provide customers with detailed usage breakdowns
        - **Revenue optimization**: Identify usage trends to optimize pricing strategies

        ## Filtering Options:

        - **Date range filtering**: Get usage history for specific time periods
        - **Meter-specific filtering**: Focus on usage for a particular meter
        - **Pagination**: Navigate through large usage histories efficiently

        ## Important Notes:

        - Only returns data for subscriptions with usage-based (metered) components
        - Usage history is organized by billing periods (subscription cycles)
        - Free threshold units are calculated and displayed separately from chargeable
          units
        - Historical data is preserved even if meter configurations change

        ## Example Query Patterns:

        - Get last 3 months:
          `?start_date=2024-01-01T00:00:00Z&end_date=2024-03-31T23:59:59Z`
        - Filter by meter: `?meter_id=mtr_api_requests`
        - Paginate results: `?page_size=20&page_number=1`
        - Recent usage: `?start_date=2024-03-01T00:00:00Z` (from March 1st to now)

        Args:
          end_date: Filter by end date (inclusive)

          meter_id: Filter by specific meter ID

          page_number: Page number (default: 0)

          page_size: Page size (default: 10, max: 100)

          start_date: Filter by start date (inclusive)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
        return self._get_api_list(
            f"/subscriptions/{subscription_id}/usage-history",
            page=SyncDefaultPageNumberPagination[SubscriptionRetrieveUsageHistoryResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_date": end_date,
                        "meter_id": meter_id,
                        "page_number": page_number,
                        "page_size": page_size,
                        "start_date": start_date,
                    },
                    subscription_retrieve_usage_history_params.SubscriptionRetrieveUsageHistoryParams,
                ),
            ),
            model=SubscriptionRetrieveUsageHistoryResponse,
        )

    @overload
    def update_payment_method(
        self,
        subscription_id: str,
        *,
        type: Literal["new"],
        return_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionUpdatePaymentMethodResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update_payment_method(
        self,
        subscription_id: str,
        *,
        payment_method_id: str,
        type: Literal["existing"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionUpdatePaymentMethodResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["type"], ["payment_method_id", "type"])
    def update_payment_method(
        self,
        subscription_id: str,
        *,
        type: Literal["new"] | Literal["existing"],
        return_url: Optional[str] | Omit = omit,
        payment_method_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionUpdatePaymentMethodResponse:
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
        return self._post(
            f"/subscriptions/{subscription_id}/update-payment-method",
            body=maybe_transform(
                {
                    "type": type,
                    "return_url": return_url,
                    "payment_method_id": payment_method_id,
                },
                subscription_update_payment_method_params.SubscriptionUpdatePaymentMethodParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionUpdatePaymentMethodResponse,
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
        addons: Optional[Iterable[AttachAddonParam]] | Omit = omit,
        allowed_payment_method_types: Optional[List[PaymentMethodTypes]] | Omit = omit,
        billing_currency: Optional[Currency] | Omit = omit,
        discount_code: Optional[str] | Omit = omit,
        force_3ds: Optional[bool] | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        on_demand: Optional[OnDemandSubscriptionParam] | Omit = omit,
        payment_link: Optional[bool] | Omit = omit,
        return_url: Optional[str] | Omit = omit,
        show_saved_payment_methods: bool | Omit = omit,
        tax_id: Optional[str] | Omit = omit,
        trial_period_days: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionCreateResponse:
        """
        Args:
          billing: Billing address information for the subscription

          customer: Customer details for the subscription

          product_id: Unique identifier of the product to subscribe to

          quantity: Number of units to subscribe for. Must be at least 1.

          addons: Attach addons to this subscription

          allowed_payment_method_types: List of payment methods allowed during checkout.

              Customers will **never** see payment methods that are **not** in this list.
              However, adding a method here **does not guarantee** customers will see it.
              Availability still depends on other factors (e.g., customer location, merchant
              settings).

          billing_currency: Fix the currency in which the end customer is billed. If Dodo Payments cannot
              support that currency for this transaction, it will not proceed

          discount_code: Discount Code to apply to the subscription

          force_3ds: Override merchant default 3DS behaviour for this subscription

          metadata: Additional metadata for the subscription Defaults to empty if not specified

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
                    "addons": addons,
                    "allowed_payment_method_types": allowed_payment_method_types,
                    "billing_currency": billing_currency,
                    "discount_code": discount_code,
                    "force_3ds": force_3ds,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        billing: Optional[BillingAddressParam] | Omit = omit,
        cancel_at_next_billing_date: Optional[bool] | Omit = omit,
        customer_name: Optional[str] | Omit = omit,
        disable_on_demand: Optional[subscription_update_params.DisableOnDemand] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        next_billing_date: Union[str, datetime, None] | Omit = omit,
        status: Optional[SubscriptionStatus] | Omit = omit,
        tax_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Subscription:
        """
        Args:
          cancel_at_next_billing_date: When set, the subscription will remain active until the end of billing period

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
                    "cancel_at_next_billing_date": cancel_at_next_billing_date,
                    "customer_name": customer_name,
                    "disable_on_demand": disable_on_demand,
                    "metadata": metadata,
                    "next_billing_date": next_billing_date,
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
        brand_id: str | Omit = omit,
        created_at_gte: Union[str, datetime] | Omit = omit,
        created_at_lte: Union[str, datetime] | Omit = omit,
        customer_id: str | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        status: Literal["pending", "active", "on_hold", "cancelled", "failed", "expired"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[SubscriptionListResponse, AsyncDefaultPageNumberPagination[SubscriptionListResponse]]:
        """
        Args:
          brand_id: filter by Brand id

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
            page=AsyncDefaultPageNumberPagination[SubscriptionListResponse],
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
                        "status": status,
                    },
                    subscription_list_params.SubscriptionListParams,
                ),
            ),
            model=SubscriptionListResponse,
        )

    async def change_plan(
        self,
        subscription_id: str,
        *,
        product_id: str,
        proration_billing_mode: Literal["prorated_immediately", "full_immediately", "difference_immediately"],
        quantity: int,
        addons: Optional[Iterable[AttachAddonParam]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          product_id: Unique identifier of the product to subscribe to

          proration_billing_mode: Proration Billing Mode

          quantity: Number of units to subscribe for. Must be at least 1.

          addons: Addons for the new plan. Note : Leaving this empty would remove any existing
              addons

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/subscriptions/{subscription_id}/change-plan",
            body=await async_maybe_transform(
                {
                    "product_id": product_id,
                    "proration_billing_mode": proration_billing_mode,
                    "quantity": quantity,
                    "addons": addons,
                },
                subscription_change_plan_params.SubscriptionChangePlanParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def charge(
        self,
        subscription_id: str,
        *,
        product_price: int,
        adaptive_currency_fees_inclusive: Optional[bool] | Omit = omit,
        customer_balance_config: Optional[subscription_charge_params.CustomerBalanceConfig] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        product_currency: Optional[Currency] | Omit = omit,
        product_description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionChargeResponse:
        """Args:
          product_price: The product price.

        Represented in the lowest denomination of the currency (e.g.,
              cents for USD). For example, to charge $1.00, pass `100`.

          adaptive_currency_fees_inclusive: Whether adaptive currency fees should be included in the product_price (true) or
              added on top (false). This field is ignored if adaptive pricing is not enabled
              for the business.

          customer_balance_config: Specify how customer balance is used for the payment

          metadata: Metadata for the payment. If not passed, the metadata of the subscription will
              be taken

          product_currency: Optional currency of the product price. If not specified, defaults to the
              currency of the product.

          product_description: Optional product description override for billing and line items. If not
              specified, the stored description of the product will be used.

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
                {
                    "product_price": product_price,
                    "adaptive_currency_fees_inclusive": adaptive_currency_fees_inclusive,
                    "customer_balance_config": customer_balance_config,
                    "metadata": metadata,
                    "product_currency": product_currency,
                    "product_description": product_description,
                },
                subscription_charge_params.SubscriptionChargeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionChargeResponse,
        )

    async def preview_change_plan(
        self,
        subscription_id: str,
        *,
        product_id: str,
        proration_billing_mode: Literal["prorated_immediately", "full_immediately", "difference_immediately"],
        quantity: int,
        addons: Optional[Iterable[AttachAddonParam]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionPreviewChangePlanResponse:
        """
        Args:
          product_id: Unique identifier of the product to subscribe to

          proration_billing_mode: Proration Billing Mode

          quantity: Number of units to subscribe for. Must be at least 1.

          addons: Addons for the new plan. Note : Leaving this empty would remove any existing
              addons

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
        return await self._post(
            f"/subscriptions/{subscription_id}/change-plan/preview",
            body=await async_maybe_transform(
                {
                    "product_id": product_id,
                    "proration_billing_mode": proration_billing_mode,
                    "quantity": quantity,
                    "addons": addons,
                },
                subscription_preview_change_plan_params.SubscriptionPreviewChangePlanParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionPreviewChangePlanResponse,
        )

    def retrieve_usage_history(
        self,
        subscription_id: str,
        *,
        end_date: Union[str, datetime, None] | Omit = omit,
        meter_id: Optional[str] | Omit = omit,
        page_number: Optional[int] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        start_date: Union[str, datetime, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[
        SubscriptionRetrieveUsageHistoryResponse,
        AsyncDefaultPageNumberPagination[SubscriptionRetrieveUsageHistoryResponse],
    ]:
        """
        Get detailed usage history for a subscription that includes usage-based billing
        (metered components). This endpoint provides insights into customer usage
        patterns and billing calculations over time.

        ## What You'll Get:

        - **Billing periods**: Each item represents a billing cycle with start and end
          dates
        - **Meter usage**: Detailed breakdown of usage for each meter configured on the
          subscription
        - **Usage calculations**: Total units consumed, free threshold units, and
          chargeable units
        - **Historical tracking**: Complete audit trail of usage-based charges

        ## Use Cases:

        - **Customer support**: Investigate billing questions and usage discrepancies
        - **Usage analytics**: Analyze customer consumption patterns over time
        - **Billing transparency**: Provide customers with detailed usage breakdowns
        - **Revenue optimization**: Identify usage trends to optimize pricing strategies

        ## Filtering Options:

        - **Date range filtering**: Get usage history for specific time periods
        - **Meter-specific filtering**: Focus on usage for a particular meter
        - **Pagination**: Navigate through large usage histories efficiently

        ## Important Notes:

        - Only returns data for subscriptions with usage-based (metered) components
        - Usage history is organized by billing periods (subscription cycles)
        - Free threshold units are calculated and displayed separately from chargeable
          units
        - Historical data is preserved even if meter configurations change

        ## Example Query Patterns:

        - Get last 3 months:
          `?start_date=2024-01-01T00:00:00Z&end_date=2024-03-31T23:59:59Z`
        - Filter by meter: `?meter_id=mtr_api_requests`
        - Paginate results: `?page_size=20&page_number=1`
        - Recent usage: `?start_date=2024-03-01T00:00:00Z` (from March 1st to now)

        Args:
          end_date: Filter by end date (inclusive)

          meter_id: Filter by specific meter ID

          page_number: Page number (default: 0)

          page_size: Page size (default: 10, max: 100)

          start_date: Filter by start date (inclusive)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
        return self._get_api_list(
            f"/subscriptions/{subscription_id}/usage-history",
            page=AsyncDefaultPageNumberPagination[SubscriptionRetrieveUsageHistoryResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_date": end_date,
                        "meter_id": meter_id,
                        "page_number": page_number,
                        "page_size": page_size,
                        "start_date": start_date,
                    },
                    subscription_retrieve_usage_history_params.SubscriptionRetrieveUsageHistoryParams,
                ),
            ),
            model=SubscriptionRetrieveUsageHistoryResponse,
        )

    @overload
    async def update_payment_method(
        self,
        subscription_id: str,
        *,
        type: Literal["new"],
        return_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionUpdatePaymentMethodResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update_payment_method(
        self,
        subscription_id: str,
        *,
        payment_method_id: str,
        type: Literal["existing"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionUpdatePaymentMethodResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["type"], ["payment_method_id", "type"])
    async def update_payment_method(
        self,
        subscription_id: str,
        *,
        type: Literal["new"] | Literal["existing"],
        return_url: Optional[str] | Omit = omit,
        payment_method_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionUpdatePaymentMethodResponse:
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
        return await self._post(
            f"/subscriptions/{subscription_id}/update-payment-method",
            body=await async_maybe_transform(
                {
                    "type": type,
                    "return_url": return_url,
                    "payment_method_id": payment_method_id,
                },
                subscription_update_payment_method_params.SubscriptionUpdatePaymentMethodParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionUpdatePaymentMethodResponse,
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
        self.change_plan = to_raw_response_wrapper(
            subscriptions.change_plan,
        )
        self.charge = to_raw_response_wrapper(
            subscriptions.charge,
        )
        self.preview_change_plan = to_raw_response_wrapper(
            subscriptions.preview_change_plan,
        )
        self.retrieve_usage_history = to_raw_response_wrapper(
            subscriptions.retrieve_usage_history,
        )
        self.update_payment_method = to_raw_response_wrapper(
            subscriptions.update_payment_method,
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
        self.change_plan = async_to_raw_response_wrapper(
            subscriptions.change_plan,
        )
        self.charge = async_to_raw_response_wrapper(
            subscriptions.charge,
        )
        self.preview_change_plan = async_to_raw_response_wrapper(
            subscriptions.preview_change_plan,
        )
        self.retrieve_usage_history = async_to_raw_response_wrapper(
            subscriptions.retrieve_usage_history,
        )
        self.update_payment_method = async_to_raw_response_wrapper(
            subscriptions.update_payment_method,
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
        self.change_plan = to_streamed_response_wrapper(
            subscriptions.change_plan,
        )
        self.charge = to_streamed_response_wrapper(
            subscriptions.charge,
        )
        self.preview_change_plan = to_streamed_response_wrapper(
            subscriptions.preview_change_plan,
        )
        self.retrieve_usage_history = to_streamed_response_wrapper(
            subscriptions.retrieve_usage_history,
        )
        self.update_payment_method = to_streamed_response_wrapper(
            subscriptions.update_payment_method,
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
        self.change_plan = async_to_streamed_response_wrapper(
            subscriptions.change_plan,
        )
        self.charge = async_to_streamed_response_wrapper(
            subscriptions.charge,
        )
        self.preview_change_plan = async_to_streamed_response_wrapper(
            subscriptions.preview_change_plan,
        )
        self.retrieve_usage_history = async_to_streamed_response_wrapper(
            subscriptions.retrieve_usage_history,
        )
        self.update_payment_method = async_to_streamed_response_wrapper(
            subscriptions.update_payment_method,
        )
