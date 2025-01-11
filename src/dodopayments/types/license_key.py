# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["LicenseKey"]


class LicenseKey(BaseModel):
    id: str
    """The unique identifier of the license key."""

    business_id: str
    """The unique identifier of the business associated with the license key."""

    created_at: datetime
    """The timestamp indicating when the license key was created, in UTC."""

    customer_id: str
    """The unique identifier of the customer associated with the license key."""

    instances_count: int
    """The current number of instances activated for this license key."""

    key: str
    """The license key string."""

    payment_id: str
    """The unique identifier of the payment associated with the license key."""

    product_id: str
    """The unique identifier of the product associated with the license key."""

    status: Literal["active", "expired", "disabled"]

    activations_limit: Optional[int] = None
    """The maximum number of activations allowed for this license key."""

    expires_at: Optional[datetime] = None
    """The timestamp indicating when the license key expires, in UTC."""

    subscription_id: Optional[str] = None
    """
    The unique identifier of the subscription associated with the license key, if
    any.
    """
