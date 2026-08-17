# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["BrandListParams"]


class BrandListParams(TypedDict, total=False):
    include_archived: bool
    """Set to true to also list archived brands. Default false."""
