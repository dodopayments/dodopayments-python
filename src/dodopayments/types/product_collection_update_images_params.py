# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["ProductCollectionUpdateImagesParams"]


class ProductCollectionUpdateImagesParams(TypedDict, total=False):
    force_update: Optional[bool]
    """If true, generates a new image ID to force cache invalidation"""
