# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SubscriptionRetrieveUsageHistoryParams"]


class SubscriptionRetrieveUsageHistoryParams(TypedDict, total=False):
    end_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Filter by end date (inclusive)"""

    meter_id: Optional[str]
    """Filter by specific meter ID"""

    page_number: Optional[int]
    """Page number (default: 0)"""

    page_size: Optional[int]
    """Page size (default: 10, max: 100)"""

    start_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Filter by start date (inclusive)"""
