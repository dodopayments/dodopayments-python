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

    metadata: Dict[str, str]

    payment_link: Optional[bool]

    return_url: Optional[str]


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

    phone_number: Optional[str]


Customer: TypeAlias = Union[CustomerAttachExistingCustomer, CustomerCreateNewCustomer]


class ProductCart(TypedDict, total=False):
    product_id: Required[str]

    quantity: Required[int]
