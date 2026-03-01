# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["CustomerCreditBalance"]


class CustomerCreditBalance(BaseModel):
    """Response for a customer's credit balance"""

    id: str

    balance: str

    created_at: datetime

    credit_entitlement_id: str

    customer_id: str

    overage: str

    updated_at: datetime

    last_transaction_at: Optional[datetime] = None
