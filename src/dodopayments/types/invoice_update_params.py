# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .currency import Currency
from .country_code import CountryCode
from .tax_category import TaxCategory
from .metadata_param import MetadataParam
from .collection_method import CollectionMethod
from .attach_addon_param import AttachAddonParam

__all__ = [
    "InvoiceUpdateParams",
    "BillingAddress",
    "Dunning",
    "Item",
    "ItemCustomItem",
    "ItemProductItem",
    "PaymentTerms",
    "PaymentTermsType",
    "PaymentTermsUnionMember1",
]


class InvoiceUpdateParams(TypedDict, total=False):
    if_match: Required[Annotated[str, PropertyInfo(alias="If-Match")]]

    billing_address: Optional[BillingAddress]
    """The billing address of an invoice request."""

    cc_emails: Optional[SequenceNotStr[str]]
    """10 addresses or fewer."""

    collection_method: Optional[CollectionMethod]

    currency: Optional[Currency]

    customer_email: Optional[str]

    customer_id: Optional[str]

    discount_ids: Optional[SequenceNotStr[str]]
    """20 codes or fewer."""

    due_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    dunning: Optional[Dunning]
    """The reminder override of one invoice.

    The business settings fill the other dunning values.
    """

    items: Optional[Iterable[Item]]
    """1 to 50 items."""

    memo: Optional[str]

    metadata: Optional[MetadataParam]
    """Arbitrary key-value metadata.

    Values can be string, integer, number, or boolean.
    """

    payment_terms: Optional[PaymentTerms]

    review_required: Optional[bool]

    tax_id: Optional[str]


class BillingAddress(TypedDict, total=False):
    """The billing address of an invoice request."""

    country: Required[CountryCode]
    """Two-letter ISO country code (ISO 3166-1 alpha-2)"""

    city: Optional[str]

    state: Optional[str]

    street: Optional[str]

    zipcode: Optional[str]


class Dunning(TypedDict, total=False):
    """The reminder override of one invoice.

    The business settings fill the other dunning values.
    """

    reminders_enabled: Required[bool]

    offsets_days: Optional[Iterable[int]]
    """Days from the due date.

    A negative value sends the reminder before the due date.
    """


class ItemCustomItem(TypedDict, total=False):
    """A line that exists only on this invoice."""

    description: Required[str]

    kind: Required[Literal["custom"]]

    tax_category: Required[TaxCategory]
    """
    Represents the different categories of taxation applicable to various products
    and services.
    """

    unit_amount: Required[int]
    """The price in the smallest currency unit."""

    quantity: Optional[int]
    """The default is 1."""


class ItemProductItem(TypedDict, total=False):
    product_id: Required[str]

    quantity: Required[int]

    addons: Optional[Iterable[AttachAddonParam]]


Item: TypeAlias = Union[ItemCustomItem, ItemProductItem]


class PaymentTermsType(TypedDict, total=False):
    type: Required[Literal["due_on_receipt"]]


class PaymentTermsUnionMember1(TypedDict, total=False):
    days: Required[int]

    type: Required[Literal["net"]]


PaymentTerms: TypeAlias = Union[PaymentTermsType, PaymentTermsUnionMember1]
