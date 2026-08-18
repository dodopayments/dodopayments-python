# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["BrandArchiveResponse"]


class BrandArchiveResponse(BaseModel):
    archived_at: datetime
    """Time the brand was archived."""

    brand_id: str
    """The archived brand."""

    collections_moved: int
    """Count of product collections moved to the target brand."""

    products_moved: int
    """Count of products moved to the target brand."""

    subscriptions_moved: int
    """Count of live subscriptions moved to the target brand."""

    moved_to_brand_id: Optional[str] = None
    """Brand that received the moved records. Null when no target was given."""
