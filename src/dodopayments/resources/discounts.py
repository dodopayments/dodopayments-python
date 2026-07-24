# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import DiscountType, discount_list_params, discount_create_params, discount_update_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
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
from ..types.discount import Discount
from ..types.discount_type import DiscountType
from ..types.metadata_param import MetadataParam

__all__ = ["DiscountsResource", "AsyncDiscountsResource"]


class DiscountsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DiscountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return DiscountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DiscountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return DiscountsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        amount: int,
        type: DiscountType,
        code: Optional[str] | Omit = omit,
        currency_options: Optional[Iterable[discount_create_params.CurrencyOption]] | Omit = omit,
        customer_eligibility: Optional[Literal["any", "first_time", "existing", "specific"]] | Omit = omit,
        expires_at: Union[str, datetime, None] | Omit = omit,
        metadata: MetadataParam | Omit = omit,
        name: Optional[str] | Omit = omit,
        per_customer_usage_limit: Optional[int] | Omit = omit,
        preserve_on_plan_change: bool | Omit = omit,
        restricted_to: Optional[SequenceNotStr[str]] | Omit = omit,
        starts_at: Union[str, datetime, None] | Omit = omit,
        subscription_cycles: Optional[int] | Omit = omit,
        usage_limit: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Discount:
        """
        POST /discounts If `code` is omitted or empty, a random 16-char uppercase code
        is generated.

        Args:
          amount: The discount amount in **basis points** (e.g. `540` means `5.4%`, `10000` means
              `100%`).

              Must be at least 1.

          type: The discount type: `percentage` or `flat` (`flat_per_unit` stays blocked).

          code: Optionally supply a code (will be uppercased).

              - Must be at least 3 characters if provided.
              - If omitted, a random 16-character code is generated.

          currency_options: Per-currency options (flat deduction / percentage cap + minimum subtotal).
              Required for `flat` codes (must include a resolvable default); optional
              per-currency caps for `percentage` codes. Per-row invariants are checked in
              `normalize_currency_options`, not via `#[validate(nested)]`.

          customer_eligibility: Who may redeem this discount code. Defaults to `any` (unrestricted). `specific`
              starts with zero attached customers (fails closed) until customers are attached
              via `POST /discounts/{id}/customers`.

          expires_at: When the discount expires, if ever.

          metadata: Additional metadata for the discount

          per_customer_usage_limit: Maximum number of times a single customer may redeem this discount. Must be
              `<= usage_limit` when both are set.

          preserve_on_plan_change: Whether this discount should be preserved when a subscription changes plans.
              Default: false (discount is removed on plan change)

          restricted_to: List of product IDs to restrict usage (if any).

          starts_at: When the discount becomes active, if scheduled for the future. NULL = active
              immediately. Must be strictly before `expires_at` when both are set.

          subscription_cycles: Number of subscription billing cycles this discount is valid for. If not
              provided, the discount will be applied indefinitely to all recurring payments
              related to the subscription.

          usage_limit: How many times this discount can be used (if any). Must be >= 1 if provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/discounts",
            body=maybe_transform(
                {
                    "amount": amount,
                    "type": type,
                    "code": code,
                    "currency_options": currency_options,
                    "customer_eligibility": customer_eligibility,
                    "expires_at": expires_at,
                    "metadata": metadata,
                    "name": name,
                    "per_customer_usage_limit": per_customer_usage_limit,
                    "preserve_on_plan_change": preserve_on_plan_change,
                    "restricted_to": restricted_to,
                    "starts_at": starts_at,
                    "subscription_cycles": subscription_cycles,
                    "usage_limit": usage_limit,
                },
                discount_create_params.DiscountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Discount,
        )

    def retrieve(
        self,
        discount_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Discount:
        """
        GET /discounts/{discount_id}

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not discount_id:
            raise ValueError(f"Expected a non-empty value for `discount_id` but received {discount_id!r}")
        return self._get(
            path_template("/discounts/{discount_id}", discount_id=discount_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Discount,
        )

    def update(
        self,
        discount_id: str,
        *,
        amount: Optional[int] | Omit = omit,
        code: Optional[str] | Omit = omit,
        currency_options: Optional[Iterable[discount_update_params.CurrencyOption]] | Omit = omit,
        customer_eligibility: Optional[Literal["any", "first_time", "existing", "specific"]] | Omit = omit,
        expires_at: Union[str, datetime, None] | Omit = omit,
        metadata: Optional[MetadataParam] | Omit = omit,
        name: Optional[str] | Omit = omit,
        per_customer_usage_limit: Optional[int] | Omit = omit,
        preserve_on_plan_change: Optional[bool] | Omit = omit,
        restricted_to: Optional[SequenceNotStr[str]] | Omit = omit,
        starts_at: Union[str, datetime, None] | Omit = omit,
        subscription_cycles: Optional[int] | Omit = omit,
        type: Optional[DiscountType] | Omit = omit,
        usage_limit: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Discount:
        """
        PATCH /discounts/{discount_id}

        Args:
          amount: If present, update the discount amount in **basis points** (e.g., `540` =
              `5.4%`, `10000` = `100%`).

              Must be at least 1 if provided.

          code: If present, update the discount code (uppercase).

          currency_options: If present, fully replaces the discount's currency options (replace-set
              semantics, like `restricted_to`). Send an empty array to clear them.

          customer_eligibility: If present, update who may redeem this discount. Plain field (not
              double-option): the DB column is `NOT NULL`, so it can never be cleared back to
              unset, only changed to another `CustomerEligibility` value.

          metadata: Additional metadata for the discount

          per_customer_usage_limit: If present, update the per-customer usage limit (double-option: send `null` to
              clear it back to unlimited). Must be `<= usage_limit` (the value in effect after
              this patch) when both are set.

          preserve_on_plan_change: Whether this discount should be preserved when a subscription changes plans. If
              not provided, the existing value is kept.

          restricted_to: If present, replaces all restricted product IDs with this new set. To remove all
              restrictions, send empty array

          starts_at: If present, update `starts_at` (double-option: send `null` to clear it).

          subscription_cycles: Number of subscription billing cycles this discount is valid for. If not
              provided, the discount will be applied indefinitely to all recurring payments
              related to the subscription.

          type: If present, update the discount type (`percentage` or `flat`).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not discount_id:
            raise ValueError(f"Expected a non-empty value for `discount_id` but received {discount_id!r}")
        return self._patch(
            path_template("/discounts/{discount_id}", discount_id=discount_id),
            body=maybe_transform(
                {
                    "amount": amount,
                    "code": code,
                    "currency_options": currency_options,
                    "customer_eligibility": customer_eligibility,
                    "expires_at": expires_at,
                    "metadata": metadata,
                    "name": name,
                    "per_customer_usage_limit": per_customer_usage_limit,
                    "preserve_on_plan_change": preserve_on_plan_change,
                    "restricted_to": restricted_to,
                    "starts_at": starts_at,
                    "subscription_cycles": subscription_cycles,
                    "type": type,
                    "usage_limit": usage_limit,
                },
                discount_update_params.DiscountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Discount,
        )

    def list(
        self,
        *,
        active: bool | Omit = omit,
        code: str | Omit = omit,
        discount_type: DiscountType | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        product_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultPageNumberPagination[Discount]:
        """GET /discounts

        Args:
          active: Filter by active status.

        `true` = currently redeemable (started, not expired,
              not usage-exhausted). `false` = not currently redeemable (expired,
              usage-exhausted, or pending a future `starts_at`).

          code: Filter by discount code (partial match, case-insensitive)

          discount_type: Filter by discount type

          page_number: Page number (default = 0).

          page_size: Page size (default = 10, max = 100).

          product_id: Filter by product restriction (only discounts that apply to this product)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/discounts",
            page=SyncDefaultPageNumberPagination[Discount],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "active": active,
                        "code": code,
                        "discount_type": discount_type,
                        "page_number": page_number,
                        "page_size": page_size,
                        "product_id": product_id,
                    },
                    discount_list_params.DiscountListParams,
                ),
            ),
            model=Discount,
        )

    def delete(
        self,
        discount_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        DELETE /discounts/{discount_id}

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not discount_id:
            raise ValueError(f"Expected a non-empty value for `discount_id` but received {discount_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/discounts/{discount_id}", discount_id=discount_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def retrieve_by_code(
        self,
        code: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Discount:
        """Validate and fetch a discount by its code name (e.g., "SAVE20").

        This allows
        real-time validation directly against the API using the human-readable discount
        code instead of requiring the internal discount_id.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        return self._get(
            path_template("/discounts/code/{code}", code=code),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Discount,
        )


class AsyncDiscountsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDiscountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDiscountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDiscountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return AsyncDiscountsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        amount: int,
        type: DiscountType,
        code: Optional[str] | Omit = omit,
        currency_options: Optional[Iterable[discount_create_params.CurrencyOption]] | Omit = omit,
        customer_eligibility: Optional[Literal["any", "first_time", "existing", "specific"]] | Omit = omit,
        expires_at: Union[str, datetime, None] | Omit = omit,
        metadata: MetadataParam | Omit = omit,
        name: Optional[str] | Omit = omit,
        per_customer_usage_limit: Optional[int] | Omit = omit,
        preserve_on_plan_change: bool | Omit = omit,
        restricted_to: Optional[SequenceNotStr[str]] | Omit = omit,
        starts_at: Union[str, datetime, None] | Omit = omit,
        subscription_cycles: Optional[int] | Omit = omit,
        usage_limit: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Discount:
        """
        POST /discounts If `code` is omitted or empty, a random 16-char uppercase code
        is generated.

        Args:
          amount: The discount amount in **basis points** (e.g. `540` means `5.4%`, `10000` means
              `100%`).

              Must be at least 1.

          type: The discount type: `percentage` or `flat` (`flat_per_unit` stays blocked).

          code: Optionally supply a code (will be uppercased).

              - Must be at least 3 characters if provided.
              - If omitted, a random 16-character code is generated.

          currency_options: Per-currency options (flat deduction / percentage cap + minimum subtotal).
              Required for `flat` codes (must include a resolvable default); optional
              per-currency caps for `percentage` codes. Per-row invariants are checked in
              `normalize_currency_options`, not via `#[validate(nested)]`.

          customer_eligibility: Who may redeem this discount code. Defaults to `any` (unrestricted). `specific`
              starts with zero attached customers (fails closed) until customers are attached
              via `POST /discounts/{id}/customers`.

          expires_at: When the discount expires, if ever.

          metadata: Additional metadata for the discount

          per_customer_usage_limit: Maximum number of times a single customer may redeem this discount. Must be
              `<= usage_limit` when both are set.

          preserve_on_plan_change: Whether this discount should be preserved when a subscription changes plans.
              Default: false (discount is removed on plan change)

          restricted_to: List of product IDs to restrict usage (if any).

          starts_at: When the discount becomes active, if scheduled for the future. NULL = active
              immediately. Must be strictly before `expires_at` when both are set.

          subscription_cycles: Number of subscription billing cycles this discount is valid for. If not
              provided, the discount will be applied indefinitely to all recurring payments
              related to the subscription.

          usage_limit: How many times this discount can be used (if any). Must be >= 1 if provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/discounts",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "type": type,
                    "code": code,
                    "currency_options": currency_options,
                    "customer_eligibility": customer_eligibility,
                    "expires_at": expires_at,
                    "metadata": metadata,
                    "name": name,
                    "per_customer_usage_limit": per_customer_usage_limit,
                    "preserve_on_plan_change": preserve_on_plan_change,
                    "restricted_to": restricted_to,
                    "starts_at": starts_at,
                    "subscription_cycles": subscription_cycles,
                    "usage_limit": usage_limit,
                },
                discount_create_params.DiscountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Discount,
        )

    async def retrieve(
        self,
        discount_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Discount:
        """
        GET /discounts/{discount_id}

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not discount_id:
            raise ValueError(f"Expected a non-empty value for `discount_id` but received {discount_id!r}")
        return await self._get(
            path_template("/discounts/{discount_id}", discount_id=discount_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Discount,
        )

    async def update(
        self,
        discount_id: str,
        *,
        amount: Optional[int] | Omit = omit,
        code: Optional[str] | Omit = omit,
        currency_options: Optional[Iterable[discount_update_params.CurrencyOption]] | Omit = omit,
        customer_eligibility: Optional[Literal["any", "first_time", "existing", "specific"]] | Omit = omit,
        expires_at: Union[str, datetime, None] | Omit = omit,
        metadata: Optional[MetadataParam] | Omit = omit,
        name: Optional[str] | Omit = omit,
        per_customer_usage_limit: Optional[int] | Omit = omit,
        preserve_on_plan_change: Optional[bool] | Omit = omit,
        restricted_to: Optional[SequenceNotStr[str]] | Omit = omit,
        starts_at: Union[str, datetime, None] | Omit = omit,
        subscription_cycles: Optional[int] | Omit = omit,
        type: Optional[DiscountType] | Omit = omit,
        usage_limit: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Discount:
        """
        PATCH /discounts/{discount_id}

        Args:
          amount: If present, update the discount amount in **basis points** (e.g., `540` =
              `5.4%`, `10000` = `100%`).

              Must be at least 1 if provided.

          code: If present, update the discount code (uppercase).

          currency_options: If present, fully replaces the discount's currency options (replace-set
              semantics, like `restricted_to`). Send an empty array to clear them.

          customer_eligibility: If present, update who may redeem this discount. Plain field (not
              double-option): the DB column is `NOT NULL`, so it can never be cleared back to
              unset, only changed to another `CustomerEligibility` value.

          metadata: Additional metadata for the discount

          per_customer_usage_limit: If present, update the per-customer usage limit (double-option: send `null` to
              clear it back to unlimited). Must be `<= usage_limit` (the value in effect after
              this patch) when both are set.

          preserve_on_plan_change: Whether this discount should be preserved when a subscription changes plans. If
              not provided, the existing value is kept.

          restricted_to: If present, replaces all restricted product IDs with this new set. To remove all
              restrictions, send empty array

          starts_at: If present, update `starts_at` (double-option: send `null` to clear it).

          subscription_cycles: Number of subscription billing cycles this discount is valid for. If not
              provided, the discount will be applied indefinitely to all recurring payments
              related to the subscription.

          type: If present, update the discount type (`percentage` or `flat`).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not discount_id:
            raise ValueError(f"Expected a non-empty value for `discount_id` but received {discount_id!r}")
        return await self._patch(
            path_template("/discounts/{discount_id}", discount_id=discount_id),
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "code": code,
                    "currency_options": currency_options,
                    "customer_eligibility": customer_eligibility,
                    "expires_at": expires_at,
                    "metadata": metadata,
                    "name": name,
                    "per_customer_usage_limit": per_customer_usage_limit,
                    "preserve_on_plan_change": preserve_on_plan_change,
                    "restricted_to": restricted_to,
                    "starts_at": starts_at,
                    "subscription_cycles": subscription_cycles,
                    "type": type,
                    "usage_limit": usage_limit,
                },
                discount_update_params.DiscountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Discount,
        )

    def list(
        self,
        *,
        active: bool | Omit = omit,
        code: str | Omit = omit,
        discount_type: DiscountType | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        product_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Discount, AsyncDefaultPageNumberPagination[Discount]]:
        """GET /discounts

        Args:
          active: Filter by active status.

        `true` = currently redeemable (started, not expired,
              not usage-exhausted). `false` = not currently redeemable (expired,
              usage-exhausted, or pending a future `starts_at`).

          code: Filter by discount code (partial match, case-insensitive)

          discount_type: Filter by discount type

          page_number: Page number (default = 0).

          page_size: Page size (default = 10, max = 100).

          product_id: Filter by product restriction (only discounts that apply to this product)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/discounts",
            page=AsyncDefaultPageNumberPagination[Discount],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "active": active,
                        "code": code,
                        "discount_type": discount_type,
                        "page_number": page_number,
                        "page_size": page_size,
                        "product_id": product_id,
                    },
                    discount_list_params.DiscountListParams,
                ),
            ),
            model=Discount,
        )

    async def delete(
        self,
        discount_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        DELETE /discounts/{discount_id}

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not discount_id:
            raise ValueError(f"Expected a non-empty value for `discount_id` but received {discount_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/discounts/{discount_id}", discount_id=discount_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def retrieve_by_code(
        self,
        code: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Discount:
        """Validate and fetch a discount by its code name (e.g., "SAVE20").

        This allows
        real-time validation directly against the API using the human-readable discount
        code instead of requiring the internal discount_id.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        return await self._get(
            path_template("/discounts/code/{code}", code=code),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Discount,
        )


