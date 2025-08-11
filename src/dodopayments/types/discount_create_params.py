# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .discount_type import DiscountType

__all__ = ["DiscountCreateParams"]


class DiscountCreateParams(TypedDict, total=False):
    amount: Required[int]
    """The discount amount.

    - If `discount_type` is **not** `percentage`, `amount` is in **USD cents**. For
      example, `100` means `$1.00`. Only USD is allowed.
    - If `discount_type` **is** `percentage`, `amount` is in **basis points**. For
      example, `540` means `5.4%`.

    Must be at least 1.
    """

    type: Required[DiscountType]
    """The discount type (e.g. `percentage`, `flat`, or `flat_per_unit`)."""

    code: Optional[str]
    """Optionally supply a code (will be uppercased).

    - Must be at least 3 characters if provided.
    - If omitted, a random 16-character code is generated.
    """

    expires_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """When the discount expires, if ever."""

    name: Optional[str]

    restricted_to: Optional[List[str]]
    """List of product IDs to restrict usage (if any)."""

    subscription_cycles: Optional[int]
    """
    Number of subscription billing cycles this discount is valid for. If not
    provided, the discount will be applied indefinitely to all recurring payments
    related to the subscription.
    """

    usage_limit: Optional[int]
    """How many times this discount can be used (if any). Must be >= 1 if provided."""
