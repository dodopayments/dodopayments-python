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

__all__ = ["MiscResource", "AsyncMiscResource"]


class MiscResource(SyncAPIResource):
    @cached_property
    def supported_countries(self) -> SupportedCountriesResource:
        return SupportedCountriesResource(self._client)

    @cached_property
    def with_raw_response(self) -> MiscResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/dodo-payments-python#accessing-raw-response-data-eg-headers
        """
        return MiscResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MiscResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/dodo-payments-python#with_streaming_response
        """
        return MiscResourceWithStreamingResponse(self)


class AsyncMiscResource(AsyncAPIResource):
    @cached_property
    def supported_countries(self) -> AsyncSupportedCountriesResource:
        return AsyncSupportedCountriesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMiscResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/dodo-payments-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMiscResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMiscResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/dodo-payments-python#with_streaming_response
        """
        return AsyncMiscResourceWithStreamingResponse(self)


class MiscResourceWithRawResponse:
    def __init__(self, misc: MiscResource) -> None:
        self._misc = misc

    @cached_property
    def supported_countries(self) -> SupportedCountriesResourceWithRawResponse:
        return SupportedCountriesResourceWithRawResponse(self._misc.supported_countries)


class AsyncMiscResourceWithRawResponse:
    def __init__(self, misc: AsyncMiscResource) -> None:
        self._misc = misc

    @cached_property
    def supported_countries(self) -> AsyncSupportedCountriesResourceWithRawResponse:
        return AsyncSupportedCountriesResourceWithRawResponse(self._misc.supported_countries)


class MiscResourceWithStreamingResponse:
    def __init__(self, misc: MiscResource) -> None:
        self._misc = misc

    @cached_property
    def supported_countries(self) -> SupportedCountriesResourceWithStreamingResponse:
        return SupportedCountriesResourceWithStreamingResponse(self._misc.supported_countries)


class AsyncMiscResourceWithStreamingResponse:
    def __init__(self, misc: AsyncMiscResource) -> None:
        self._misc = misc

    @cached_property
    def supported_countries(self) -> AsyncSupportedCountriesResourceWithStreamingResponse:
        return AsyncSupportedCountriesResourceWithStreamingResponse(self._misc.supported_countries)
