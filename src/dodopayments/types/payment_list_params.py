# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PaymentListParams"]


class PaymentListParams(TypedDict, total=False):
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

    product_id: str
    """Filter by product id"""

    status: Literal[
        "succeeded",
        "failed",
        "cancelled",
        "processing",
        "requires_customer_action",
        "requires_merchant_action",
        "requires_payment_method",
        "requires_confirmation",
        "requires_capture",
        "partially_captured",
        "partially_captured_and_capturable",
    ]
    """Filter by status"""

    subscription_id: str
    """Filter by subscription id"""
