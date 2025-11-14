# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["SubscriptionUpdatePaymentMethodParams", "Variant0", "Variant1"]


class Variant0(TypedDict, total=False):
    type: Required[Literal["new"]]

    return_url: Optional[str]


class Variant1(TypedDict, total=False):
    payment_method_id: Required[str]

    type: Required[Literal["existing"]]


SubscriptionUpdatePaymentMethodParams: TypeAlias = Union[Variant0, Variant1]
