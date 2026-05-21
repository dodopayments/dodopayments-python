# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["GroupProductParam"]


class GroupProductParam(TypedDict, total=False):
    product_id: Required[str]
    """Product ID to include in the group"""

    status: Optional[bool]
    """Status of the product in this group (defaults to true if not provided)"""
