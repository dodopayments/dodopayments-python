# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

from .integration_config_param import IntegrationConfigParam

__all__ = ["EntitlementUpdateParams"]


class EntitlementUpdateParams(TypedDict, total=False):
    description: Optional[str]

    integration_config: Optional[IntegrationConfigParam]
    """
    Platform-specific configuration for an entitlement. Each variant uses unique
    field names so `#[serde(untagged)]` can disambiguate correctly.
    """

    metadata: Optional[Dict[str, str]]

    name: Optional[str]
