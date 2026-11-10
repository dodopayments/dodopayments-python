# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .metadata import Metadata

__all__ = ["Customer"]


class Customer(BaseModel):
    business_id: str

    created_at: datetime

    customer_id: str

    email: str

    name: str

    blocked_at: Optional[datetime] = None
    """When the merchant blocked this customer.

    The dashboard shows the "Blocked" badge and the unblock action from it. The list
    route leaves it empty; only the single-customer route resolves it.
    """

    blocklist_entry_id: Optional[str] = None
    """Blocklist entry behind `blocked_at`, so the dashboard can link to it."""

    metadata: Optional[Metadata] = None
    """Additional metadata for the customer"""

    phone_number: Optional[str] = None
