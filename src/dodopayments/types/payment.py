# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .dispute import Dispute
from .._models import BaseModel
from .currency import Currency
from .country_code import CountryCode
from .intent_status import IntentStatus
from .refund_status import RefundStatus
from .billing_address import BillingAddress
from .customer_limited_details import CustomerLimitedDetails

__all__ = ["Payment", "Refund", "ProductCart"]


class Refund(BaseModel):
    business_id: str
    """The unique identifier of the business issuing the refund."""

    created_at: datetime
    """The timestamp of when the refund was created in UTC."""

    is_partial: bool
    """If true the refund is a partial refund"""

    payment_id: str
    """The unique identifier of the payment associated with the refund."""

    refund_id: str
    """The unique identifier of the refund."""

    status: RefundStatus
    """The current status of the refund."""

    amount: Optional[int] = None
    """The refunded amount."""

    currency: Optional[Currency] = None
    """The currency of the refund, represented as an ISO 4217 currency code."""

    reason: Optional[str] = None
    """The reason provided for the refund, if any. Optional."""


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
    """brand id this payment belongs to"""

    disputes: List[Dispute]
    """List of disputes associated with this payment"""

    metadata: Dict[str, str]
    """Additional custom data associated with the payment"""

    payment_id: str
    """Unique identifier for the payment"""

    refunds: List[Refund]
    """List of refunds issued for this payment"""

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

    total_amount: int
    """
    Total amount charged to the customer including tax, in smallest currency unit
    (e.g. cents)
    """

    card_holder_name: Optional[str] = None
    """Cardholder name"""

    card_issuing_country: Optional[CountryCode] = None
    """ISO2 country code of the card"""

    card_last_four: Optional[str] = None
    """The last four digits of the card"""

    card_network: Optional[str] = None
    """Card network like VISA, MASTERCARD etc."""

    card_type: Optional[str] = None
    """The type of card DEBIT or CREDIT"""

    checkout_session_id: Optional[str] = None
    """
    If payment is made using a checkout session, this field is set to the id of the
    session.
    """

    discount_id: Optional[str] = None
    """The discount id if discount is applied"""

    error_code: Optional[str] = None
    """An error code if the payment failed"""

    error_message: Optional[str] = None
    """An error message if the payment failed"""

    invoice_id: Optional[str] = None
    """Invoice ID for this payment. Uses India-specific invoice ID if available."""

    invoice_url: Optional[str] = None
    """URL to download the invoice PDF for this payment."""

    payment_link: Optional[str] = None
    """Checkout URL"""

    payment_method: Optional[str] = None
    """Payment method used by customer (e.g. "card", "bank_transfer")"""

    payment_method_type: Optional[str] = None
    """Specific type of payment method (e.g. "visa", "mastercard")"""

    product_cart: Optional[List[ProductCart]] = None
    """List of products purchased in a one-time payment"""

    settlement_tax: Optional[int] = None
    """
    This represents the portion of settlement_amount that corresponds to taxes
    collected. Especially relevant for adaptive pricing where the tax component must
    be tracked separately in your Dodo balance.
    """

    status: Optional[IntentStatus] = None
    """Current status of the payment intent"""

    subscription_id: Optional[str] = None
    """Identifier of the subscription if payment is part of a subscription"""

    tax: Optional[int] = None
    """Amount of tax collected in smallest currency unit (e.g. cents)"""

    updated_at: Optional[datetime] = None
    """Timestamp when the payment was last updated"""
