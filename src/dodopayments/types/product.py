# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .price import Price
from .._models import BaseModel
from .tax_category import TaxCategory
from .license_key_duration import LicenseKeyDuration

__all__ = ["Product", "DigitalProductDelivery", "DigitalProductDeliveryFile"]


class DigitalProductDeliveryFile(BaseModel):
    file_id: str

    file_name: str

    url: str


class DigitalProductDelivery(BaseModel):
    external_url: Optional[str] = None
    """External URL to digital product"""

    files: Optional[List[DigitalProductDeliveryFile]] = None
    """Uploaded files ids of digital product"""

    instructions: Optional[str] = None
    """Instructions to download and use the digital product"""


class Product(BaseModel):
    brand_id: str

    business_id: str
    """Unique identifier for the business to which the product belongs."""

    created_at: datetime
    """Timestamp when the product was created."""

    is_recurring: bool
    """Indicates if the product is recurring (e.g., subscriptions)."""

    license_key_enabled: bool
    """Indicates whether the product requires a license key."""

    metadata: Dict[str, str]
    """Additional custom data associated with the product"""

    price: Price
    """Pricing information for the product."""

    product_id: str
    """Unique identifier for the product."""

    tax_category: TaxCategory
    """Tax category associated with the product."""

    updated_at: datetime
    """Timestamp when the product was last updated."""

    addons: Optional[List[str]] = None
    """Available Addons for subscription products"""

    description: Optional[str] = None
    """Description of the product, optional."""

    digital_product_delivery: Optional[DigitalProductDelivery] = None

    image: Optional[str] = None
    """URL of the product image, optional."""

    license_key_activation_message: Optional[str] = None
    """Message sent upon license key activation, if applicable."""

    license_key_activations_limit: Optional[int] = None
    """Limit on the number of activations for the license key, if enabled."""

    license_key_duration: Optional[LicenseKeyDuration] = None
    """Duration of the license key validity, if enabled."""

    name: Optional[str] = None
    """Name of the product, optional."""

    product_collection_id: Optional[str] = None
    """The product collection ID this product belongs to, if any"""
