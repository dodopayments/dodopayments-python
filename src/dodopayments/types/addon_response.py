# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .currency import Currency
from .tax_category import TaxCategory

__all__ = ["AddonResponse"]


class AddonResponse(BaseModel):
    id: str
    """id of the Addon"""

    business_id: str
    """Unique identifier for the business to which the addon belongs."""

    created_at: datetime
    """Created time"""

    currency: Currency

    name: str
    """Name of the Addon"""

    price: int
    """Amount of the addon"""

    tax_category: TaxCategory
    """
    Represents the different categories of taxation applicable to various products
    and services.
    """

    updated_at: datetime
    """Updated time"""

    description: Optional[str] = None
    """Optional description of the Addon"""

    image: Optional[str] = None
    """Image of the Addon"""
