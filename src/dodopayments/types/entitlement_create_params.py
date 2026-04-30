# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

from .integration_config_param import IntegrationConfigParam
from .entitlement_integration_type import EntitlementIntegrationType

__all__ = ["EntitlementCreateParams"]


class EntitlementCreateParams(TypedDict, total=False):
    integration_config: Required[IntegrationConfigParam]
    """Platform-specific configuration (validated per integration_type)"""

    integration_type: Required[EntitlementIntegrationType]
    """Which platform integration this entitlement uses"""

    name: Required[str]
    """Display name for this entitlement"""

    description: Optional[str]
    """Optional description"""

    metadata: Optional[Dict[str, str]]
    """Optional user-facing metadata"""
