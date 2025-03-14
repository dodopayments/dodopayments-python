# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .discount_type import DiscountType

__all__ = ["Discount"]


class Discount(BaseModel):
    amount: int
    """The discount amount.

    - If `discount_type` is `percentage`, this is in **basis points** (e.g., 540 =>
      5.4%).
    - Otherwise, this is **USD cents** (e.g., 100 => `$1.00`).
    """

    business_id: str
    """The business this discount belongs to."""

    code: str
    """The discount code (up to 16 chars)."""

    created_at: datetime
    """Timestamp when the discount is created"""

    discount_id: str
    """The unique discount ID"""

    restricted_to: List[str]
    """List of product IDs to which this discount is restricted."""

    times_used: int
    """How many times this discount has been used."""

    type: DiscountType

    expires_at: Optional[datetime] = None
    """Optional date/time after which discount is expired."""

    name: Optional[str] = None
    """Name for the Discount"""

    usage_limit: Optional[int] = None
    """Usage limit for this discount, if any."""
