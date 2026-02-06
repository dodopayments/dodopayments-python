# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .attach_addon_param import AttachAddonParam

__all__ = ["ProductItemReqParam"]


class ProductItemReqParam(TypedDict, total=False):
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
