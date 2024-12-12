# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ProductListResponse", "Item"]


class Item(BaseModel):
    business_id: str

    created_at: datetime

    is_recurring: bool

    product_id: str

    tax_category: Literal["digital_products", "saas", "e_book"]
    """
    Represents the different categories of taxation applicable to various products
    and services.
    """

    updated_at: datetime

    description: Optional[str] = None

    image: Optional[str] = None

    name: Optional[str] = None

    price: Optional[int] = None


class ProductListResponse(BaseModel):
    items: List[Item]
