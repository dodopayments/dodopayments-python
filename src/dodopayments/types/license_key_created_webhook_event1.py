# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .license_key import LicenseKey

__all__ = ["LicenseKeyCreatedWebhookEvent", "Data"]


class Data(LicenseKey):
    """Event-specific data"""

    payload_type: Optional[Literal["LicenseKey"]] = None
    """The type of payload in the data field"""


class LicenseKeyCreatedWebhookEvent(BaseModel):
    business_id: str
    """The business identifier"""

    data: Data
    """Event-specific data"""

    timestamp: datetime
    """The timestamp of when the event occurred"""

    type: Literal["license_key.created"]
    """The event type"""
