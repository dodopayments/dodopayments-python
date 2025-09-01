# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["UsageEventListParams"]


class UsageEventListParams(TypedDict, total=False):
    customer_id: str
    """Filter events by customer ID"""

    end: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter events created before this timestamp"""

    event_name: str
    """Filter events by event name.

    If both event_name and meter_id are provided, they must match the meter's
    configured event_name
    """

    meter_id: str
    """Filter events by meter ID.

    When provided, only events that match the meter's event_name and filter criteria
    will be returned
    """

    page_number: int
    """Page number (0-based, default: 0)"""

    page_size: int
    """Number of events to return per page (default: 10)"""

    start: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter events created after this timestamp"""
