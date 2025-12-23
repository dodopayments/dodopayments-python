# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["ShortLinkCreateResponse"]


class ShortLinkCreateResponse(BaseModel):
    full_url: str
    """Full URL."""

    short_url: str
    """Short URL."""
