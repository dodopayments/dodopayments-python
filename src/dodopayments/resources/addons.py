# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import Currency, TaxCategory, addon_list_params, addon_create_params, addon_update_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.currency import Currency
from ..types.tax_category import TaxCategory
from ..types.addon_response import AddonResponse
from ..types.addon_update_images_response import AddonUpdateImagesResponse

__all__ = ["AddonsResource", "AsyncAddonsResource"]


class AddonsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AddonsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return AddonsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AddonsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return AddonsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        currency: Currency,
        name: str,
        price: int,
        tax_category: TaxCategory,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AddonResponse:
        """
        Args:
          currency: The currency of the Addon

          name: Name of the Addon

          price: Amount of the addon

          tax_category: Tax category applied to this Addon

          description: Optional description of the Addon

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/addons",
            body=maybe_transform(
                {
                    "currency": currency,
                    "name": name,
                    "price": price,
                    "tax_category": tax_category,
                    "description": description,
                },
                addon_create_params.AddonCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddonResponse,
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
    ) -> AddonResponse:
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
            f"/addons/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddonResponse,
        )

    def update(
        self,
        id: str,
        *,
        currency: Optional[Currency] | Omit = omit,
        description: Optional[str] | Omit = omit,
        image_id: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        price: Optional[int] | Omit = omit,
        tax_category: Optional[TaxCategory] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AddonResponse:
        """
        Args:
          currency: The currency of the Addon

          description: Description of the Addon, optional and must be at most 1000 characters.

          image_id: Addon image id after its uploaded to S3

          name: Name of the Addon, optional and must be at most 100 characters.

          price: Amount of the addon

          tax_category: Tax category of the Addon.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/addons/{id}",
            body=maybe_transform(
                {
                    "currency": currency,
                    "description": description,
                    "image_id": image_id,
                    "name": name,
                    "price": price,
                    "tax_category": tax_category,
                },
                addon_update_params.AddonUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddonResponse,
        )

    def list(
        self,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultPageNumberPagination[AddonResponse]:
        """
        Args:
          page_number: Page number default is 0

          page_size: Page size default is 10 max is 100

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/addons",
            page=SyncDefaultPageNumberPagination[AddonResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    addon_list_params.AddonListParams,
                ),
            ),
            model=AddonResponse,
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
    ) -> AddonUpdateImagesResponse:
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
            f"/addons/{id}/images",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddonUpdateImagesResponse,
        )


class AsyncAddonsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAddonsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAddonsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAddonsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return AsyncAddonsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        currency: Currency,
        name: str,
        price: int,
        tax_category: TaxCategory,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AddonResponse:
        """
        Args:
          currency: The currency of the Addon

          name: Name of the Addon

          price: Amount of the addon

          tax_category: Tax category applied to this Addon

          description: Optional description of the Addon

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/addons",
            body=await async_maybe_transform(
                {
                    "currency": currency,
                    "name": name,
                    "price": price,
                    "tax_category": tax_category,
                    "description": description,
                },
                addon_create_params.AddonCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddonResponse,
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
    ) -> AddonResponse:
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
            f"/addons/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddonResponse,
        )

    async def update(
        self,
        id: str,
        *,
        currency: Optional[Currency] | Omit = omit,
        description: Optional[str] | Omit = omit,
        image_id: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        price: Optional[int] | Omit = omit,
        tax_category: Optional[TaxCategory] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AddonResponse:
        """
        Args:
          currency: The currency of the Addon

          description: Description of the Addon, optional and must be at most 1000 characters.

          image_id: Addon image id after its uploaded to S3

          name: Name of the Addon, optional and must be at most 100 characters.

          price: Amount of the addon

          tax_category: Tax category of the Addon.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/addons/{id}",
            body=await async_maybe_transform(
                {
                    "currency": currency,
                    "description": description,
                    "image_id": image_id,
                    "name": name,
                    "price": price,
                    "tax_category": tax_category,
                },
                addon_update_params.AddonUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddonResponse,
        )

    def list(
        self,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AddonResponse, AsyncDefaultPageNumberPagination[AddonResponse]]:
        """
        Args:
          page_number: Page number default is 0

          page_size: Page size default is 10 max is 100

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/addons",
            page=AsyncDefaultPageNumberPagination[AddonResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    addon_list_params.AddonListParams,
                ),
            ),
            model=AddonResponse,
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
    ) -> AddonUpdateImagesResponse:
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
            f"/addons/{id}/images",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddonUpdateImagesResponse,
        )


class AddonsResourceWithRawResponse:
    def __init__(self, addons: AddonsResource) -> None:
        self._addons = addons

        self.create = to_raw_response_wrapper(
            addons.create,
        )
        self.retrieve = to_raw_response_wrapper(
            addons.retrieve,
        )
        self.update = to_raw_response_wrapper(
            addons.update,
        )
        self.list = to_raw_response_wrapper(
            addons.list,
        )
        self.update_images = to_raw_response_wrapper(
            addons.update_images,
        )


class AsyncAddonsResourceWithRawResponse:
    def __init__(self, addons: AsyncAddonsResource) -> None:
        self._addons = addons

        self.create = async_to_raw_response_wrapper(
            addons.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            addons.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            addons.update,
        )
        self.list = async_to_raw_response_wrapper(
            addons.list,
        )
        self.update_images = async_to_raw_response_wrapper(
            addons.update_images,
        )


class AddonsResourceWithStreamingResponse:
    def __init__(self, addons: AddonsResource) -> None:
        self._addons = addons

        self.create = to_streamed_response_wrapper(
            addons.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            addons.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            addons.update,
        )
        self.list = to_streamed_response_wrapper(
            addons.list,
        )
        self.update_images = to_streamed_response_wrapper(
            addons.update_images,
        )


class AsyncAddonsResourceWithStreamingResponse:
    def __init__(self, addons: AsyncAddonsResource) -> None:
        self._addons = addons

        self.create = async_to_streamed_response_wrapper(
            addons.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            addons.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            addons.update,
        )
        self.list = async_to_streamed_response_wrapper(
            addons.list,
        )
        self.update_images = async_to_streamed_response_wrapper(
            addons.update_images,
        )
