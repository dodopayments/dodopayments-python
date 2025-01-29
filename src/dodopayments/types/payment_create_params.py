# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .misc.country_code import CountryCode

__all__ = [
    "PaymentCreateParams",
    "Billing",
    "Customer",
    "CustomerAttachExistingCustomer",
    "CustomerCreateNewCustomer",
    "ProductCart",
]


class PaymentCreateParams(TypedDict, total=False):
    billing: Required[Billing]

    customer: Required[Customer]

    product_cart: Required[Iterable[ProductCart]]
    """List of products in the cart. Must contain at least 1 and at most 100 items."""

    metadata: Dict[str, str]

    payment_link: Optional[bool]
    """Whether to generate a payment link. Defaults to false if not specified."""

    return_url: Optional[str]
    """
    Optional URL to redirect the customer after payment. Must be a valid URL if
    provided.
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
    When false, the most recently created customer object with the given email is
    used if exists. When true, a new customer object is always created False by
    default
    """

    phone_number: Optional[str]


Customer: TypeAlias = Union[CustomerAttachExistingCustomer, CustomerCreateNewCustomer]


class ProductCart(TypedDict, total=False):
    product_id: Required[str]

    quantity: Required[int]

    amount: Optional[int]
    """Amount the customer pays if pay_what_you_want is enabled.

    If disabled then amount will be ignored
    """
