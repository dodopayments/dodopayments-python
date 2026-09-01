# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .customers.customers import (
    CustomersResource,
    AsyncCustomersResource,
    CustomersResourceWithRawResponse,
    AsyncCustomersResourceWithRawResponse,
    CustomersResourceWithStreamingResponse,
    AsyncCustomersResourceWithStreamingResponse,
)

__all__ = ["BlocklistResource", "AsyncBlocklistResource"]


class BlocklistResource(SyncAPIResource):
    @cached_property
    def customers(self) -> CustomersResource:
        return CustomersResource(self._client)

    @cached_property
    def with_raw_response(self) -> BlocklistResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return BlocklistResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BlocklistResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return BlocklistResourceWithStreamingResponse(self)


class AsyncBlocklistResource(AsyncAPIResource):
    @cached_property
    def customers(self) -> AsyncCustomersResource:
        return AsyncCustomersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBlocklistResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBlocklistResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBlocklistResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return AsyncBlocklistResourceWithStreamingResponse(self)


class BlocklistResourceWithRawResponse:
    def __init__(self, blocklist: BlocklistResource) -> None:
        self._blocklist = blocklist

    @cached_property
    def customers(self) -> CustomersResourceWithRawResponse:
        return CustomersResourceWithRawResponse(self._blocklist.customers)


class AsyncBlocklistResourceWithRawResponse:
    def __init__(self, blocklist: AsyncBlocklistResource) -> None:
        self._blocklist = blocklist

    @cached_property
    def customers(self) -> AsyncCustomersResourceWithRawResponse:
        return AsyncCustomersResourceWithRawResponse(self._blocklist.customers)


class BlocklistResourceWithStreamingResponse:
    def __init__(self, blocklist: BlocklistResource) -> None:
        self._blocklist = blocklist

    @cached_property
    def customers(self) -> CustomersResourceWithStreamingResponse:
        return CustomersResourceWithStreamingResponse(self._blocklist.customers)


class AsyncBlocklistResourceWithStreamingResponse:
    def __init__(self, blocklist: AsyncBlocklistResource) -> None:
        self._blocklist = blocklist

    @cached_property
    def customers(self) -> AsyncCustomersResourceWithStreamingResponse:
        return AsyncCustomersResourceWithStreamingResponse(self._blocklist.customers)
