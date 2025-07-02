# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .price import Price
from .._models import BaseModel
from .currency import Currency
from .tax_category import TaxCategory

__all__ = ["ProductListResponse"]


class ProductListResponse(BaseModel):
    business_id: str
    """Unique identifier for the business to which the product belongs."""

    created_at: datetime
    """Timestamp when the product was created."""

    is_recurring: bool
    """Indicates if the product is recurring (e.g., subscriptions)."""

    product_id: str
    """Unique identifier for the product."""

    tax_category: TaxCategory
    """Tax category associated with the product."""

    updated_at: datetime
    """Timestamp when the product was last updated."""

    currency: Optional[Currency] = None
    """Currency of the price"""

    description: Optional[str] = None
    """Description of the product, optional."""

    image: Optional[str] = None
    """URL of the product image, optional."""

    name: Optional[str] = None
    """Name of the product, optional."""

    price: Optional[int] = None
    """Price of the product, optional.

    The price is represented in the lowest denomination of the currency. For
    example:

    - In USD, a price of `$12.34` would be represented as `1234` (cents).
    - In JPY, a price of `¥1500` would be represented as `1500` (yen).
    - In INR, a price of `₹1234.56` would be represented as `123456` (paise).

    This ensures precision and avoids floating-point rounding errors.
    """

    price_detail: Optional[Price] = None
    """Details of the price"""

    tax_inclusive: Optional[bool] = None
    """Indicates if the price is tax inclusive"""
