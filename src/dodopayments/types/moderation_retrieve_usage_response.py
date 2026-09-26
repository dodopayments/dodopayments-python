# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import List

from .._models import BaseModel

__all__ = ["ModerationRetrieveUsageResponse", "Daily"]


class Daily(BaseModel):
    date: datetime.date
    """The UTC day."""

    screens: int
    """Billable screens on that day."""


class ModerationRetrieveUsageResponse(BaseModel):
    """Your moderation usage."""

    daily: List[Daily]
    """Your billable screens per UTC day for the last 30 days, charged or not.

    A day with no screens is not in the list.
    """

    screens_to_next_block: int
    """Billable screens still needed to fill the next block of 1000.

    A full block is charged within one hour, so this value is 1000 when your
    unbilled screens fill whole blocks.
    """

    unbilled_screens: int
    """Billable screens that Dodo Payments has not charged for yet."""
