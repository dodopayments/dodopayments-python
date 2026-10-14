# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .currency import Currency
from .metadata import Metadata
from .intent_status import IntentStatus
from .dispute_status import DisputeStatus
from .payment_refund_status import PaymentRefundStatus
from .customer_limited_details import CustomerLimitedDetails
from .subscription_service_period import SubscriptionServicePeriod

__all__ = ["PaymentListResponse"]


class PaymentListResponse(BaseModel):
    brand_id: str

    created_at: datetime

    currency: Currency

    customer: CustomerLimitedDetails

    digital_products_delivered: bool

    has_license_key: bool

    is_multi_subscription: bool
    """True when one payment starts more than one subscription.

    Read this field to find the payment type. Do not read the length of
    `subscription_ids`. Do not read `subscription_id` for null.
    """

    metadata: Metadata
    """Arbitrary key-value metadata.

    Values can be string, integer, number, or boolean.
    """

    payment_id: str

    payment_provider: Literal["stripe", "adyen", "dodo"]
    """Which processor handled this payment.

    `stripe` / `adyen` for BYOP routes (the merchant's own payment connector);
    `dodo` for everything Dodo processed itself.
    """

    retry_attempt: int
    """The retry attempt number of this payment.

    The value is `0` for the original payment. Each retry after a failed
    subscription renewal adds `1`. The value is always `0` for a payment that is not
    for a subscription.
    """

    service_periods: List[SubscriptionServicePeriod]
    """
    The service period of each subscription that this payment pays for. The order is
    the same as `subscription_ids`. For a plan change charge, the period starts at
    the plan change and ends at the next billing date. The list is empty unless the
    payment status is `succeeded`. The list is also empty for a one-time payment, an
    on-demand charge, or a payment method update.
    """

    subscription_ids: List[str]
    """
    Every subscription that this payment starts or charges, in a stable order. It is
    empty for a one-time payment. It holds the value of `subscription_id` when the
    payment names one subscription.
    """

    total_amount: int

    card_last_four: Optional[str] = None
    """The last four digits of the card"""

    card_network: Optional[str] = None
    """Card network like VISA, MASTERCARD etc."""

    checkout_session_id: Optional[str] = None
    """The ID of the checkout session for this payment.

    The value is null when the payment does not use a checkout session.
    """

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
