# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from ..._types import Body, Query, Headers, NoneType, NotGiven, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.webhooks import header_update_params
from ...types.webhooks.header_retrieve_response import HeaderRetrieveResponse

__all__ = ["HeadersResource", "AsyncHeadersResource"]


class HeadersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HeadersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return HeadersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HeadersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return HeadersResourceWithStreamingResponse(self)

    def retrieve(
        self,
        webhook_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HeaderRetrieveResponse:
        """
        Get a webhook by id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not webhook_id:
            raise ValueError(f"Expected a non-empty value for `webhook_id` but received {webhook_id!r}")
        return self._get(
            f"/webhooks/{webhook_id}/headers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HeaderRetrieveResponse,
        )

    def update(
        self,
        webhook_id: str,
        *,
        headers: Dict[str, str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Patch a webhook by id

        Args:
          headers: Object of header-value pair to update or add

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not webhook_id:
            raise ValueError(f"Expected a non-empty value for `webhook_id` but received {webhook_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._patch(
            f"/webhooks/{webhook_id}/headers",
            body=maybe_transform({"headers": headers}, header_update_params.HeaderUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncHeadersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHeadersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return AsyncHeadersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHeadersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return AsyncHeadersResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        webhook_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HeaderRetrieveResponse:
        """
        Get a webhook by id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not webhook_id:
            raise ValueError(f"Expected a non-empty value for `webhook_id` but received {webhook_id!r}")
        return await self._get(
            f"/webhooks/{webhook_id}/headers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HeaderRetrieveResponse,
        )

    async def update(
        self,
        webhook_id: str,
        *,
        headers: Dict[str, str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Patch a webhook by id

        Args:
          headers: Object of header-value pair to update or add

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not webhook_id:
            raise ValueError(f"Expected a non-empty value for `webhook_id` but received {webhook_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._patch(
            f"/webhooks/{webhook_id}/headers",
            body=await async_maybe_transform({"headers": headers}, header_update_params.HeaderUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class HeadersResourceWithRawResponse:
    def __init__(self, headers: HeadersResource) -> None:
        self._headers = headers

        self.retrieve = to_raw_response_wrapper(
            headers.retrieve,
        )
        self.update = to_raw_response_wrapper(
            headers.update,
        )


class AsyncHeadersResourceWithRawResponse:
    def __init__(self, headers: AsyncHeadersResource) -> None:
        self._headers = headers

        self.retrieve = async_to_raw_response_wrapper(
            headers.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            headers.update,
        )


class HeadersResourceWithStreamingResponse:
    def __init__(self, headers: HeadersResource) -> None:
        self._headers = headers

        self.retrieve = to_streamed_response_wrapper(
            headers.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            headers.update,
        )


class AsyncHeadersResourceWithStreamingResponse:
    def __init__(self, headers: AsyncHeadersResource) -> None:
        self._headers = headers

        self.retrieve = async_to_streamed_response_wrapper(
            headers.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            headers.update,
        )
