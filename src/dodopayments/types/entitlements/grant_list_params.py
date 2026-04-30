# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["GrantListParams"]


class GrantListParams(TypedDict, total=False):
    customer_id: str
    """Filter by customer ID"""

    page_number: int
    """Page number (default 0)"""

    page_size: int
    """Page size (default 10, max 100)"""

    status: Literal["Pending", "Delivered", "Failed", "Revoked"]
    """Filter by grant status"""
