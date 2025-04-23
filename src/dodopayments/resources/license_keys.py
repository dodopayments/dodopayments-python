# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime

import httpx

from ..types import LicenseKeyStatus, license_key_list_params, license_key_update_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ..types.license_key import LicenseKey
from ..types.license_key_status import LicenseKeyStatus

__all__ = ["LicenseKeysResource", "AsyncLicenseKeysResource"]


class LicenseKeysResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LicenseKeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return LicenseKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LicenseKeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return LicenseKeysResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LicenseKey:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/license_keys/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LicenseKey,
        )

    def update(
        self,
        id: str,
        *,
        activations_limit: Optional[int] | NotGiven = NOT_GIVEN,
        disabled: Optional[bool] | NotGiven = NOT_GIVEN,
        expires_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LicenseKey:
        """Args:
          activations_limit: The updated activation limit for the license key.

        Use `null` to remove the
              limit, or omit this field to leave it unchanged.

          disabled: Indicates whether the license key should be disabled. A value of `true` disables
              the key, while `false` enables it. Omit this field to leave it unchanged.

          expires_at: The updated expiration timestamp for the license key in UTC. Use `null` to
              remove the expiration date, or omit this field to leave it unchanged.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/license_keys/{id}",
            body=maybe_transform(
                {
                    "activations_limit": activations_limit,
                    "disabled": disabled,
                    "expires_at": expires_at,
                },
                license_key_update_params.LicenseKeyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LicenseKey,
        )

    def list(
        self,
        *,
        customer_id: Optional[str] | NotGiven = NOT_GIVEN,
        page_number: Optional[int] | NotGiven = NOT_GIVEN,
        page_size: Optional[int] | NotGiven = NOT_GIVEN,
        product_id: Optional[str] | NotGiven = NOT_GIVEN,
        status: Optional[LicenseKeyStatus] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncDefaultPageNumberPagination[LicenseKey]:
        """
        Args:
          customer_id: Filter by customer ID

          page_number: Page number default is 0

          page_size: Page size default is 10 max is 100

          product_id: Filter by product ID

          status: Filter by license key status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/license_keys",
            page=SyncDefaultPageNumberPagination[LicenseKey],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "customer_id": customer_id,
                        "page_number": page_number,
                        "page_size": page_size,
                        "product_id": product_id,
                        "status": status,
                    },
                    license_key_list_params.LicenseKeyListParams,
                ),
            ),
            model=LicenseKey,
        )


class AsyncLicenseKeysResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLicenseKeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLicenseKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLicenseKeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return AsyncLicenseKeysResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LicenseKey:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/license_keys/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LicenseKey,
        )

    async def update(
        self,
        id: str,
        *,
        activations_limit: Optional[int] | NotGiven = NOT_GIVEN,
        disabled: Optional[bool] | NotGiven = NOT_GIVEN,
        expires_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LicenseKey:
        """Args:
          activations_limit: The updated activation limit for the license key.

        Use `null` to remove the
              limit, or omit this field to leave it unchanged.

          disabled: Indicates whether the license key should be disabled. A value of `true` disables
              the key, while `false` enables it. Omit this field to leave it unchanged.

          expires_at: The updated expiration timestamp for the license key in UTC. Use `null` to
              remove the expiration date, or omit this field to leave it unchanged.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/license_keys/{id}",
            body=await async_maybe_transform(
                {
                    "activations_limit": activations_limit,
                    "disabled": disabled,
                    "expires_at": expires_at,
                },
                license_key_update_params.LicenseKeyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LicenseKey,
        )

    def list(
        self,
        *,
        customer_id: Optional[str] | NotGiven = NOT_GIVEN,
        page_number: Optional[int] | NotGiven = NOT_GIVEN,
        page_size: Optional[int] | NotGiven = NOT_GIVEN,
        product_id: Optional[str] | NotGiven = NOT_GIVEN,
        status: Optional[LicenseKeyStatus] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[LicenseKey, AsyncDefaultPageNumberPagination[LicenseKey]]:
        """
        Args:
          customer_id: Filter by customer ID

          page_number: Page number default is 0

          page_size: Page size default is 10 max is 100

          product_id: Filter by product ID

          status: Filter by license key status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/license_keys",
            page=AsyncDefaultPageNumberPagination[LicenseKey],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "customer_id": customer_id,
                        "page_number": page_number,
                        "page_size": page_size,
                        "product_id": product_id,
                        "status": status,
                    },
                    license_key_list_params.LicenseKeyListParams,
                ),
            ),
            model=LicenseKey,
        )


class LicenseKeysResourceWithRawResponse:
    def __init__(self, license_keys: LicenseKeysResource) -> None:
        self._license_keys = license_keys

        self.retrieve = to_raw_response_wrapper(
            license_keys.retrieve,
        )
        self.update = to_raw_response_wrapper(
            license_keys.update,
        )
        self.list = to_raw_response_wrapper(
            license_keys.list,
        )


class AsyncLicenseKeysResourceWithRawResponse:
    def __init__(self, license_keys: AsyncLicenseKeysResource) -> None:
        self._license_keys = license_keys

        self.retrieve = async_to_raw_response_wrapper(
            license_keys.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            license_keys.update,
        )
        self.list = async_to_raw_response_wrapper(
            license_keys.list,
        )


class LicenseKeysResourceWithStreamingResponse:
    def __init__(self, license_keys: LicenseKeysResource) -> None:
        self._license_keys = license_keys

        self.retrieve = to_streamed_response_wrapper(
            license_keys.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            license_keys.update,
        )
        self.list = to_streamed_response_wrapper(
            license_keys.list,
        )


class AsyncLicenseKeysResourceWithStreamingResponse:
    def __init__(self, license_keys: AsyncLicenseKeysResource) -> None:
        self._license_keys = license_keys

        self.retrieve = async_to_streamed_response_wrapper(
            license_keys.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            license_keys.update,
        )
        self.list = async_to_streamed_response_wrapper(
            license_keys.list,
        )
