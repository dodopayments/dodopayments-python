# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["OneTimeProductCartItemParam"]


class OneTimeProductCartItemParam(TypedDict, total=False):
    product_id: Required[str]

    quantity: Required[int]

    amount: Optional[int]
    """Amount the customer pays if pay_what_you_want is enabled.

    If disabled then amount will be ignored
    """
