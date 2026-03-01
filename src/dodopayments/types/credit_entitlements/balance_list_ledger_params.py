# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BalanceListLedgerParams"]


class BalanceListLedgerParams(TypedDict, total=False):
    credit_entitlement_id: Required[str]

    end_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter by end date"""

    page_number: int
    """Page number default is 0"""

    page_size: int
    """Page size default is 10 max is 100"""

    start_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter by start date"""

    transaction_type: str
    """
    Filter by transaction type (snake_case: credit_added, credit_deducted,
    credit_expired, etc.)
    """
