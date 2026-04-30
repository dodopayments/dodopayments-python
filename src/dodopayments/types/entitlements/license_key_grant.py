# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["LicenseKeyGrant"]


class LicenseKeyGrant(BaseModel):
    """Nested representation of license-key grant fields.

    Present only when the
    grant's entitlement has `integration_type = 'license_key'` and a row exists
    in `license_keys`. The grant's top-level `status` is the source of truth
    for the grant's lifecycle — no per-license-key status is exposed here.
    """

    activations_used: int

    key: str

    activations_limit: Optional[int] = None

    expires_at: Optional[datetime] = None
