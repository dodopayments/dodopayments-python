# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
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
from ...types.products import short_link_list_params, short_link_create_params
from ...types.products.short_link_list_response import ShortLinkListResponse
from ...types.products.short_link_create_response import ShortLinkCreateResponse

__all__ = ["ShortLinksResource", "AsyncShortLinksResource"]


class ShortLinksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ShortLinksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return ShortLinksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ShortLinksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return ShortLinksResourceWithStreamingResponse(self)

    def create(
        self,
        id: str,
        *,
        slug: str,
        static_checkout_params: Optional[Dict[str, str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShortLinkCreateResponse:
        """Gives a Short Checkout URL with custom slug for a product.

        Uses a Static
        Checkout URL under the hood.

        Args:
          slug: Slug for the short link.

          static_checkout_params: Static Checkout URL parameters to apply to the resulting short URL.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/products/{id}/short_links",
            body=maybe_transform(
                {
                    "slug": slug,
                    "static_checkout_params": static_checkout_params,
                },
                short_link_create_params.ShortLinkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShortLinkCreateResponse,
        )

    def list(
        self,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        product_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultPageNumberPagination[ShortLinkListResponse]:
        """
        Lists all short links created by the business.

        Args:
          page_number: Page number default is 0

          page_size: Page size default is 10 max is 100

          product_id: Filter by product ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/products/short_links",
            page=SyncDefaultPageNumberPagination[ShortLinkListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                        "product_id": product_id,
                    },
                    short_link_list_params.ShortLinkListParams,
                ),
            ),
            model=ShortLinkListResponse,
        )


class AsyncShortLinksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncShortLinksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return AsyncShortLinksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncShortLinksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return AsyncShortLinksResourceWithStreamingResponse(self)

    async def create(
        self,
        id: str,
        *,
        slug: str,
        static_checkout_params: Optional[Dict[str, str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShortLinkCreateResponse:
        """Gives a Short Checkout URL with custom slug for a product.

        Uses a Static
        Checkout URL under the hood.

        Args:
          slug: Slug for the short link.

          static_checkout_params: Static Checkout URL parameters to apply to the resulting short URL.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/products/{id}/short_links",
            body=await async_maybe_transform(
                {
                    "slug": slug,
                    "static_checkout_params": static_checkout_params,
                },
                short_link_create_params.ShortLinkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShortLinkCreateResponse,
        )

    def list(
        self,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        product_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ShortLinkListResponse, AsyncDefaultPageNumberPagination[ShortLinkListResponse]]:
        """
        Lists all short links created by the business.

        Args:
          page_number: Page number default is 0

          page_size: Page size default is 10 max is 100

          product_id: Filter by product ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/products/short_links",
            page=AsyncDefaultPageNumberPagination[ShortLinkListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                        "product_id": product_id,
                    },
                    short_link_list_params.ShortLinkListParams,
                ),
            ),
            model=ShortLinkListResponse,
        )


class ShortLinksResourceWithRawResponse:
    def __init__(self, short_links: ShortLinksResource) -> None:
        self._short_links = short_links

        self.create = to_raw_response_wrapper(
            short_links.create,
        )
        self.list = to_raw_response_wrapper(
            short_links.list,
        )


class AsyncShortLinksResourceWithRawResponse:
    def __init__(self, short_links: AsyncShortLinksResource) -> None:
        self._short_links = short_links

        self.create = async_to_raw_response_wrapper(
            short_links.create,
        )
        self.list = async_to_raw_response_wrapper(
            short_links.list,
        )


class ShortLinksResourceWithStreamingResponse:
    def __init__(self, short_links: ShortLinksResource) -> None:
        self._short_links = short_links

        self.create = to_streamed_response_wrapper(
            short_links.create,
        )
        self.list = to_streamed_response_wrapper(
            short_links.list,
        )


class AsyncShortLinksResourceWithStreamingResponse:
    def __init__(self, short_links: AsyncShortLinksResource) -> None:
        self._short_links = short_links

        self.create = async_to_streamed_response_wrapper(
            short_links.create,
        )
        self.list = async_to_streamed_response_wrapper(
            short_links.list,
        )
