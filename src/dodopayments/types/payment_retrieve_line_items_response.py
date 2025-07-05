# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .currency import Currency

__all__ = ["PaymentRetrieveLineItemsResponse", "Item"]


class Item(BaseModel):
    amount: int

    items_id: str

    refundable_amount: int

    tax: int

    description: Optional[str] = None

    name: Optional[str] = None


class PaymentRetrieveLineItemsResponse(BaseModel):
    currency: Currency

    items: List[Item]
