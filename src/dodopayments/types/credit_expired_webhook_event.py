# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .credit_entitlements.credit_ledger_entry import CreditLedgerEntry

__all__ = ["CreditExpiredWebhookEvent"]


class CreditExpiredWebhookEvent(BaseModel):
    business_id: str
    """The business identifier"""

    data: CreditLedgerEntry
    """Response for a ledger entry"""

    timestamp: datetime
    """The timestamp of when the event occurred"""

    type: Literal["credit.expired"]
    """The event type"""
