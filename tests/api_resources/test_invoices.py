# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from dodopayments import DodoPayments, AsyncDodoPayments
from dodopayments.types import (
    Invoice,
    InvoiceListEventsResponse,
    InvoiceCreateHostedLinkResponse,
)
from dodopayments._utils import parse_datetime
from dodopayments.pagination import SyncDefaultPageNumberPagination, AsyncDefaultPageNumberPagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInvoices:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: DodoPayments) -> None:
        invoice = client.invoices.create(
            collection_method="auto_charge",
            currency="AED",
            customer_id="customer_id",
            items=[
                {
                    "description": "description",
                    "kind": "custom",
                    "tax_category": "digital_products",
                    "unit_amount": 0,
                }
            ],
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: DodoPayments) -> None:
        invoice = client.invoices.create(
            collection_method="auto_charge",
            currency="AED",
            customer_id="customer_id",
            items=[
                {
                    "description": "description",
                    "kind": "custom",
                    "tax_category": "digital_products",
                    "unit_amount": 0,
                    "quantity": 0,
                }
            ],
            billing_address={
                "country": "AF",
                "city": "city",
                "state": "state",
                "street": "street",
                "zipcode": "zipcode",
            },
            cc_emails=["string"],
            customer_email="customer_email",
            discount_ids=["string"],
            due_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            dunning={
                "reminders_enabled": True,
                "offsets_days": [0],
            },
            memo="memo",
            metadata={"foo": "string"},
            payment_terms={"type": "due_on_receipt"},
            review_required=True,
            tax_id="tax_id",
            idempotency_key="Idempotency-Key",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: DodoPayments) -> None:
        response = client.invoices.with_raw_response.create(
            collection_method="auto_charge",
            currency="AED",
            customer_id="customer_id",
            items=[
                {
                    "description": "description",
                    "kind": "custom",
                    "tax_category": "digital_products",
                    "unit_amount": 0,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: DodoPayments) -> None:
        with client.invoices.with_streaming_response.create(
            collection_method="auto_charge",
            currency="AED",
            customer_id="customer_id",
            items=[
                {
                    "description": "description",
                    "kind": "custom",
                    "tax_category": "digital_products",
                    "unit_amount": 0,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(Invoice, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: DodoPayments) -> None:
        invoice = client.invoices.retrieve(
            "invoice_id",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: DodoPayments) -> None:
        response = client.invoices.with_raw_response.retrieve(
            "invoice_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: DodoPayments) -> None:
        with client.invoices.with_streaming_response.retrieve(
            "invoice_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(Invoice, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            client.invoices.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: DodoPayments) -> None:
        invoice = client.invoices.update(
            invoice_id="invoice_id",
            if_match="If-Match",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: DodoPayments) -> None:
        invoice = client.invoices.update(
            invoice_id="invoice_id",
            if_match="If-Match",
            billing_address={
                "country": "AF",
                "city": "city",
                "state": "state",
                "street": "street",
                "zipcode": "zipcode",
            },
            cc_emails=["string"],
            collection_method="auto_charge",
            currency="AED",
            customer_email="customer_email",
            customer_id="customer_id",
            discount_ids=["string"],
            due_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            dunning={
                "reminders_enabled": True,
                "offsets_days": [0],
            },
            items=[
                {
                    "description": "description",
                    "kind": "custom",
                    "tax_category": "digital_products",
                    "unit_amount": 0,
                    "quantity": 0,
                }
            ],
            memo="memo",
            metadata={"foo": "string"},
            payment_terms={"type": "due_on_receipt"},
            review_required=True,
            tax_id="tax_id",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: DodoPayments) -> None:
        response = client.invoices.with_raw_response.update(
            invoice_id="invoice_id",
            if_match="If-Match",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: DodoPayments) -> None:
        with client.invoices.with_streaming_response.update(
            invoice_id="invoice_id",
            if_match="If-Match",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(Invoice, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            client.invoices.with_raw_response.update(
                invoice_id="",
                if_match="If-Match",
            )

    @parametrize
    def test_method_list(self, client: DodoPayments) -> None:
        invoice = client.invoices.list()
        assert_matches_type(SyncDefaultPageNumberPagination[Invoice], invoice, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: DodoPayments) -> None:
        invoice = client.invoices.list(
            collection_method="auto_charge",
            created_at_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            customer_id="customer_id",
            due_at_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            due_at_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            page_number=0,
            page_size=0,
            status=["open"],
            subscription_id="subscription_id",
            tags=["refunded"],
            total_amount_gte=0,
            total_amount_lte=0,
        )
        assert_matches_type(SyncDefaultPageNumberPagination[Invoice], invoice, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: DodoPayments) -> None:
        response = client.invoices.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(SyncDefaultPageNumberPagination[Invoice], invoice, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: DodoPayments) -> None:
        with client.invoices.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(SyncDefaultPageNumberPagination[Invoice], invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: DodoPayments) -> None:
        invoice = client.invoices.delete(
            invoice_id="invoice_id",
            if_match="If-Match",
        )
        assert invoice is None

    @parametrize
    def test_raw_response_delete(self, client: DodoPayments) -> None:
        response = client.invoices.with_raw_response.delete(
            invoice_id="invoice_id",
            if_match="If-Match",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert invoice is None

    @parametrize
    def test_streaming_response_delete(self, client: DodoPayments) -> None:
        with client.invoices.with_streaming_response.delete(
            invoice_id="invoice_id",
            if_match="If-Match",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert invoice is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            client.invoices.with_raw_response.delete(
                invoice_id="",
                if_match="If-Match",
            )

    @parametrize
    def test_method_add_note(self, client: DodoPayments) -> None:
        invoice = client.invoices.add_note(
            invoice_id="invoice_id",
            text="text",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_raw_response_add_note(self, client: DodoPayments) -> None:
        response = client.invoices.with_raw_response.add_note(
            invoice_id="invoice_id",
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_streaming_response_add_note(self, client: DodoPayments) -> None:
        with client.invoices.with_streaming_response.add_note(
            invoice_id="invoice_id",
            text="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(Invoice, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_add_note(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            client.invoices.with_raw_response.add_note(
                invoice_id="",
                text="text",
            )

    @parametrize
    def test_method_create_hosted_link(self, client: DodoPayments) -> None:
        invoice = client.invoices.create_hosted_link(
            "invoice_id",
        )
        assert_matches_type(InvoiceCreateHostedLinkResponse, invoice, path=["response"])

    @parametrize
    def test_raw_response_create_hosted_link(self, client: DodoPayments) -> None:
        response = client.invoices.with_raw_response.create_hosted_link(
            "invoice_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(InvoiceCreateHostedLinkResponse, invoice, path=["response"])

    @parametrize
    def test_streaming_response_create_hosted_link(self, client: DodoPayments) -> None:
        with client.invoices.with_streaming_response.create_hosted_link(
            "invoice_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(InvoiceCreateHostedLinkResponse, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_hosted_link(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            client.invoices.with_raw_response.create_hosted_link(
                "",
            )

    @parametrize
    def test_method_duplicate(self, client: DodoPayments) -> None:
        invoice = client.invoices.duplicate(
            "invoice_id",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_raw_response_duplicate(self, client: DodoPayments) -> None:
        response = client.invoices.with_raw_response.duplicate(
            "invoice_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_streaming_response_duplicate(self, client: DodoPayments) -> None:
        with client.invoices.with_streaming_response.duplicate(
            "invoice_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(Invoice, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_duplicate(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            client.invoices.with_raw_response.duplicate(
                "",
            )

    @parametrize
    def test_method_finalize(self, client: DodoPayments) -> None:
        invoice = client.invoices.finalize(
            invoice_id="invoice_id",
            if_match="If-Match",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_method_finalize_with_all_params(self, client: DodoPayments) -> None:
        invoice = client.invoices.finalize(
            invoice_id="invoice_id",
            if_match="If-Match",
            cc_emails=["string"],
            customer_email="customer_email",
            send=True,
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_raw_response_finalize(self, client: DodoPayments) -> None:
        response = client.invoices.with_raw_response.finalize(
            invoice_id="invoice_id",
            if_match="If-Match",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_streaming_response_finalize(self, client: DodoPayments) -> None:
        with client.invoices.with_streaming_response.finalize(
            invoice_id="invoice_id",
            if_match="If-Match",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(Invoice, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_finalize(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            client.invoices.with_raw_response.finalize(
                invoice_id="",
                if_match="If-Match",
            )

    @parametrize
    def test_method_list_events(self, client: DodoPayments) -> None:
        invoice = client.invoices.list_events(
            "invoice_id",
        )
        assert_matches_type(InvoiceListEventsResponse, invoice, path=["response"])

    @parametrize
    def test_raw_response_list_events(self, client: DodoPayments) -> None:
        response = client.invoices.with_raw_response.list_events(
            "invoice_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(InvoiceListEventsResponse, invoice, path=["response"])

    @parametrize
    def test_streaming_response_list_events(self, client: DodoPayments) -> None:
        with client.invoices.with_streaming_response.list_events(
            "invoice_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(InvoiceListEventsResponse, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_events(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            client.invoices.with_raw_response.list_events(
                "",
            )

    @parametrize
    def test_method_mark_uncollectable(self, client: DodoPayments) -> None:
        invoice = client.invoices.mark_uncollectable(
            invoice_id="invoice_id",
            if_match="If-Match",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_raw_response_mark_uncollectable(self, client: DodoPayments) -> None:
        response = client.invoices.with_raw_response.mark_uncollectable(
            invoice_id="invoice_id",
            if_match="If-Match",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_streaming_response_mark_uncollectable(self, client: DodoPayments) -> None:
        with client.invoices.with_streaming_response.mark_uncollectable(
            invoice_id="invoice_id",
            if_match="If-Match",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(Invoice, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_mark_uncollectable(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            client.invoices.with_raw_response.mark_uncollectable(
                invoice_id="",
                if_match="If-Match",
            )

    @parametrize
    def test_method_preview(self, client: DodoPayments) -> None:
        invoice = client.invoices.preview(
            collection_method="auto_charge",
            currency="AED",
            customer_id="customer_id",
            items=[
                {
                    "description": "description",
                    "kind": "custom",
                    "tax_category": "digital_products",
                    "unit_amount": 0,
                }
            ],
        )
        assert invoice is None

    @parametrize
    def test_method_preview_with_all_params(self, client: DodoPayments) -> None:
        invoice = client.invoices.preview(
            collection_method="auto_charge",
            currency="AED",
            customer_id="customer_id",
            items=[
                {
                    "description": "description",
                    "kind": "custom",
                    "tax_category": "digital_products",
                    "unit_amount": 0,
                    "quantity": 0,
                }
            ],
            format="json",
            billing_address={
                "country": "AF",
                "city": "city",
                "state": "state",
                "street": "street",
                "zipcode": "zipcode",
            },
            cc_emails=["string"],
            customer_email="customer_email",
            discount_ids=["string"],
            due_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            dunning={
                "reminders_enabled": True,
                "offsets_days": [0],
            },
            memo="memo",
            metadata={"foo": "string"},
            payment_terms={"type": "due_on_receipt"},
            review_required=True,
            tax_id="tax_id",
        )
        assert invoice is None

    @parametrize
    def test_raw_response_preview(self, client: DodoPayments) -> None:
        response = client.invoices.with_raw_response.preview(
            collection_method="auto_charge",
            currency="AED",
            customer_id="customer_id",
            items=[
                {
                    "description": "description",
                    "kind": "custom",
                    "tax_category": "digital_products",
                    "unit_amount": 0,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert invoice is None

    @parametrize
    def test_streaming_response_preview(self, client: DodoPayments) -> None:
        with client.invoices.with_streaming_response.preview(
            collection_method="auto_charge",
            currency="AED",
            customer_id="customer_id",
            items=[
                {
                    "description": "description",
                    "kind": "custom",
                    "tax_category": "digital_products",
                    "unit_amount": 0,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert invoice is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_preview_existing(self, client: DodoPayments) -> None:
        invoice = client.invoices.preview_existing(
            invoice_id="invoice_id",
        )
        assert invoice is None

    @parametrize
    def test_method_preview_existing_with_all_params(self, client: DodoPayments) -> None:
        invoice = client.invoices.preview_existing(
            invoice_id="invoice_id",
            format="json",
        )
        assert invoice is None

    @parametrize
    def test_raw_response_preview_existing(self, client: DodoPayments) -> None:
        response = client.invoices.with_raw_response.preview_existing(
            invoice_id="invoice_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert invoice is None

    @parametrize
    def test_streaming_response_preview_existing(self, client: DodoPayments) -> None:
        with client.invoices.with_streaming_response.preview_existing(
            invoice_id="invoice_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert invoice is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_preview_existing(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            client.invoices.with_raw_response.preview_existing(
                invoice_id="",
            )

    @parametrize
    def test_method_retry(self, client: DodoPayments) -> None:
        invoice = client.invoices.retry(
            invoice_id="invoice_id",
            if_match="If-Match",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_raw_response_retry(self, client: DodoPayments) -> None:
        response = client.invoices.with_raw_response.retry(
            invoice_id="invoice_id",
            if_match="If-Match",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_streaming_response_retry(self, client: DodoPayments) -> None:
        with client.invoices.with_streaming_response.retry(
            invoice_id="invoice_id",
            if_match="If-Match",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(Invoice, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retry(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            client.invoices.with_raw_response.retry(
                invoice_id="",
                if_match="If-Match",
            )

    @parametrize
    def test_method_send(self, client: DodoPayments) -> None:
        invoice = client.invoices.send(
            invoice_id="invoice_id",
            if_match="If-Match",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_raw_response_send(self, client: DodoPayments) -> None:
        response = client.invoices.with_raw_response.send(
            invoice_id="invoice_id",
            if_match="If-Match",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_streaming_response_send(self, client: DodoPayments) -> None:
        with client.invoices.with_streaming_response.send(
            invoice_id="invoice_id",
            if_match="If-Match",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(Invoice, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_send(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            client.invoices.with_raw_response.send(
                invoice_id="",
                if_match="If-Match",
            )

    @parametrize
    def test_method_update_dunning(self, client: DodoPayments) -> None:
        invoice = client.invoices.update_dunning(
            invoice_id="invoice_id",
            action="pause",
            if_match="If-Match",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_method_update_dunning_with_all_params(self, client: DodoPayments) -> None:
        invoice = client.invoices.update_dunning(
            invoice_id="invoice_id",
            action="pause",
            if_match="If-Match",
            offsets_days=[0],
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_raw_response_update_dunning(self, client: DodoPayments) -> None:
        response = client.invoices.with_raw_response.update_dunning(
            invoice_id="invoice_id",
            action="pause",
            if_match="If-Match",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_streaming_response_update_dunning(self, client: DodoPayments) -> None:
        with client.invoices.with_streaming_response.update_dunning(
            invoice_id="invoice_id",
            action="pause",
            if_match="If-Match",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(Invoice, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_dunning(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            client.invoices.with_raw_response.update_dunning(
                invoice_id="",
                action="pause",
                if_match="If-Match",
            )

    @parametrize
    def test_method_void(self, client: DodoPayments) -> None:
        invoice = client.invoices.void(
            invoice_id="invoice_id",
            if_match="If-Match",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_raw_response_void(self, client: DodoPayments) -> None:
        response = client.invoices.with_raw_response.void(
            invoice_id="invoice_id",
            if_match="If-Match",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_streaming_response_void(self, client: DodoPayments) -> None:
        with client.invoices.with_streaming_response.void(
            invoice_id="invoice_id",
            if_match="If-Match",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(Invoice, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_void(self, client: DodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            client.invoices.with_raw_response.void(
                invoice_id="",
                if_match="If-Match",
            )


class TestAsyncInvoices:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncDodoPayments) -> None:
        invoice = await async_client.invoices.create(
            collection_method="auto_charge",
            currency="AED",
            customer_id="customer_id",
            items=[
                {
                    "description": "description",
                    "kind": "custom",
                    "tax_category": "digital_products",
                    "unit_amount": 0,
                }
            ],
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDodoPayments) -> None:
        invoice = await async_client.invoices.create(
            collection_method="auto_charge",
            currency="AED",
            customer_id="customer_id",
            items=[
                {
                    "description": "description",
                    "kind": "custom",
                    "tax_category": "digital_products",
                    "unit_amount": 0,
                    "quantity": 0,
                }
            ],
            billing_address={
                "country": "AF",
                "city": "city",
                "state": "state",
                "street": "street",
                "zipcode": "zipcode",
            },
            cc_emails=["string"],
            customer_email="customer_email",
            discount_ids=["string"],
            due_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            dunning={
                "reminders_enabled": True,
                "offsets_days": [0],
            },
            memo="memo",
            metadata={"foo": "string"},
            payment_terms={"type": "due_on_receipt"},
            review_required=True,
            tax_id="tax_id",
            idempotency_key="Idempotency-Key",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.invoices.with_raw_response.create(
            collection_method="auto_charge",
            currency="AED",
            customer_id="customer_id",
            items=[
                {
                    "description": "description",
                    "kind": "custom",
                    "tax_category": "digital_products",
                    "unit_amount": 0,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = await response.parse()
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.invoices.with_streaming_response.create(
            collection_method="auto_charge",
            currency="AED",
            customer_id="customer_id",
            items=[
                {
                    "description": "description",
                    "kind": "custom",
                    "tax_category": "digital_products",
                    "unit_amount": 0,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(Invoice, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDodoPayments) -> None:
        invoice = await async_client.invoices.retrieve(
            "invoice_id",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.invoices.with_raw_response.retrieve(
            "invoice_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = await response.parse()
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.invoices.with_streaming_response.retrieve(
            "invoice_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(Invoice, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            await async_client.invoices.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncDodoPayments) -> None:
        invoice = await async_client.invoices.update(
            invoice_id="invoice_id",
            if_match="If-Match",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncDodoPayments) -> None:
        invoice = await async_client.invoices.update(
            invoice_id="invoice_id",
            if_match="If-Match",
            billing_address={
                "country": "AF",
                "city": "city",
                "state": "state",
                "street": "street",
                "zipcode": "zipcode",
            },
            cc_emails=["string"],
            collection_method="auto_charge",
            currency="AED",
            customer_email="customer_email",
            customer_id="customer_id",
            discount_ids=["string"],
            due_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            dunning={
                "reminders_enabled": True,
                "offsets_days": [0],
            },
            items=[
                {
                    "description": "description",
                    "kind": "custom",
                    "tax_category": "digital_products",
                    "unit_amount": 0,
                    "quantity": 0,
                }
            ],
            memo="memo",
            metadata={"foo": "string"},
            payment_terms={"type": "due_on_receipt"},
            review_required=True,
            tax_id="tax_id",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.invoices.with_raw_response.update(
            invoice_id="invoice_id",
            if_match="If-Match",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = await response.parse()
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.invoices.with_streaming_response.update(
            invoice_id="invoice_id",
            if_match="If-Match",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(Invoice, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            await async_client.invoices.with_raw_response.update(
                invoice_id="",
                if_match="If-Match",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncDodoPayments) -> None:
        invoice = await async_client.invoices.list()
        assert_matches_type(AsyncDefaultPageNumberPagination[Invoice], invoice, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDodoPayments) -> None:
        invoice = await async_client.invoices.list(
            collection_method="auto_charge",
            created_at_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            customer_id="customer_id",
            due_at_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            due_at_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            page_number=0,
            page_size=0,
            status=["open"],
            subscription_id="subscription_id",
            tags=["refunded"],
            total_amount_gte=0,
            total_amount_lte=0,
        )
        assert_matches_type(AsyncDefaultPageNumberPagination[Invoice], invoice, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.invoices.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = await response.parse()
        assert_matches_type(AsyncDefaultPageNumberPagination[Invoice], invoice, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.invoices.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(AsyncDefaultPageNumberPagination[Invoice], invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncDodoPayments) -> None:
        invoice = await async_client.invoices.delete(
            invoice_id="invoice_id",
            if_match="If-Match",
        )
        assert invoice is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.invoices.with_raw_response.delete(
            invoice_id="invoice_id",
            if_match="If-Match",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = await response.parse()
        assert invoice is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.invoices.with_streaming_response.delete(
            invoice_id="invoice_id",
            if_match="If-Match",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert invoice is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            await async_client.invoices.with_raw_response.delete(
                invoice_id="",
                if_match="If-Match",
            )

    @parametrize
    async def test_method_add_note(self, async_client: AsyncDodoPayments) -> None:
        invoice = await async_client.invoices.add_note(
            invoice_id="invoice_id",
            text="text",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_raw_response_add_note(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.invoices.with_raw_response.add_note(
            invoice_id="invoice_id",
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = await response.parse()
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_streaming_response_add_note(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.invoices.with_streaming_response.add_note(
            invoice_id="invoice_id",
            text="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(Invoice, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_add_note(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            await async_client.invoices.with_raw_response.add_note(
                invoice_id="",
                text="text",
            )

    @parametrize
    async def test_method_create_hosted_link(self, async_client: AsyncDodoPayments) -> None:
        invoice = await async_client.invoices.create_hosted_link(
            "invoice_id",
        )
        assert_matches_type(InvoiceCreateHostedLinkResponse, invoice, path=["response"])

    @parametrize
    async def test_raw_response_create_hosted_link(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.invoices.with_raw_response.create_hosted_link(
            "invoice_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = await response.parse()
        assert_matches_type(InvoiceCreateHostedLinkResponse, invoice, path=["response"])

    @parametrize
    async def test_streaming_response_create_hosted_link(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.invoices.with_streaming_response.create_hosted_link(
            "invoice_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(InvoiceCreateHostedLinkResponse, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_hosted_link(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            await async_client.invoices.with_raw_response.create_hosted_link(
                "",
            )

    @parametrize
    async def test_method_duplicate(self, async_client: AsyncDodoPayments) -> None:
        invoice = await async_client.invoices.duplicate(
            "invoice_id",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_raw_response_duplicate(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.invoices.with_raw_response.duplicate(
            "invoice_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = await response.parse()
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_streaming_response_duplicate(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.invoices.with_streaming_response.duplicate(
            "invoice_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(Invoice, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_duplicate(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            await async_client.invoices.with_raw_response.duplicate(
                "",
            )

    @parametrize
    async def test_method_finalize(self, async_client: AsyncDodoPayments) -> None:
        invoice = await async_client.invoices.finalize(
            invoice_id="invoice_id",
            if_match="If-Match",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_method_finalize_with_all_params(self, async_client: AsyncDodoPayments) -> None:
        invoice = await async_client.invoices.finalize(
            invoice_id="invoice_id",
            if_match="If-Match",
            cc_emails=["string"],
            customer_email="customer_email",
            send=True,
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_raw_response_finalize(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.invoices.with_raw_response.finalize(
            invoice_id="invoice_id",
            if_match="If-Match",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = await response.parse()
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_streaming_response_finalize(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.invoices.with_streaming_response.finalize(
            invoice_id="invoice_id",
            if_match="If-Match",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(Invoice, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_finalize(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            await async_client.invoices.with_raw_response.finalize(
                invoice_id="",
                if_match="If-Match",
            )

    @parametrize
    async def test_method_list_events(self, async_client: AsyncDodoPayments) -> None:
        invoice = await async_client.invoices.list_events(
            "invoice_id",
        )
        assert_matches_type(InvoiceListEventsResponse, invoice, path=["response"])

    @parametrize
    async def test_raw_response_list_events(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.invoices.with_raw_response.list_events(
            "invoice_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = await response.parse()
        assert_matches_type(InvoiceListEventsResponse, invoice, path=["response"])

    @parametrize
    async def test_streaming_response_list_events(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.invoices.with_streaming_response.list_events(
            "invoice_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(InvoiceListEventsResponse, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_events(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            await async_client.invoices.with_raw_response.list_events(
                "",
            )

    @parametrize
    async def test_method_mark_uncollectable(self, async_client: AsyncDodoPayments) -> None:
        invoice = await async_client.invoices.mark_uncollectable(
            invoice_id="invoice_id",
            if_match="If-Match",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_raw_response_mark_uncollectable(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.invoices.with_raw_response.mark_uncollectable(
            invoice_id="invoice_id",
            if_match="If-Match",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = await response.parse()
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_streaming_response_mark_uncollectable(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.invoices.with_streaming_response.mark_uncollectable(
            invoice_id="invoice_id",
            if_match="If-Match",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(Invoice, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_mark_uncollectable(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            await async_client.invoices.with_raw_response.mark_uncollectable(
                invoice_id="",
                if_match="If-Match",
            )

    @parametrize
    async def test_method_preview(self, async_client: AsyncDodoPayments) -> None:
        invoice = await async_client.invoices.preview(
            collection_method="auto_charge",
            currency="AED",
            customer_id="customer_id",
            items=[
                {
                    "description": "description",
                    "kind": "custom",
                    "tax_category": "digital_products",
                    "unit_amount": 0,
                }
            ],
        )
        assert invoice is None

    @parametrize
    async def test_method_preview_with_all_params(self, async_client: AsyncDodoPayments) -> None:
        invoice = await async_client.invoices.preview(
            collection_method="auto_charge",
            currency="AED",
            customer_id="customer_id",
            items=[
                {
                    "description": "description",
                    "kind": "custom",
                    "tax_category": "digital_products",
                    "unit_amount": 0,
                    "quantity": 0,
                }
            ],
            format="json",
            billing_address={
                "country": "AF",
                "city": "city",
                "state": "state",
                "street": "street",
                "zipcode": "zipcode",
            },
            cc_emails=["string"],
            customer_email="customer_email",
            discount_ids=["string"],
            due_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            dunning={
                "reminders_enabled": True,
                "offsets_days": [0],
            },
            memo="memo",
            metadata={"foo": "string"},
            payment_terms={"type": "due_on_receipt"},
            review_required=True,
            tax_id="tax_id",
        )
        assert invoice is None

    @parametrize
    async def test_raw_response_preview(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.invoices.with_raw_response.preview(
            collection_method="auto_charge",
            currency="AED",
            customer_id="customer_id",
            items=[
                {
                    "description": "description",
                    "kind": "custom",
                    "tax_category": "digital_products",
                    "unit_amount": 0,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = await response.parse()
        assert invoice is None

    @parametrize
    async def test_streaming_response_preview(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.invoices.with_streaming_response.preview(
            collection_method="auto_charge",
            currency="AED",
            customer_id="customer_id",
            items=[
                {
                    "description": "description",
                    "kind": "custom",
                    "tax_category": "digital_products",
                    "unit_amount": 0,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert invoice is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_preview_existing(self, async_client: AsyncDodoPayments) -> None:
        invoice = await async_client.invoices.preview_existing(
            invoice_id="invoice_id",
        )
        assert invoice is None

    @parametrize
    async def test_method_preview_existing_with_all_params(self, async_client: AsyncDodoPayments) -> None:
        invoice = await async_client.invoices.preview_existing(
            invoice_id="invoice_id",
            format="json",
        )
        assert invoice is None

    @parametrize
    async def test_raw_response_preview_existing(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.invoices.with_raw_response.preview_existing(
            invoice_id="invoice_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = await response.parse()
        assert invoice is None

    @parametrize
    async def test_streaming_response_preview_existing(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.invoices.with_streaming_response.preview_existing(
            invoice_id="invoice_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert invoice is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_preview_existing(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            await async_client.invoices.with_raw_response.preview_existing(
                invoice_id="",
            )

    @parametrize
    async def test_method_retry(self, async_client: AsyncDodoPayments) -> None:
        invoice = await async_client.invoices.retry(
            invoice_id="invoice_id",
            if_match="If-Match",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_raw_response_retry(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.invoices.with_raw_response.retry(
            invoice_id="invoice_id",
            if_match="If-Match",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = await response.parse()
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_streaming_response_retry(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.invoices.with_streaming_response.retry(
            invoice_id="invoice_id",
            if_match="If-Match",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(Invoice, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retry(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            await async_client.invoices.with_raw_response.retry(
                invoice_id="",
                if_match="If-Match",
            )

    @parametrize
    async def test_method_send(self, async_client: AsyncDodoPayments) -> None:
        invoice = await async_client.invoices.send(
            invoice_id="invoice_id",
            if_match="If-Match",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_raw_response_send(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.invoices.with_raw_response.send(
            invoice_id="invoice_id",
            if_match="If-Match",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = await response.parse()
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_streaming_response_send(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.invoices.with_streaming_response.send(
            invoice_id="invoice_id",
            if_match="If-Match",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(Invoice, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_send(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            await async_client.invoices.with_raw_response.send(
                invoice_id="",
                if_match="If-Match",
            )

    @parametrize
    async def test_method_update_dunning(self, async_client: AsyncDodoPayments) -> None:
        invoice = await async_client.invoices.update_dunning(
            invoice_id="invoice_id",
            action="pause",
            if_match="If-Match",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_method_update_dunning_with_all_params(self, async_client: AsyncDodoPayments) -> None:
        invoice = await async_client.invoices.update_dunning(
            invoice_id="invoice_id",
            action="pause",
            if_match="If-Match",
            offsets_days=[0],
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_raw_response_update_dunning(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.invoices.with_raw_response.update_dunning(
            invoice_id="invoice_id",
            action="pause",
            if_match="If-Match",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = await response.parse()
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_streaming_response_update_dunning(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.invoices.with_streaming_response.update_dunning(
            invoice_id="invoice_id",
            action="pause",
            if_match="If-Match",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(Invoice, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_dunning(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            await async_client.invoices.with_raw_response.update_dunning(
                invoice_id="",
                action="pause",
                if_match="If-Match",
            )

    @parametrize
    async def test_method_void(self, async_client: AsyncDodoPayments) -> None:
        invoice = await async_client.invoices.void(
            invoice_id="invoice_id",
            if_match="If-Match",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_raw_response_void(self, async_client: AsyncDodoPayments) -> None:
        response = await async_client.invoices.with_raw_response.void(
            invoice_id="invoice_id",
            if_match="If-Match",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = await response.parse()
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_streaming_response_void(self, async_client: AsyncDodoPayments) -> None:
        async with async_client.invoices.with_streaming_response.void(
            invoice_id="invoice_id",
            if_match="If-Match",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(Invoice, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_void(self, async_client: AsyncDodoPayments) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            await async_client.invoices.with_raw_response.void(
                invoice_id="",
                if_match="If-Match",
            )
