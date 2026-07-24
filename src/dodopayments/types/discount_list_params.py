# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .discount_type import DiscountType

__all__ = ["DiscountListParams"]


class DiscountListParams(TypedDict, total=False):
    active: bool
    """Filter by active status.

    `true` = currently redeemable (started, not expired, not usage-exhausted).
    `false` = not currently redeemable (expired, usage-exhausted, or pending a
    future `starts_at`).
    """

    code: str
    """Filter by discount code (partial match, case-insensitive)"""

    discount_type: DiscountType
    """Filter by discount type"""

    page_number: int
    """Page number (default = 0)."""

    page_size: int
    """Page size (default = 10, max = 100)."""

    product_id: str
    """Filter by product restriction (only discounts that apply to this product)"""
