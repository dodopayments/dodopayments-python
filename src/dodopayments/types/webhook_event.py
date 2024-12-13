# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["WebhookEvent"]


class WebhookEvent(BaseModel):
    business_id: str

    created_at: datetime

    event_id: str

    event_type: str

    object_id: str

    latest_attempted_at: Optional[datetime] = None

    request: Optional[str] = None

    response: Optional[str] = None
