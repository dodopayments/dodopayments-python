# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .customer_limited_details import CustomerLimitedDetails

__all__ = ["LicenseActivateResponse", "Product"]


class Product(BaseModel):
    """Related product info. Present if the license key is tied to a product."""

    product_id: str
    """Unique identifier for the product."""

    name: Optional[str] = None
    """Name of the product, if set by the merchant."""


class LicenseActivateResponse(BaseModel):
    id: str
    """License key instance ID"""

    business_id: str
    """Business ID"""

    created_at: datetime
    """Creation timestamp"""

    customer: CustomerLimitedDetails
    """Limited customer details associated with the license key."""

    license_key_id: str
    """Associated license key ID"""

    name: str
    """Instance name"""

    product: Product
    """Related product info. Present if the license key is tied to a product."""
