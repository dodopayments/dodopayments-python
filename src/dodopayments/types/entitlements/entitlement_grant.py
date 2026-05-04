# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .license_key_grant import LicenseKeyGrant
from ..digital_product_delivery import DigitalProductDelivery

__all__ = ["EntitlementGrant"]


class EntitlementGrant(BaseModel):
    """
    Detailed view of a single entitlement grant: who it's for, its
    lifecycle state, and any integration-specific delivery payload.
    """

    id: str
    """Unique identifier of the grant."""

    business_id: str
    """Identifier of the business that owns the grant."""

    created_at: datetime
    """Timestamp when the grant was created."""

    customer_id: str
    """Identifier of the customer the grant was issued to."""

    entitlement_id: str
    """Identifier of the entitlement this grant was issued from."""

    metadata: Dict[str, str]
    """Arbitrary key-value metadata recorded on the grant."""

    status: Literal["Pending", "Delivered", "Failed", "Revoked"]
    """Lifecycle status of the grant."""

    updated_at: datetime
    """Timestamp when the grant was last modified."""

    delivered_at: Optional[datetime] = None
    """Timestamp when the grant transitioned to `delivered`, when applicable."""

    digital_product_delivery: Optional[DigitalProductDelivery] = None
    """
    Digital-product-delivery payload, present when the entitlement integration is
    `digital_files`.
    """

    error_code: Optional[str] = None
    """Machine-readable code reported when delivery failed, when applicable."""

    error_message: Optional[str] = None
    """Human-readable message reported when delivery failed, when applicable."""

    license_key: Optional[LicenseKeyGrant] = None
    """
    License-key delivery payload, present when the entitlement integration is
    `license_key`.
    """

    oauth_expires_at: Optional[datetime] = None
    """Timestamp when `oauth_url` stops being valid, when applicable."""

    oauth_url: Optional[str] = None
    """Customer-facing OAuth URL for OAuth-style integrations.

    Populated during the customer-portal accept flow; `null` until the customer
    completes that step, and on grants for non-OAuth integrations.
    """

    payment_id: Optional[str] = None
    """Identifier of the payment that triggered this grant, when applicable."""

    revocation_reason: Optional[str] = None
    """Reason recorded when the grant was revoked, when applicable."""

    revoked_at: Optional[datetime] = None
    """Timestamp when the grant transitioned to `revoked`, when applicable."""

    subscription_id: Optional[str] = None
    """Identifier of the subscription that triggered this grant, when applicable."""
