# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["RefundCreateParams"]


class RefundCreateParams(TypedDict, total=False):
    payment_id: Required[str]

    amount: Optional[int]

    reason: Optional[str]
