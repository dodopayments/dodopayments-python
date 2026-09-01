# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["NoteUpdateParams"]


class NoteUpdateParams(TypedDict, total=False):
    entry_id: Required[str]

    note: Required[str]
