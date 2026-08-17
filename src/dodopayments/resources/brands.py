# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import brand_list_params, brand_create_params, brand_update_params, brand_archive_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..types.brand import Brand
from .._base_client import make_request_options
from ..types.brand_list_response import BrandListResponse
from ..types.brand_archive_response import BrandArchiveResponse
from ..types.brand_update_images_response import BrandUpdateImagesResponse

__all__ = ["BrandsResource", "AsyncBrandsResource"]


class BrandsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BrandsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return BrandsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BrandsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return BrandsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        description: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        statement_descriptor: Optional[str] | Omit = omit,
        support_email: Optional[str] | Omit = omit,
        url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Brand:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/brands",
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "statement_descriptor": statement_descriptor,
                    "support_email": support_email,
                    "url": url,
                },
                brand_create_params.BrandCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Brand,
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
    ) -> Brand:
        """
        Thin handler just calls `get_brand` and wraps in `Json(...)`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/brands/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Brand,
        )

    def update(
        self,
        id: str,
        *,
        description: Optional[str] | Omit = omit,
        image_id: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        statement_descriptor: Optional[str] | Omit = omit,
        support_email: Optional[str] | Omit = omit,
        url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Brand:
        """
        Args:
          image_id: The UUID you got back from the presigned‐upload call

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/brands/{id}", id=id),
            body=maybe_transform(
                {
                    "description": description,
                    "image_id": image_id,
                    "name": name,
                    "statement_descriptor": statement_descriptor,
                    "support_email": support_email,
                    "url": url,
                },
                brand_update_params.BrandUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Brand,
        )

    def list(
        self,
        *,
        include_archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandListResponse:
        """Args:
          include_archived: Set to true to also list archived brands.

        Default false.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/brands",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"include_archived": include_archived}, brand_list_params.BrandListParams),
            ),
            cast_to=BrandListResponse,
        )

    def archive(
        self,
        id: str,
        *,
        move_products_to: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandArchiveResponse:
        """Archive a brand.

        Its products, live subscriptions, and product collections move
        to the `move_products_to` brand. Archive is permanent.

        Args:
          move_products_to: Brand that takes over the products and the live subscriptions of the brand you
              archive. It must be a brand of the same business, and it must not be archived.
              The primary brand (its brand id is the business id) is a valid target. Omit this
              field only when the brand holds no products and no live subscriptions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/brands/{id}/archive", id=id),
            body=maybe_transform({"move_products_to": move_products_to}, brand_archive_params.BrandArchiveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandArchiveResponse,
        )

    def update_images(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandUpdateImagesResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            path_template("/brands/{id}/images", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandUpdateImagesResponse,
        )


class AsyncBrandsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBrandsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBrandsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBrandsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return AsyncBrandsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        description: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        statement_descriptor: Optional[str] | Omit = omit,
        support_email: Optional[str] | Omit = omit,
        url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Brand:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/brands",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "statement_descriptor": statement_descriptor,
                    "support_email": support_email,
                    "url": url,
                },
                brand_create_params.BrandCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Brand,
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
    ) -> Brand:
        """
        Thin handler just calls `get_brand` and wraps in `Json(...)`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/brands/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Brand,
        )

    async def update(
        self,
        id: str,
        *,
        description: Optional[str] | Omit = omit,
        image_id: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        statement_descriptor: Optional[str] | Omit = omit,
        support_email: Optional[str] | Omit = omit,
        url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Brand:
        """
        Args:
          image_id: The UUID you got back from the presigned‐upload call

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/brands/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "description": description,
                    "image_id": image_id,
                    "name": name,
                    "statement_descriptor": statement_descriptor,
                    "support_email": support_email,
                    "url": url,
                },
                brand_update_params.BrandUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Brand,
        )

    async def list(
        self,
        *,
        include_archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandListResponse:
        """Args:
          include_archived: Set to true to also list archived brands.

        Default false.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/brands",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"include_archived": include_archived}, brand_list_params.BrandListParams
                ),
            ),
            cast_to=BrandListResponse,
        )

    async def archive(
        self,
        id: str,
        *,
        move_products_to: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandArchiveResponse:
        """Archive a brand.

        Its products, live subscriptions, and product collections move
        to the `move_products_to` brand. Archive is permanent.

        Args:
          move_products_to: Brand that takes over the products and the live subscriptions of the brand you
              archive. It must be a brand of the same business, and it must not be archived.
              The primary brand (its brand id is the business id) is a valid target. Omit this
              field only when the brand holds no products and no live subscriptions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/brands/{id}/archive", id=id),
            body=await async_maybe_transform(
                {"move_products_to": move_products_to}, brand_archive_params.BrandArchiveParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandArchiveResponse,
        )

    async def update_images(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandUpdateImagesResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            path_template("/brands/{id}/images", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandUpdateImagesResponse,
        )


class BrandsResourceWithRawResponse:
    def __init__(self, brands: BrandsResource) -> None:
        self._brands = brands

        self.create = to_raw_response_wrapper(
            brands.create,
        )
        self.retrieve = to_raw_response_wrapper(
            brands.retrieve,
        )
        self.update = to_raw_response_wrapper(
            brands.update,
        )
        self.list = to_raw_response_wrapper(
            brands.list,
        )
        self.archive = to_raw_response_wrapper(
            brands.archive,
        )
        self.update_images = to_raw_response_wrapper(
            brands.update_images,
        )


class AsyncBrandsResourceWithRawResponse:
    def __init__(self, brands: AsyncBrandsResource) -> None:
        self._brands = brands

        self.create = async_to_raw_response_wrapper(
            brands.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            brands.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            brands.update,
        )
        self.list = async_to_raw_response_wrapper(
            brands.list,
        )
        self.archive = async_to_raw_response_wrapper(
            brands.archive,
        )
        self.update_images = async_to_raw_response_wrapper(
            brands.update_images,
        )


class BrandsResourceWithStreamingResponse:
    def __init__(self, brands: BrandsResource) -> None:
        self._brands = brands

        self.create = to_streamed_response_wrapper(
            brands.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            brands.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            brands.update,
        )
        self.list = to_streamed_response_wrapper(
            brands.list,
        )
        self.archive = to_streamed_response_wrapper(
            brands.archive,
        )
        self.update_images = to_streamed_response_wrapper(
            brands.update_images,
        )


class AsyncBrandsResourceWithStreamingResponse:
    def __init__(self, brands: AsyncBrandsResource) -> None:
        self._brands = brands

        self.create = async_to_streamed_response_wrapper(
            brands.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            brands.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            brands.update,
        )
        self.list = async_to_streamed_response_wrapper(
            brands.list,
        )
        self.archive = async_to_streamed_response_wrapper(
            brands.archive,
        )
        self.update_images = async_to_streamed_response_wrapper(
            brands.update_images,
        )
