# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel

__all__ = ["SubscriptionCreateResponse", "Customer"]


class Customer(BaseModel):
    customer_id: str

    email: str

    name: str


class SubscriptionCreateResponse(BaseModel):
    customer: Customer

    metadata: Dict[str, str]

    recurring_pre_tax_amount: int

    subscription_id: str

    client_secret: Optional[str] = None

    payment_link: Optional[str] = None
