# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import TypedDict

from .price_param import PriceParam
from .tax_category import TaxCategory
from .license_key_duration_param import LicenseKeyDurationParam

__all__ = ["ProductUpdateParams", "DigitalProductDelivery"]


class ProductUpdateParams(TypedDict, total=False):
    addons: Optional[List[str]]
    """Available Addons for subscription products"""

    brand_id: Optional[str]

    description: Optional[str]
    """Description of the product, optional and must be at most 1000 characters."""

    digital_product_delivery: Optional[DigitalProductDelivery]
    """Choose how you would like you digital product delivered"""

    image_id: Optional[str]
    """Product image id after its uploaded to S3"""

    license_key_activation_message: Optional[str]
    """Message sent to the customer upon license key activation.

    Only applicable if `license_key_enabled` is `true`. This message contains
    instructions for activating the license key.
    """

    license_key_activations_limit: Optional[int]
    """Limit for the number of activations for the license key.

    Only applicable if `license_key_enabled` is `true`. Represents the maximum
    number of times the license key can be activated.
    """

    license_key_duration: Optional[LicenseKeyDurationParam]
    """Duration of the license key if enabled.

    Only applicable if `license_key_enabled` is `true`. Represents the duration in
    days for which the license key is valid.
    """

    license_key_enabled: Optional[bool]
    """Whether the product requires a license key.

    If `true`, additional fields related to license key (duration, activations
    limit, activation message) become applicable.
    """

    metadata: Optional[Dict[str, str]]
    """Additional metadata for the product"""

    name: Optional[str]
    """Name of the product, optional and must be at most 100 characters."""

    price: Optional[PriceParam]
    """Price details of the product."""

    tax_category: Optional[TaxCategory]
    """Tax category of the product."""


class DigitalProductDelivery(TypedDict, total=False):
    external_url: Optional[str]
    """External URL to digital product"""

    files: Optional[List[str]]
    """Uploaded files ids of digital product"""

    instructions: Optional[str]
    """Instructions to download and use the digital product"""
