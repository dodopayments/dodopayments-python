# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["GroupUpdateParams"]


class GroupUpdateParams(TypedDict, total=False):
    id: Required[str]

    group_name: Optional[str]
    """
    Optional group name update: Some(Some(name)) = set name, Some(None) = clear
    name, None = no change
    """

    product_order: Optional[SequenceNotStr[str]]
    """
    Optional new order for products in this group (array of
    product_collection_group_pdts UUIDs)
    """

    status: Optional[bool]
    """Optional status update"""
