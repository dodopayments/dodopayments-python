# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["SubscriptionUpdatePaymentMethodResponse"]


class SubscriptionUpdatePaymentMethodResponse(BaseModel):
    client_secret: Optional[str] = None

    expires_on: Optional[datetime] = None

    payment_id: Optional[str] = None

    payment_link: Optional[str] = None
