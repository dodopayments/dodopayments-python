# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .currency import Currency
from .time_interval import TimeInterval
from .cbb_overage_behavior import CbbOverageBehavior

__all__ = ["CreditEntitlement"]


class CreditEntitlement(BaseModel):
    id: str

    business_id: str

    created_at: datetime

    name: str

    overage_behavior: CbbOverageBehavior
    """Controls how overage is handled at billing cycle end."""

    overage_enabled: bool

    precision: int

    rollover_enabled: bool

    unit: str

    updated_at: datetime

    currency: Optional[Currency] = None

    description: Optional[str] = None

    expires_after_days: Optional[int] = None

    max_rollover_count: Optional[int] = None

    overage_limit: Optional[int] = None

    price_per_unit: Optional[str] = None
    """Price per credit unit"""

    rollover_percentage: Optional[int] = None

    rollover_timeframe_count: Optional[int] = None

    rollover_timeframe_interval: Optional[TimeInterval] = None
