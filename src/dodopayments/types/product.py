# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .price import Price
from .._models import BaseModel
from .license_key_duration import LicenseKeyDuration

__all__ = ["Product"]


class Product(BaseModel):
    business_id: str
    """Unique identifier for the business to which the product belongs."""

    created_at: datetime
    """Timestamp when the product was created."""

    is_recurring: bool
    """Indicates if the product is recurring (e.g., subscriptions)."""

    license_key_enabled: bool
    """Indicates whether the product requires a license key."""

    price: Price

    product_id: str
    """Unique identifier for the product."""

    tax_category: Literal["digital_products", "saas", "e_book", "edtech"]
    """
    Represents the different categories of taxation applicable to various products
    and services.
    """

    updated_at: datetime
    """Timestamp when the product was last updated."""

    addons: Optional[List[str]] = None
    """Available Addons for subscription products"""

    description: Optional[str] = None
    """Description of the product, optional."""

    image: Optional[str] = None
    """URL of the product image, optional."""

    license_key_activation_message: Optional[str] = None
    """Message sent upon license key activation, if applicable."""

    license_key_activations_limit: Optional[int] = None
    """Limit on the number of activations for the license key, if enabled."""

    license_key_duration: Optional[LicenseKeyDuration] = None

    name: Optional[str] = None
    """Name of the product, optional."""
