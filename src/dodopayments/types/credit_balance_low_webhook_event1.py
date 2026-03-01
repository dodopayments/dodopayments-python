# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CreditBalanceLowWebhookEvent", "Data"]


class Data(BaseModel):
    """Webhook payload for credit.balance_low event"""

    available_balance: str

    credit_entitlement_id: str

    credit_entitlement_name: str

    customer_id: str

    subscription_credits_amount: str

    subscription_id: str

    threshold_amount: str

    threshold_percent: int


class CreditBalanceLowWebhookEvent(BaseModel):
    business_id: str
    """The business identifier"""

    data: Data
    """Webhook payload for credit.balance_low event"""

    timestamp: datetime
    """The timestamp of when the event occurred"""

    type: Literal["credit.balance_low"]
    """The event type"""
