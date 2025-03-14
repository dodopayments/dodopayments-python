# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.misc_list_supported_countries_response import MiscListSupportedCountriesResponse

__all__ = ["MiscResource", "AsyncMiscResource"]


class MiscResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MiscResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return MiscResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MiscResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return MiscResourceWithStreamingResponse(self)

    def list_supported_countries(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MiscListSupportedCountriesResponse:
        return self._get(
            "/checkout/supported_countries",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MiscListSupportedCountriesResponse,
        )


class AsyncMiscResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMiscResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMiscResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMiscResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return AsyncMiscResourceWithStreamingResponse(self)

    async def list_supported_countries(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MiscListSupportedCountriesResponse:
        return await self._get(
            "/checkout/supported_countries",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MiscListSupportedCountriesResponse,
        )


class MiscResourceWithRawResponse:
    def __init__(self, misc: MiscResource) -> None:
        self._misc = misc

        self.list_supported_countries = to_raw_response_wrapper(
            misc.list_supported_countries,
        )


class AsyncMiscResourceWithRawResponse:
    def __init__(self, misc: AsyncMiscResource) -> None:
        self._misc = misc

        self.list_supported_countries = async_to_raw_response_wrapper(
            misc.list_supported_countries,
        )


class MiscResourceWithStreamingResponse:
    def __init__(self, misc: MiscResource) -> None:
        self._misc = misc

        self.list_supported_countries = to_streamed_response_wrapper(
            misc.list_supported_countries,
        )


class AsyncMiscResourceWithStreamingResponse:
    def __init__(self, misc: AsyncMiscResource) -> None:
        self._misc = misc

        self.list_supported_countries = async_to_streamed_response_wrapper(
            misc.list_supported_countries,
        )
