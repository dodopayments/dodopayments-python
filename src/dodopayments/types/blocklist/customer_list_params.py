# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CustomerListParams"]


class CustomerListParams(TypedDict, total=False):
    blocked_by_email: Optional[str]
    """Filter by the dashboard user who blocked the customer."""

    created_at_gte: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Blocked on or after this time."""

    created_at_lte: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Blocked on or before this time."""

    identifier: Optional[str]
    """Partial, case-insensitive match on the email and on the customer id."""

    page_number: Optional[int]
    """Page number. Default 0."""

    page_size: Optional[int]
    """Page size. Default 10, maximum 100."""
