# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .product_collections.product_collection_group_details_param import ProductCollectionGroupDetailsParam

__all__ = ["ProductCollectionCreateParams"]


class ProductCollectionCreateParams(TypedDict, total=False):
    groups: Required[Iterable[ProductCollectionGroupDetailsParam]]
    """Groups of products in this collection"""

    name: Required[str]
    """Name of the product collection"""

    brand_id: Optional[str]
    """Brand id for the collection, if not provided will default to primary brand"""

    description: Optional[str]
    """Optional description of the product collection"""
