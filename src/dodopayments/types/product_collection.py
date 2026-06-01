# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .product_collections.product_collection_group_response import ProductCollectionGroupResponse

__all__ = ["ProductCollection"]


class ProductCollection(BaseModel):
    id: str
    """Unique identifier for the product collection"""

    brand_id: str
    """Brand ID for the collection"""

    created_at: datetime
    """Timestamp when the collection was created"""

    groups: List[ProductCollectionGroupResponse]
    """Groups in this collection"""

    name: str
    """Name of the collection"""

    updated_at: datetime
    """Timestamp when the collection was last updated"""

    description: Optional[str] = None
    """Description of the collection"""

    image: Optional[str] = None
    """URL of the collection image"""
