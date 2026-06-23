# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .metadata_param import MetadataParam
from .integration_config_param import IntegrationConfigParam

__all__ = ["EntitlementUpdateParams"]


class EntitlementUpdateParams(TypedDict, total=False):
    description: Optional[str]

    integration_config: Optional[IntegrationConfigParam]
    """
    Integration-specific configuration supplied when creating or updating an
    entitlement. The shape required matches the entitlement's `integration_type`.
    """

    metadata: Optional[MetadataParam]

    name: Optional[str]
