# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["InvoiceEvent"]


class InvoiceEvent(BaseModel):
    actor: str
    """A user ID, `api_key`, `customer` or `system`."""

    created_at: datetime

    event_id: str

    event_type: str

    payload: object

    row_version: int

    actor_email: Optional[str] = None
