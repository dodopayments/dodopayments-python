# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["BreakupRetrieveResponse", "BreakupRetrieveResponseItem"]


class BreakupRetrieveResponseItem(BaseModel):
    """Payout breakup aggregated by event type, with amounts in the payout's currency."""

    event_type: str
    """
    The type of balance ledger event (e.g., "payment", "refund", "dispute",
    "payment_fees").
    """

    total: int
    """
    Total amount for this event type in the payout's currency (in smallest currency
    unit, e.g., cents).
    """


BreakupRetrieveResponse: TypeAlias = List[BreakupRetrieveResponseItem]
