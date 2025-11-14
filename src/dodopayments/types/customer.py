# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Customer"]


class Customer(BaseModel):
    business_id: str

    created_at: datetime

    customer_id: str

    email: str

    name: str

    metadata: Optional[Dict[str, str]] = None
    """Additional metadata for the customer"""

    phone_number: Optional[str] = None
