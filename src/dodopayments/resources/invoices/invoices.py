# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .payments import (
    PaymentsResource,
    AsyncPaymentsResource,
    PaymentsResourceWithRawResponse,
    AsyncPaymentsResourceWithRawResponse,
    PaymentsResourceWithStreamingResponse,
    AsyncPaymentsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["InvoicesResource", "AsyncInvoicesResource"]


class InvoicesResource(SyncAPIResource):
    @cached_property
    def payments(self) -> PaymentsResource:
        return PaymentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> InvoicesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return InvoicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InvoicesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return InvoicesResourceWithStreamingResponse(self)


class AsyncInvoicesResource(AsyncAPIResource):
    @cached_property
    def payments(self) -> AsyncPaymentsResource:
        return AsyncPaymentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncInvoicesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInvoicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInvoicesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dodopayments/dodopayments-python#with_streaming_response
        """
        return AsyncInvoicesResourceWithStreamingResponse(self)


class InvoicesResourceWithRawResponse:
    def __init__(self, invoices: InvoicesResource) -> None:
        self._invoices = invoices

    @cached_property
    def payments(self) -> PaymentsResourceWithRawResponse:
        return PaymentsResourceWithRawResponse(self._invoices.payments)


class AsyncInvoicesResourceWithRawResponse:
    def __init__(self, invoices: AsyncInvoicesResource) -> None:
        self._invoices = invoices

    @cached_property
    def payments(self) -> AsyncPaymentsResourceWithRawResponse:
        return AsyncPaymentsResourceWithRawResponse(self._invoices.payments)


class InvoicesResourceWithStreamingResponse:
    def __init__(self, invoices: InvoicesResource) -> None:
        self._invoices = invoices

    @cached_property
    def payments(self) -> PaymentsResourceWithStreamingResponse:
        return PaymentsResourceWithStreamingResponse(self._invoices.payments)


class AsyncInvoicesResourceWithStreamingResponse:
    def __init__(self, invoices: AsyncInvoicesResource) -> None:
        self._invoices = invoices

    @cached_property
    def payments(self) -> AsyncPaymentsResourceWithStreamingResponse:
        return AsyncPaymentsResourceWithStreamingResponse(self._invoices.payments)
