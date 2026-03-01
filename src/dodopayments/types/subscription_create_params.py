# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable, Optional
from typing_extensions import Required, TypedDict

from .currency import Currency
from .attach_addon_param import AttachAddonParam
from .payment_method_types import PaymentMethodTypes
from .billing_address_param import BillingAddressParam
from .customer_request_param import CustomerRequestParam
from .on_demand_subscription_param import OnDemandSubscriptionParam

__all__ = ["SubscriptionCreateParams", "OneTimeProductCart"]


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

    force_3ds: Optional[bool]
    """Override merchant default 3DS behaviour for this subscription"""

    metadata: Dict[str, str]
    """Additional metadata for the subscription Defaults to empty if not specified"""

    on_demand: Optional[OnDemandSubscriptionParam]

    one_time_product_cart: Optional[Iterable[OneTimeProductCart]]
    """
    List of one time products that will be bundled with the first payment for this
    subscription
    """

    payment_link: Optional[bool]
    """If true, generates a payment link. Defaults to false if not specified."""

    payment_method_id: Optional[str]
    """
    Optional payment method ID to use for this subscription. If provided,
    customer_id must also be provided (via AttachExistingCustomer). The payment
    method will be validated for eligibility with the subscription's currency.
    """

    redirect_immediately: bool
    """
    If true, redirects the customer immediately after payment completion False by
    default
    """

    return_url: Optional[str]
    """Optional URL to redirect after successful subscription creation"""

    short_link: Optional[bool]
    """If true, returns a shortened payment link. Defaults to false if not specified."""

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


class OneTimeProductCart(TypedDict, total=False):
    product_id: Required[str]

    quantity: Required[int]

    amount: Optional[int]
    """Amount the customer pays if pay_what_you_want is enabled.

    If disabled then amount will be ignored Represented in the lowest denomination
    of the currency (e.g., cents for USD). For example, to charge $1.00, pass `100`.
    """
