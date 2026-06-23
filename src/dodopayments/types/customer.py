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

    metadata: Optional[Metadata] = None
    """Additional metadata for the customer"""

    phone_number: Optional[str] = None
