# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .discount_type import DiscountType

__all__ = ["DiscountUpdateParams"]


class DiscountUpdateParams(TypedDict, total=False):
    amount: Optional[int]
    """If present, update the discount amount:

    - If `discount_type` is `percentage`, this represents **basis points** (e.g.,
      `540` = `5.4%`).
    - Otherwise, this represents **USD cents** (e.g., `100` = `$1.00`).

    Must be at least 1 if provided.
    """

    code: Optional[str]
    """If present, update the discount code (uppercase)."""

    expires_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    name: Optional[str]

    restricted_to: Optional[List[str]]
    """
    If present, replaces all restricted product IDs with this new set. To remove all
    restrictions, send empty array
    """

    subscription_cycles: Optional[int]
    """
    Number of subscription billing cycles this discount is valid for. If not
    provided, the discount will be applied indefinitely to all recurring payments
    related to the subscription.
    """

    type: Optional[DiscountType]
    """If present, update the discount type."""

    usage_limit: Optional[int]
