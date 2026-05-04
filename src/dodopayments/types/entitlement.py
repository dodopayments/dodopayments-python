# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel
from .integration_config_response import IntegrationConfigResponse
from .entitlement_integration_type import EntitlementIntegrationType

__all__ = ["Entitlement"]


class Entitlement(BaseModel):
    """
    Detailed view of a single entitlement: identity, integration type,
    integration-specific configuration, and metadata.
    """

    id: str
    """Unique identifier of the entitlement."""

    business_id: str
    """Identifier of the business that owns this entitlement."""

    created_at: datetime
    """Timestamp when the entitlement was created."""

    integration_config: IntegrationConfigResponse
    """Integration-specific configuration.

    For `digital_files` entitlements this includes presigned download URLs for each
    attached file.
    """

    integration_type: EntitlementIntegrationType
    """Platform integration this entitlement uses."""

    is_active: bool
    """
    Always `true` for entitlements returned by the public API; soft-deleted
    entitlements are not returned.
    """

    metadata: Dict[str, str]
    """Arbitrary key-value metadata supplied at creation or via PATCH."""

    name: str
    """Display name supplied at creation."""

    updated_at: datetime
    """Timestamp when the entitlement was last modified."""

    description: Optional[str] = None
    """Optional description supplied at creation."""
