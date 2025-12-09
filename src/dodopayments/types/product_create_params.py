# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr
from .price_param import PriceParam
from .tax_category import TaxCategory
from .license_key_duration_param import LicenseKeyDurationParam

__all__ = ["ProductCreateParams", "DigitalProductDelivery"]


class ProductCreateParams(TypedDict, total=False):
    name: Required[str]
    """Name of the product"""

    price: Required[PriceParam]
    """Price configuration for the product"""

    tax_category: Required[TaxCategory]
    """Tax category applied to this product"""

    addons: Optional[SequenceNotStr[str]]
    """Addons available for subscription product"""

    brand_id: Optional[str]
    """Brand id for the product, if not provided will default to primary brand"""

    description: Optional[str]
    """Optional description of the product"""

    digital_product_delivery: Optional[DigitalProductDelivery]
    """Choose how you would like you digital product delivered"""

    license_key_activation_message: Optional[str]
    """Optional message displayed during license key activation"""

    license_key_activations_limit: Optional[int]
    """The number of times the license key can be activated. Must be 0 or greater"""

    license_key_duration: Optional[LicenseKeyDurationParam]
    """
    Duration configuration for the license key. Set to null if you don't want the
    license key to expire. For subscriptions, the lifetime of the license key is
    tied to the subscription period
    """

    license_key_enabled: Optional[bool]
    """
    When true, generates and sends a license key to your customer. Defaults to false
    """

    metadata: Dict[str, str]
    """Additional metadata for the product"""


class DigitalProductDelivery(TypedDict, total=False):
    """Choose how you would like you digital product delivered"""

    external_url: Optional[str]
    """External URL to digital product"""

    instructions: Optional[str]
    """Instructions to download and use the digital product"""
