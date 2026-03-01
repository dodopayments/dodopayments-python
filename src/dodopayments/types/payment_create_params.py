# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable, Optional
from typing_extensions import Required, TypedDict

from .currency import Currency
from .payment_method_types import PaymentMethodTypes
from .billing_address_param import BillingAddressParam
from .customer_request_param import CustomerRequestParam

__all__ = ["PaymentCreateParams", "ProductCart"]


class PaymentCreateParams(TypedDict, total=False):
    billing: Required[BillingAddressParam]
    """Billing address details for the payment"""

    customer: Required[CustomerRequestParam]
    """Customer information for the payment"""

    product_cart: Required[Iterable[ProductCart]]
    """List of products in the cart. Must contain at least 1 and at most 100 items."""

    allowed_payment_method_types: Optional[List[PaymentMethodTypes]]
    """List of payment methods allowed during checkout.

    Customers will **never** see payment methods that are **not** in this list.
    However, adding a method here **does not guarantee** customers will see it.
    Availability still depends on other factors (e.g., customer location, merchant
    settings).
    """

    billing_currency: Optional[Currency]
    """
    Fix the currency in which the end customer is billed. If Dodo Payments cannot
    support that currency for this transaction, it will not proceed
    """

    discount_code: Optional[str]
    """Discount Code to apply to the transaction"""

    force_3ds: Optional[bool]
    """Override merchant default 3DS behaviour for this payment"""

    metadata: Dict[str, str]
    """
    Additional metadata associated with the payment. Defaults to empty if not
    provided.
    """

    payment_link: Optional[bool]
    """Whether to generate a payment link. Defaults to false if not specified."""

    payment_method_id: Optional[str]
    """
    Optional payment method ID to use for this payment. If provided, customer_id
    must also be provided. The payment method will be validated for eligibility with
    the payment's currency.
    """

    redirect_immediately: bool
    """
    If true, redirects the customer immediately after payment completion False by
    default
    """

    return_url: Optional[str]
    """
    Optional URL to redirect the customer after payment. Must be a valid URL if
    provided.
    """

    short_link: Optional[bool]
    """If true, returns a shortened payment link. Defaults to false if not specified."""

    show_saved_payment_methods: bool
    """Display saved payment methods of a returning customer False by default"""

    tax_id: Optional[str]
    """Tax ID in case the payment is B2B.

    If tax id validation fails the payment creation will fail
    """


class ProductCart(TypedDict, total=False):
    product_id: Required[str]

    quantity: Required[int]

    amount: Optional[int]
    """Amount the customer pays if pay_what_you_want is enabled.

    If disabled then amount will be ignored Represented in the lowest denomination
    of the currency (e.g., cents for USD). For example, to charge $1.00, pass `100`.
    """
