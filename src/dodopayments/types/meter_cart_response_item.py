# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .currency import Currency

__all__ = ["MeterCartResponseItem"]


class MeterCartResponseItem(BaseModel):
    """Response struct representing usage-based meter cart details for a subscription"""

    currency: Currency

    free_threshold: int

    measurement_unit: str

    meter_id: str

    name: str

    description: Optional[str] = None

    price_per_unit: Optional[str] = None
