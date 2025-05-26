# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["BrandCreateResponse"]


class BrandCreateResponse(BaseModel):
    brand_id: str

    business_id: str

    enabled: bool

    statement_descriptor: str

    verification_enabled: bool

    verification_status: Literal["Success", "Fail", "Review", "Hold"]

    description: Optional[str] = None

    image: Optional[str] = None

    name: Optional[str] = None

    reason_for_hold: Optional[str] = None
    """Incase the brand verification fails or is put on hold"""

    support_email: Optional[str] = None

    url: Optional[str] = None
