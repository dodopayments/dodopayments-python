# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["WebhookEventListParams"]


class WebhookEventListParams(TypedDict, total=False):
    created_at_gte: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Get events after this created time"""

    created_at_lte: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Get events created before this time"""

    limit: Optional[int]
    """Min : 1, Max : 100, default 10"""

    object_id: Optional[str]
    """
    Get events history of a specific object like payment/subscription/refund/dispute
    """

    page_number: Optional[int]
    """Page number default is 0"""

    page_size: Optional[int]
    """Page size default is 10 max is 100"""