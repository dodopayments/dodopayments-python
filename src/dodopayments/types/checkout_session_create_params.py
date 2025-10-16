# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .currency import Currency
from .country_code import CountryCode
from .attach_addon_param import AttachAddonParam
from .payment_method_types import PaymentMethodTypes
from .customer_request_param import CustomerRequestParam
from .on_demand_subscription_param import OnDemandSubscriptionParam

__all__ = [
    "CheckoutSessionCreateParams",
    "ProductCart",
    "BillingAddress",
    "Customization",
    "FeatureFlags",
    "SubscriptionData",
]


class CheckoutSessionCreateParams(TypedDict, total=False):
    product_cart: Required[Iterable[ProductCart]]

    allowed_payment_method_types: Optional[List[PaymentMethodTypes]]
    """
    Customers will never see payment methods that are not in this list. However,
    adding a method here does not guarantee customers will see it. Availability
    still depends on other factors (e.g., customer location, merchant settings).

    Disclaimar: Always provide 'credit' and 'debit' as a fallback. If all payment
    methods are unavailable, checkout session will fail.
    """

    billing_address: Optional[BillingAddress]
    """Billing address information for the session"""

    billing_currency: Optional[Currency]
    """This field is ingored if adaptive pricing is disabled"""

    confirm: bool
    """If confirm is true, all the details will be finalized.

    If required data is missing, an API error is thrown.
    """

    customer: Optional[CustomerRequestParam]
    """Customer details for the session"""

    customization: Customization
    """Customization for the checkout session page"""

    discount_code: Optional[str]

    feature_flags: FeatureFlags

    force_3ds: Optional[bool]
    """Override merchant default 3DS behaviour for this session"""

    metadata: Optional[Dict[str, str]]
    """Additional metadata associated with the payment.

    Defaults to empty if not provided.
    """

    return_url: Optional[str]
    """The url to redirect after payment failure or success."""

    show_saved_payment_methods: bool
    """Display saved payment methods of a returning customer False by default"""

    subscription_data: Optional[SubscriptionData]


class ProductCart(TypedDict, total=False):
    product_id: Required[str]
    """unique id of the product"""

    quantity: Required[int]

    addons: Optional[Iterable[AttachAddonParam]]
    """only valid if product is a subscription"""

    amount: Optional[int]
    """Amount the customer pays if pay_what_you_want is enabled.

    If disabled then amount will be ignored Represented in the lowest denomination
    of the currency (e.g., cents for USD). For example, to charge $1.00, pass `100`.
    Only applicable for one time payments

    If amount is not set for pay_what_you_want product, customer is allowed to
    select the amount.
    """


class BillingAddress(TypedDict, total=False):
    country: Required[CountryCode]
    """Two-letter ISO country code (ISO 3166-1 alpha-2)"""

    city: Optional[str]
    """City name"""

    state: Optional[str]
    """State or province name"""

    street: Optional[str]
    """Street address including house number and unit/apartment if applicable"""

    zipcode: Optional[str]
    """Postal code or ZIP code"""


class Customization(TypedDict, total=False):
    force_language: Optional[str]
    """Force the checkout interface to render in a specific language (e.g. `en`, `es`)"""

    show_on_demand_tag: bool
    """Show on demand tag

    Default is true
    """

    show_order_details: bool
    """Show order details by default

    Default is true
    """

    theme: Literal["dark", "light", "system"]
    """Theme of the page

    Default is `System`.
    """


class FeatureFlags(TypedDict, total=False):
    allow_currency_selection: bool
    """if customer is allowed to change currency, set it to true

    Default is true
    """

    allow_discount_code: bool
    """If the customer is allowed to apply discount code, set it to true.

    Default is true
    """

    allow_phone_number_collection: bool
    """If phone number is collected from customer, set it to rue

    Default is true
    """

    allow_tax_id: bool
    """If the customer is allowed to add tax id, set it to true

    Default is true
    """

    always_create_new_customer: bool
    """
    Set to true if a new customer object should be created. By default email is used
    to find an existing customer to attach the session to

    Default is false
    """


class SubscriptionData(TypedDict, total=False):
    on_demand: Optional[OnDemandSubscriptionParam]

    trial_period_days: Optional[int]
    """
    Optional trial period in days If specified, this value overrides the trial
    period set in the product's price Must be between 0 and 10000 days
    """
