# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform
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
from ...types.entitlements import grant_list_params
from ...types.entitlements.grant_list_response import GrantListResponse
from ...types.entitlements.grant_revoke_response import GrantRevokeResponse

__all__ = ["GrantsResource", "AsyncGrantsResource"]


class GrantsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GrantsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return GrantsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GrantsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return GrantsResourceWithStreamingResponse(self)

    def list(
        self,
        id: str,
        *,
        customer_id: str | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        status: Literal["Pending", "Delivered", "Failed", "Revoked"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultPageNumberPagination[GrantListResponse]:
        """
        GET /entitlements/{id}/grants (public API)

        Args:
          customer_id: Filter by customer ID

          page_number: Page number (default 0)

          page_size: Page size (default 10, max 100)

          status: Filter by grant status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get_api_list(
            path_template("/entitlements/{id}/grants", id=id),
            page=SyncDefaultPageNumberPagination[GrantListResponse],
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
                        "status": status,
                    },
                    grant_list_params.GrantListParams,
                ),
            ),
            model=GrantListResponse,
        )

    def revoke(
        self,
        grant_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GrantRevokeResponse:
        """Revokes a single entitlement grant for the caller's business.

        For LicenseKey
        integrations, also disables the backing license key. Idempotent: re-revoking an
        already-revoked grant returns 200 with current state. The revocation reason is
        always set to "manual" for API-initiated revocations.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not grant_id:
            raise ValueError(f"Expected a non-empty value for `grant_id` but received {grant_id!r}")
        return self._delete(
            path_template("/entitlements/{id}/grants/{grant_id}", id=id, grant_id=grant_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GrantRevokeResponse,
        )


class AsyncGrantsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGrantsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGrantsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGrantsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return AsyncGrantsResourceWithStreamingResponse(self)

    def list(
        self,
        id: str,
        *,
        customer_id: str | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        status: Literal["Pending", "Delivered", "Failed", "Revoked"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[GrantListResponse, AsyncDefaultPageNumberPagination[GrantListResponse]]:
        """
        GET /entitlements/{id}/grants (public API)

        Args:
          customer_id: Filter by customer ID

          page_number: Page number (default 0)

          page_size: Page size (default 10, max 100)

          status: Filter by grant status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get_api_list(
            path_template("/entitlements/{id}/grants", id=id),
            page=AsyncDefaultPageNumberPagination[GrantListResponse],
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
                        "status": status,
                    },
                    grant_list_params.GrantListParams,
                ),
            ),
            model=GrantListResponse,
        )

    async def revoke(
        self,
        grant_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GrantRevokeResponse:
        """Revokes a single entitlement grant for the caller's business.

        For LicenseKey
        integrations, also disables the backing license key. Idempotent: re-revoking an
        already-revoked grant returns 200 with current state. The revocation reason is
        always set to "manual" for API-initiated revocations.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not grant_id:
            raise ValueError(f"Expected a non-empty value for `grant_id` but received {grant_id!r}")
        return await self._delete(
            path_template("/entitlements/{id}/grants/{grant_id}", id=id, grant_id=grant_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GrantRevokeResponse,
        )


class GrantsResourceWithRawResponse:
    def __init__(self, grants: GrantsResource) -> None:
        self._grants = grants

        self.list = to_raw_response_wrapper(
            grants.list,
        )
        self.revoke = to_raw_response_wrapper(
            grants.revoke,
        )


class AsyncGrantsResourceWithRawResponse:
    def __init__(self, grants: AsyncGrantsResource) -> None:
        self._grants = grants

        self.list = async_to_raw_response_wrapper(
            grants.list,
        )
        self.revoke = async_to_raw_response_wrapper(
            grants.revoke,
        )


class GrantsResourceWithStreamingResponse:
    def __init__(self, grants: GrantsResource) -> None:
        self._grants = grants

        self.list = to_streamed_response_wrapper(
            grants.list,
        )
        self.revoke = to_streamed_response_wrapper(
            grants.revoke,
        )


class AsyncGrantsResourceWithStreamingResponse:
    def __init__(self, grants: AsyncGrantsResource) -> None:
        self._grants = grants

        self.list = async_to_streamed_response_wrapper(
            grants.list,
        )
        self.revoke = async_to_streamed_response_wrapper(
            grants.revoke,
        )
