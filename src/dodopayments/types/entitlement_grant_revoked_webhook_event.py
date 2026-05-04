# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .entitlements.entitlement_grant import EntitlementGrant

__all__ = ["EntitlementGrantRevokedWebhookEvent"]


class EntitlementGrantRevokedWebhookEvent(BaseModel):
    business_id: str
    """The business identifier"""

    data: EntitlementGrant
    """
    Detailed view of a single entitlement grant: who it's for, its lifecycle state,
    and any integration-specific delivery payload.
    """

    timestamp: datetime
    """The timestamp of when the event occurred"""

    type: Literal["entitlement_grant.revoked"]
    """The event type"""
