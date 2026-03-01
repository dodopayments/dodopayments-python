# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ...types import (
    Currency,
    TimeInterval,
    CbbOverageBehavior,
    credit_entitlement_list_params,
    credit_entitlement_create_params,
    credit_entitlement_update_params,
)
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from .balances import (
    BalancesResource,
    AsyncBalancesResource,
    BalancesResourceWithRawResponse,
    AsyncBalancesResourceWithRawResponse,
    BalancesResourceWithStreamingResponse,
    AsyncBalancesResourceWithStreamingResponse,
)
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
from ...types.currency import Currency
from ...types.time_interval import TimeInterval
from ...types.credit_entitlement import CreditEntitlement
from ...types.cbb_overage_behavior import CbbOverageBehavior

__all__ = ["CreditEntitlementsResource", "AsyncCreditEntitlementsResource"]


class CreditEntitlementsResource(SyncAPIResource):
    @cached_property
    def balances(self) -> BalancesResource:
        return BalancesResource(self._client)

    @cached_property
    def with_raw_response(self) -> CreditEntitlementsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return CreditEntitlementsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CreditEntitlementsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return CreditEntitlementsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        overage_enabled: bool,
        precision: int,
        rollover_enabled: bool,
        unit: str,
        currency: Optional[Currency] | Omit = omit,
        description: Optional[str] | Omit = omit,
        expires_after_days: Optional[int] | Omit = omit,
        max_rollover_count: Optional[int] | Omit = omit,
        overage_behavior: Optional[CbbOverageBehavior] | Omit = omit,
        overage_limit: Optional[int] | Omit = omit,
        price_per_unit: Optional[str] | Omit = omit,
        rollover_percentage: Optional[int] | Omit = omit,
        rollover_timeframe_count: Optional[int] | Omit = omit,
        rollover_timeframe_interval: Optional[TimeInterval] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreditEntitlement:
        """
        Credit entitlements define reusable credit templates that can be attached to
        products. Each entitlement defines how credits behave in terms of expiration,
        rollover, and overage.

        # Authentication

        Requires an API key with `Editor` role.

        # Request Body

        - `name` - Human-readable name of the credit entitlement (1-255 characters,
          required)
        - `description` - Optional description (max 1000 characters)
        - `precision` - Decimal precision for credit amounts (0-10 decimal places)
        - `unit` - Unit of measurement for the credit (e.g., "API Calls", "Tokens",
          "Credits")
        - `expires_after_days` - Number of days after which credits expire (optional)
        - `rollover_enabled` - Whether unused credits can rollover to the next period
        - `rollover_percentage` - Percentage of unused credits that rollover (0-100)
        - `rollover_timeframe_count` - Count of timeframe periods for rollover limit
        - `rollover_timeframe_interval` - Interval type (day, week, month, year)
        - `max_rollover_count` - Maximum number of times credits can be rolled over
        - `overage_enabled` - Whether overage charges apply when credits run out
          (requires price_per_unit)
        - `overage_limit` - Maximum overage units allowed (optional)
        - `currency` - Currency for pricing (required if price_per_unit is set)
        - `price_per_unit` - Price per credit unit (decimal)

        # Responses

        - `201 Created` - Credit entitlement created successfully, returns the full
          entitlement object
        - `422 Unprocessable Entity` - Invalid request parameters or validation failure
        - `500 Internal Server Error` - Database or server error

        # Business Logic

        - A unique ID with prefix `cde_` is automatically generated for the entitlement
        - Created and updated timestamps are automatically set
        - Currency is required when price_per_unit is set
        - price_per_unit is required when overage_enabled is true
        - rollover_timeframe_count and rollover_timeframe_interval must both be set or
          both be null

        Args:
          name: Name of the credit entitlement

          overage_enabled: Whether overage charges are enabled when credits run out

          precision: Precision for credit amounts (0-10 decimal places)

          rollover_enabled: Whether rollover is enabled for unused credits

          unit: Unit of measurement for the credit (e.g., "API Calls", "Tokens", "Credits")

          currency: Currency for pricing (required if price_per_unit is set)

          description: Optional description of the credit entitlement

          expires_after_days: Number of days after which credits expire (optional)

          max_rollover_count: Maximum number of times credits can be rolled over

          overage_behavior: Controls how overage is handled at billing cycle end. Defaults to
              forgive_at_reset if not specified.

          overage_limit: Maximum overage units allowed (optional)

          price_per_unit: Price per credit unit

          rollover_percentage: Percentage of unused credits that can rollover (0-100)

          rollover_timeframe_count: Count of timeframe periods for rollover limit

          rollover_timeframe_interval: Interval type for rollover timeframe

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/credit-entitlements",
            body=maybe_transform(
                {
                    "name": name,
                    "overage_enabled": overage_enabled,
                    "precision": precision,
                    "rollover_enabled": rollover_enabled,
                    "unit": unit,
                    "currency": currency,
                    "description": description,
                    "expires_after_days": expires_after_days,
                    "max_rollover_count": max_rollover_count,
                    "overage_behavior": overage_behavior,
                    "overage_limit": overage_limit,
                    "price_per_unit": price_per_unit,
                    "rollover_percentage": rollover_percentage,
                    "rollover_timeframe_count": rollover_timeframe_count,
                    "rollover_timeframe_interval": rollover_timeframe_interval,
                },
                credit_entitlement_create_params.CreditEntitlementCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditEntitlement,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreditEntitlement:
        """
        Returns the full details of a single credit entitlement including all
        configuration settings for expiration, rollover, and overage policies.

        # Authentication

        Requires an API key with `Viewer` role or higher.

        # Path Parameters

        - `id` - The unique identifier of the credit entitlement (format: `cde_...`)

        # Responses

        - `200 OK` - Returns the full credit entitlement object
        - `404 Not Found` - Credit entitlement does not exist or does not belong to the
          authenticated business
        - `500 Internal Server Error` - Database or server error

        # Business Logic

        - Only non-deleted credit entitlements can be retrieved through this endpoint
        - The entitlement must belong to the authenticated business (business_id check)
        - Deleted entitlements return a 404 error and must be retrieved via the list
          endpoint with `deleted=true`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/credit-entitlements/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditEntitlement,
        )

    def update(
        self,
        id: str,
        *,
        currency: Optional[Currency] | Omit = omit,
        description: Optional[str] | Omit = omit,
        expires_after_days: Optional[int] | Omit = omit,
        max_rollover_count: Optional[int] | Omit = omit,
        name: Optional[str] | Omit = omit,
        overage_behavior: Optional[CbbOverageBehavior] | Omit = omit,
        overage_enabled: Optional[bool] | Omit = omit,
        overage_limit: Optional[int] | Omit = omit,
        price_per_unit: Optional[str] | Omit = omit,
        rollover_enabled: Optional[bool] | Omit = omit,
        rollover_percentage: Optional[int] | Omit = omit,
        rollover_timeframe_count: Optional[int] | Omit = omit,
        rollover_timeframe_interval: Optional[TimeInterval] | Omit = omit,
        unit: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Allows partial updates to a credit entitlement's configuration.

        Only the fields
        provided in the request body will be updated; all other fields remain unchanged.
        This endpoint supports nullable fields using the double option pattern.

        # Authentication

        Requires an API key with `Editor` role.

        # Path Parameters

        - `id` - The unique identifier of the credit entitlement to update (format:
          `cde_...`)

        # Request Body (all fields optional)

        - `name` - Human-readable name of the credit entitlement (1-255 characters)
        - `description` - Optional description (max 1000 characters)
        - `unit` - Unit of measurement for the credit (1-50 characters)

        Note: `precision` cannot be modified after creation as it would invalidate
        existing grants.

        - `expires_after_days` - Number of days after which credits expire (use `null`
          to remove expiration)
        - `rollover_enabled` - Whether unused credits can rollover to the next period
        - `rollover_percentage` - Percentage of unused credits that rollover (0-100,
          nullable)
        - `rollover_timeframe_count` - Count of timeframe periods for rollover limit
          (nullable)
        - `rollover_timeframe_interval` - Interval type (day, week, month, year,
          nullable)
        - `max_rollover_count` - Maximum number of times credits can be rolled over
          (nullable)
        - `overage_enabled` - Whether overage charges apply when credits run out
        - `overage_limit` - Maximum overage units allowed (nullable)
        - `currency` - Currency for pricing (nullable)
        - `price_per_unit` - Price per credit unit (decimal, nullable)

        # Responses

        - `200 OK` - Credit entitlement updated successfully
        - `404 Not Found` - Credit entitlement does not exist or does not belong to the
          authenticated business
        - `422 Unprocessable Entity` - Invalid request parameters or validation failure
        - `500 Internal Server Error` - Database or server error

        # Business Logic

        - Only non-deleted credit entitlements can be updated
        - Fields set to `null` explicitly will clear the database value (using double
          option pattern)
        - The `updated_at` timestamp is automatically updated on successful modification
        - Changes take effect immediately but do not retroactively affect existing
          credit grants
        - The merged state is validated: currency required with price, rollover
          timeframe fields together, price required for overage

        Args:
          currency: Currency for pricing

          description: Optional description of the credit entitlement

          expires_after_days: Number of days after which credits expire

          max_rollover_count: Maximum number of times credits can be rolled over

          name: Name of the credit entitlement

          overage_behavior: Controls how overage is handled at billing cycle end.

          overage_enabled: Whether overage charges are enabled when credits run out

          overage_limit: Maximum overage units allowed

          price_per_unit: Price per credit unit

          rollover_enabled: Whether rollover is enabled for unused credits

          rollover_percentage: Percentage of unused credits that can rollover (0-100)

          rollover_timeframe_count: Count of timeframe periods for rollover limit

          rollover_timeframe_interval: Interval type for rollover timeframe

          unit: Unit of measurement for the credit (e.g., "API Calls", "Tokens", "Credits")

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._patch(
            f"/credit-entitlements/{id}",
            body=maybe_transform(
                {
                    "currency": currency,
                    "description": description,
                    "expires_after_days": expires_after_days,
                    "max_rollover_count": max_rollover_count,
                    "name": name,
                    "overage_behavior": overage_behavior,
                    "overage_enabled": overage_enabled,
                    "overage_limit": overage_limit,
                    "price_per_unit": price_per_unit,
                    "rollover_enabled": rollover_enabled,
                    "rollover_percentage": rollover_percentage,
                    "rollover_timeframe_count": rollover_timeframe_count,
                    "rollover_timeframe_interval": rollover_timeframe_interval,
                    "unit": unit,
                },
                credit_entitlement_update_params.CreditEntitlementUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        deleted: bool | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultPageNumberPagination[CreditEntitlement]:
        """
        Returns a paginated list of credit entitlements, allowing filtering of deleted
        entitlements. By default, only non-deleted entitlements are returned.

        # Authentication

        Requires an API key with `Viewer` role or higher.

        # Query Parameters

        - `page_size` - Number of items per page (default: 10, max: 100)
        - `page_number` - Zero-based page number (default: 0)
        - `deleted` - Boolean flag to list deleted entitlements instead of active ones
          (default: false)

        # Responses

        - `200 OK` - Returns a list of credit entitlements wrapped in a response object
        - `422 Unprocessable Entity` - Invalid query parameters (e.g., page_size > 100)
        - `500 Internal Server Error` - Database or server error

        # Business Logic

        - Results are ordered by creation date in descending order (newest first)
        - Only entitlements belonging to the authenticated business are returned
        - The `deleted` parameter controls visibility of soft-deleted entitlements
        - Pagination uses offset-based pagination (offset = page_number \\** page_size)

        Args:
          deleted: List deleted credit entitlements

          page_number: Page number default is 0

          page_size: Page size default is 10 max is 100

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/credit-entitlements",
            page=SyncDefaultPageNumberPagination[CreditEntitlement],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "deleted": deleted,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    credit_entitlement_list_params.CreditEntitlementListParams,
                ),
            ),
            model=CreditEntitlement,
        )

    def delete(
        self,
        id: str,
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
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/credit-entitlements/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def undelete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Undeletes a soft-deleted credit entitlement by clearing `deleted_at`, making it
        available again through standard list and get endpoints.

        # Authentication

        Requires an API key with `Editor` role.

        # Path Parameters

        - `id` - The unique identifier of the credit entitlement to restore (format:
          `cde_...`)

        # Responses

        - `200 OK` - Credit entitlement restored successfully
        - `500 Internal Server Error` - Database error, entitlement not found, or
          entitlement is not deleted

        # Business Logic

        - Only deleted credit entitlements can be restored
        - The query filters for `deleted_at IS NOT NULL`, so non-deleted entitlements
          will result in 0 rows affected
        - If no rows are affected (entitlement doesn't exist, doesn't belong to
          business, or is not deleted), returns 500
        - The `updated_at` timestamp is automatically updated on successful restoration
        - Once restored, the entitlement becomes immediately available in the standard
          list and get endpoints
        - All configuration settings are preserved during delete/restore operations

        # Error Handling

        This endpoint returns 500 Internal Server Error in several cases:

        - The credit entitlement does not exist
        - The credit entitlement belongs to a different business
        - The credit entitlement is not currently deleted (already active)

        Callers should verify the entitlement exists and is deleted before calling this
        endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/credit-entitlements/{id}/undelete",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncCreditEntitlementsResource(AsyncAPIResource):
    @cached_property
    def balances(self) -> AsyncBalancesResource:
        return AsyncBalancesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCreditEntitlementsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCreditEntitlementsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCreditEntitlementsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return AsyncCreditEntitlementsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        overage_enabled: bool,
        precision: int,
        rollover_enabled: bool,
        unit: str,
        currency: Optional[Currency] | Omit = omit,
        description: Optional[str] | Omit = omit,
        expires_after_days: Optional[int] | Omit = omit,
        max_rollover_count: Optional[int] | Omit = omit,
        overage_behavior: Optional[CbbOverageBehavior] | Omit = omit,
        overage_limit: Optional[int] | Omit = omit,
        price_per_unit: Optional[str] | Omit = omit,
        rollover_percentage: Optional[int] | Omit = omit,
        rollover_timeframe_count: Optional[int] | Omit = omit,
        rollover_timeframe_interval: Optional[TimeInterval] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreditEntitlement:
        """
        Credit entitlements define reusable credit templates that can be attached to
        products. Each entitlement defines how credits behave in terms of expiration,
        rollover, and overage.

        # Authentication

        Requires an API key with `Editor` role.

        # Request Body

        - `name` - Human-readable name of the credit entitlement (1-255 characters,
          required)
        - `description` - Optional description (max 1000 characters)
        - `precision` - Decimal precision for credit amounts (0-10 decimal places)
        - `unit` - Unit of measurement for the credit (e.g., "API Calls", "Tokens",
          "Credits")
        - `expires_after_days` - Number of days after which credits expire (optional)
        - `rollover_enabled` - Whether unused credits can rollover to the next period
        - `rollover_percentage` - Percentage of unused credits that rollover (0-100)
        - `rollover_timeframe_count` - Count of timeframe periods for rollover limit
        - `rollover_timeframe_interval` - Interval type (day, week, month, year)
        - `max_rollover_count` - Maximum number of times credits can be rolled over
        - `overage_enabled` - Whether overage charges apply when credits run out
          (requires price_per_unit)
        - `overage_limit` - Maximum overage units allowed (optional)
        - `currency` - Currency for pricing (required if price_per_unit is set)
        - `price_per_unit` - Price per credit unit (decimal)

        # Responses

        - `201 Created` - Credit entitlement created successfully, returns the full
          entitlement object
        - `422 Unprocessable Entity` - Invalid request parameters or validation failure
        - `500 Internal Server Error` - Database or server error

        # Business Logic

        - A unique ID with prefix `cde_` is automatically generated for the entitlement
        - Created and updated timestamps are automatically set
        - Currency is required when price_per_unit is set
        - price_per_unit is required when overage_enabled is true
        - rollover_timeframe_count and rollover_timeframe_interval must both be set or
          both be null

        Args:
          name: Name of the credit entitlement

          overage_enabled: Whether overage charges are enabled when credits run out

          precision: Precision for credit amounts (0-10 decimal places)

          rollover_enabled: Whether rollover is enabled for unused credits

          unit: Unit of measurement for the credit (e.g., "API Calls", "Tokens", "Credits")

          currency: Currency for pricing (required if price_per_unit is set)

          description: Optional description of the credit entitlement

          expires_after_days: Number of days after which credits expire (optional)

          max_rollover_count: Maximum number of times credits can be rolled over

          overage_behavior: Controls how overage is handled at billing cycle end. Defaults to
              forgive_at_reset if not specified.

          overage_limit: Maximum overage units allowed (optional)

          price_per_unit: Price per credit unit

          rollover_percentage: Percentage of unused credits that can rollover (0-100)

          rollover_timeframe_count: Count of timeframe periods for rollover limit

          rollover_timeframe_interval: Interval type for rollover timeframe

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/credit-entitlements",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "overage_enabled": overage_enabled,
                    "precision": precision,
                    "rollover_enabled": rollover_enabled,
                    "unit": unit,
                    "currency": currency,
                    "description": description,
                    "expires_after_days": expires_after_days,
                    "max_rollover_count": max_rollover_count,
                    "overage_behavior": overage_behavior,
                    "overage_limit": overage_limit,
                    "price_per_unit": price_per_unit,
                    "rollover_percentage": rollover_percentage,
                    "rollover_timeframe_count": rollover_timeframe_count,
                    "rollover_timeframe_interval": rollover_timeframe_interval,
                },
                credit_entitlement_create_params.CreditEntitlementCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditEntitlement,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreditEntitlement:
        """
        Returns the full details of a single credit entitlement including all
        configuration settings for expiration, rollover, and overage policies.

        # Authentication

        Requires an API key with `Viewer` role or higher.

        # Path Parameters

        - `id` - The unique identifier of the credit entitlement (format: `cde_...`)

        # Responses

        - `200 OK` - Returns the full credit entitlement object
        - `404 Not Found` - Credit entitlement does not exist or does not belong to the
          authenticated business
        - `500 Internal Server Error` - Database or server error

        # Business Logic

        - Only non-deleted credit entitlements can be retrieved through this endpoint
        - The entitlement must belong to the authenticated business (business_id check)
        - Deleted entitlements return a 404 error and must be retrieved via the list
          endpoint with `deleted=true`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/credit-entitlements/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditEntitlement,
        )

    async def update(
        self,
        id: str,
        *,
        currency: Optional[Currency] | Omit = omit,
        description: Optional[str] | Omit = omit,
        expires_after_days: Optional[int] | Omit = omit,
        max_rollover_count: Optional[int] | Omit = omit,
        name: Optional[str] | Omit = omit,
        overage_behavior: Optional[CbbOverageBehavior] | Omit = omit,
        overage_enabled: Optional[bool] | Omit = omit,
        overage_limit: Optional[int] | Omit = omit,
        price_per_unit: Optional[str] | Omit = omit,
        rollover_enabled: Optional[bool] | Omit = omit,
        rollover_percentage: Optional[int] | Omit = omit,
        rollover_timeframe_count: Optional[int] | Omit = omit,
        rollover_timeframe_interval: Optional[TimeInterval] | Omit = omit,
        unit: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Allows partial updates to a credit entitlement's configuration.

        Only the fields
        provided in the request body will be updated; all other fields remain unchanged.
        This endpoint supports nullable fields using the double option pattern.

        # Authentication

        Requires an API key with `Editor` role.

        # Path Parameters

        - `id` - The unique identifier of the credit entitlement to update (format:
          `cde_...`)

        # Request Body (all fields optional)

        - `name` - Human-readable name of the credit entitlement (1-255 characters)
        - `description` - Optional description (max 1000 characters)
        - `unit` - Unit of measurement for the credit (1-50 characters)

        Note: `precision` cannot be modified after creation as it would invalidate
        existing grants.

        - `expires_after_days` - Number of days after which credits expire (use `null`
          to remove expiration)
        - `rollover_enabled` - Whether unused credits can rollover to the next period
        - `rollover_percentage` - Percentage of unused credits that rollover (0-100,
          nullable)
        - `rollover_timeframe_count` - Count of timeframe periods for rollover limit
          (nullable)
        - `rollover_timeframe_interval` - Interval type (day, week, month, year,
          nullable)
        - `max_rollover_count` - Maximum number of times credits can be rolled over
          (nullable)
        - `overage_enabled` - Whether overage charges apply when credits run out
        - `overage_limit` - Maximum overage units allowed (nullable)
        - `currency` - Currency for pricing (nullable)
        - `price_per_unit` - Price per credit unit (decimal, nullable)

        # Responses

        - `200 OK` - Credit entitlement updated successfully
        - `404 Not Found` - Credit entitlement does not exist or does not belong to the
          authenticated business
        - `422 Unprocessable Entity` - Invalid request parameters or validation failure
        - `500 Internal Server Error` - Database or server error

        # Business Logic

        - Only non-deleted credit entitlements can be updated
        - Fields set to `null` explicitly will clear the database value (using double
          option pattern)
        - The `updated_at` timestamp is automatically updated on successful modification
        - Changes take effect immediately but do not retroactively affect existing
          credit grants
        - The merged state is validated: currency required with price, rollover
          timeframe fields together, price required for overage

        Args:
          currency: Currency for pricing

          description: Optional description of the credit entitlement

          expires_after_days: Number of days after which credits expire

          max_rollover_count: Maximum number of times credits can be rolled over

          name: Name of the credit entitlement

          overage_behavior: Controls how overage is handled at billing cycle end.

          overage_enabled: Whether overage charges are enabled when credits run out

          overage_limit: Maximum overage units allowed

          price_per_unit: Price per credit unit

          rollover_enabled: Whether rollover is enabled for unused credits

          rollover_percentage: Percentage of unused credits that can rollover (0-100)

          rollover_timeframe_count: Count of timeframe periods for rollover limit

          rollover_timeframe_interval: Interval type for rollover timeframe

          unit: Unit of measurement for the credit (e.g., "API Calls", "Tokens", "Credits")

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._patch(
            f"/credit-entitlements/{id}",
            body=await async_maybe_transform(
                {
                    "currency": currency,
                    "description": description,
                    "expires_after_days": expires_after_days,
                    "max_rollover_count": max_rollover_count,
                    "name": name,
                    "overage_behavior": overage_behavior,
                    "overage_enabled": overage_enabled,
                    "overage_limit": overage_limit,
                    "price_per_unit": price_per_unit,
                    "rollover_enabled": rollover_enabled,
                    "rollover_percentage": rollover_percentage,
                    "rollover_timeframe_count": rollover_timeframe_count,
                    "rollover_timeframe_interval": rollover_timeframe_interval,
                    "unit": unit,
                },
                credit_entitlement_update_params.CreditEntitlementUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        deleted: bool | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[CreditEntitlement, AsyncDefaultPageNumberPagination[CreditEntitlement]]:
        """
        Returns a paginated list of credit entitlements, allowing filtering of deleted
        entitlements. By default, only non-deleted entitlements are returned.

        # Authentication

        Requires an API key with `Viewer` role or higher.

        # Query Parameters

        - `page_size` - Number of items per page (default: 10, max: 100)
        - `page_number` - Zero-based page number (default: 0)
        - `deleted` - Boolean flag to list deleted entitlements instead of active ones
          (default: false)

        # Responses

        - `200 OK` - Returns a list of credit entitlements wrapped in a response object
        - `422 Unprocessable Entity` - Invalid query parameters (e.g., page_size > 100)
        - `500 Internal Server Error` - Database or server error

        # Business Logic

        - Results are ordered by creation date in descending order (newest first)
        - Only entitlements belonging to the authenticated business are returned
        - The `deleted` parameter controls visibility of soft-deleted entitlements
        - Pagination uses offset-based pagination (offset = page_number \\** page_size)

        Args:
          deleted: List deleted credit entitlements

          page_number: Page number default is 0

          page_size: Page size default is 10 max is 100

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/credit-entitlements",
            page=AsyncDefaultPageNumberPagination[CreditEntitlement],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "deleted": deleted,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    credit_entitlement_list_params.CreditEntitlementListParams,
                ),
            ),
            model=CreditEntitlement,
        )

    async def delete(
        self,
        id: str,
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
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/credit-entitlements/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def undelete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Undeletes a soft-deleted credit entitlement by clearing `deleted_at`, making it
        available again through standard list and get endpoints.

        # Authentication

        Requires an API key with `Editor` role.

        # Path Parameters

        - `id` - The unique identifier of the credit entitlement to restore (format:
          `cde_...`)

        # Responses

        - `200 OK` - Credit entitlement restored successfully
        - `500 Internal Server Error` - Database error, entitlement not found, or
          entitlement is not deleted

        # Business Logic

        - Only deleted credit entitlements can be restored
        - The query filters for `deleted_at IS NOT NULL`, so non-deleted entitlements
          will result in 0 rows affected
        - If no rows are affected (entitlement doesn't exist, doesn't belong to
          business, or is not deleted), returns 500
        - The `updated_at` timestamp is automatically updated on successful restoration
        - Once restored, the entitlement becomes immediately available in the standard
          list and get endpoints
        - All configuration settings are preserved during delete/restore operations

        # Error Handling

        This endpoint returns 500 Internal Server Error in several cases:

        - The credit entitlement does not exist
        - The credit entitlement belongs to a different business
        - The credit entitlement is not currently deleted (already active)

        Callers should verify the entitlement exists and is deleted before calling this
        endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/credit-entitlements/{id}/undelete",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class CreditEntitlementsResourceWithRawResponse:
    def __init__(self, credit_entitlements: CreditEntitlementsResource) -> None:
        self._credit_entitlements = credit_entitlements

        self.create = to_raw_response_wrapper(
            credit_entitlements.create,
        )
        self.retrieve = to_raw_response_wrapper(
            credit_entitlements.retrieve,
        )
        self.update = to_raw_response_wrapper(
            credit_entitlements.update,
        )
        self.list = to_raw_response_wrapper(
            credit_entitlements.list,
        )
        self.delete = to_raw_response_wrapper(
            credit_entitlements.delete,
        )
        self.undelete = to_raw_response_wrapper(
            credit_entitlements.undelete,
        )

    @cached_property
    def balances(self) -> BalancesResourceWithRawResponse:
        return BalancesResourceWithRawResponse(self._credit_entitlements.balances)


class AsyncCreditEntitlementsResourceWithRawResponse:
    def __init__(self, credit_entitlements: AsyncCreditEntitlementsResource) -> None:
        self._credit_entitlements = credit_entitlements

        self.create = async_to_raw_response_wrapper(
            credit_entitlements.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            credit_entitlements.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            credit_entitlements.update,
        )
        self.list = async_to_raw_response_wrapper(
            credit_entitlements.list,
        )
        self.delete = async_to_raw_response_wrapper(
            credit_entitlements.delete,
        )
        self.undelete = async_to_raw_response_wrapper(
            credit_entitlements.undelete,
        )

    @cached_property
    def balances(self) -> AsyncBalancesResourceWithRawResponse:
        return AsyncBalancesResourceWithRawResponse(self._credit_entitlements.balances)


class CreditEntitlementsResourceWithStreamingResponse:
    def __init__(self, credit_entitlements: CreditEntitlementsResource) -> None:
        self._credit_entitlements = credit_entitlements

        self.create = to_streamed_response_wrapper(
            credit_entitlements.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            credit_entitlements.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            credit_entitlements.update,
        )
        self.list = to_streamed_response_wrapper(
            credit_entitlements.list,
        )
        self.delete = to_streamed_response_wrapper(
            credit_entitlements.delete,
        )
        self.undelete = to_streamed_response_wrapper(
            credit_entitlements.undelete,
        )

    @cached_property
    def balances(self) -> BalancesResourceWithStreamingResponse:
        return BalancesResourceWithStreamingResponse(self._credit_entitlements.balances)


class AsyncCreditEntitlementsResourceWithStreamingResponse:
    def __init__(self, credit_entitlements: AsyncCreditEntitlementsResource) -> None:
        self._credit_entitlements = credit_entitlements

        self.create = async_to_streamed_response_wrapper(
            credit_entitlements.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            credit_entitlements.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            credit_entitlements.update,
        )
        self.list = async_to_streamed_response_wrapper(
            credit_entitlements.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            credit_entitlements.delete,
        )
        self.undelete = async_to_streamed_response_wrapper(
            credit_entitlements.undelete,
        )

    @cached_property
    def balances(self) -> AsyncBalancesResourceWithStreamingResponse:
        return AsyncBalancesResourceWithStreamingResponse(self._credit_entitlements.balances)
