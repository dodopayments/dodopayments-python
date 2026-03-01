# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel
from .currency import Currency
from .intent_status import IntentStatus
from .dispute_status import DisputeStatus
from .payment_refund_status import PaymentRefundStatus
from .customer_limited_details import CustomerLimitedDetails

__all__ = ["PaymentListResponse"]


class PaymentListResponse(BaseModel):
    brand_id: str

    created_at: datetime

    currency: Currency

    customer: CustomerLimitedDetails

    digital_products_delivered: bool

    has_license_key: bool

    metadata: Dict[str, str]

    payment_id: str

    total_amount: int

    dispute_status: Optional[DisputeStatus] = None
    """The most recent dispute status for this payment. None if no disputes exist."""

    invoice_id: Optional[str] = None
    """Invoice ID for this payment. Uses India-specific invoice ID if available."""

    invoice_url: Optional[str] = None
    """URL to download the invoice PDF for this payment."""

    payment_method: Optional[str] = None

    payment_method_type: Optional[str] = None

    refund_status: Optional[PaymentRefundStatus] = None
    """Summary of the refund status for this payment.

    None if no succeeded refunds exist.
    """

    status: Optional[IntentStatus] = None

    subscription_id: Optional[str] = None
