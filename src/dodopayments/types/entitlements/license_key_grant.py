# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel
from ..license_key_status import LicenseKeyStatus

__all__ = ["LicenseKeyGrant"]


class LicenseKeyGrant(BaseModel):
    """License-key delivery payload, present on grants for `license_key`
    entitlements.

    The grant's top-level `status` is the source of truth
    for the grant's lifecycle.
    """

    id: str
    """Identifier of the issued license key."""

    activations_used: int
    """Number of instances currently active.

    Activation increments it and deactivation decrements it, so it is a live count
    and not a total.
    """

    key: str
    """Issued license key."""

    status: LicenseKeyStatus
    """Current status of the license key.

    Activation fails unless it is `active`, so a client can warn before the customer
    tries.
    """

    activations_limit: Optional[int] = None
    """Maximum activations allowed by the entitlement, when set."""

    expires_at: Optional[datetime] = None
    """When the license key expires, when applicable."""
