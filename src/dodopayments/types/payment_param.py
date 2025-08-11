# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .currency import Currency
from .country_code import CountryCode
from .refund_param import RefundParam
from .dispute_param import DisputeParam
from .intent_status import IntentStatus
from .billing_address_param import BillingAddressParam
from .customer_limited_details_param import CustomerLimitedDetailsParam

__all__ = ["PaymentParam", "ProductCart"]


class ProductCart(TypedDict, total=False):
    product_id: Required[str]

    quantity: Required[int]


class PaymentParam(TypedDict, total=False):
    billing: Required[BillingAddressParam]
    """Billing address details for payments"""

    brand_id: Required[str]
    """brand id this payment belongs to"""

    business_id: Required[str]
    """Identifier of the business associated with the payment"""

    created_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Timestamp when the payment was created"""

    currency: Required[Currency]
    """Currency used for the payment"""

    customer: Required[CustomerLimitedDetailsParam]
    """Details about the customer who made the payment"""

    digital_products_delivered: Required[bool]
    """brand id this payment belongs to"""

    disputes: Required[Iterable[DisputeParam]]
    """List of disputes associated with this payment"""

    metadata: Required[Dict[str, str]]
    """Additional custom data associated with the payment"""

    payment_id: Required[str]
    """Unique identifier for the payment"""

    refunds: Required[Iterable[RefundParam]]
    """List of refunds issued for this payment"""

    settlement_amount: Required[int]
    """
    The amount that will be credited to your Dodo balance after currency conversion
    and processing. Especially relevant for adaptive pricing where the customer's
    payment currency differs from your settlement currency.
    """

    settlement_currency: Required[Currency]
    """
    The currency in which the settlement_amount will be credited to your Dodo
    balance. This may differ from the customer's payment currency in adaptive
    pricing scenarios.
    """

    total_amount: Required[int]
    """
    Total amount charged to the customer including tax, in smallest currency unit
    (e.g. cents)
    """

    card_issuing_country: Optional[CountryCode]
    """ISO2 country code of the card"""

    card_last_four: Optional[str]
    """The last four digits of the card"""

    card_network: Optional[str]
    """Card network like VISA, MASTERCARD etc."""

    card_type: Optional[str]
    """The type of card DEBIT or CREDIT"""

    discount_id: Optional[str]
    """The discount id if discount is applied"""

    error_code: Optional[str]
    """An error code if the payment failed"""

    error_message: Optional[str]
    """An error message if the payment failed"""

    payment_link: Optional[str]
    """Checkout URL"""

    payment_method: Optional[str]
    """Payment method used by customer (e.g. "card", "bank_transfer")"""

    payment_method_type: Optional[str]
    """Specific type of payment method (e.g. "visa", "mastercard")"""

    product_cart: Optional[Iterable[ProductCart]]
    """List of products purchased in a one-time payment"""

    settlement_tax: Optional[int]
    """
    This represents the portion of settlement_amount that corresponds to taxes
    collected. Especially relevant for adaptive pricing where the tax component must
    be tracked separately in your Dodo balance.
    """

    status: Optional[IntentStatus]
    """Current status of the payment intent"""

    subscription_id: Optional[str]
    """Identifier of the subscription if payment is part of a subscription"""

    tax: Optional[int]
    """Amount of tax collected in smallest currency unit (e.g. cents)"""

    updated_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Timestamp when the payment was last updated"""
