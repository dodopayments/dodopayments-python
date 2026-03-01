# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["BalanceListGrantsParams"]


class BalanceListGrantsParams(TypedDict, total=False):
    credit_entitlement_id: Required[str]

    page_number: int
    """Page number default is 0"""

    page_size: int
    """Page size default is 10 max is 100"""

    status: Literal["active", "expired", "depleted"]
    """Filter by grant status: active, expired, depleted"""
