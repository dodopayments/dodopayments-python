# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ...types import Currency, CountryCode
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.currency import Currency
from ...types.products import localized_price_create_params, localized_price_update_params
from ...types.country_code import CountryCode
from ...types.products.localized_price import LocalizedPrice
from ...types.products.list_localized_prices_response import ListLocalizedPricesResponse

__all__ = ["LocalizedPricesResource", "AsyncLocalizedPricesResource"]


class LocalizedPricesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LocalizedPricesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return LocalizedPricesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LocalizedPricesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return LocalizedPricesResourceWithStreamingResponse(self)

    def create(
        self,
        product_id: str,
        *,
        amount: int,
        currency: Currency,
        country_code: Optional[CountryCode] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LocalizedPrice:
        """Args:
          amount: Amount in the smallest currency unit (e.g., cents).

        Must be greater than zero.

          currency: Currency to charge in. Must be a supported currency.

          country_code: Required when the product's pricing_mode is by_country; forbidden when
              by_currency.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not product_id:
            raise ValueError(f"Expected a non-empty value for `product_id` but received {product_id!r}")
        return self._post(
            path_template("/products/{product_id}/localized-prices", product_id=product_id),
            body=maybe_transform(
                {
                    "amount": amount,
                    "currency": currency,
                    "country_code": country_code,
                },
                localized_price_create_params.LocalizedPriceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LocalizedPrice,
        )

    def retrieve(
        self,
        id: str,
        *,
        product_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LocalizedPrice:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not product_id:
            raise ValueError(f"Expected a non-empty value for `product_id` but received {product_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/products/{product_id}/localized-prices/{id}", product_id=product_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LocalizedPrice,
        )

    def update(
        self,
        id: str,
        *,
        product_id: str,
        amount: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LocalizedPrice:
        """Args:
          amount: New amount in the smallest currency unit (e.g., cents).

        Must be greater than
              zero. The currency and country_code of an existing rule cannot be changed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not product_id:
            raise ValueError(f"Expected a non-empty value for `product_id` but received {product_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/products/{product_id}/localized-prices/{id}", product_id=product_id, id=id),
            body=maybe_transform({"amount": amount}, localized_price_update_params.LocalizedPriceUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LocalizedPrice,
        )

    def list(
        self,
        product_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListLocalizedPricesResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not product_id:
            raise ValueError(f"Expected a non-empty value for `product_id` but received {product_id!r}")
        return self._get(
            path_template("/products/{product_id}/localized-prices", product_id=product_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ListLocalizedPricesResponse,
        )

    def archive(
        self,
        id: str,
        *,
        product_id: str,
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
        if not product_id:
            raise ValueError(f"Expected a non-empty value for `product_id` but received {product_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/products/{product_id}/localized-prices/{id}", product_id=product_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncLocalizedPricesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLocalizedPricesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLocalizedPricesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLocalizedPricesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return AsyncLocalizedPricesResourceWithStreamingResponse(self)

    async def create(
        self,
        product_id: str,
        *,
        amount: int,
        currency: Currency,
        country_code: Optional[CountryCode] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LocalizedPrice:
        """Args:
          amount: Amount in the smallest currency unit (e.g., cents).

        Must be greater than zero.

          currency: Currency to charge in. Must be a supported currency.

          country_code: Required when the product's pricing_mode is by_country; forbidden when
              by_currency.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not product_id:
            raise ValueError(f"Expected a non-empty value for `product_id` but received {product_id!r}")
        return await self._post(
            path_template("/products/{product_id}/localized-prices", product_id=product_id),
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "currency": currency,
                    "country_code": country_code,
                },
                localized_price_create_params.LocalizedPriceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LocalizedPrice,
        )

    async def retrieve(
        self,
        id: str,
        *,
        product_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LocalizedPrice:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not product_id:
            raise ValueError(f"Expected a non-empty value for `product_id` but received {product_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/products/{product_id}/localized-prices/{id}", product_id=product_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LocalizedPrice,
        )

    async def update(
        self,
        id: str,
        *,
        product_id: str,
        amount: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LocalizedPrice:
        """Args:
          amount: New amount in the smallest currency unit (e.g., cents).

        Must be greater than
              zero. The currency and country_code of an existing rule cannot be changed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not product_id:
            raise ValueError(f"Expected a non-empty value for `product_id` but received {product_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/products/{product_id}/localized-prices/{id}", product_id=product_id, id=id),
            body=await async_maybe_transform(
                {"amount": amount}, localized_price_update_params.LocalizedPriceUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LocalizedPrice,
        )

    async def list(
        self,
        product_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListLocalizedPricesResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not product_id:
            raise ValueError(f"Expected a non-empty value for `product_id` but received {product_id!r}")
        return await self._get(
            path_template("/products/{product_id}/localized-prices", product_id=product_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ListLocalizedPricesResponse,
        )

    async def archive(
        self,
        id: str,
        *,
        product_id: str,
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
        if not product_id:
            raise ValueError(f"Expected a non-empty value for `product_id` but received {product_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/products/{product_id}/localized-prices/{id}", product_id=product_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class LocalizedPricesResourceWithRawResponse:
    def __init__(self, localized_prices: LocalizedPricesResource) -> None:
        self._localized_prices = localized_prices

        self.create = to_raw_response_wrapper(
            localized_prices.create,
        )
        self.retrieve = to_raw_response_wrapper(
            localized_prices.retrieve,
        )
        self.update = to_raw_response_wrapper(
            localized_prices.update,
        )
        self.list = to_raw_response_wrapper(
            localized_prices.list,
        )
        self.archive = to_raw_response_wrapper(
            localized_prices.archive,
        )


class AsyncLocalizedPricesResourceWithRawResponse:
    def __init__(self, localized_prices: AsyncLocalizedPricesResource) -> None:
        self._localized_prices = localized_prices

        self.create = async_to_raw_response_wrapper(
            localized_prices.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            localized_prices.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            localized_prices.update,
        )
        self.list = async_to_raw_response_wrapper(
            localized_prices.list,
        )
        self.archive = async_to_raw_response_wrapper(
            localized_prices.archive,
        )


class LocalizedPricesResourceWithStreamingResponse:
    def __init__(self, localized_prices: LocalizedPricesResource) -> None:
        self._localized_prices = localized_prices

        self.create = to_streamed_response_wrapper(
            localized_prices.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            localized_prices.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            localized_prices.update,
        )
        self.list = to_streamed_response_wrapper(
            localized_prices.list,
        )
        self.archive = to_streamed_response_wrapper(
            localized_prices.archive,
        )


class AsyncLocalizedPricesResourceWithStreamingResponse:
    def __init__(self, localized_prices: AsyncLocalizedPricesResource) -> None:
        self._localized_prices = localized_prices

        self.create = async_to_streamed_response_wrapper(
            localized_prices.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            localized_prices.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            localized_prices.update,
        )
        self.list = async_to_streamed_response_wrapper(
            localized_prices.list,
        )
        self.archive = async_to_streamed_response_wrapper(
            localized_prices.archive,
        )
