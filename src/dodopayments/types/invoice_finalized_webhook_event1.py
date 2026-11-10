# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .invoice import Invoice
from .._models import BaseModel

__all__ = ["InvoiceFinalizedWebhookEvent"]


class InvoiceFinalizedWebhookEvent(BaseModel):
    business_id: str
    """The business identifier"""

    data: Invoice
    """An invoice-led invoice.

    Every read and every `invoice.*` webhook uses this schema.
    """

    timestamp: datetime
    """The timestamp of when the event occurred"""

    type: Literal["invoice.finalized"]
    """The event type"""
