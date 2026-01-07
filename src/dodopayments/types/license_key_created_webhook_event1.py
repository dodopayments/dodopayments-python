# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .license_key import LicenseKey

__all__ = ["LicenseKeyCreatedWebhookEvent"]


class LicenseKeyCreatedWebhookEvent(BaseModel):
    business_id: str
    """The business identifier"""

    data: LicenseKey

    timestamp: datetime
    """The timestamp of when the event occurred"""

    type: Literal["license_key.created"]
    """The event type"""
