# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .discount_type import DiscountType

__all__ = ["DiscountUpdateParams"]


class DiscountUpdateParams(TypedDict, total=False):
    amount: Optional[int]
    """
    If present, update the discount amount in **basis points** (e.g., `540` =
    `5.4%`, `10000` = `100%`).

    Must be at least 1 if provided.
    """

    code: Optional[str]
    """If present, update the discount code (uppercase)."""

    expires_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    metadata: Optional[Dict[str, str]]
    """Additional metadata for the discount"""

    name: Optional[str]

    preserve_on_plan_change: Optional[bool]
    """
    Whether this discount should be preserved when a subscription changes plans. If
    not provided, the existing value is kept.
    """

    restricted_to: Optional[SequenceNotStr[str]]
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
    """If present, update the discount type. Currently only `percentage` is supported."""

    usage_limit: Optional[int]
