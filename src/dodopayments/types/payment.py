# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .refund import Refund
from .dispute import Dispute
from .._models import BaseModel
from .currency import Currency
from .country_code import CountryCode
from .intent_status import IntentStatus
from .billing_address import BillingAddress
from .customer_limited_details import CustomerLimitedDetails

__all__ = ["Payment", "ProductCart"]


class ProductCart(BaseModel):
    product_id: str

    quantity: int


class Payment(BaseModel):
    billing: BillingAddress

    business_id: str
    """Identifier of the business associated with the payment"""

    created_at: datetime
    """Timestamp when the payment was created"""

    currency: Currency

    customer: CustomerLimitedDetails

    disputes: List[Dispute]
    """List of disputes associated with this payment"""

    metadata: Dict[str, str]

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

    total_amount: int
    """
    Total amount charged to the customer including tax, in smallest currency unit
    (e.g. cents)
    """

    card_issuing_country: Optional[CountryCode] = None
    """ISO country code alpha2 variant"""

    card_last_four: Optional[str] = None
    """The last four digits of the card"""

    card_network: Optional[str] = None
    """Card network like VISA, MASTERCARD etc."""

    card_type: Optional[str] = None
    """The type of card DEBIT or CREDIT"""

    discount_id: Optional[str] = None
    """The discount id if discount is applied"""

    error_message: Optional[str] = None
    """An error message if the payment failed"""

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

    subscription_id: Optional[str] = None
    """Identifier of the subscription if payment is part of a subscription"""

    tax: Optional[int] = None
    """Amount of tax collected in smallest currency unit (e.g. cents)"""

    updated_at: Optional[datetime] = None
    """Timestamp when the payment was last updated"""
