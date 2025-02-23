# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .session import (
    SessionResource,
    AsyncSessionResource,
    SessionResourceWithRawResponse,
    AsyncSessionResourceWithRawResponse,
    SessionResourceWithStreamingResponse,
    AsyncSessionResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["CustomerPortalResource", "AsyncCustomerPortalResource"]


class CustomerPortalResource(SyncAPIResource):
    @cached_property
    def session(self) -> SessionResource:
        return SessionResource(self._client)

    @cached_property
    def with_raw_response(self) -> CustomerPortalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return CustomerPortalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomerPortalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return CustomerPortalResourceWithStreamingResponse(self)


class AsyncCustomerPortalResource(AsyncAPIResource):
    @cached_property
    def session(self) -> AsyncSessionResource:
        return AsyncSessionResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCustomerPortalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCustomerPortalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomerPortalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return AsyncCustomerPortalResourceWithStreamingResponse(self)


class CustomerPortalResourceWithRawResponse:
    def __init__(self, customer_portal: CustomerPortalResource) -> None:
        self._customer_portal = customer_portal

    @cached_property
    def session(self) -> SessionResourceWithRawResponse:
        return SessionResourceWithRawResponse(self._customer_portal.session)


class AsyncCustomerPortalResourceWithRawResponse:
    def __init__(self, customer_portal: AsyncCustomerPortalResource) -> None:
        self._customer_portal = customer_portal

    @cached_property
    def session(self) -> AsyncSessionResourceWithRawResponse:
        return AsyncSessionResourceWithRawResponse(self._customer_portal.session)


class CustomerPortalResourceWithStreamingResponse:
    def __init__(self, customer_portal: CustomerPortalResource) -> None:
        self._customer_portal = customer_portal

    @cached_property
    def session(self) -> SessionResourceWithStreamingResponse:
        return SessionResourceWithStreamingResponse(self._customer_portal.session)


class AsyncCustomerPortalResourceWithStreamingResponse:
    def __init__(self, customer_portal: AsyncCustomerPortalResource) -> None:
        self._customer_portal = customer_portal

    @cached_property
    def session(self) -> AsyncSessionResourceWithStreamingResponse:
        return AsyncSessionResourceWithStreamingResponse(self._customer_portal.session)
