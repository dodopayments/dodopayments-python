# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..price import Price
from ..._models import BaseModel
from ..currency import Currency
from ..tax_category import TaxCategory

__all__ = ["GroupCreateResponse", "Product"]


class Product(BaseModel):
    id: str

    addons_count: int

    files_count: int

    has_credit_entitlements: bool
    """Whether this product has any credit entitlements attached"""

    is_recurring: bool

    license_key_enabled: bool

    meters_count: int

    product_id: str

    status: bool

    currency: Optional[Currency] = None

    description: Optional[str] = None

    name: Optional[str] = None

    price: Optional[int] = None

    price_detail: Optional[Price] = None
    """One-time price details."""

    tax_category: Optional[TaxCategory] = None
    """
    Represents the different categories of taxation applicable to various products
    and services.
    """

    tax_inclusive: Optional[bool] = None


class GroupCreateResponse(BaseModel):
    group_id: str

    products: List[Product]

    status: bool

    group_name: Optional[str] = None
