# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["ManualRetryState"]


class ManualRetryState(BaseModel):
    can_retry: bool

    sends_allowed: int

    sends_used: int

    automatic_retry_number: Optional[int] = None
    """The number of the queued automatic retry, starting at 1."""

    automatic_retry_total: Optional[int] = None
    """
    The number of automatic retries that the current configuration plans for this
    invoice. It is never less than `automatic_retry_number`.
    """

    next_automatic_retry_at: Optional[datetime] = None
    """When the next automatic retry on this invoice is scheduled.

    Null when no automatic retry is queued or automatic retries are disabled.
    """

    reason: Optional[str] = None
    """The code `POST` would fail with. Null when `can_retry` is true."""

    retry_available_at: Optional[datetime] = None
    """When the next send becomes available.

    Null when no send is left, or when the block has nothing to do with the
    cooldown.
    """
