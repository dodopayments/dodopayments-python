# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["ProductCollectionUpdateParams"]


class ProductCollectionUpdateParams(TypedDict, total=False):
    brand_id: Optional[str]
    """Optional brand_id update"""

    description: Optional[str]
    """Optional description update - pass null to remove, omit to keep unchanged"""

    group_order: Optional[SequenceNotStr[str]]
    """Optional new order for groups (array of group UUIDs in desired order)"""

    image_id: Optional[str]
    """Optional image update - pass null to remove, omit to keep unchanged"""

    name: Optional[str]
    """Optional new name for the collection"""
