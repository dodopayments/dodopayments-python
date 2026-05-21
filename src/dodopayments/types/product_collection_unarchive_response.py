# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["ProductCollectionUnarchiveResponse"]


class ProductCollectionUnarchiveResponse(BaseModel):
    collection_id: str
    """Collection ID that was unarchived"""

    excluded_product_ids: List[str]
    """Product IDs that were excluded because they are archived"""

    message: str
    """Success message"""
