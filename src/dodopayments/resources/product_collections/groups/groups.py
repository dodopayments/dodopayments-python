# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from .items import (
    ItemsResource,
    AsyncItemsResource,
    ItemsResourceWithRawResponse,
    AsyncItemsResourceWithRawResponse,
    ItemsResourceWithStreamingResponse,
    AsyncItemsResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.product_collections import group_create_params, group_update_params
from ....types.product_collections.group_create_response import GroupCreateResponse

__all__ = ["GroupsResource", "AsyncGroupsResource"]


class GroupsResource(SyncAPIResource):
    @cached_property
    def items(self) -> ItemsResource:
        return ItemsResource(self._client)

    @cached_property
    def with_raw_response(self) -> GroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return GroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return GroupsResourceWithStreamingResponse(self)

    def create(
        self,
        id: str,
        *,
        products: Iterable[group_create_params.Product],
        group_name: Optional[str] | Omit = omit,
        status: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GroupCreateResponse:
        """Args:
          products: Products in this group

          group_name: Optional group name.

        Multiple groups can have null names, but named groups must
              be unique per collection

          status: Status of the group (defaults to true if not provided)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/product-collections/{id}/groups", id=id),
            body=maybe_transform(
                {
                    "products": products,
                    "group_name": group_name,
                    "status": status,
                },
                group_create_params.GroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroupCreateResponse,
        )

    def update(
        self,
        group_id: str,
        *,
        id: str,
        group_name: Optional[str] | Omit = omit,
        product_order: Optional[SequenceNotStr[str]] | Omit = omit,
        status: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          group_name: Optional group name update: Some(Some(name)) = set name, Some(None) = clear
              name, None = no change

          product_order: Optional new order for products in this group (array of
              product_collection_group_pdts UUIDs)

          status: Optional status update

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._patch(
            path_template("/product-collections/{id}/groups/{group_id}", id=id, group_id=group_id),
            body=maybe_transform(
                {
                    "group_name": group_name,
                    "product_order": product_order,
                    "status": status,
                },
                group_update_params.GroupUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def delete(
        self,
        group_id: str,
        *,
        id: str,
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
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/product-collections/{id}/groups/{group_id}", id=id, group_id=group_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncGroupsResource(AsyncAPIResource):
    @cached_property
    def items(self) -> AsyncItemsResource:
        return AsyncItemsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return AsyncGroupsResourceWithStreamingResponse(self)

    async def create(
        self,
        id: str,
        *,
        products: Iterable[group_create_params.Product],
        group_name: Optional[str] | Omit = omit,
        status: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GroupCreateResponse:
        """Args:
          products: Products in this group

          group_name: Optional group name.

        Multiple groups can have null names, but named groups must
              be unique per collection

          status: Status of the group (defaults to true if not provided)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/product-collections/{id}/groups", id=id),
            body=await async_maybe_transform(
                {
                    "products": products,
                    "group_name": group_name,
                    "status": status,
                },
                group_create_params.GroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroupCreateResponse,
        )

    async def update(
        self,
        group_id: str,
        *,
        id: str,
        group_name: Optional[str] | Omit = omit,
        product_order: Optional[SequenceNotStr[str]] | Omit = omit,
        status: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          group_name: Optional group name update: Some(Some(name)) = set name, Some(None) = clear
              name, None = no change

          product_order: Optional new order for products in this group (array of
              product_collection_group_pdts UUIDs)

          status: Optional status update

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._patch(
            path_template("/product-collections/{id}/groups/{group_id}", id=id, group_id=group_id),
            body=await async_maybe_transform(
                {
                    "group_name": group_name,
                    "product_order": product_order,
                    "status": status,
                },
                group_update_params.GroupUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def delete(
        self,
        group_id: str,
        *,
        id: str,
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
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/product-collections/{id}/groups/{group_id}", id=id, group_id=group_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class GroupsResourceWithRawResponse:
    def __init__(self, groups: GroupsResource) -> None:
        self._groups = groups

        self.create = to_raw_response_wrapper(
            groups.create,
        )
        self.update = to_raw_response_wrapper(
            groups.update,
        )
        self.delete = to_raw_response_wrapper(
            groups.delete,
        )

    @cached_property
    def items(self) -> ItemsResourceWithRawResponse:
        return ItemsResourceWithRawResponse(self._groups.items)


class AsyncGroupsResourceWithRawResponse:
    def __init__(self, groups: AsyncGroupsResource) -> None:
        self._groups = groups

        self.create = async_to_raw_response_wrapper(
            groups.create,
        )
        self.update = async_to_raw_response_wrapper(
            groups.update,
        )
        self.delete = async_to_raw_response_wrapper(
            groups.delete,
        )

    @cached_property
    def items(self) -> AsyncItemsResourceWithRawResponse:
        return AsyncItemsResourceWithRawResponse(self._groups.items)


class GroupsResourceWithStreamingResponse:
    def __init__(self, groups: GroupsResource) -> None:
        self._groups = groups

        self.create = to_streamed_response_wrapper(
            groups.create,
        )
        self.update = to_streamed_response_wrapper(
            groups.update,
        )
        self.delete = to_streamed_response_wrapper(
            groups.delete,
        )

    @cached_property
    def items(self) -> ItemsResourceWithStreamingResponse:
        return ItemsResourceWithStreamingResponse(self._groups.items)


class AsyncGroupsResourceWithStreamingResponse:
    def __init__(self, groups: AsyncGroupsResource) -> None:
        self._groups = groups

        self.create = async_to_streamed_response_wrapper(
            groups.create,
        )
        self.update = async_to_streamed_response_wrapper(
            groups.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            groups.delete,
        )

    @cached_property
    def items(self) -> AsyncItemsResourceWithStreamingResponse:
        return AsyncItemsResourceWithStreamingResponse(self._groups.items)
