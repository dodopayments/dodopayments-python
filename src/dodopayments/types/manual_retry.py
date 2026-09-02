# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .intent_status import IntentStatus

__all__ = ["ManualRetry"]


class ManualRetry(BaseModel):
    invoice_id: str
    """The invoice the send charged."""

    is_manual_retry: bool
    """Always true on this route. Tells the row apart from an automatic attempt."""

    payment_id: str
    """The payment row this send created."""

    retry_attempt: int
    """Which attempt this send is, counting manual sends on the invoice."""

    sends_allowed: int

    sends_used: int
    """Manual sends spent on this invoice, including this one."""

    retry_available_at: Optional[datetime] = None
    """When the next send becomes available. Null when no send is left."""

    status: Optional[IntentStatus] = None
    """Outcome of the charge.

    `processing` means the processor has not settled it yet, and the payment
    webhooks report the result.
    """
