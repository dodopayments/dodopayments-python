# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["TranslationUpdateParams"]


class TranslationUpdateParams(TypedDict, total=False):
    id: Required[str]

    activation_message: Optional[str]
    """The translated activation message. Only a `license_key` entitlement has it."""

    description: Optional[str]
    """The translated description."""

    instructions: Optional[str]
    """The translated delivery instructions.

    Only a `digital_files` entitlement has them.
    """

    name: Optional[str]
    """The translated name."""
