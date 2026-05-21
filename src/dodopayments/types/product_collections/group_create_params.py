# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .group_product_param import GroupProductParam

__all__ = ["GroupCreateParams"]


class GroupCreateParams(TypedDict, total=False):
    products: Required[Iterable[GroupProductParam]]
    """Products in this group"""

    group_name: Optional[str]
    """Optional group name.

    Multiple groups can have null names, but named groups must be unique per
    collection
    """

    status: Optional[bool]
    """Status of the group (defaults to true if not provided)"""
