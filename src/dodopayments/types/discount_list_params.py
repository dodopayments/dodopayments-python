# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["DiscountListParams"]


class DiscountListParams(TypedDict, total=False):
    page_number: int
    """Page number (default = 0)."""

    page_size: int
    """Page size (default = 10, max = 100)."""