class DiscountsResourceWithRawResponse:
    def __init__(self, discounts: DiscountsResource) -> None:
        self._discounts = discounts

        self.create = to_raw_response_wrapper(
            discounts.create,
        )
        self.retrieve = to_raw_response_wrapper(
            discounts.retrieve,
        )
        self.update = to_raw_response_wrapper(
            discounts.update,
        )
        self.list = to_raw_response_wrapper(
            discounts.list,
        )
        self.delete = to_raw_response_wrapper(
            discounts.delete,
        )
        self.retrieve_by_code = to_raw_response_wrapper(
            discounts.retrieve_by_code,
        )


class AsyncDiscountsResourceWithRawResponse:
    def __init__(self, discounts: AsyncDiscountsResource) -> None:
        self._discounts = discounts

        self.create = async_to_raw_response_wrapper(
            discounts.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            discounts.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            discounts.update,
        )
        self.list = async_to_raw_response_wrapper(
            discounts.list,
        )
        self.delete = async_to_raw_response_wrapper(
            discounts.delete,
        )
        self.retrieve_by_code = async_to_raw_response_wrapper(
            discounts.retrieve_by_code,
        )


class DiscountsResourceWithStreamingResponse:
    def __init__(self, discounts: DiscountsResource) -> None:
        self._discounts = discounts

        self.create = to_streamed_response_wrapper(
            discounts.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            discounts.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            discounts.update,
        )
        self.list = to_streamed_response_wrapper(
            discounts.list,
        )
        self.delete = to_streamed_response_wrapper(
            discounts.delete,
        )
        self.retrieve_by_code = to_streamed_response_wrapper(
            discounts.retrieve_by_code,
        )


class AsyncDiscountsResourceWithStreamingResponse:
    def __init__(self, discounts: AsyncDiscountsResource) -> None:
        self._discounts = discounts

        self.create = async_to_streamed_response_wrapper(
            discounts.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            discounts.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            discounts.update,
        )
        self.list = async_to_streamed_response_wrapper(
            discounts.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            discounts.delete,
        )
        self.retrieve_by_code = async_to_streamed_response_wrapper(
            discounts.retrieve_by_code,
        )
