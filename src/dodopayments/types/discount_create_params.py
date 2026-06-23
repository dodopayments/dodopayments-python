# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .discount_type import DiscountType
from .metadata_param import MetadataParam

__all__ = ["DiscountCreateParams"]


class DiscountCreateParams(TypedDict, total=False):
    amount: Required[int]
    """The discount amount in **basis points** (e.g.

    `540` means `5.4%`, `10000` means `100%`).

    Must be at least 1.
    """

    type: Required[DiscountType]
    """The discount type. Currently only `percentage` is supported."""

    code: Optional[str]
    """Optionally supply a code (will be uppercased).

    - Must be at least 3 characters if provided.
    - If omitted, a random 16-character code is generated.
    """

    expires_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """When the discount expires, if ever."""

    metadata: MetadataParam
    """Additional metadata for the discount"""

    name: Optional[str]

    preserve_on_plan_change: bool
    """
    Whether this discount should be preserved when a subscription changes plans.
    Default: false (discount is removed on plan change)
    """

    restricted_to: Optional[SequenceNotStr[str]]
    """List of product IDs to restrict usage (if any)."""

    subscription_cycles: Optional[int]
    """
    Number of subscription billing cycles this discount is valid for. If not
    provided, the discount will be applied indefinitely to all recurring payments
    related to the subscription.
    """

    usage_limit: Optional[int]
    """How many times this discount can be used (if any). Must be >= 1 if provided."""
