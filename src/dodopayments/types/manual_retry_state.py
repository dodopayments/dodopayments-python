# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["ManualRetryState"]


class ManualRetryState(BaseModel):
    can_retry: bool

    sends_allowed: int

    sends_used: int

    reason: Optional[str] = None
    """The code `POST` would fail with. Null when `can_retry` is true."""

    retry_available_at: Optional[datetime] = None
    """When the next send becomes available.

    Null when no send is left, or when the block has nothing to do with the
    cooldown.
    """
