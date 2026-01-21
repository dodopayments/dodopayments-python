# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr
from .currency import Currency
from .country_code import CountryCode
from .attach_addon_param import AttachAddonParam
from .payment_method_types import PaymentMethodTypes
from .customer_request_param import CustomerRequestParam
from .on_demand_subscription_param import OnDemandSubscriptionParam

__all__ = [
    "CheckoutSessionPreviewParams",
    "ProductCart",
    "BillingAddress",
    "CustomField",
    "Customization",
    "FeatureFlags",
    "SubscriptionData",
]


class CheckoutSessionPreviewParams(TypedDict, total=False):
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

    custom_fields: Optional[Iterable[CustomField]]
    """Custom fields to collect from customer during checkout (max 5 fields)"""

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

    minimal_address: bool
    """
    If true, only zipcode is required when confirm is true; other address fields
    remain optional
    """

    payment_method_id: Optional[str]
    """
    Optional payment method ID to use for this checkout session. Only allowed when
    `confirm` is true. If provided, existing customer id must also be provided.
    """

    product_collection_id: Optional[str]
    """Product collection ID for collection-based checkout flow"""

    return_url: Optional[str]
    """The url to redirect after payment failure or success."""

    short_link: bool
    """If true, returns a shortened checkout URL. Defaults to false if not specified."""

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
    """Billing address information for the session"""

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


class CustomField(TypedDict, total=False):
    """Definition of a custom field for checkout"""

    field_type: Required[Literal["text", "number", "email", "url", "phone", "date", "datetime", "dropdown", "boolean"]]
    """Type of field determining validation rules"""

    key: Required[str]
    """Unique identifier for this field (used as key in responses)"""

    label: Required[str]
    """Display label shown to customer"""

    options: Optional[SequenceNotStr[str]]
    """Options for dropdown type (required for dropdown, ignored for others)"""

    placeholder: Optional[str]
    """Placeholder text for the input"""

    required: bool
    """Whether this field is required"""


class Customization(TypedDict, total=False):
    """Customization for the checkout session page"""

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

    allow_customer_editing_city: bool

    allow_customer_editing_country: bool

    allow_customer_editing_email: bool

    allow_customer_editing_name: bool

    allow_customer_editing_state: bool

    allow_customer_editing_street: bool

    allow_customer_editing_zipcode: bool

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

    redirect_immediately: bool
    """If true, redirects the customer immediately after payment completion

    Default is false
    """


class SubscriptionData(TypedDict, total=False):
    on_demand: Optional[OnDemandSubscriptionParam]

    trial_period_days: Optional[int]
    """
    Optional trial period in days If specified, this value overrides the trial
    period set in the product's price Must be between 0 and 10000 days
    """
