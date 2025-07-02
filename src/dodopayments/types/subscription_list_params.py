# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SubscriptionListParams"]


class SubscriptionListParams(TypedDict, total=False):
    brand_id: str
    """filter by Brand id"""

    created_at_gte: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Get events after this created time"""

    created_at_lte: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Get events created before this time"""

    customer_id: str
    """Filter by customer id"""

    page_number: int
    """Page number default is 0"""

    page_size: int
    """Page size default is 10 max is 100"""

    status: Literal["pending", "active", "on_hold", "paused", "cancelled", "failed", "expired"]
    """Filter by status"""
