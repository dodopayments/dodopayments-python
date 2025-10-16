# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PayoutListParams"]


class PayoutListParams(TypedDict, total=False):
    created_at_gte: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Get payouts created after this time (inclusive)"""

    created_at_lte: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Get payouts created before this time (inclusive)"""

    page_number: int
    """Page number default is 0"""

    page_size: int
    """Page size default is 10 max is 100"""
