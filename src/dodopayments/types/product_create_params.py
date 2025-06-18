# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, TypedDict

from .price_param import PriceParam
from .tax_category import TaxCategory
from .license_key_duration_param import LicenseKeyDurationParam

__all__ = ["ProductCreateParams", "DigitalProductDelivery"]


class ProductCreateParams(TypedDict, total=False):
    price: Required[PriceParam]

    tax_category: Required[TaxCategory]
    """
    Represents the different categories of taxation applicable to various products
    and services.
    """

    addons: Optional[List[str]]
    """Addons available for subscription product"""

    brand_id: Optional[str]
    """Brand id for the product, if not provided will default to primary brand"""

    description: Optional[str]
    """Optional description of the product"""

    digital_product_delivery: Optional[DigitalProductDelivery]

    license_key_activation_message: Optional[str]
    """Optional message displayed during license key activation"""

    license_key_activations_limit: Optional[int]
    """The number of times the license key can be activated. Must be 0 or greater"""

    license_key_duration: Optional[LicenseKeyDurationParam]

    license_key_enabled: Optional[bool]
    """
    When true, generates and sends a license key to your customer. Defaults to false
    """

    name: Optional[str]
    """Optional name of the product"""


class DigitalProductDelivery(TypedDict, total=False):
    external_url: Optional[str]
    """External URL to digital product"""

    instructions: Optional[str]
    """Instructions to download and use the digital product"""
