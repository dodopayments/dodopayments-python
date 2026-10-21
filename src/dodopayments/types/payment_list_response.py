# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .currency import Currency
from .metadata import Metadata
from .charge_type import ChargeType
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

    includes_usage: bool
    """True when this payment also bills metered usage or credit overage.

    The usage is for the billing cycle before the service period, not for the
    service period. The value is set for each payment status. It is false when
    `charge_type` is null.
    """

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
    on-demand charge, or a payment method update. The list is set for `new`,
    `renewal` and `plan_change` charges that succeeded. It can be empty for some
    zero-amount payments. A `renewal` with no entry for its subscription bills usage
    only. That payment does not extend the service period.
    """

    subscription_ids: List[str]
    """
    Every subscription that this payment starts or charges, in a stable order. It is
    empty for a one-time payment. It holds the value of `subscription_id` when the
    payment names one subscription.
    """

    total_amount: int

    card_exp_month: Optional[str] = None
    """Expiry month of the card, as two digits from `01` to `12`.

    For Apple Pay and Google Pay, this is the expiry of the wallet token, which can
    differ from the expiry of the physical card.
    """

    card_exp_year: Optional[str] = None
    """Expiry year of the card, as four digits, for example `2029`.

    For Apple Pay and Google Pay, this is the expiry of the wallet token, which can
    differ from the expiry of the physical card.
    """

    card_last_four: Optional[str] = None
    """The last four digits of the card"""

    card_network: Optional[str] = None
    """Card network, in lowercase, for example `visa`, `mastercard` or `amex`.

    Older payments can carry other casing.
    """

    card_type: Optional[str] = None
    """The type of card, in lowercase: `credit`, `debit` or `prepaid`.

    Older payments can carry other casing.
    """

    charge_type: Optional[ChargeType] = None
    """The type of subscription charge that this payment is for.

    Refer to `ChargeType`. The value is set for each payment status, not only for
    `succeeded`. The value is null when this payment charges no subscription.
    """

    checkout_session_id: Optional[str] = None
    """The ID of the checkout session for this payment.

    The value is null when the payment does not use a checkout session.
    """

    dispute_status: Optional[DisputeStatus] = None
    """The most recent dispute status for this payment. None if no disputes exist."""

    invoice_id: Optional[str] = None
    """Invoice ID for this payment. Uses India-specific invoice ID if available."""

    invoice_url: Optional[str] = None
    """
    DEPRECATED: Use `GET /invoices/payments/{payment_id}` with an API key. URL to
    download the invoice PDF for this payment. The URL has no signed token. If the
    business asks for a credential on its invoice links, the URL needs an API key.
    """

    payment_method: Optional[str] = None

    payment_method_type: Optional[str] = None

    refund_status: Optional[PaymentRefundStatus] = None
    """Summary of the refund status for this payment.

    None if no succeeded refunds exist.
    """

    status: Optional[IntentStatus] = None

    subscription_id: Optional[str] = None
