# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel
from .dispute_stage import DisputeStage
from .dispute_status import DisputeStatus

__all__ = ["DisputeListResponse"]


class DisputeListResponse(BaseModel):
    amount: str
    """
    The amount involved in the dispute, represented as a string to accommodate
    precision.
    """

    business_id: str
    """The unique identifier of the business involved in the dispute."""

    created_at: datetime
    """The timestamp of when the dispute was created, in UTC."""

    currency: str
    """The currency of the disputed amount, represented as an ISO 4217 currency code."""

    dispute_id: str
    """The unique identifier of the dispute."""

    dispute_stage: DisputeStage
    """The current stage of the dispute process."""

    dispute_status: DisputeStatus
    """The current status of the dispute."""

    payment_id: str
    """The unique identifier of the payment associated with the dispute."""
