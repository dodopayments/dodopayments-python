# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["LicenseKeyGrant"]


class LicenseKeyGrant(BaseModel):
    """License-key delivery payload, present on grants for `license_key`
    entitlements.

    The grant's top-level `status` is the source of truth
    for the grant's lifecycle.
    """

    activations_used: int
    """Number of activations consumed so far."""

    key: str
    """Issued license key."""

    activations_limit: Optional[int] = None
    """Maximum activations allowed by the entitlement, when set."""

    expires_at: Optional[datetime] = None
    """When the license key expires, when applicable."""
