# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .time_interval import TimeInterval
from .cbb_overage_behavior import CbbOverageBehavior

__all__ = ["CreditEntitlementCartResponseParam"]


class CreditEntitlementCartResponseParam(TypedDict, total=False):
    """Response struct representing credit entitlement cart details for a subscription"""

    credit_entitlement_id: Required[str]

    credit_entitlement_name: Required[str]

    credits_amount: Required[str]

    overage_balance: Required[str]
    """Customer's current overage balance for this entitlement"""

    overage_behavior: Required[CbbOverageBehavior]
    """Controls how overage is handled at the end of a billing cycle.

    | Preset                     | Charge at billing | Credits reduce overage | Preserve overage at reset |
    | -------------------------- | :---------------: | :--------------------: | :-----------------------: |
    | `forgive_at_reset`         |        No         |           No           |            No             |
    | `invoice_at_billing`       |        Yes        |           No           |            No             |
    | `carry_deficit`            |        No         |           No           |            Yes            |
    | `carry_deficit_auto_repay` |        No         |          Yes           |            Yes            |
    """

    overage_enabled: Required[bool]

    product_id: Required[str]

    remaining_balance: Required[str]
    """Customer's current remaining credit balance for this entitlement"""

    rollover_enabled: Required[bool]

    unit: Required[str]
    """Unit label for the credit entitlement (e.g., "API Calls", "Tokens")"""

    expires_after_days: Optional[int]

    low_balance_threshold_percent: Optional[int]

    max_rollover_count: Optional[int]

    overage_limit: Optional[str]

    rollover_percentage: Optional[int]

    rollover_timeframe_count: Optional[int]

    rollover_timeframe_interval: Optional[TimeInterval]
