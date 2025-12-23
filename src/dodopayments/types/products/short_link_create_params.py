# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["ShortLinkCreateParams"]


class ShortLinkCreateParams(TypedDict, total=False):
    slug: Required[str]
    """Slug for the short link."""

    static_checkout_params: Optional[Dict[str, str]]
    """Static Checkout URL parameters to apply to the resulting short URL."""
