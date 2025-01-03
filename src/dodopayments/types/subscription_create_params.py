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

    quantity: Required[int]

    metadata: Dict[str, str]

    payment_link: Optional[bool]
    """False by default"""

    return_url: Optional[str]

    trial_period_days: Optional[int]
    """
    If specified this will override the trial period days given in the products
    price
    """


class Billing(TypedDict, total=False):
    city: Required[str]

    country: Required[CountryCode]
    """ISO country code alpha2 variant"""

    state: Required[str]

    street: Required[str]

    zipcode: Required[int]


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
