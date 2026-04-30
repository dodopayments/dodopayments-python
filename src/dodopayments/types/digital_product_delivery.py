# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .digital_product_delivery_file import DigitalProductDeliveryFile

__all__ = ["DigitalProductDelivery"]


class DigitalProductDelivery(BaseModel):
    """Digital-product-delivery payload for a grant.

    Populated for grants whose
    entitlement has `integration_type = 'digital_files'`. `files` carries
    presigned download URLs; the source (EE service or legacy in-process S3
    presigning) is opaque to the caller.
    """

    files: List[DigitalProductDeliveryFile]

    external_url: Optional[str] = None

    instructions: Optional[str] = None
