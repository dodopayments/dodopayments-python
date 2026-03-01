# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .currency import Currency
from .time_interval import TimeInterval
from .cbb_overage_behavior import CbbOverageBehavior

__all__ = ["CreditEntitlementUpdateParams"]


class CreditEntitlementUpdateParams(TypedDict, total=False):
    currency: Optional[Currency]
    """Currency for pricing"""

    description: Optional[str]
    """Optional description of the credit entitlement"""

    expires_after_days: Optional[int]
    """Number of days after which credits expire"""

    max_rollover_count: Optional[int]
    """Maximum number of times credits can be rolled over"""

    name: Optional[str]
    """Name of the credit entitlement"""

    overage_behavior: Optional[CbbOverageBehavior]
    """Controls how overage is handled at billing cycle end."""

    overage_enabled: Optional[bool]
    """Whether overage charges are enabled when credits run out"""

    overage_limit: Optional[int]
    """Maximum overage units allowed"""

    price_per_unit: Optional[str]
    """Price per credit unit"""

    rollover_enabled: Optional[bool]
    """Whether rollover is enabled for unused credits"""

    rollover_percentage: Optional[int]
    """Percentage of unused credits that can rollover (0-100)"""

    rollover_timeframe_count: Optional[int]
    """Count of timeframe periods for rollover limit"""

    rollover_timeframe_interval: Optional[TimeInterval]
    """Interval type for rollover timeframe"""

    unit: Optional[str]
    """Unit of measurement for the credit (e.g., "API Calls", "Tokens", "Credits")"""
