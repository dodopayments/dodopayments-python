# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel
from .blocked_customer_source import BlockedCustomerSource
from .customers.blocked_customer_note import BlockedCustomerNote

__all__ = ["BlockedCustomer"]


class BlockedCustomer(BaseModel):
    id: str

    created_at: datetime

    customer_email: str

    customer_id: str

    customer_name: str

    identifier: str
    """Customer id or email that the merchant supplied."""

    source: BlockedCustomerSource
    """Where a block came from.

    `Api` marks an API-key caller, which carries no dashboard actor. The other
    values name the screen the merchant used.
    """

    blocked_by_email: Optional[str] = None
    """Dashboard user who blocked the customer. `null` for an API-key caller."""

    cancelled_subscription_ids: Optional[List[str]] = None
    """Subscriptions this block cancelled. Present on the create response only."""

    notes: Optional[List[BlockedCustomerNote]] = None
    """Activity log. Present on the detail response only."""

    reason: Optional[str] = None

    remaining_subscription_ids: Optional[List[str]] = None
    """
    Subscriptions this block left live, because the cancel failed or the inline
    batch filled up. Repeat the create call to continue; the block itself is already
    in force.
    """

    subscriptions_swept: Optional[bool] = None
    """
    False when the block left live subscriptions behind, including the case where
    the sweep could not list them and `remaining_subscription_ids` is therefore
    unknown. Repeat the create call until it reads true.
    """

    unblocked_at: Optional[datetime] = None
