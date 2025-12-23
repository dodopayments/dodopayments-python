# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ..._models import BaseModel

__all__ = ["ShortLinkListResponse"]


class ShortLinkListResponse(BaseModel):
    created_at: datetime
    """When the short url was created"""

    full_url: str
    """Full URL the short url redirects to"""

    product_id: str
    """Product ID associated with the short link"""

    short_url: str
    """Short URL"""
