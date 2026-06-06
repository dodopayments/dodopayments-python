# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .payment_method_types import PaymentMethodTypes

__all__ = ["SubscriptionUpdatePaymentMethodParams", "PaymentMethod", "PaymentMethodNew", "PaymentMethodExisting"]


class SubscriptionUpdatePaymentMethodParams(TypedDict, total=False):
    payment_method: Required[PaymentMethod]


class PaymentMethodNew(TypedDict, total=False):
    type: Required[Literal["new"]]

    allowed_payment_method_types: Optional[List[PaymentMethodTypes]]
    """List of payment methods allowed during checkout.

    Customers will **never** see payment methods that are **not** in this list.
    However, adding a method here **does not guarantee** customers will see it.
    Availability still depends on other factors (e.g., customer location, merchant
    settings).
    """

    return_url: Optional[str]


class PaymentMethodExisting(TypedDict, total=False):
    payment_method_id: Required[str]

    type: Required[Literal["existing"]]


PaymentMethod: TypeAlias = Union[PaymentMethodNew, PaymentMethodExisting]
