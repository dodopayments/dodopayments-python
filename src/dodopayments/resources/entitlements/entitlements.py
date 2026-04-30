# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal

import httpx

from .files import (
    FilesResource,
    AsyncFilesResource,
    FilesResourceWithRawResponse,
    AsyncFilesResourceWithRawResponse,
    FilesResourceWithStreamingResponse,
    AsyncFilesResourceWithStreamingResponse,
)
from .grants import (
    GrantsResource,
    AsyncGrantsResource,
    GrantsResourceWithRawResponse,
    AsyncGrantsResourceWithRawResponse,
    GrantsResourceWithStreamingResponse,
    AsyncGrantsResourceWithStreamingResponse,
)
from ...types import entitlement_list_params, entitlement_create_params, entitlement_update_params
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
from ...pagination import SyncDefaultPageNumberPagination, AsyncDefaultPageNumberPagination
from ..._base_client import AsyncPaginator, make_request_options
from ...types.entitlement_list_response import EntitlementListResponse
from ...types.entitlement_create_response import EntitlementCreateResponse
from ...types.entitlement_update_response import EntitlementUpdateResponse
from ...types.entitlement_retrieve_response import EntitlementRetrieveResponse

__all__ = ["EntitlementsResource", "AsyncEntitlementsResource"]


class EntitlementsResource(SyncAPIResource):
    @cached_property
    def files(self) -> FilesResource:
        return FilesResource(self._client)

    @cached_property
    def grants(self) -> GrantsResource:
        return GrantsResource(self._client)

    @cached_property
    def with_raw_response(self) -> EntitlementsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return EntitlementsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EntitlementsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return EntitlementsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        integration_config: entitlement_create_params.IntegrationConfig,
        integration_type: Literal[
            "discord", "telegram", "github", "figma", "framer", "notion", "digital_files", "license_key"
        ],
        name: str,
        description: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntitlementCreateResponse:
        """
        POST /entitlements

        Args:
          integration_config: Platform-specific configuration (validated per integration_type)

          integration_type: Which platform integration this entitlement uses

          name: Display name for this entitlement

          description: Optional description

          metadata: Optional user-facing metadata

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/entitlements",
            body=maybe_transform(
                {
                    "integration_config": integration_config,
                    "integration_type": integration_type,
                    "name": name,
                    "description": description,
                    "metadata": metadata,
                },
                entitlement_create_params.EntitlementCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntitlementCreateResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntitlementRetrieveResponse:
        """
        GET /entitlements/{id}

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/entitlements/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntitlementRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        description: Optional[str] | Omit = omit,
        integration_config: Optional[entitlement_update_params.IntegrationConfig] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntitlementUpdateResponse:
        """
        PATCH /entitlements/{id}

        Args:
          integration_config: Platform-specific configuration for an entitlement. Each variant uses unique
              field names so `#[serde(untagged)]` can disambiguate correctly.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/entitlements/{id}", id=id),
            body=maybe_transform(
                {
                    "description": description,
                    "integration_config": integration_config,
                    "metadata": metadata,
                    "name": name,
                },
                entitlement_update_params.EntitlementUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntitlementUpdateResponse,
        )

    def list(
        self,
        *,
        integration_type: Literal[
            "discord", "telegram", "github", "figma", "framer", "notion", "digital_files", "license_key"
        ]
        | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultPageNumberPagination[EntitlementListResponse]:
        """
        GET /entitlements

        Args:
          integration_type: Filter by integration type

          page_number: Page number (default 0)

          page_size: Page size (default 10, max 100)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/entitlements",
            page=SyncDefaultPageNumberPagination[EntitlementListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "integration_type": integration_type,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    entitlement_list_params.EntitlementListParams,
                ),
            ),
            model=EntitlementListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        DELETE /entitlements/{id} (soft-delete)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/entitlements/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncEntitlementsResource(AsyncAPIResource):
    @cached_property
    def files(self) -> AsyncFilesResource:
        return AsyncFilesResource(self._client)

    @cached_property
    def grants(self) -> AsyncGrantsResource:
        return AsyncGrantsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEntitlementsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEntitlementsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEntitlementsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return AsyncEntitlementsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        integration_config: entitlement_create_params.IntegrationConfig,
        integration_type: Literal[
            "discord", "telegram", "github", "figma", "framer", "notion", "digital_files", "license_key"
        ],
        name: str,
        description: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntitlementCreateResponse:
        """
        POST /entitlements

        Args:
          integration_config: Platform-specific configuration (validated per integration_type)

          integration_type: Which platform integration this entitlement uses

          name: Display name for this entitlement

          description: Optional description

          metadata: Optional user-facing metadata

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/entitlements",
            body=await async_maybe_transform(
                {
                    "integration_config": integration_config,
                    "integration_type": integration_type,
                    "name": name,
                    "description": description,
                    "metadata": metadata,
                },
                entitlement_create_params.EntitlementCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntitlementCreateResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntitlementRetrieveResponse:
        """
        GET /entitlements/{id}

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/entitlements/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntitlementRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        description: Optional[str] | Omit = omit,
        integration_config: Optional[entitlement_update_params.IntegrationConfig] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntitlementUpdateResponse:
        """
        PATCH /entitlements/{id}

        Args:
          integration_config: Platform-specific configuration for an entitlement. Each variant uses unique
              field names so `#[serde(untagged)]` can disambiguate correctly.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/entitlements/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "description": description,
                    "integration_config": integration_config,
                    "metadata": metadata,
                    "name": name,
                },
                entitlement_update_params.EntitlementUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntitlementUpdateResponse,
        )

    def list(
        self,
        *,
        integration_type: Literal[
            "discord", "telegram", "github", "figma", "framer", "notion", "digital_files", "license_key"
        ]
        | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[EntitlementListResponse, AsyncDefaultPageNumberPagination[EntitlementListResponse]]:
        """
        GET /entitlements

        Args:
          integration_type: Filter by integration type

          page_number: Page number (default 0)

          page_size: Page size (default 10, max 100)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/entitlements",
            page=AsyncDefaultPageNumberPagination[EntitlementListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "integration_type": integration_type,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    entitlement_list_params.EntitlementListParams,
                ),
            ),
            model=EntitlementListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        DELETE /entitlements/{id} (soft-delete)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/entitlements/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class EntitlementsResourceWithRawResponse:
    def __init__(self, entitlements: EntitlementsResource) -> None:
        self._entitlements = entitlements

        self.create = to_raw_response_wrapper(
            entitlements.create,
        )
        self.retrieve = to_raw_response_wrapper(
            entitlements.retrieve,
        )
        self.update = to_raw_response_wrapper(
            entitlements.update,
        )
        self.list = to_raw_response_wrapper(
            entitlements.list,
        )
        self.delete = to_raw_response_wrapper(
            entitlements.delete,
        )

    @cached_property
    def files(self) -> FilesResourceWithRawResponse:
        return FilesResourceWithRawResponse(self._entitlements.files)

    @cached_property
    def grants(self) -> GrantsResourceWithRawResponse:
        return GrantsResourceWithRawResponse(self._entitlements.grants)


