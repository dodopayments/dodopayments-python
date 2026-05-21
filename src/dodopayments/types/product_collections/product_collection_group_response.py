# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .groups.product_collection_product import ProductCollectionProduct

__all__ = ["ProductCollectionGroupResponse"]


class ProductCollectionGroupResponse(BaseModel):
    group_id: str

    products: List[ProductCollectionProduct]

    status: bool

    group_name: Optional[str] = None
