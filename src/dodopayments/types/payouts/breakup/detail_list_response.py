# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["DetailListResponse"]


class DetailListResponse(BaseModel):
    """
    Individual balance ledger entry for a payout, with amounts pro-rated into the payout's currency.
    """

    id: str
    """Unique identifier of the balance ledger entry."""

    created_at: datetime
    """Timestamp when this entry was created."""

    event_type: str
    """
    The type of balance ledger event (e.g., "payment", "refund", "dispute",
    "payment_fees").
    """

    original_amount: int
    """
    Original amount in the original currency (in smallest currency unit, e.g.,
    cents).
    """

    original_currency: str
    """Original currency as ISO 4217 code (e.g., "USD", "EUR")."""

    payout_currency_amount: int
    """Amount in the payout's currency (in smallest currency unit).

    Uses cumulative rounding to ensure sum matches payout total exactly.
    """

    usd_equivalent_amount: int
    """USD equivalent of the original amount (in cents)."""

    description: Optional[str] = None
    """Human-readable description of the transaction."""

    reference_object_id: Optional[str] = None
    """ID of the related object (e.g., payment ID, refund ID) if applicable."""
