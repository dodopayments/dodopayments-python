# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .integration_config_response import IntegrationConfigResponse
from .entitlement_integration_type import EntitlementIntegrationType

__all__ = ["ProductEntitlementSummary"]


class ProductEntitlementSummary(BaseModel):
    """Summary of an entitlement attached to a product.

    `integration_config` uses [`IntegrationConfigResponse`] (NOT the
    persisted [`IntegrationConfig`]) so digital_files entitlements embed the
    resolved `digital_files` object — matching what `GET /entitlements/{id}`
    returns. All other variants pass through unchanged via
    `#[serde(untagged)]`.
    """

    id: str

    integration_config: IntegrationConfigResponse
    """Integration-specific configuration on an entitlement read response.

    For `digital_files` entitlements the response includes presigned download URLs
    for each attached file; other integrations match the shape supplied at creation.
    """

    integration_type: EntitlementIntegrationType

    name: str

    description: Optional[str] = None
