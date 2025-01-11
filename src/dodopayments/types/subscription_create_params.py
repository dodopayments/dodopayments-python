# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .misc.country_code import CountryCode

__all__ = [
    "SubscriptionCreateParams",
    "Billing",
    "Customer",
    "CustomerAttachExistingCustomer",
    "CustomerCreateNewCustomer",
]


class SubscriptionCreateParams(TypedDict, total=False):
    billing: Required[Billing]

    customer: Required[Customer]

    product_id: Required[str]
    """Unique identifier of the product to subscribe to"""

    quantity: Required[int]
    """Number of units to subscribe for. Must be at least 1."""

    metadata: Dict[str, str]

    payment_link: Optional[bool]
    """If true, generates a payment link. Defaults to false if not specified."""

    return_url: Optional[str]
    """Optional URL to redirect after successful subscription creation"""

    trial_period_days: Optional[int]
    """
    Optional trial period in days If specified, this value overrides the trial
    period set in the product's price Must be between 0 and 10000 days
    """


class Billing(TypedDict, total=False):
    city: Required[str]
    """City name"""

    country: Required[CountryCode]
    """ISO country code alpha2 variant"""

    state: Required[str]
    """State or province name"""

    street: Required[str]
    """Street address including house number and unit/apartment if applicable"""

    zipcode: Required[str]
    """Postal code or ZIP code"""


class CustomerAttachExistingCustomer(TypedDict, total=False):
    customer_id: Required[str]


class CustomerCreateNewCustomer(TypedDict, total=False):
    email: Required[str]

    name: Required[str]

    create_new_customer: bool
    """
    When true, the most recently created customer object with the given email is
    used if exists. False by default
    """

    phone_number: Optional[str]


Customer: TypeAlias = Union[CustomerAttachExistingCustomer, CustomerCreateNewCustomer]
