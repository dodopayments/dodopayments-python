# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .currency import Currency
from .time_interval import TimeInterval
from .cbb_overage_behavior import CbbOverageBehavior
from .cbb_proration_behavior import CbbProrationBehavior

__all__ = ["AttachCreditEntitlementParam"]


class AttachCreditEntitlementParam(TypedDict, total=False):
    """Request struct for attaching a credit entitlement to a product"""

    credit_entitlement_id: Required[str]
    """ID of the credit entitlement to attach"""

    credits_amount: Required[str]
    """Number of credits to grant when this product is purchased"""

    currency: Optional[Currency]
    """Currency for credit-related pricing"""

    expires_after_days: Optional[int]
    """Number of days after which credits expire"""

    low_balance_threshold_percent: Optional[int]
    """Balance threshold percentage for low balance notifications (0-100)"""

    max_rollover_count: Optional[int]
    """Maximum number of rollover cycles allowed"""

    overage_behavior: Optional[CbbOverageBehavior]
    """Controls how overage is handled at billing cycle end."""

    overage_enabled: Optional[bool]
    """Whether overage usage is allowed beyond credit balance"""

    overage_limit: Optional[str]
    """Maximum amount of overage allowed"""

    price_per_unit: Optional[str]
    """Price per credit unit for purchasing additional credits"""

    proration_behavior: Optional[CbbProrationBehavior]
    """Proration behavior for credit grants during plan changes"""

    rollover_enabled: Optional[bool]
    """Whether unused credits can roll over to the next billing period"""

    rollover_percentage: Optional[int]
    """Percentage of unused credits that can roll over (0-100)"""

    rollover_timeframe_count: Optional[int]
    """Number of timeframe units for rollover window"""

    rollover_timeframe_interval: Optional[TimeInterval]
    """Time interval for rollover window (day, week, month, year)"""

    trial_credits: Optional[str]
    """Credits granted during trial period"""

    trial_credits_expire_after_trial: Optional[bool]
    """Whether trial credits expire when trial ends"""
