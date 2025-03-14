# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DisputeListParams"]


class DisputeListParams(TypedDict, total=False):
    created_at_gte: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Get events after this created time"""

    created_at_lte: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Get events created before this time"""

    customer_id: Optional[str]
    """Filter by customer_id"""

    dispute_stage: Optional[Literal["pre_dispute", "dispute", "pre_arbitration"]]
    """Filter by dispute stage"""

    dispute_status: Optional[
        Literal[
            "dispute_opened",
            "dispute_expired",
            "dispute_accepted",
            "dispute_cancelled",
            "dispute_challenged",
            "dispute_won",
            "dispute_lost",
        ]
    ]
    """Filter by dispute status"""

    page_number: Optional[int]
    """Page number default is 0"""

    page_size: Optional[int]
    """Page size default is 10 max is 100"""
