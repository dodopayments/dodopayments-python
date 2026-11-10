# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...types import (
    Currency,
    CollectionMethod,
    invoice_list_params,
    invoice_create_params,
    invoice_update_params,
    invoice_preview_params,
    invoice_add_note_params,
    invoice_finalize_params,
    invoice_update_dunning_params,
    invoice_preview_existing_params,
)
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
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
from ..._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from ...pagination import SyncDefaultPageNumberPagination, AsyncDefaultPageNumberPagination
from ..._base_client import AsyncPaginator, make_request_options
from ...types.invoice import Invoice
from ...types.currency import Currency
from ...types.metadata_param import MetadataParam
from ...types.collection_method import CollectionMethod
from ...types.invoice_list_events_response import InvoiceListEventsResponse
from ...types.invoice_create_hosted_link_response import InvoiceCreateHostedLinkResponse

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

    def create(
        self,
        *,
        collection_method: CollectionMethod,
        currency: Currency,
        customer_id: str,
        items: Iterable[invoice_create_params.Item],
        billing_address: Optional[invoice_create_params.BillingAddress] | Omit = omit,
        cc_emails: Optional[SequenceNotStr[str]] | Omit = omit,
        customer_email: Optional[str] | Omit = omit,
        discount_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        due_at: Union[str, datetime, None] | Omit = omit,
        dunning: Optional[invoice_create_params.Dunning] | Omit = omit,
        memo: Optional[str] | Omit = omit,
        metadata: MetadataParam | Omit = omit,
        payment_terms: Optional[invoice_create_params.PaymentTerms] | Omit = omit,
        review_required: bool | Omit = omit,
        tax_id: Optional[str] | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Invoice:
        """Creates a draft.

        A repeat with the same `Idempotency-Key` returns the first
        draft.

        Args:
          items: 1 to 50 items.

          billing_address: The billing address of an invoice request.

          cc_emails: 10 addresses or fewer.

          customer_email: The customer email is used when this is not set.

          discount_ids: 20 codes or fewer.

          due_at: A custom due date. Do not send it with `payment_terms`.

          dunning: The reminder override of one invoice. The business settings fill the other
              dunning values.

          metadata: Arbitrary key-value metadata. Values can be string, integer, number, or boolean.

          payment_terms: Do not send it with `due_at`.

          review_required: `true` keeps a renewal draft for review before it finalises.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            "/billing/invoices",
            body=maybe_transform(
                {
                    "collection_method": collection_method,
                    "currency": currency,
                    "customer_id": customer_id,
                    "items": items,
                    "billing_address": billing_address,
                    "cc_emails": cc_emails,
                    "customer_email": customer_email,
                    "discount_ids": discount_ids,
                    "due_at": due_at,
                    "dunning": dunning,
                    "memo": memo,
                    "metadata": metadata,
                    "payment_terms": payment_terms,
                    "review_required": review_required,
                    "tax_id": tax_id,
                },
                invoice_create_params.InvoiceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Invoice,
        )

    def retrieve(
        self,
        invoice_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Invoice:
        """
        Get an invoice

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        return self._get(
            path_template("/billing/invoices/{invoice_id}", invoice_id=invoice_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Invoice,
        )

    def update(
        self,
        invoice_id: str,
        *,
        if_match: str,
        billing_address: Optional[invoice_update_params.BillingAddress] | Omit = omit,
        cc_emails: Optional[SequenceNotStr[str]] | Omit = omit,
        collection_method: Optional[CollectionMethod] | Omit = omit,
        currency: Optional[Currency] | Omit = omit,
        customer_email: Optional[str] | Omit = omit,
        customer_id: Optional[str] | Omit = omit,
        discount_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        due_at: Union[str, datetime, None] | Omit = omit,
        dunning: Optional[invoice_update_params.Dunning] | Omit = omit,
        items: Optional[Iterable[invoice_update_params.Item]] | Omit = omit,
        memo: Optional[str] | Omit = omit,
        metadata: Optional[MetadataParam] | Omit = omit,
        payment_terms: Optional[invoice_update_params.PaymentTerms] | Omit = omit,
        review_required: Optional[bool] | Omit = omit,
        tax_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Invoice:
        """Changes only the sent fields.

        `null` clears a field that can be empty.

        Args:
          billing_address: The billing address of an invoice request.

          cc_emails: 10 addresses or fewer.

          discount_ids: 20 codes or fewer.

          dunning: The reminder override of one invoice. The business settings fill the other
              dunning values.

          items: 1 to 50 items.

          metadata: Arbitrary key-value metadata. Values can be string, integer, number, or boolean.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        extra_headers = {"If-Match": if_match, **(extra_headers or {})}
        return self._patch(
            path_template("/billing/invoices/{invoice_id}", invoice_id=invoice_id),
            body=maybe_transform(
                {
                    "billing_address": billing_address,
                    "cc_emails": cc_emails,
                    "collection_method": collection_method,
                    "currency": currency,
                    "customer_email": customer_email,
                    "customer_id": customer_id,
                    "discount_ids": discount_ids,
                    "due_at": due_at,
                    "dunning": dunning,
                    "items": items,
                    "memo": memo,
                    "metadata": metadata,
                    "payment_terms": payment_terms,
                    "review_required": review_required,
                    "tax_id": tax_id,
                },
                invoice_update_params.InvoiceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Invoice,
        )

    def list(
        self,
        *,
        collection_method: Literal["auto_charge", "manual"] | Omit = omit,
        created_at_gte: Union[str, datetime] | Omit = omit,
        created_at_lte: Union[str, datetime] | Omit = omit,
        customer_id: str | Omit = omit,
        due_at_gte: Union[str, datetime] | Omit = omit,
        due_at_lte: Union[str, datetime] | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        status: List[Literal["open", "paid", "void", "draft", "past_due", "uncollectable"]] | Omit = omit,
        subscription_id: str | Omit = omit,
        tags: List[Literal["refunded", "partially_refunded", "disputed", "payment_reversed"]] | Omit = omit,
        total_amount_gte: int | Omit = omit,
        total_amount_lte: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultPageNumberPagination[Invoice]:
        """Lists invoice-led invoices, newest first.

        The items have no `lines` and no
        `payments`.

        Args:
          page_number: Page number. The default is 0.

          page_size: Page size. The default is 10 and the maximum is 100.

          status: Repeat the key to match more than one status, for example
              `status=open&status=past_due`.

          tags: Repeat the key to match an invoice that has any one of the tags.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/billing/invoices",
            page=SyncDefaultPageNumberPagination[Invoice],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "collection_method": collection_method,
                        "created_at_gte": created_at_gte,
                        "created_at_lte": created_at_lte,
                        "customer_id": customer_id,
                        "due_at_gte": due_at_gte,
                        "due_at_lte": due_at_lte,
                        "page_number": page_number,
                        "page_size": page_size,
                        "status": status,
                        "subscription_id": subscription_id,
                        "tags": tags,
                        "total_amount_gte": total_amount_gte,
                        "total_amount_lte": total_amount_lte,
                    },
                    invoice_list_params.InvoiceListParams,
                ),
            ),
            model=Invoice,
        )

    def delete(
        self,
        invoice_id: str,
        *,
        if_match: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a draft invoice

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers.update({"If-Match": if_match})
        return self._delete(
            path_template("/billing/invoices/{invoice_id}", invoice_id=invoice_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def add_note(
        self,
        invoice_id: str,
        *,
        text: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Invoice:
        """A note changes no field, so it needs no `If-Match`.

        The note shows in `/events`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        return self._post(
            path_template("/billing/invoices/{invoice_id}/notes", invoice_id=invoice_id),
            body=maybe_transform({"text": text}, invoice_add_note_params.InvoiceAddNoteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Invoice,
        )

    def create_hosted_link(
        self,
        invoice_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvoiceCreateHostedLinkResponse:
        """Returns the page where the customer pays.

        A copied link counts as a send, so the
        first call sets `sent_at`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        return self._post(
            path_template("/billing/invoices/{invoice_id}/hosted-link", invoice_id=invoice_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvoiceCreateHostedLinkResponse,
        )

    def duplicate(
        self,
        invoice_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Invoice:
        """
        Copies the customer, the product lines, the terms and the recipients into a new
        draft. Usage lines are not copied.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        return self._post(
            path_template("/billing/invoices/{invoice_id}/duplicate", invoice_id=invoice_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Invoice,
        )

    def finalize(
        self,
        invoice_id: str,
        *,
        if_match: str,
        cc_emails: Optional[SequenceNotStr[str]] | Omit = omit,
        customer_email: Optional[str] | Omit = omit,
        send: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Invoice:
        """Issues the draft.

        With `send: true`, the invoice email goes out after the issue.
        A failed send keeps the invoice issued. Call `/send` again with the new `ETag`.

        Args:
          cc_emails: 10 addresses or fewer.

          send: `true` sends the invoice email after finalise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        extra_headers = {"If-Match": if_match, **(extra_headers or {})}
        return self._post(
            path_template("/billing/invoices/{invoice_id}/finalize", invoice_id=invoice_id),
            body=maybe_transform(
                {
                    "cc_emails": cc_emails,
                    "customer_email": customer_email,
                    "send": send,
                },
                invoice_finalize_params.InvoiceFinalizeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Invoice,
        )

    def list_events(
        self,
        invoice_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvoiceListEventsResponse:
        """
        Returns the change history of the invoice, oldest first.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        return self._get(
            path_template("/billing/invoices/{invoice_id}/events", invoice_id=invoice_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvoiceListEventsResponse,
        )

    def mark_uncollectable(
        self,
        invoice_id: str,
        *,
        if_match: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Invoice:
        """
        Mark an invoice uncollectable

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        extra_headers = {"If-Match": if_match, **(extra_headers or {})}
        return self._post(
            path_template("/billing/invoices/{invoice_id}/mark-uncollectable", invoice_id=invoice_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Invoice,
        )

    def preview(
        self,
        *,
        collection_method: CollectionMethod,
        currency: Currency,
        customer_id: str,
        items: Iterable[invoice_preview_params.Item],
        format: Literal["json", "pdf", "email"] | Omit = omit,
        billing_address: Optional[invoice_preview_params.BillingAddress] | Omit = omit,
        cc_emails: Optional[SequenceNotStr[str]] | Omit = omit,
        customer_email: Optional[str] | Omit = omit,
        discount_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        due_at: Union[str, datetime, None] | Omit = omit,
        dunning: Optional[invoice_preview_params.Dunning] | Omit = omit,
        memo: Optional[str] | Omit = omit,
        metadata: MetadataParam | Omit = omit,
        payment_terms: Optional[invoice_preview_params.PaymentTerms] | Omit = omit,
        review_required: bool | Omit = omit,
        tax_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """Prices the body as a draft and returns it.

        No row is saved.

        Args:
          items: 1 to 50 items.

          format: The preview body. `json` returns the invoice JSON. `pdf` returns the PDF with a
              draft mark. `email` returns the HTML of the invoice email. A preview saves no
              row.

          billing_address: The billing address of an invoice request.

          cc_emails: 10 addresses or fewer.

          customer_email: The customer email is used when this is not set.

          discount_ids: 20 codes or fewer.

          due_at: A custom due date. Do not send it with `payment_terms`.

          dunning: The reminder override of one invoice. The business settings fill the other
              dunning values.

          metadata: Arbitrary key-value metadata. Values can be string, integer, number, or boolean.

          payment_terms: Do not send it with `due_at`.

          review_required: `true` keeps a renewal draft for review before it finalises.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/pdf", **(extra_headers or {})}
        return self._post(
            "/billing/invoices/preview",
            body=maybe_transform(
                {
                    "collection_method": collection_method,
                    "currency": currency,
                    "customer_id": customer_id,
                    "items": items,
                    "billing_address": billing_address,
                    "cc_emails": cc_emails,
                    "customer_email": customer_email,
                    "discount_ids": discount_ids,
                    "due_at": due_at,
                    "dunning": dunning,
                    "memo": memo,
                    "metadata": metadata,
                    "payment_terms": payment_terms,
                    "review_required": review_required,
                    "tax_id": tax_id,
                },
                invoice_preview_params.InvoicePreviewParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"format": format}, invoice_preview_params.InvoicePreviewParams),
            ),
            cast_to=BinaryAPIResponse,
        )

    def preview_existing(
        self,
        invoice_id: str,
        *,
        format: Literal["json", "pdf", "email"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """Preview a draft invoice

        Args:
          format: The preview body.

        `json` returns the invoice JSON. `pdf` returns the PDF with a
              draft mark. `email` returns the HTML of the invoice email. A preview saves no
              row.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        extra_headers = {"Accept": "application/pdf", **(extra_headers or {})}
        return self._get(
            path_template("/billing/invoices/{invoice_id}/preview", invoice_id=invoice_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"format": format}, invoice_preview_existing_params.InvoicePreviewExistingParams),
            ),
            cast_to=BinaryAPIResponse,
        )

    def retry(
        self,
        invoice_id: str,
        *,
        if_match: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Invoice:
        """
        Charges the saved payment method of the invoice subscription now.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        extra_headers = {"If-Match": if_match, **(extra_headers or {})}
        return self._post(
            path_template("/billing/invoices/{invoice_id}/retry", invoice_id=invoice_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Invoice,
        )

    def send(
        self,
        invoice_id: str,
        *,
        if_match: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Invoice:
        """
        Emails the invoice to the customer email and the CC emails.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        extra_headers = {"If-Match": if_match, **(extra_headers or {})}
        return self._post(
            path_template("/billing/invoices/{invoice_id}/send", invoice_id=invoice_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Invoice,
        )

    def update_dunning(
        self,
        invoice_id: str,
        *,
        action: Literal["pause", "resume", "reschedule"],
        if_match: str,
        offsets_days: Optional[Iterable[int]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Invoice:
        """
        Pauses, resumes or moves the reminders of an open or past-due invoice.

        Args:
          offsets_days: Needed for `reschedule`. Days from the due date.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        extra_headers = {"If-Match": if_match, **(extra_headers or {})}
        return self._post(
            path_template("/billing/invoices/{invoice_id}/dunning", invoice_id=invoice_id),
            body=maybe_transform(
                {
                    "action": action,
                    "offsets_days": offsets_days,
                },
                invoice_update_dunning_params.InvoiceUpdateDunningParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Invoice,
        )

    def void(
        self,
        invoice_id: str,
        *,
        if_match: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Invoice:
        """Closes an open or past-due invoice.

        Applied credits go back to the customer
        wallet.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        extra_headers = {"If-Match": if_match, **(extra_headers or {})}
        return self._post(
            path_template("/billing/invoices/{invoice_id}/void", invoice_id=invoice_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Invoice,
        )


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

    async def create(
        self,
        *,
        collection_method: CollectionMethod,
        currency: Currency,
        customer_id: str,
        items: Iterable[invoice_create_params.Item],
        billing_address: Optional[invoice_create_params.BillingAddress] | Omit = omit,
        cc_emails: Optional[SequenceNotStr[str]] | Omit = omit,
        customer_email: Optional[str] | Omit = omit,
        discount_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        due_at: Union[str, datetime, None] | Omit = omit,
        dunning: Optional[invoice_create_params.Dunning] | Omit = omit,
        memo: Optional[str] | Omit = omit,
        metadata: MetadataParam | Omit = omit,
        payment_terms: Optional[invoice_create_params.PaymentTerms] | Omit = omit,
        review_required: bool | Omit = omit,
        tax_id: Optional[str] | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Invoice:
        """Creates a draft.

        A repeat with the same `Idempotency-Key` returns the first
        draft.

        Args:
          items: 1 to 50 items.

          billing_address: The billing address of an invoice request.

          cc_emails: 10 addresses or fewer.

          customer_email: The customer email is used when this is not set.

          discount_ids: 20 codes or fewer.

          due_at: A custom due date. Do not send it with `payment_terms`.

          dunning: The reminder override of one invoice. The business settings fill the other
              dunning values.

          metadata: Arbitrary key-value metadata. Values can be string, integer, number, or boolean.

          payment_terms: Do not send it with `due_at`.

          review_required: `true` keeps a renewal draft for review before it finalises.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            "/billing/invoices",
            body=await async_maybe_transform(
                {
                    "collection_method": collection_method,
                    "currency": currency,
                    "customer_id": customer_id,
                    "items": items,
                    "billing_address": billing_address,
                    "cc_emails": cc_emails,
                    "customer_email": customer_email,
                    "discount_ids": discount_ids,
                    "due_at": due_at,
                    "dunning": dunning,
                    "memo": memo,
                    "metadata": metadata,
                    "payment_terms": payment_terms,
                    "review_required": review_required,
                    "tax_id": tax_id,
                },
                invoice_create_params.InvoiceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Invoice,
        )

    async def retrieve(
        self,
        invoice_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Invoice:
        """
        Get an invoice

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        return await self._get(
            path_template("/billing/invoices/{invoice_id}", invoice_id=invoice_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Invoice,
        )

    async def update(
        self,
        invoice_id: str,
        *,
        if_match: str,
        billing_address: Optional[invoice_update_params.BillingAddress] | Omit = omit,
        cc_emails: Optional[SequenceNotStr[str]] | Omit = omit,
        collection_method: Optional[CollectionMethod] | Omit = omit,
        currency: Optional[Currency] | Omit = omit,
        customer_email: Optional[str] | Omit = omit,
        customer_id: Optional[str] | Omit = omit,
        discount_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        due_at: Union[str, datetime, None] | Omit = omit,
        dunning: Optional[invoice_update_params.Dunning] | Omit = omit,
        items: Optional[Iterable[invoice_update_params.Item]] | Omit = omit,
        memo: Optional[str] | Omit = omit,
        metadata: Optional[MetadataParam] | Omit = omit,
        payment_terms: Optional[invoice_update_params.PaymentTerms] | Omit = omit,
        review_required: Optional[bool] | Omit = omit,
        tax_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Invoice:
        """Changes only the sent fields.

        `null` clears a field that can be empty.

        Args:
          billing_address: The billing address of an invoice request.

          cc_emails: 10 addresses or fewer.

          discount_ids: 20 codes or fewer.

          dunning: The reminder override of one invoice. The business settings fill the other
              dunning values.

          items: 1 to 50 items.

          metadata: Arbitrary key-value metadata. Values can be string, integer, number, or boolean.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        extra_headers = {"If-Match": if_match, **(extra_headers or {})}
        return await self._patch(
            path_template("/billing/invoices/{invoice_id}", invoice_id=invoice_id),
            body=await async_maybe_transform(
                {
                    "billing_address": billing_address,
                    "cc_emails": cc_emails,
                    "collection_method": collection_method,
                    "currency": currency,
                    "customer_email": customer_email,
                    "customer_id": customer_id,
                    "discount_ids": discount_ids,
                    "due_at": due_at,
                    "dunning": dunning,
                    "items": items,
                    "memo": memo,
                    "metadata": metadata,
                    "payment_terms": payment_terms,
                    "review_required": review_required,
                    "tax_id": tax_id,
                },
                invoice_update_params.InvoiceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Invoice,
        )

    def list(
        self,
        *,
        collection_method: Literal["auto_charge", "manual"] | Omit = omit,
        created_at_gte: Union[str, datetime] | Omit = omit,
        created_at_lte: Union[str, datetime] | Omit = omit,
        customer_id: str | Omit = omit,
        due_at_gte: Union[str, datetime] | Omit = omit,
        due_at_lte: Union[str, datetime] | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        status: List[Literal["open", "paid", "void", "draft", "past_due", "uncollectable"]] | Omit = omit,
        subscription_id: str | Omit = omit,
        tags: List[Literal["refunded", "partially_refunded", "disputed", "payment_reversed"]] | Omit = omit,
        total_amount_gte: int | Omit = omit,
        total_amount_lte: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Invoice, AsyncDefaultPageNumberPagination[Invoice]]:
        """Lists invoice-led invoices, newest first.

        The items have no `lines` and no
        `payments`.

        Args:
          page_number: Page number. The default is 0.

          page_size: Page size. The default is 10 and the maximum is 100.

          status: Repeat the key to match more than one status, for example
              `status=open&status=past_due`.

          tags: Repeat the key to match an invoice that has any one of the tags.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/billing/invoices",
            page=AsyncDefaultPageNumberPagination[Invoice],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "collection_method": collection_method,
                        "created_at_gte": created_at_gte,
                        "created_at_lte": created_at_lte,
                        "customer_id": customer_id,
                        "due_at_gte": due_at_gte,
                        "due_at_lte": due_at_lte,
                        "page_number": page_number,
                        "page_size": page_size,
                        "status": status,
                        "subscription_id": subscription_id,
                        "tags": tags,
                        "total_amount_gte": total_amount_gte,
                        "total_amount_lte": total_amount_lte,
                    },
                    invoice_list_params.InvoiceListParams,
                ),
            ),
            model=Invoice,
        )

    async def delete(
        self,
        invoice_id: str,
        *,
        if_match: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a draft invoice

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers.update({"If-Match": if_match})
        return await self._delete(
            path_template("/billing/invoices/{invoice_id}", invoice_id=invoice_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def add_note(
        self,
        invoice_id: str,
        *,
        text: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Invoice:
        """A note changes no field, so it needs no `If-Match`.

        The note shows in `/events`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        return await self._post(
            path_template("/billing/invoices/{invoice_id}/notes", invoice_id=invoice_id),
            body=await async_maybe_transform({"text": text}, invoice_add_note_params.InvoiceAddNoteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Invoice,
        )

    async def create_hosted_link(
        self,
        invoice_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvoiceCreateHostedLinkResponse:
        """Returns the page where the customer pays.

        A copied link counts as a send, so the
        first call sets `sent_at`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        return await self._post(
            path_template("/billing/invoices/{invoice_id}/hosted-link", invoice_id=invoice_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvoiceCreateHostedLinkResponse,
        )

    async def duplicate(
        self,
        invoice_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Invoice:
        """
        Copies the customer, the product lines, the terms and the recipients into a new
        draft. Usage lines are not copied.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        return await self._post(
            path_template("/billing/invoices/{invoice_id}/duplicate", invoice_id=invoice_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Invoice,
        )

    async def finalize(
        self,
        invoice_id: str,
        *,
        if_match: str,
        cc_emails: Optional[SequenceNotStr[str]] | Omit = omit,
        customer_email: Optional[str] | Omit = omit,
        send: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Invoice:
        """Issues the draft.

        With `send: true`, the invoice email goes out after the issue.
        A failed send keeps the invoice issued. Call `/send` again with the new `ETag`.

        Args:
          cc_emails: 10 addresses or fewer.

          send: `true` sends the invoice email after finalise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        extra_headers = {"If-Match": if_match, **(extra_headers or {})}
        return await self._post(
            path_template("/billing/invoices/{invoice_id}/finalize", invoice_id=invoice_id),
            body=await async_maybe_transform(
                {
                    "cc_emails": cc_emails,
                    "customer_email": customer_email,
                    "send": send,
                },
                invoice_finalize_params.InvoiceFinalizeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Invoice,
        )

    async def list_events(
        self,
        invoice_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvoiceListEventsResponse:
        """
        Returns the change history of the invoice, oldest first.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        return await self._get(
            path_template("/billing/invoices/{invoice_id}/events", invoice_id=invoice_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvoiceListEventsResponse,
        )

    async def mark_uncollectable(
        self,
        invoice_id: str,
        *,
        if_match: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Invoice:
        """
        Mark an invoice uncollectable

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        extra_headers = {"If-Match": if_match, **(extra_headers or {})}
        return await self._post(
            path_template("/billing/invoices/{invoice_id}/mark-uncollectable", invoice_id=invoice_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Invoice,
        )

    async def preview(
        self,
        *,
        collection_method: CollectionMethod,
        currency: Currency,
        customer_id: str,
        items: Iterable[invoice_preview_params.Item],
        format: Literal["json", "pdf", "email"] | Omit = omit,
        billing_address: Optional[invoice_preview_params.BillingAddress] | Omit = omit,
        cc_emails: Optional[SequenceNotStr[str]] | Omit = omit,
        customer_email: Optional[str] | Omit = omit,
        discount_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        due_at: Union[str, datetime, None] | Omit = omit,
        dunning: Optional[invoice_preview_params.Dunning] | Omit = omit,
        memo: Optional[str] | Omit = omit,
        metadata: MetadataParam | Omit = omit,
        payment_terms: Optional[invoice_preview_params.PaymentTerms] | Omit = omit,
        review_required: bool | Omit = omit,
        tax_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """Prices the body as a draft and returns it.

        No row is saved.

        Args:
          items: 1 to 50 items.

          format: The preview body. `json` returns the invoice JSON. `pdf` returns the PDF with a
              draft mark. `email` returns the HTML of the invoice email. A preview saves no
              row.

          billing_address: The billing address of an invoice request.

          cc_emails: 10 addresses or fewer.

          customer_email: The customer email is used when this is not set.

          discount_ids: 20 codes or fewer.

          due_at: A custom due date. Do not send it with `payment_terms`.

          dunning: The reminder override of one invoice. The business settings fill the other
              dunning values.

          metadata: Arbitrary key-value metadata. Values can be string, integer, number, or boolean.

          payment_terms: Do not send it with `due_at`.

          review_required: `true` keeps a renewal draft for review before it finalises.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/pdf", **(extra_headers or {})}
        return await self._post(
            "/billing/invoices/preview",
            body=await async_maybe_transform(
                {
                    "collection_method": collection_method,
                    "currency": currency,
                    "customer_id": customer_id,
                    "items": items,
                    "billing_address": billing_address,
                    "cc_emails": cc_emails,
                    "customer_email": customer_email,
                    "discount_ids": discount_ids,
                    "due_at": due_at,
                    "dunning": dunning,
                    "memo": memo,
                    "metadata": metadata,
                    "payment_terms": payment_terms,
                    "review_required": review_required,
                    "tax_id": tax_id,
                },
                invoice_preview_params.InvoicePreviewParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"format": format}, invoice_preview_params.InvoicePreviewParams),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def preview_existing(
        self,
        invoice_id: str,
        *,
        format: Literal["json", "pdf", "email"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """Preview a draft invoice

        Args:
          format: The preview body.

        `json` returns the invoice JSON. `pdf` returns the PDF with a
              draft mark. `email` returns the HTML of the invoice email. A preview saves no
              row.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        extra_headers = {"Accept": "application/pdf", **(extra_headers or {})}
        return await self._get(
            path_template("/billing/invoices/{invoice_id}/preview", invoice_id=invoice_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"format": format}, invoice_preview_existing_params.InvoicePreviewExistingParams
                ),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def retry(
        self,
        invoice_id: str,
        *,
        if_match: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Invoice:
        """
        Charges the saved payment method of the invoice subscription now.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        extra_headers = {"If-Match": if_match, **(extra_headers or {})}
        return await self._post(
            path_template("/billing/invoices/{invoice_id}/retry", invoice_id=invoice_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Invoice,
        )

    async def send(
        self,
        invoice_id: str,
        *,
        if_match: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Invoice:
        """
        Emails the invoice to the customer email and the CC emails.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        extra_headers = {"If-Match": if_match, **(extra_headers or {})}
        return await self._post(
            path_template("/billing/invoices/{invoice_id}/send", invoice_id=invoice_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Invoice,
        )

    async def update_dunning(
        self,
        invoice_id: str,
        *,
        action: Literal["pause", "resume", "reschedule"],
        if_match: str,
        offsets_days: Optional[Iterable[int]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Invoice:
        """
        Pauses, resumes or moves the reminders of an open or past-due invoice.

        Args:
          offsets_days: Needed for `reschedule`. Days from the due date.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        extra_headers = {"If-Match": if_match, **(extra_headers or {})}
        return await self._post(
            path_template("/billing/invoices/{invoice_id}/dunning", invoice_id=invoice_id),
            body=await async_maybe_transform(
                {
                    "action": action,
                    "offsets_days": offsets_days,
                },
                invoice_update_dunning_params.InvoiceUpdateDunningParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Invoice,
        )

    async def void(
        self,
        invoice_id: str,
        *,
        if_match: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Invoice:
        """Closes an open or past-due invoice.

        Applied credits go back to the customer
        wallet.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        extra_headers = {"If-Match": if_match, **(extra_headers or {})}
        return await self._post(
            path_template("/billing/invoices/{invoice_id}/void", invoice_id=invoice_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Invoice,
        )


class InvoicesResourceWithRawResponse:
    def __init__(self, invoices: InvoicesResource) -> None:
        self._invoices = invoices

        self.create = to_raw_response_wrapper(
            invoices.create,
        )
        self.retrieve = to_raw_response_wrapper(
            invoices.retrieve,
        )
        self.update = to_raw_response_wrapper(
            invoices.update,
        )
        self.list = to_raw_response_wrapper(
            invoices.list,
        )
        self.delete = to_raw_response_wrapper(
            invoices.delete,
        )
        self.add_note = to_raw_response_wrapper(
            invoices.add_note,
        )
        self.create_hosted_link = to_raw_response_wrapper(
            invoices.create_hosted_link,
        )
        self.duplicate = to_raw_response_wrapper(
            invoices.duplicate,
        )
        self.finalize = to_raw_response_wrapper(
            invoices.finalize,
        )
        self.list_events = to_raw_response_wrapper(
            invoices.list_events,
        )
        self.mark_uncollectable = to_raw_response_wrapper(
            invoices.mark_uncollectable,
        )
        self.preview = to_custom_raw_response_wrapper(
            invoices.preview,
            BinaryAPIResponse,
        )
        self.preview_existing = to_custom_raw_response_wrapper(
            invoices.preview_existing,
            BinaryAPIResponse,
        )
        self.retry = to_raw_response_wrapper(
            invoices.retry,
        )
        self.send = to_raw_response_wrapper(
            invoices.send,
        )
        self.update_dunning = to_raw_response_wrapper(
            invoices.update_dunning,
        )
        self.void = to_raw_response_wrapper(
            invoices.void,
        )

    @cached_property
    def payments(self) -> PaymentsResourceWithRawResponse:
        return PaymentsResourceWithRawResponse(self._invoices.payments)


class AsyncInvoicesResourceWithRawResponse:
    def __init__(self, invoices: AsyncInvoicesResource) -> None:
        self._invoices = invoices

        self.create = async_to_raw_response_wrapper(
            invoices.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            invoices.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            invoices.update,
        )
        self.list = async_to_raw_response_wrapper(
            invoices.list,
        )
        self.delete = async_to_raw_response_wrapper(
            invoices.delete,
        )
        self.add_note = async_to_raw_response_wrapper(
            invoices.add_note,
        )
        self.create_hosted_link = async_to_raw_response_wrapper(
            invoices.create_hosted_link,
        )
        self.duplicate = async_to_raw_response_wrapper(
            invoices.duplicate,
        )
        self.finalize = async_to_raw_response_wrapper(
            invoices.finalize,
        )
        self.list_events = async_to_raw_response_wrapper(
            invoices.list_events,
        )
        self.mark_uncollectable = async_to_raw_response_wrapper(
            invoices.mark_uncollectable,
        )
        self.preview = async_to_custom_raw_response_wrapper(
            invoices.preview,
            AsyncBinaryAPIResponse,
        )
        self.preview_existing = async_to_custom_raw_response_wrapper(
            invoices.preview_existing,
            AsyncBinaryAPIResponse,
        )
        self.retry = async_to_raw_response_wrapper(
            invoices.retry,
        )
        self.send = async_to_raw_response_wrapper(
            invoices.send,
        )
        self.update_dunning = async_to_raw_response_wrapper(
            invoices.update_dunning,
        )
        self.void = async_to_raw_response_wrapper(
            invoices.void,
        )

    @cached_property
    def payments(self) -> AsyncPaymentsResourceWithRawResponse:
        return AsyncPaymentsResourceWithRawResponse(self._invoices.payments)


class InvoicesResourceWithStreamingResponse:
    def __init__(self, invoices: InvoicesResource) -> None:
        self._invoices = invoices

        self.create = to_streamed_response_wrapper(
            invoices.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            invoices.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            invoices.update,
        )
        self.list = to_streamed_response_wrapper(
            invoices.list,
        )
        self.delete = to_streamed_response_wrapper(
            invoices.delete,
        )
        self.add_note = to_streamed_response_wrapper(
            invoices.add_note,
        )
        self.create_hosted_link = to_streamed_response_wrapper(
            invoices.create_hosted_link,
        )
        self.duplicate = to_streamed_response_wrapper(
            invoices.duplicate,
        )
        self.finalize = to_streamed_response_wrapper(
            invoices.finalize,
        )
        self.list_events = to_streamed_response_wrapper(
            invoices.list_events,
        )
        self.mark_uncollectable = to_streamed_response_wrapper(
            invoices.mark_uncollectable,
        )
        self.preview = to_custom_streamed_response_wrapper(
            invoices.preview,
            StreamedBinaryAPIResponse,
        )
        self.preview_existing = to_custom_streamed_response_wrapper(
            invoices.preview_existing,
            StreamedBinaryAPIResponse,
        )
        self.retry = to_streamed_response_wrapper(
            invoices.retry,
        )
        self.send = to_streamed_response_wrapper(
            invoices.send,
        )
        self.update_dunning = to_streamed_response_wrapper(
            invoices.update_dunning,
        )
        self.void = to_streamed_response_wrapper(
            invoices.void,
        )

    @cached_property
    def payments(self) -> PaymentsResourceWithStreamingResponse:
        return PaymentsResourceWithStreamingResponse(self._invoices.payments)


class AsyncInvoicesResourceWithStreamingResponse:
    def __init__(self, invoices: AsyncInvoicesResource) -> None:
        self._invoices = invoices

        self.create = async_to_streamed_response_wrapper(
            invoices.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            invoices.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            invoices.update,
        )
        self.list = async_to_streamed_response_wrapper(
            invoices.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            invoices.delete,
        )
        self.add_note = async_to_streamed_response_wrapper(
            invoices.add_note,
        )
        self.create_hosted_link = async_to_streamed_response_wrapper(
            invoices.create_hosted_link,
        )
        self.duplicate = async_to_streamed_response_wrapper(
            invoices.duplicate,
        )
        self.finalize = async_to_streamed_response_wrapper(
            invoices.finalize,
        )
        self.list_events = async_to_streamed_response_wrapper(
            invoices.list_events,
        )
        self.mark_uncollectable = async_to_streamed_response_wrapper(
            invoices.mark_uncollectable,
        )
        self.preview = async_to_custom_streamed_response_wrapper(
            invoices.preview,
            AsyncStreamedBinaryAPIResponse,
        )
        self.preview_existing = async_to_custom_streamed_response_wrapper(
            invoices.preview_existing,
            AsyncStreamedBinaryAPIResponse,
        )
        self.retry = async_to_streamed_response_wrapper(
            invoices.retry,
        )
        self.send = async_to_streamed_response_wrapper(
            invoices.send,
        )
        self.update_dunning = async_to_streamed_response_wrapper(
            invoices.update_dunning,
        )
        self.void = async_to_streamed_response_wrapper(
            invoices.void,
        )

    @cached_property
    def payments(self) -> AsyncPaymentsResourceWithStreamingResponse:
        return AsyncPaymentsResourceWithStreamingResponse(self._invoices.payments)
