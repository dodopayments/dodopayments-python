# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from .._models import BaseModel
from .currency import Currency

__all__ = ["SubscriptionRetrieveUsageHistoryResponse", "Meter"]


class Meter(BaseModel):
    id: str
    """Meter identifier"""

    chargeable_units: str
    """Chargeable units (after free threshold) as string for precision"""

    consumed_units: str
    """Total units consumed as string for precision"""

    currency: Currency
    """Currency for the price per unit"""

    free_threshold: int
    """Free threshold units for this meter"""

    name: str
    """Meter name"""

    price_per_unit: str
    """Price per unit in string format for precision"""

    total_price: int
    """Total price charged for this meter in smallest currency unit (cents)"""


class SubscriptionRetrieveUsageHistoryResponse(BaseModel):
    end_date: datetime
    """End date of the billing period"""

    meters: List[Meter]
    """List of meters and their usage for this billing period"""

    start_date: datetime
    """Start date of the billing period"""
