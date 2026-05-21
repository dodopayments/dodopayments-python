# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["ProductCollectionListResponse"]


class ProductCollectionListResponse(BaseModel):
    id: str
    """Collection ID"""

    created_at: datetime
    """Timestamp when created"""

    name: str
    """Collection name"""

    products_count: int
    """Number of products in the collection"""

    updated_at: datetime
    """Timestamp when last updated"""

    description: Optional[str] = None
    """Collection description"""

    image: Optional[str] = None
    """Collection image URL"""
