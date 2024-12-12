# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .supported_countries import (
    SupportedCountriesResource,
    AsyncSupportedCountriesResource,
    SupportedCountriesResourceWithRawResponse,
    AsyncSupportedCountriesResourceWithRawResponse,
    SupportedCountriesResourceWithStreamingResponse,
    AsyncSupportedCountriesResourceWithStreamingResponse,
)

__all__ = ["CheckoutResource", "AsyncCheckoutResource"]


class CheckoutResource(SyncAPIResource):
    @cached_property
    def supported_countries(self) -> SupportedCountriesResource:
        return SupportedCountriesResource(self._client)

    @cached_property
    def with_raw_response(self) -> CheckoutResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/dodo-payments-python#accessing-raw-response-data-eg-headers
        """
        return CheckoutResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CheckoutResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/dodo-payments-python#with_streaming_response
        """
        return CheckoutResourceWithStreamingResponse(self)


class AsyncCheckoutResource(AsyncAPIResource):
    @cached_property
    def supported_countries(self) -> AsyncSupportedCountriesResource:
        return AsyncSupportedCountriesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCheckoutResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/dodo-payments-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCheckoutResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCheckoutResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/dodo-payments-python#with_streaming_response
        """
        return AsyncCheckoutResourceWithStreamingResponse(self)


class CheckoutResourceWithRawResponse:
    def __init__(self, checkout: CheckoutResource) -> None:
        self._checkout = checkout

    @cached_property
    def supported_countries(self) -> SupportedCountriesResourceWithRawResponse:
        return SupportedCountriesResourceWithRawResponse(self._checkout.supported_countries)


class AsyncCheckoutResourceWithRawResponse:
    def __init__(self, checkout: AsyncCheckoutResource) -> None:
        self._checkout = checkout

    @cached_property
    def supported_countries(self) -> AsyncSupportedCountriesResourceWithRawResponse:
        return AsyncSupportedCountriesResourceWithRawResponse(self._checkout.supported_countries)


class CheckoutResourceWithStreamingResponse:
    def __init__(self, checkout: CheckoutResource) -> None:
        self._checkout = checkout

    @cached_property
    def supported_countries(self) -> SupportedCountriesResourceWithStreamingResponse:
        return SupportedCountriesResourceWithStreamingResponse(self._checkout.supported_countries)


class AsyncCheckoutResourceWithStreamingResponse:
    def __init__(self, checkout: AsyncCheckoutResource) -> None:
        self._checkout = checkout

    @cached_property
    def supported_countries(self) -> AsyncSupportedCountriesResourceWithStreamingResponse:
        return AsyncSupportedCountriesResourceWithStreamingResponse(self._checkout.supported_countries)
