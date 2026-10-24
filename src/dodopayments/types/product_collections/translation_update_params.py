# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["TranslationUpdateParams"]


class TranslationUpdateParams(TypedDict, total=False):
    id: Required[str]

    description: Optional[str]
    """The translated description."""

    name: Optional[str]
    """The translated name."""
