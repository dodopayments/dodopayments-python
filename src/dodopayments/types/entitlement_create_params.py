# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .time_interval import TimeInterval

__all__ = [
    "EntitlementCreateParams",
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


class EntitlementCreateParams(TypedDict, total=False):
    integration_config: Required[IntegrationConfig]
    """Platform-specific configuration (validated per integration_type)"""

    integration_type: Required[
        Literal["discord", "telegram", "github", "figma", "framer", "notion", "digital_files", "license_key"]
    ]
    """Which platform integration this entitlement uses"""

    name: Required[str]
    """Display name for this entitlement"""

    description: Optional[str]
    """Optional description"""

    metadata: Optional[Dict[str, str]]
    """Optional user-facing metadata"""


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
