# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["BrandArchiveParams"]


class BrandArchiveParams(TypedDict, total=False):
    move_products_to: Optional[str]
    """
    Brand that takes over the products and the live subscriptions of the brand you
    archive. It must be a brand of the same business, and it must not be archived.
    The primary brand (its brand id is the business id) is a valid target. Omit this
    field only when the brand holds no products and no live subscriptions.
    """
