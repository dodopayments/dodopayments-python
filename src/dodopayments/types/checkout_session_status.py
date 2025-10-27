# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .intent_status import IntentStatus

__all__ = ["CheckoutSessionStatus"]


class CheckoutSessionStatus(BaseModel):
    id: str
    """Id of the checkout session"""

    created_at: datetime
    """Created at timestamp"""

    customer_email: Optional[str] = None
    """Customer email: prefers payment's customer, falls back to session"""

    customer_name: Optional[str] = None
    """Customer name: prefers payment's customer, falls back to session"""

    payment_id: Optional[str] = None
    """Id of the payment created by the checkout sessions.

    Null if checkout sessions is still at the details collection stage.
    """

    payment_status: Optional[IntentStatus] = None
    """status of the payment.

    Null if checkout sessions is still at the details collection stage.
    """
