# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["CustomerLimitedDetails"]


class CustomerLimitedDetails(BaseModel):
    customer_id: str
    """Unique identifier for the customer"""

    email: str
    """Email address of the customer"""

    name: str
    """Full name of the customer"""

    phone_number: Optional[str] = None
    """Phone number of the customer"""
