# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime

import httpx

from ..types import DiscountType, discount_list_params, discount_create_params, discount_update_params
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven, SequenceNotStr
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
from ..types.discount import Discount
from ..types.discount_type import DiscountType

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
        code: Optional[str] | NotGiven = NOT_GIVEN,
        expires_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        restricted_to: Optional[SequenceNotStr[str]] | NotGiven = NOT_GIVEN,
        subscription_cycles: Optional[int] | NotGiven = NOT_GIVEN,
        usage_limit: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Discount:
        """
        POST /discounts If `code` is omitted or empty, a random 16-char uppercase code
        is generated.

        Args:
          amount: The discount amount.

              - If `discount_type` is **not** `percentage`, `amount` is in **USD cents**. For
                example, `100` means `$1.00`. Only USD is allowed.
              - If `discount_type` **is** `percentage`, `amount` is in **basis points**. For
                example, `540` means `5.4%`.

              Must be at least 1.

          type: The discount type (e.g. `percentage`, `flat`, or `flat_per_unit`).

          code: Optionally supply a code (will be uppercased).

              - Must be at least 3 characters if provided.
              - If omitted, a random 16-character code is generated.

          expires_at: When the discount expires, if ever.

          restricted_to: List of product IDs to restrict usage (if any).

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
                    "expires_at": expires_at,
                    "name": name,
                    "restricted_to": restricted_to,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
            f"/discounts/{discount_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Discount,
        )

    def update(
        self,
        discount_id: str,
        *,
        amount: Optional[int] | NotGiven = NOT_GIVEN,
        code: Optional[str] | NotGiven = NOT_GIVEN,
        expires_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        restricted_to: Optional[SequenceNotStr[str]] | NotGiven = NOT_GIVEN,
        subscription_cycles: Optional[int] | NotGiven = NOT_GIVEN,
        type: Optional[DiscountType] | NotGiven = NOT_GIVEN,
        usage_limit: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Discount:
        """
        PATCH /discounts/{discount_id}

        Args:
          amount:
              If present, update the discount amount:

              - If `discount_type` is `percentage`, this represents **basis points** (e.g.,
                `540` = `5.4%`).
              - Otherwise, this represents **USD cents** (e.g., `100` = `$1.00`).

              Must be at least 1 if provided.

          code: If present, update the discount code (uppercase).

          restricted_to: If present, replaces all restricted product IDs with this new set. To remove all
              restrictions, send empty array

          subscription_cycles: Number of subscription billing cycles this discount is valid for. If not
              provided, the discount will be applied indefinitely to all recurring payments
              related to the subscription.

          type: If present, update the discount type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not discount_id:
            raise ValueError(f"Expected a non-empty value for `discount_id` but received {discount_id!r}")
        return self._patch(
            f"/discounts/{discount_id}",
            body=maybe_transform(
                {
                    "amount": amount,
                    "code": code,
                    "expires_at": expires_at,
                    "name": name,
                    "restricted_to": restricted_to,
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
        page_number: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncDefaultPageNumberPagination[Discount]:
        """
        GET /discounts

        Args:
          page_number: Page number (default = 0).

          page_size: Page size (default = 10, max = 100).

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
                        "page_number": page_number,
                        "page_size": page_size,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
            f"/discounts/{discount_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
        code: Optional[str] | NotGiven = NOT_GIVEN,
        expires_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        restricted_to: Optional[SequenceNotStr[str]] | NotGiven = NOT_GIVEN,
        subscription_cycles: Optional[int] | NotGiven = NOT_GIVEN,
        usage_limit: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Discount:
        """
        POST /discounts If `code` is omitted or empty, a random 16-char uppercase code
        is generated.

        Args:
          amount: The discount amount.

              - If `discount_type` is **not** `percentage`, `amount` is in **USD cents**. For
                example, `100` means `$1.00`. Only USD is allowed.
              - If `discount_type` **is** `percentage`, `amount` is in **basis points**. For
                example, `540` means `5.4%`.

              Must be at least 1.

          type: The discount type (e.g. `percentage`, `flat`, or `flat_per_unit`).

          code: Optionally supply a code (will be uppercased).

              - Must be at least 3 characters if provided.
              - If omitted, a random 16-character code is generated.

          expires_at: When the discount expires, if ever.

          restricted_to: List of product IDs to restrict usage (if any).

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
                    "expires_at": expires_at,
                    "name": name,
                    "restricted_to": restricted_to,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
            f"/discounts/{discount_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Discount,
        )

    async def update(
        self,
        discount_id: str,
        *,
        amount: Optional[int] | NotGiven = NOT_GIVEN,
        code: Optional[str] | NotGiven = NOT_GIVEN,
        expires_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        restricted_to: Optional[SequenceNotStr[str]] | NotGiven = NOT_GIVEN,
        subscription_cycles: Optional[int] | NotGiven = NOT_GIVEN,
        type: Optional[DiscountType] | NotGiven = NOT_GIVEN,
        usage_limit: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Discount:
        """
        PATCH /discounts/{discount_id}

        Args:
          amount:
              If present, update the discount amount:

              - If `discount_type` is `percentage`, this represents **basis points** (e.g.,
                `540` = `5.4%`).
              - Otherwise, this represents **USD cents** (e.g., `100` = `$1.00`).

              Must be at least 1 if provided.

          code: If present, update the discount code (uppercase).

          restricted_to: If present, replaces all restricted product IDs with this new set. To remove all
              restrictions, send empty array

          subscription_cycles: Number of subscription billing cycles this discount is valid for. If not
              provided, the discount will be applied indefinitely to all recurring payments
              related to the subscription.

          type: If present, update the discount type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not discount_id:
            raise ValueError(f"Expected a non-empty value for `discount_id` but received {discount_id!r}")
        return await self._patch(
            f"/discounts/{discount_id}",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "code": code,
                    "expires_at": expires_at,
                    "name": name,
                    "restricted_to": restricted_to,
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
        page_number: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Discount, AsyncDefaultPageNumberPagination[Discount]]:
        """
        GET /discounts

        Args:
          page_number: Page number (default = 0).

          page_size: Page size (default = 10, max = 100).

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
                        "page_number": page_number,
                        "page_size": page_size,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
            f"/discounts/{discount_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
