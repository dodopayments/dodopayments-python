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

    Untagged enum: variants are matched in order. `FeatureFlag` must precede
    `LicenseKey`, whose fields are all optional and would otherwise match a
    `feature_flag` config.
    """

    metadata: Optional[MetadataParam]
    """Arbitrary key-value metadata.

    Values can be string, integer, number, or boolean.
    """

    name: Optional[str]