class AsyncEntitlementsResourceWithRawResponse:
    def __init__(self, entitlements: AsyncEntitlementsResource) -> None:
        self._entitlements = entitlements

        self.create = async_to_raw_response_wrapper(
            entitlements.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            entitlements.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            entitlements.update,
        )
        self.list = async_to_raw_response_wrapper(
            entitlements.list,
        )
        self.delete = async_to_raw_response_wrapper(
            entitlements.delete,
        )

    @cached_property
    def files(self) -> AsyncFilesResourceWithRawResponse:
        return AsyncFilesResourceWithRawResponse(self._entitlements.files)

    @cached_property
    def grants(self) -> AsyncGrantsResourceWithRawResponse:
        return AsyncGrantsResourceWithRawResponse(self._entitlements.grants)


class EntitlementsResourceWithStreamingResponse:
    def __init__(self, entitlements: EntitlementsResource) -> None:
        self._entitlements = entitlements

        self.create = to_streamed_response_wrapper(
            entitlements.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            entitlements.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            entitlements.update,
        )
        self.list = to_streamed_response_wrapper(
            entitlements.list,
        )
        self.delete = to_streamed_response_wrapper(
            entitlements.delete,
        )

    @cached_property
    def files(self) -> FilesResourceWithStreamingResponse:
        return FilesResourceWithStreamingResponse(self._entitlements.files)

    @cached_property
    def grants(self) -> GrantsResourceWithStreamingResponse:
        return GrantsResourceWithStreamingResponse(self._entitlements.grants)


class AsyncEntitlementsResourceWithStreamingResponse:
    def __init__(self, entitlements: AsyncEntitlementsResource) -> None:
        self._entitlements = entitlements

        self.create = async_to_streamed_response_wrapper(
            entitlements.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            entitlements.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            entitlements.update,
        )
        self.list = async_to_streamed_response_wrapper(
            entitlements.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            entitlements.delete,
        )

    @cached_property
    def files(self) -> AsyncFilesResourceWithStreamingResponse:
        return AsyncFilesResourceWithStreamingResponse(self._entitlements.files)

    @cached_property
    def grants(self) -> AsyncGrantsResourceWithStreamingResponse:
        return AsyncGrantsResourceWithStreamingResponse(self._entitlements.grants)
