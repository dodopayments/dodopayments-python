# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .integration_config_response import IntegrationConfigResponse
from .entitlement_integration_type import EntitlementIntegrationType

__all__ = ["Entitlement"]


class Entitlement(BaseModel):
    id: str

    business_id: str

    created_at: datetime

    integration_config: IntegrationConfigResponse
    """Public-facing variant of [`IntegrationConfig`].

    Mirrors every variant shape on the wire EXCEPT `DigitalFiles`, which is replaced
    with a hydrated `digital_files` object (resolved download URLs etc.). The
    persisted JSONB stays ID-only via [`IntegrationConfig`]; this enum is
    response-only.
    """

    integration_type: EntitlementIntegrationType

    is_active: bool

    name: str

    updated_at: datetime

    description: Optional[str] = None

    metadata: Optional[object] = None
