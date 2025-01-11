# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["RefundCreateParams"]


class RefundCreateParams(TypedDict, total=False):
    payment_id: Required[str]
    """The unique identifier of the payment to be refunded."""

    amount: Optional[int]
    """The amount to be refunded.

    Must be non-negative. Optional. Partial refunds are currently disabled.
    """

    reason: Optional[str]
    """The reason for the refund, if any. Maximum length is 3000 characters. Optional."""
