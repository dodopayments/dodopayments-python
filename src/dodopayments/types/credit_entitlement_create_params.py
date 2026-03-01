# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .currency import Currency
from .time_interval import TimeInterval
from .cbb_overage_behavior import CbbOverageBehavior

__all__ = ["CreditEntitlementCreateParams"]


class CreditEntitlementCreateParams(TypedDict, total=False):
    name: Required[str]
    """Name of the credit entitlement"""

    overage_enabled: Required[bool]
    """Whether overage charges are enabled when credits run out"""

    precision: Required[int]
    """Precision for credit amounts (0-10 decimal places)"""

    rollover_enabled: Required[bool]
    """Whether rollover is enabled for unused credits"""

    unit: Required[str]
    """Unit of measurement for the credit (e.g., "API Calls", "Tokens", "Credits")"""

    currency: Optional[Currency]
    """Currency for pricing (required if price_per_unit is set)"""

    description: Optional[str]
    """Optional description of the credit entitlement"""

    expires_after_days: Optional[int]
    """Number of days after which credits expire (optional)"""

    max_rollover_count: Optional[int]
    """Maximum number of times credits can be rolled over"""

    overage_behavior: Optional[CbbOverageBehavior]
    """
    Controls how overage is handled at billing cycle end. Defaults to
    forgive_at_reset if not specified.
    """

    overage_limit: Optional[int]
    """Maximum overage units allowed (optional)"""

    price_per_unit: Optional[str]
    """Price per credit unit"""

    rollover_percentage: Optional[int]
    """Percentage of unused credits that can rollover (0-100)"""

    rollover_timeframe_count: Optional[int]
    """Count of timeframe periods for rollover limit"""

    rollover_timeframe_interval: Optional[TimeInterval]
    """Interval type for rollover timeframe"""
