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
    """Public-facing variant of [`IntegrationConfig`].

    Mirrors every variant shape on the wire EXCEPT `DigitalFiles`, which is replaced
    with a hydrated `digital_files` object (resolved download URLs etc.). The
    persisted JSONB stays ID-only via [`IntegrationConfig`]; this enum is
    response-only.
    """

    integration_type: EntitlementIntegrationType

    name: str

    description: Optional[str] = None
