# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["BlockedCustomerNote"]


class BlockedCustomerNote(BaseModel):
    id: str

    created_at: datetime

    note: str

    author_email: Optional[str] = None

    updated_at: Optional[datetime] = None
