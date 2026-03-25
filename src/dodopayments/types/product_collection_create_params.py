# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["ProductCollectionCreateParams", "Group", "GroupProduct"]


class ProductCollectionCreateParams(TypedDict, total=False):
    groups: Required[Iterable[Group]]
    """Groups of products in this collection"""

    name: Required[str]
    """Name of the product collection"""

    brand_id: Optional[str]
    """Brand id for the collection, if not provided will default to primary brand"""

    description: Optional[str]
    """Optional description of the product collection"""


class GroupProduct(TypedDict, total=False):
    product_id: Required[str]
    """Product ID to include in the group"""

    status: Optional[bool]
    """Status of the product in this group (defaults to true if not provided)"""


class Group(TypedDict, total=False):
    products: Required[Iterable[GroupProduct]]
    """Products in this group"""

    group_name: Optional[str]
    """Optional group name.

    Multiple groups can have null names, but named groups must be unique per
    collection
    """

    status: Optional[bool]
    """Status of the group (defaults to true if not provided)"""
