# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["SubscriptionUpdateParams"]


class SubscriptionUpdateParams(TypedDict, total=False):
    metadata: Optional[Dict[str, str]]

    status: Optional[Literal["pending", "active", "on_hold", "paused", "cancelled", "failed", "expired"]]
