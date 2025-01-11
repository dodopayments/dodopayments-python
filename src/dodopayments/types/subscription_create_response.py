# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel

__all__ = ["SubscriptionCreateResponse", "Customer"]


class Customer(BaseModel):
    customer_id: str
    """Unique identifier for the customer"""

    email: str
    """Email address of the customer"""

    name: str
    """Full name of the customer"""


class SubscriptionCreateResponse(BaseModel):
    customer: Customer

    metadata: Dict[str, str]

    recurring_pre_tax_amount: int
    """
    Tax will be added to the amount and charged to the customer on each billing
    cycle
    """

    subscription_id: str
    """Unique identifier for the subscription"""

    client_secret: Optional[str] = None
    """
    Client secret used to load Dodo checkout SDK NOTE : Dodo checkout SDK will be
    coming soon
    """

    payment_link: Optional[str] = None
    """URL to checkout page"""
