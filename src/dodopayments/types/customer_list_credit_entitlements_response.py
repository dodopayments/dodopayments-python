# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["CustomerListCreditEntitlementsResponse", "Item"]


class Item(BaseModel):
    """A credit entitlement with the customer's current balance"""

    balance: str
    """Customer's current remaining credit balance"""

    credit_entitlement_id: str
    """Credit entitlement ID"""

    name: str
    """Name of the credit entitlement"""

    overage: str
    """Customer's current overage balance"""

    unit: str
    """Unit label (e.g. "API Calls", "Tokens")"""

    description: Optional[str] = None
    """Description of the credit entitlement"""


class CustomerListCreditEntitlementsResponse(BaseModel):
    items: List[Item]
