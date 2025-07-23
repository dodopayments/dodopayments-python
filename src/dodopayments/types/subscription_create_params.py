# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable, Optional
from typing_extensions import Required, TypedDict

from .currency import Currency
from .attach_addon_param import AttachAddonParam
from .payment_method_types import PaymentMethodTypes
from .billing_address_param import BillingAddressParam
from .customer_request_param import CustomerRequestParam

__all__ = ["SubscriptionCreateParams", "OnDemand"]


class SubscriptionCreateParams(TypedDict, total=False):
    billing: Required[BillingAddressParam]
    """Billing address information for the subscription"""

    customer: Required[CustomerRequestParam]
    """Customer details for the subscription"""

    product_id: Required[str]
    """Unique identifier of the product to subscribe to"""

    quantity: Required[int]
    """Number of units to subscribe for. Must be at least 1."""

    addons: Optional[Iterable[AttachAddonParam]]
    """Attach addons to this subscription"""

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
    """Discount Code to apply to the subscription"""

    metadata: Dict[str, str]
    """Additional metadata for the subscription Defaults to empty if not specified"""

    on_demand: Optional[OnDemand]

    payment_link: Optional[bool]
    """If true, generates a payment link. Defaults to false if not specified."""

    return_url: Optional[str]
    """Optional URL to redirect after successful subscription creation"""

    show_saved_payment_methods: bool
    """Display saved payment methods of a returning customer False by default"""

    tax_id: Optional[str]
    """Tax ID in case the payment is B2B.

    If tax id validation fails the payment creation will fail
    """

    trial_period_days: Optional[int]
    """
    Optional trial period in days If specified, this value overrides the trial
    period set in the product's price Must be between 0 and 10000 days
    """


class OnDemand(TypedDict, total=False):
    mandate_only: Required[bool]
    """
    If set as True, does not perform any charge and only authorizes payment method
    details for future use.
    """

    adaptive_currency_fees_inclusive: Optional[bool]
    """
    Whether adaptive currency fees should be included in the product_price (true) or
    added on top (false). This field is ignored if adaptive pricing is not enabled
    for the business.
    """

    product_currency: Optional[Currency]
    """Optional currency of the product price.

    If not specified, defaults to the currency of the product.
    """

    product_description: Optional[str]
    """
    Optional product description override for billing and line items. If not
    specified, the stored description of the product will be used.
    """

    product_price: Optional[int]
    """
    Product price for the initial charge to customer If not specified the stored
    price of the product will be used Represented in the lowest denomination of the
    currency (e.g., cents for USD). For example, to charge $1.00, pass `100`.
    """
