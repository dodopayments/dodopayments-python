# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.misc.supported_country_list_response import SupportedCountryListResponse

__all__ = ["SupportedCountriesResource", "AsyncSupportedCountriesResource"]


class SupportedCountriesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SupportedCountriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/dodo-payments-python#accessing-raw-response-data-eg-headers
        """
        return SupportedCountriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SupportedCountriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/dodo-payments-python#with_streaming_response
        """
        return SupportedCountriesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SupportedCountryListResponse:
        return self._get(
            "/checkout/supported_countries",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SupportedCountryListResponse,
        )


class AsyncSupportedCountriesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSupportedCountriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/dodo-payments-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSupportedCountriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSupportedCountriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/dodo-payments-python#with_streaming_response
        """
        return AsyncSupportedCountriesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SupportedCountryListResponse:
        return await self._get(
            "/checkout/supported_countries",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SupportedCountryListResponse,
        )


class SupportedCountriesResourceWithRawResponse:
    def __init__(self, supported_countries: SupportedCountriesResource) -> None:
        self._supported_countries = supported_countries

        self.list = to_raw_response_wrapper(
            supported_countries.list,
        )


class AsyncSupportedCountriesResourceWithRawResponse:
    def __init__(self, supported_countries: AsyncSupportedCountriesResource) -> None:
        self._supported_countries = supported_countries

        self.list = async_to_raw_response_wrapper(
            supported_countries.list,
        )


class SupportedCountriesResourceWithStreamingResponse:
    def __init__(self, supported_countries: SupportedCountriesResource) -> None:
        self._supported_countries = supported_countries

        self.list = to_streamed_response_wrapper(
            supported_countries.list,
        )


class AsyncSupportedCountriesResourceWithStreamingResponse:
    def __init__(self, supported_countries: AsyncSupportedCountriesResource) -> None:
        self._supported_countries = supported_countries

        self.list = async_to_streamed_response_wrapper(
            supported_countries.list,
        )
