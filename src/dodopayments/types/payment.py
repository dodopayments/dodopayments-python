# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .dispute import Dispute
from .._models import BaseModel
from .currency import Currency
from .metadata import Metadata
from .charge_type import ChargeType
from .country_code import CountryCode
from .intent_status import IntentStatus
from .billing_address import BillingAddress
from .discount_detail import DiscountDetail
from .refund_list_item import RefundListItem
from .custom_field_response import CustomFieldResponse
from .payment_refund_status import PaymentRefundStatus
from .customer_limited_details import CustomerLimitedDetails
from .subscription_service_period import SubscriptionServicePeriod

__all__ = ["Payment", "ProductCart"]


class ProductCart(BaseModel):
    product_id: str

    quantity: int


class Payment(BaseModel):
    billing: BillingAddress
    """Billing address details for payments"""

    brand_id: str
    """brand id this payment belongs to"""

    business_id: str
    """Identifier of the business associated with the payment"""

    created_at: datetime
    """Timestamp when the payment was created"""

    currency: Currency
    """Currency used for the payment"""

    customer: CustomerLimitedDetails
    """Details about the customer who made the payment"""

    digital_products_delivered: bool
    """Whether the digital products purchased in this payment have been delivered."""

    disputes: List[Dispute]
    """List of disputes associated with this payment"""

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

    is_update_payment_method: bool
    """
    Whether this payment was created solely to update a subscription's payment
    method (a zero-/setup-amount charge). `false` for normal charges.
    """

    metadata: Metadata
    """Additional custom data associated with the payment"""

    payment_id: str
    """Unique identifier for the payment"""

    payment_provider: Literal["stripe", "adyen", "dodo"]
    """Which processor handled this payment.

    `stripe` / `adyen` for BYOP routes (the merchant's own payment connector);
    `dodo` for everything Dodo processed itself.
    """

    refunds: List[RefundListItem]
    """List of refunds issued for this payment"""

    retry_attempt: int
    """
    Retry attempt number for subscription renewal payments. `0` for the original
    payment, `1`+ for each scheduled off-session retry after a failed renewal.
    Always `0` for non-subscription payments.
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

    settlement_amount: int
    """
    The amount that will be credited to your Dodo balance after currency conversion
    and processing. Especially relevant for adaptive pricing where the customer's
    payment currency differs from your settlement currency.
    """

    settlement_currency: Currency
    """
    The currency in which the settlement_amount will be credited to your Dodo
    balance. This may differ from the customer's payment currency in adaptive
    pricing scenarios.
    """

    subscription_ids: List[str]
    """
    Every subscription that this payment starts or charges, in a stable order. It is
    empty for a one-time payment. It holds the value of `subscription_id` when the
    payment names one subscription.
    """

    total_amount: int
    """
    Total amount charged to the customer including tax, in the currency's smallest
    unit (e.g. cents for USD, yen for JPY, fils for KWD — see the currency's decimal
    places)
    """

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

    card_holder_name: Optional[str] = None
    """Cardholder name"""

    card_issuing_country: Optional[CountryCode] = None
    """ISO2 country code of the card"""

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
    """
    If payment is made using a checkout session, this field is set to the id of the
    session.
    """

    custom_field_responses: Optional[List[CustomFieldResponse]] = None
    """Customer's responses to custom fields collected during checkout"""

    discount_id: Optional[str] = None
    """DEPRECATED: Use discounts instead. Returns the first discount's ID if present."""

    discounts: Optional[List[DiscountDetail]] = None
    """All stacked discounts applied, ordered by position"""

    error_code: Optional[str] = None
    """An error code if the payment failed"""

    error_message: Optional[str] = None
    """An error message if the payment failed.

    When `error_code` is a recognised unified code, this is the merchant-facing
    headline + recommended action (Payment Details copy) rather than the raw
    connector text.
    """

    invoice_id: Optional[str] = None
    """Invoice ID for this payment. Uses India-specific invoice ID if available."""

    invoice_url: Optional[str] = None
    """
    DEPRECATED: Use `GET /invoices/payments/{payment_id}` with an API key. URL to
    download the invoice PDF for this payment. The URL has no signed token. If the
    business asks for a credential on its invoice links, the URL needs an API key.
    """

    payment_link: Optional[str] = None
    """Checkout URL"""

    payment_method: Optional[str] = None
    """Payment method used by customer (e.g. "card", "bank_transfer")"""

    payment_method_id: Optional[str] = None
    """Identifier of the saved payment method used for this payment, if any."""

    payment_method_type: Optional[str] = None
    """Specific type of payment method (e.g. "visa", "mastercard")"""

    product_cart: Optional[List[ProductCart]] = None
    """List of products purchased in a one-time payment"""

    refund_status: Optional[PaymentRefundStatus] = None
    """Summary of the refund status for this payment.

    None if no succeeded refunds exist.
    """

    settlement_tax: Optional[int] = None
    """
    This represents the portion of settlement_amount that corresponds to taxes
    collected. Especially relevant for adaptive pricing where the tax component must
    be tracked separately in your Dodo balance.
    """

    status: Optional[IntentStatus] = None
    """Current status of the payment intent"""

    subscription_id: Optional[str] = None
    """
    Identifier of the subscription if payment is part of a subscription. A
    multi-subscription payment leaves this null, because no single subscription owns
    the payment. Read `subscription_ids` for those.
    """

    tax: Optional[int] = None
    """Amount of tax collected in the currency's smallest unit (e.g.

    cents for USD, yen for JPY, fils for KWD)
    """

    updated_at: Optional[datetime] = None
    """Timestamp when the payment was last updated"""
