# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ...types import (
    product_collection_list_params,
    product_collection_create_params,
    product_collection_update_params,
    product_collection_update_images_params,
)
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
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
from .groups.groups import (
    GroupsResource,
    AsyncGroupsResource,
    GroupsResourceWithRawResponse,
    AsyncGroupsResourceWithRawResponse,
    GroupsResourceWithStreamingResponse,
    AsyncGroupsResourceWithStreamingResponse,
)
from ..._base_client import AsyncPaginator, make_request_options
from ...types.product_collection_list_response import ProductCollectionListResponse
from ...types.product_collection_create_response import ProductCollectionCreateResponse
from ...types.product_collection_retrieve_response import ProductCollectionRetrieveResponse
from ...types.product_collection_unarchive_response import ProductCollectionUnarchiveResponse
from ...types.product_collection_update_images_response import ProductCollectionUpdateImagesResponse

__all__ = ["ProductCollectionsResource", "AsyncProductCollectionsResource"]


class ProductCollectionsResource(SyncAPIResource):
    @cached_property
    def groups(self) -> GroupsResource:
        return GroupsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ProductCollectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return ProductCollectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProductCollectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return ProductCollectionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        groups: Iterable[product_collection_create_params.Group],
        name: str,
        brand_id: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProductCollectionCreateResponse:
        """
        Args:
          groups: Groups of products in this collection

          name: Name of the product collection

          brand_id: Brand id for the collection, if not provided will default to primary brand

          description: Optional description of the product collection

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/product-collections",
            body=maybe_transform(
                {
                    "groups": groups,
                    "name": name,
                    "brand_id": brand_id,
                    "description": description,
                },
                product_collection_create_params.ProductCollectionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProductCollectionCreateResponse,
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
    ) -> ProductCollectionRetrieveResponse:
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
            path_template("/product-collections/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProductCollectionRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        brand_id: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        group_order: Optional[SequenceNotStr[str]] | Omit = omit,
        image_id: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          brand_id: Optional brand_id update

          description: Optional description update - pass null to remove, omit to keep unchanged

          group_order: Optional new order for groups (array of group UUIDs in desired order)

          image_id: Optional image update - pass null to remove, omit to keep unchanged

          name: Optional new name for the collection

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._patch(
            path_template("/product-collections/{id}", id=id),
            body=maybe_transform(
                {
                    "brand_id": brand_id,
                    "description": description,
                    "group_order": group_order,
                    "image_id": image_id,
                    "name": name,
                },
                product_collection_update_params.ProductCollectionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        archived: bool | Omit = omit,
        brand_id: str | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultPageNumberPagination[ProductCollectionListResponse]:
        """
        Args:
          archived: List archived collections

          brand_id: Filter by Brand id

          page_number: Page number default is 0

          page_size: Page size default is 10 max is 100

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/product-collections",
            page=SyncDefaultPageNumberPagination[ProductCollectionListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "archived": archived,
                        "brand_id": brand_id,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    product_collection_list_params.ProductCollectionListParams,
                ),
            ),
            model=ProductCollectionListResponse,
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
            path_template("/product-collections/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def unarchive(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProductCollectionUnarchiveResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/product-collections/{id}/unarchive", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProductCollectionUnarchiveResponse,
        )

    def update_images(
        self,
        id: str,
        *,
        force_update: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProductCollectionUpdateImagesResponse:
        """
        Args:
          force_update: If true, generates a new image ID to force cache invalidation

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            path_template("/product-collections/{id}/images", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"force_update": force_update},
                    product_collection_update_images_params.ProductCollectionUpdateImagesParams,
                ),
            ),
            cast_to=ProductCollectionUpdateImagesResponse,
        )


class AsyncProductCollectionsResource(AsyncAPIResource):
    @cached_property
    def groups(self) -> AsyncGroupsResource:
        return AsyncGroupsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncProductCollectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProductCollectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProductCollectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return AsyncProductCollectionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        groups: Iterable[product_collection_create_params.Group],
        name: str,
        brand_id: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProductCollectionCreateResponse:
        """
        Args:
          groups: Groups of products in this collection

          name: Name of the product collection

          brand_id: Brand id for the collection, if not provided will default to primary brand

          description: Optional description of the product collection

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/product-collections",
            body=await async_maybe_transform(
                {
                    "groups": groups,
                    "name": name,
                    "brand_id": brand_id,
                    "description": description,
                },
                product_collection_create_params.ProductCollectionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProductCollectionCreateResponse,
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
    ) -> ProductCollectionRetrieveResponse:
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
            path_template("/product-collections/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProductCollectionRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        brand_id: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        group_order: Optional[SequenceNotStr[str]] | Omit = omit,
        image_id: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          brand_id: Optional brand_id update

          description: Optional description update - pass null to remove, omit to keep unchanged

          group_order: Optional new order for groups (array of group UUIDs in desired order)

          image_id: Optional image update - pass null to remove, omit to keep unchanged

          name: Optional new name for the collection

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._patch(
            path_template("/product-collections/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "brand_id": brand_id,
                    "description": description,
                    "group_order": group_order,
                    "image_id": image_id,
                    "name": name,
                },
                product_collection_update_params.ProductCollectionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        archived: bool | Omit = omit,
        brand_id: str | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ProductCollectionListResponse, AsyncDefaultPageNumberPagination[ProductCollectionListResponse]]:
        """
        Args:
          archived: List archived collections

          brand_id: Filter by Brand id

          page_number: Page number default is 0

          page_size: Page size default is 10 max is 100

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/product-collections",
            page=AsyncDefaultPageNumberPagination[ProductCollectionListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "archived": archived,
                        "brand_id": brand_id,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    product_collection_list_params.ProductCollectionListParams,
                ),
            ),
            model=ProductCollectionListResponse,
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
            path_template("/product-collections/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def unarchive(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProductCollectionUnarchiveResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/product-collections/{id}/unarchive", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProductCollectionUnarchiveResponse,
        )

    async def update_images(
        self,
        id: str,
        *,
        force_update: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProductCollectionUpdateImagesResponse:
        """
        Args:
          force_update: If true, generates a new image ID to force cache invalidation

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            path_template("/product-collections/{id}/images", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"force_update": force_update},
                    product_collection_update_images_params.ProductCollectionUpdateImagesParams,
                ),
            ),
            cast_to=ProductCollectionUpdateImagesResponse,
        )


