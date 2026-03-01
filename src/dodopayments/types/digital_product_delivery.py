# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .digital_product_delivery_file import DigitalProductDeliveryFile

__all__ = ["DigitalProductDelivery"]


class DigitalProductDelivery(BaseModel):
    external_url: Optional[str] = None
    """External URL to digital product"""

    files: Optional[List[DigitalProductDeliveryFile]] = None
    """Uploaded files ids of digital product"""

    instructions: Optional[str] = None
    """Instructions to download and use the digital product"""
