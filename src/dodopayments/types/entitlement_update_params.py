# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .time_interval import TimeInterval

__all__ = [
    "EntitlementUpdateParams",
    "IntegrationConfig",
    "IntegrationConfigGitHubConfig",
    "IntegrationConfigDiscordConfig",
    "IntegrationConfigTelegramConfig",
    "IntegrationConfigFigmaConfig",
    "IntegrationConfigFramerConfig",
    "IntegrationConfigNotionConfig",
    "IntegrationConfigDigitalFilesConfig",
    "IntegrationConfigLicenseKeyConfig",
]


class EntitlementUpdateParams(TypedDict, total=False):
    description: Optional[str]

    integration_config: Optional[IntegrationConfig]
    """
    Platform-specific configuration for an entitlement. Each variant uses unique
    field names so `#[serde(untagged)]` can disambiguate correctly.
    """

    metadata: Optional[Dict[str, str]]

    name: Optional[str]


class IntegrationConfigGitHubConfig(TypedDict, total=False):
    permission: Required[str]
    """One of: pull, push, admin, maintain, triage"""

    target_id: Required[str]


class IntegrationConfigDiscordConfig(TypedDict, total=False):
    guild_id: Required[str]

    role_id: Optional[str]


class IntegrationConfigTelegramConfig(TypedDict, total=False):
    chat_id: Required[str]


class IntegrationConfigFigmaConfig(TypedDict, total=False):
    figma_file_id: Required[str]


class IntegrationConfigFramerConfig(TypedDict, total=False):
    framer_template_id: Required[str]


class IntegrationConfigNotionConfig(TypedDict, total=False):
    notion_template_id: Required[str]


class IntegrationConfigDigitalFilesConfig(TypedDict, total=False):
    digital_file_ids: Required[SequenceNotStr[str]]

    external_url: Optional[str]

    instructions: Optional[str]

    legacy_file_ids: Optional[SequenceNotStr[str]]
    """Three-way patchable field (mirrors the credit_entitlements pattern):

    - omitted → preserve persisted (`None`)
    - `null` → clear (`Some(None)`)
    - `[...]` → replace (`Some(Some(...))`)

    On Create / storage we collapse "clear" and empty-array to `None` so the
    persisted JSONB never carries a `null` legacy_file_ids key.
    """


class IntegrationConfigLicenseKeyConfig(TypedDict, total=False):
    activation_message: Optional[str]

    activations_limit: Optional[int]

    duration_count: Optional[int]

    duration_interval: Optional[TimeInterval]


IntegrationConfig: TypeAlias = Union[
    IntegrationConfigGitHubConfig,
    IntegrationConfigDiscordConfig,
    IntegrationConfigTelegramConfig,
    IntegrationConfigFigmaConfig,
    IntegrationConfigFramerConfig,
    IntegrationConfigNotionConfig,
    IntegrationConfigDigitalFilesConfig,
    IntegrationConfigLicenseKeyConfig,
]
