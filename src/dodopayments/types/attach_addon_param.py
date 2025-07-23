# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AttachAddonParam"]


class AttachAddonParam(TypedDict, total=False):
    addon_id: Required[str]

    quantity: Required[int]
