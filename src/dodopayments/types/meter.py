# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .meter_filter import MeterFilter
from .meter_aggregation import MeterAggregation

__all__ = ["Meter"]


class Meter(BaseModel):
    id: str

    aggregation: MeterAggregation

    business_id: str

    created_at: datetime

    event_name: str

    measurement_unit: str

    name: str

    updated_at: datetime

    description: Optional[str] = None

    filter: Optional[MeterFilter] = None
    """
    A filter structure that combines multiple conditions with logical conjunctions
    (AND/OR).

    Supports up to 3 levels of nesting to create complex filter expressions. Each
    filter has a conjunction (and/or) and clauses that can be either direct
    conditions or nested filters.
    """
