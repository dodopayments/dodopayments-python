# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import license_activate_params, license_validate_params, license_deactivate_params
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.license_key_instance import LicenseKeyInstance
from ..types.license_validate_response import LicenseValidateResponse

__all__ = ["LicensesResource", "AsyncLicensesResource"]


class LicensesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LicensesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return LicensesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LicensesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return LicensesResourceWithStreamingResponse(self)

    def activate(
        self,
        *,
        license_key: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LicenseKeyInstance:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/licenses/activate",
            body=maybe_transform(
                {
                    "license_key": license_key,
                    "name": name,
                },
                license_activate_params.LicenseActivateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LicenseKeyInstance,
        )

    def deactivate(
        self,
        *,
        license_key: str,
        license_key_instance_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/licenses/deactivate",
            body=maybe_transform(
                {
                    "license_key": license_key,
                    "license_key_instance_id": license_key_instance_id,
                },
                license_deactivate_params.LicenseDeactivateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def validate(
        self,
        *,
        license_key: str,
        license_key_instance_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LicenseValidateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/licenses/validate",
            body=maybe_transform(
                {
                    "license_key": license_key,
                    "license_key_instance_id": license_key_instance_id,
                },
                license_validate_params.LicenseValidateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LicenseValidateResponse,
        )


class AsyncLicensesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLicensesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLicensesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLicensesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return AsyncLicensesResourceWithStreamingResponse(self)

    async def activate(
        self,
        *,
        license_key: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LicenseKeyInstance:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/licenses/activate",
            body=await async_maybe_transform(
                {
                    "license_key": license_key,
                    "name": name,
                },
                license_activate_params.LicenseActivateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LicenseKeyInstance,
        )

    async def deactivate(
        self,
        *,
        license_key: str,
        license_key_instance_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/licenses/deactivate",
            body=await async_maybe_transform(
                {
                    "license_key": license_key,
                    "license_key_instance_id": license_key_instance_id,
                },
                license_deactivate_params.LicenseDeactivateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def validate(
        self,
        *,
        license_key: str,
        license_key_instance_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LicenseValidateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/licenses/validate",
            body=await async_maybe_transform(
                {
                    "license_key": license_key,
                    "license_key_instance_id": license_key_instance_id,
                },
                license_validate_params.LicenseValidateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LicenseValidateResponse,
        )


class LicensesResourceWithRawResponse:
    def __init__(self, licenses: LicensesResource) -> None:
        self._licenses = licenses

        self.activate = to_raw_response_wrapper(
            licenses.activate,
        )
        self.deactivate = to_raw_response_wrapper(
            licenses.deactivate,
        )
        self.validate = to_raw_response_wrapper(
            licenses.validate,
        )


class AsyncLicensesResourceWithRawResponse:
    def __init__(self, licenses: AsyncLicensesResource) -> None:
        self._licenses = licenses

        self.activate = async_to_raw_response_wrapper(
            licenses.activate,
        )
        self.deactivate = async_to_raw_response_wrapper(
            licenses.deactivate,
        )
        self.validate = async_to_raw_response_wrapper(
            licenses.validate,
        )


class LicensesResourceWithStreamingResponse:
    def __init__(self, licenses: LicensesResource) -> None:
        self._licenses = licenses

        self.activate = to_streamed_response_wrapper(
            licenses.activate,
        )
        self.deactivate = to_streamed_response_wrapper(
            licenses.deactivate,
        )
        self.validate = to_streamed_response_wrapper(
            licenses.validate,
        )


class AsyncLicensesResourceWithStreamingResponse:
    def __init__(self, licenses: AsyncLicensesResource) -> None:
        self._licenses = licenses

        self.activate = async_to_streamed_response_wrapper(
            licenses.activate,
        )
        self.deactivate = async_to_streamed_response_wrapper(
            licenses.deactivate,
        )
        self.validate = async_to_streamed_response_wrapper(
            licenses.validate,
        )
