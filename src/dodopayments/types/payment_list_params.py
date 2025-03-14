# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .intent_status import IntentStatus

__all__ = ["PaymentListParams"]


class PaymentListParams(TypedDict, total=False):
    created_at_gte: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Get events after this created time"""

    created_at_lte: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Get events created before this time"""

    customer_id: Optional[str]
    """Filter by customer id"""

    page_number: Optional[int]
    """Page number default is 0"""

    page_size: Optional[int]
    """Page size default is 10 max is 100"""

    status: Optional[IntentStatus]
    """Filter by status"""

    subscription_id: Optional[str]
    """Filter by subscription id"""
