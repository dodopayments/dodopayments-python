# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .digital_product_delivery_file import DigitalProductDeliveryFile

__all__ = ["DigitalProductDelivery"]


class DigitalProductDelivery(BaseModel):
    """
    Digital-product-delivery payload, present on grants for `digital_files`
    entitlements. Each file carries a short-lived presigned download URL.
    """

    files: List[DigitalProductDeliveryFile]
    """One entry per attached file."""

    external_url: Optional[str] = None
    """Optional external URL, passed through from the entitlement configuration."""

    instructions: Optional[str] = None
    """
    Optional human-readable delivery instructions, passed through from the
    entitlement configuration.
    """
