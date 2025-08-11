# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .currency import Currency
from .refund_status import RefundStatus

__all__ = ["RefundParam"]


class RefundParam(TypedDict, total=False):
    business_id: Required[str]
    """The unique identifier of the business issuing the refund."""

    created_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """The timestamp of when the refund was created in UTC."""

    is_partial: Required[bool]
    """If true the refund is a partial refund"""

    payment_id: Required[str]
    """The unique identifier of the payment associated with the refund."""

    refund_id: Required[str]
    """The unique identifier of the refund."""

    status: Required[RefundStatus]
    """The current status of the refund."""

    amount: Optional[int]
    """The refunded amount."""

    currency: Optional[Currency]
    """The currency of the refund, represented as an ISO 4217 currency code."""

    reason: Optional[str]
    """The reason provided for the refund, if any. Optional."""
