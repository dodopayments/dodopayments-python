# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["SubscriptionStartTrialResponse"]


class SubscriptionStartTrialResponse(BaseModel):
    invoice_id: str
    """The paid $0 invoice of the trial."""

    subscription_id: str

    trial_ends_at: datetime
    """The first invoice after the trial bills at this time."""
