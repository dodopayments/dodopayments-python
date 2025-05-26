# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import TypedDict

from .price_param import PriceParam
from .tax_category import TaxCategory
from .license_key_duration_param import LicenseKeyDurationParam

__all__ = ["ProductUpdateParams"]


class ProductUpdateParams(TypedDict, total=False):
    addons: Optional[List[str]]
    """Available Addons for subscription products"""

    brand_id: Optional[str]

    description: Optional[str]
    """Description of the product, optional and must be at most 1000 characters."""

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

    license_key_enabled: Optional[bool]
    """Whether the product requires a license key.

    If `true`, additional fields related to license key (duration, activations
    limit, activation message) become applicable.
    """

    name: Optional[str]
    """Name of the product, optional and must be at most 100 characters."""

    price: Optional[PriceParam]

    tax_category: Optional[TaxCategory]
    """
    Represents the different categories of taxation applicable to various products
    and services.
    """