class ProductCollectionsResourceWithRawResponse:
    def __init__(self, product_collections: ProductCollectionsResource) -> None:
        self._product_collections = product_collections

        self.create = to_raw_response_wrapper(
            product_collections.create,
        )
        self.retrieve = to_raw_response_wrapper(
            product_collections.retrieve,
        )
        self.update = to_raw_response_wrapper(
            product_collections.update,
        )
        self.list = to_raw_response_wrapper(
            product_collections.list,
        )
        self.delete = to_raw_response_wrapper(
            product_collections.delete,
        )
        self.unarchive = to_raw_response_wrapper(
            product_collections.unarchive,
        )
        self.update_images = to_raw_response_wrapper(
            product_collections.update_images,
        )

    @cached_property
    def groups(self) -> GroupsResourceWithRawResponse:
        return GroupsResourceWithRawResponse(self._product_collections.groups)


class AsyncProductCollectionsResourceWithRawResponse:
    def __init__(self, product_collections: AsyncProductCollectionsResource) -> None:
        self._product_collections = product_collections

        self.create = async_to_raw_response_wrapper(
            product_collections.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            product_collections.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            product_collections.update,
        )
        self.list = async_to_raw_response_wrapper(
            product_collections.list,
        )
        self.delete = async_to_raw_response_wrapper(
            product_collections.delete,
        )
        self.unarchive = async_to_raw_response_wrapper(
            product_collections.unarchive,
        )
        self.update_images = async_to_raw_response_wrapper(
            product_collections.update_images,
        )

    @cached_property
    def groups(self) -> AsyncGroupsResourceWithRawResponse:
        return AsyncGroupsResourceWithRawResponse(self._product_collections.groups)


class ProductCollectionsResourceWithStreamingResponse:
    def __init__(self, product_collections: ProductCollectionsResource) -> None:
        self._product_collections = product_collections

        self.create = to_streamed_response_wrapper(
            product_collections.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            product_collections.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            product_collections.update,
        )
        self.list = to_streamed_response_wrapper(
            product_collections.list,
        )
        self.delete = to_streamed_response_wrapper(
            product_collections.delete,
        )
        self.unarchive = to_streamed_response_wrapper(
            product_collections.unarchive,
        )
        self.update_images = to_streamed_response_wrapper(
            product_collections.update_images,
        )

    @cached_property
    def groups(self) -> GroupsResourceWithStreamingResponse:
        return GroupsResourceWithStreamingResponse(self._product_collections.groups)


class AsyncProductCollectionsResourceWithStreamingResponse:
    def __init__(self, product_collections: AsyncProductCollectionsResource) -> None:
        self._product_collections = product_collections

        self.create = async_to_streamed_response_wrapper(
            product_collections.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            product_collections.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            product_collections.update,
        )
        self.list = async_to_streamed_response_wrapper(
            product_collections.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            product_collections.delete,
        )
        self.unarchive = async_to_streamed_response_wrapper(
            product_collections.unarchive,
        )
        self.update_images = async_to_streamed_response_wrapper(
            product_collections.update_images,
        )

    @cached_property
    def groups(self) -> AsyncGroupsResourceWithStreamingResponse:
        return AsyncGroupsResourceWithStreamingResponse(self._product_collections.groups)
