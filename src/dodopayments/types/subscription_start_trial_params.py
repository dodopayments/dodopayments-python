# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .currency import Currency
from .country_code import CountryCode
from .collection_method import CollectionMethod

__all__ = [
    "SubscriptionStartTrialParams",
    "BillingAddress",
    "PaymentTerms",
    "PaymentTermsDueOnReceipt",
    "PaymentTermsNet",
]


class SubscriptionStartTrialParams(TypedDict, total=False):
    collection_method: Required[CollectionMethod]

    currency: Required[Currency]

    customer_id: Required[str]

    product_id: Required[str]
    """A recurring product."""

    billing_address: Optional[BillingAddress]
    """The billing address of an invoice request."""

    payment_method_id: Optional[str]
    """A saved card of the customer. Automatic charge needs it."""

    payment_terms: Optional[PaymentTerms]
    """The terms of the invoices after the trial."""

    quantity: int

    review_required: bool
    """`true` keeps each renewal draft for review before it finalises."""

    tax_id: Optional[str]

    trial_period_days: Optional[int]
    """1 to 730 days.

    When this is not set, the product trial applies and the trial misuse check runs.
    """

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]


class BillingAddress(TypedDict, total=False):
    """The billing address of an invoice request."""

    country: Required[CountryCode]
    """Two-letter ISO country code (ISO 3166-1 alpha-2)"""

    city: Optional[str]

    state: Optional[str]

    street: Optional[str]

    zipcode: Optional[str]


class PaymentTermsDueOnReceipt(TypedDict, total=False):
    type: Required[Literal["due_on_receipt"]]


class PaymentTermsNet(TypedDict, total=False):
    days: Required[int]

    type: Required[Literal["net"]]


PaymentTerms: TypeAlias = Union[PaymentTermsDueOnReceipt, PaymentTermsNet]
