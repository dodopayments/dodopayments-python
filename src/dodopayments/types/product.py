# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .price import Price
from .._models import BaseModel
from .currency import Currency
from .tax_category import TaxCategory
from .time_interval import TimeInterval
from .license_key_duration import LicenseKeyDuration

__all__ = ["Product", "CreditEntitlement", "DigitalProductDelivery", "DigitalProductDeliveryFile"]


class CreditEntitlement(BaseModel):
    """Response struct for credit entitlement mapping"""

    id: str
    """Unique ID of this mapping"""

    credit_entitlement_id: str
    """ID of the credit entitlement"""

    credit_entitlement_name: str
    """Name of the credit entitlement"""

    credit_entitlement_unit: str
    """Unit label for the credit entitlement"""

    credits_amount: str
    """Number of credits granted"""

    credits_reduce_overage: bool
    """Whether new credit grants reduce existing overage"""

    overage_charge_at_billing: bool
    """Whether overage is charged at billing"""

    overage_enabled: bool
    """Whether overage is enabled"""

    preserve_overage_at_reset: bool
    """Whether to preserve overage balance when credits reset"""

    proration_behavior: Literal["prorate", "no_prorate"]
    """Proration behavior for credit grants during plan changes"""

    rollover_enabled: bool
    """Whether rollover is enabled"""

    trial_credits_expire_after_trial: bool
    """Whether trial credits expire after trial"""

    currency: Optional[Currency] = None
    """Currency"""

    expires_after_days: Optional[int] = None
    """Days until credits expire"""

    low_balance_threshold_percent: Optional[int] = None
    """Low balance threshold percentage"""

    max_rollover_count: Optional[int] = None
    """Maximum rollover cycles"""

    overage_limit: Optional[str] = None
    """Overage limit"""

    price_per_unit: Optional[str] = None
    """Price per unit"""

    rollover_percentage: Optional[int] = None
    """Rollover percentage"""

    rollover_timeframe_count: Optional[int] = None
    """Rollover timeframe count"""

    rollover_timeframe_interval: Optional[TimeInterval] = None
    """Rollover timeframe interval"""

    trial_credits: Optional[str] = None
    """Trial credits"""


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

    credit_entitlements: List[CreditEntitlement]
    """Attached credit entitlements with settings"""

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
