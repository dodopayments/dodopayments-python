# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.app_installation_retrieve_settings_response import AppInstallationRetrieveSettingsResponse

__all__ = ["AppInstallationResource", "AsyncAppInstallationResource"]


class AppInstallationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AppInstallationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return AppInstallationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AppInstallationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return AppInstallationResourceWithStreamingResponse(self)

    def retrieve_settings(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppInstallationRetrieveSettingsResponse:
        """
        The settings of the App Installation of the app token, with the secret values.
        The token grant gives the installation. The token needs `app_settings:read`.
        """
        return self._get(
            "/app-installation/settings",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AppInstallationRetrieveSettingsResponse,
        )


class AsyncAppInstallationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAppInstallationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAppInstallationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAppInstallationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return AsyncAppInstallationResourceWithStreamingResponse(self)

    async def retrieve_settings(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppInstallationRetrieveSettingsResponse:
        """
        The settings of the App Installation of the app token, with the secret values.
        The token grant gives the installation. The token needs `app_settings:read`.
        """
        return await self._get(
            "/app-installation/settings",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AppInstallationRetrieveSettingsResponse,
        )


class AppInstallationResourceWithRawResponse:
    def __init__(self, app_installation: AppInstallationResource) -> None:
        self._app_installation = app_installation

        self.retrieve_settings = to_raw_response_wrapper(
            app_installation.retrieve_settings,
        )


class AsyncAppInstallationResourceWithRawResponse:
    def __init__(self, app_installation: AsyncAppInstallationResource) -> None:
        self._app_installation = app_installation

        self.retrieve_settings = async_to_raw_response_wrapper(
            app_installation.retrieve_settings,
        )


class AppInstallationResourceWithStreamingResponse:
    def __init__(self, app_installation: AppInstallationResource) -> None:
        self._app_installation = app_installation

        self.retrieve_settings = to_streamed_response_wrapper(
            app_installation.retrieve_settings,
        )


class AsyncAppInstallationResourceWithStreamingResponse:
    def __init__(self, app_installation: AsyncAppInstallationResource) -> None:
        self._app_installation = app_installation

        self.retrieve_settings = async_to_streamed_response_wrapper(
            app_installation.retrieve_settings,
        )
