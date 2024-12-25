# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["LicenseKey"]


class LicenseKey(BaseModel):
    id: str

    business_id: str

    created_at: datetime

    customer_id: str

    instances_count: int

    key: str

    payment_id: str

    product_id: str

    status: Literal["active", "expired", "disabled"]

    activations_limit: Optional[int] = None

    expires_at: Optional[datetime] = None

    subscription_id: Optional[str] = None
