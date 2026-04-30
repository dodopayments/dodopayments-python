# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .time_interval import TimeInterval

__all__ = [
    "IntegrationConfigParam",
    "GitHubConfig",
    "DiscordConfig",
    "TelegramConfig",
    "FigmaConfig",
    "FramerConfig",
    "NotionConfig",
    "DigitalFilesConfig",
    "LicenseKeyConfig",
]


class GitHubConfig(TypedDict, total=False):
    permission: Required[str]
    """One of: pull, push, admin, maintain, triage"""

    target_id: Required[str]


class DiscordConfig(TypedDict, total=False):
    guild_id: Required[str]

    role_id: Optional[str]


class TelegramConfig(TypedDict, total=False):
    chat_id: Required[str]


class FigmaConfig(TypedDict, total=False):
    figma_file_id: Required[str]


class FramerConfig(TypedDict, total=False):
    framer_template_id: Required[str]


class NotionConfig(TypedDict, total=False):
    notion_template_id: Required[str]


class DigitalFilesConfig(TypedDict, total=False):
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


class LicenseKeyConfig(TypedDict, total=False):
    activation_message: Optional[str]

    activations_limit: Optional[int]

    duration_count: Optional[int]

    duration_interval: Optional[TimeInterval]


IntegrationConfigParam: TypeAlias = Union[
    GitHubConfig,
    DiscordConfig,
    TelegramConfig,
    FigmaConfig,
    FramerConfig,
    NotionConfig,
    DigitalFilesConfig,
    LicenseKeyConfig,
]
