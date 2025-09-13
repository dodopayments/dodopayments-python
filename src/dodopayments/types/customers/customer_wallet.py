# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ..._models import BaseModel
from ..currency import Currency

__all__ = ["CustomerWallet"]


class CustomerWallet(BaseModel):
    balance: int

    created_at: datetime

    currency: Currency

    customer_id: str

    updated_at: datetime
