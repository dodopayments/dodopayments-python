# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import brand_create_params, brand_update_params
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
from .._base_client import make_request_options
from ..types.brand_list_response import BrandListResponse
from ..types.brand_create_response import BrandCreateResponse
from ..types.brand_update_response import BrandUpdateResponse
from ..types.brand_retrieve_response import BrandRetrieveResponse
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
        description: Optional[str] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        statement_descriptor: Optional[str] | NotGiven = NOT_GIVEN,
        support_email: Optional[str] | NotGiven = NOT_GIVEN,
        url: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BrandCreateResponse:
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
            cast_to=BrandCreateResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BrandRetrieveResponse:
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
            f"/brands/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        image_id: Optional[str] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        statement_descriptor: Optional[str] | NotGiven = NOT_GIVEN,
        support_email: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BrandUpdateResponse:
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
            f"/brands/{id}",
            body=maybe_transform(
                {
                    "image_id": image_id,
                    "name": name,
                    "statement_descriptor": statement_descriptor,
                    "support_email": support_email,
                },
                brand_update_params.BrandUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandUpdateResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BrandListResponse:
        return self._get(
            "/brands",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandListResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
            f"/brands/{id}/images",
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
        description: Optional[str] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        statement_descriptor: Optional[str] | NotGiven = NOT_GIVEN,
        support_email: Optional[str] | NotGiven = NOT_GIVEN,
        url: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BrandCreateResponse:
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
            cast_to=BrandCreateResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BrandRetrieveResponse:
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
            f"/brands/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        image_id: Optional[str] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        statement_descriptor: Optional[str] | NotGiven = NOT_GIVEN,
        support_email: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BrandUpdateResponse:
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
            f"/brands/{id}",
            body=await async_maybe_transform(
                {
                    "image_id": image_id,
                    "name": name,
                    "statement_descriptor": statement_descriptor,
                    "support_email": support_email,
                },
                brand_update_params.BrandUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandUpdateResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BrandListResponse:
        return await self._get(
            "/brands",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandListResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
            f"/brands/{id}/images",
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
        self.update_images = async_to_streamed_response_wrapper(
            brands.update_images,
        )
