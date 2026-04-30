# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .digital_product_delivery import DigitalProductDelivery

__all__ = ["EntitlementGrantFailedWebhookEvent", "Data", "DataLicenseKey"]


class DataLicenseKey(BaseModel):
    """Present only when the entitlement integration_type is `license_key`."""

    activations_used: int

    key: str

    activations_limit: Optional[int] = None

    expires_at: Optional[datetime] = None


class Data(BaseModel):
    id: str

    business_id: str

    created_at: datetime

    customer_id: str

    entitlement_id: str

    external_id: str

    status: Literal["Pending", "Delivered", "Failed", "Revoked"]

    updated_at: datetime

    delivered_at: Optional[datetime] = None

    digital_product_delivery: Optional[DigitalProductDelivery] = None
    """
    Present only when the entitlement integration_type is `digital_files`. Populated
    eagerly on every list and single-record endpoint.
    """

    error_code: Optional[str] = None

    error_message: Optional[str] = None

    license_key: Optional[DataLicenseKey] = None
    """Present only when the entitlement integration_type is `license_key`."""

    metadata: Optional[object] = None

    oauth_expires_at: Optional[datetime] = None

    oauth_url: Optional[str] = None

    payment_id: Optional[str] = None

    revocation_reason: Optional[str] = None

    revoked_at: Optional[datetime] = None

    subscription_id: Optional[str] = None


class EntitlementGrantFailedWebhookEvent(BaseModel):
    business_id: str
    """The business identifier"""

    data: Data

    timestamp: datetime
    """The timestamp of when the event occurred"""

    type: Literal["entitlement_grant.failed"]
    """The event type"""
