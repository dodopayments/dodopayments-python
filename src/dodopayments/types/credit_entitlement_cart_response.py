# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .time_interval import TimeInterval
from .cbb_overage_behavior import CbbOverageBehavior

__all__ = ["CreditEntitlementCartResponse"]


class CreditEntitlementCartResponse(BaseModel):
    """Response struct representing credit entitlement cart details for a subscription"""

    credit_entitlement_id: str

    credit_entitlement_name: str

    credits_amount: str

    overage_balance: str
    """Customer's current overage balance for this entitlement"""

    overage_behavior: CbbOverageBehavior
    """Controls how overage is handled at the end of a billing cycle.

    | Preset                     | Charge at billing | Credits reduce overage | Preserve overage at reset |
    | -------------------------- | :---------------: | :--------------------: | :-----------------------: |
    | `forgive_at_reset`         |        No         |           No           |            No             |
    | `invoice_at_billing`       |        Yes        |           No           |            No             |
    | `carry_deficit`            |        No         |           No           |            Yes            |
    | `carry_deficit_auto_repay` |        No         |          Yes           |            Yes            |
    """

    overage_enabled: bool

    product_id: str

    remaining_balance: str
    """Customer's current remaining credit balance for this entitlement"""

    rollover_enabled: bool

    unit: str
    """Unit label for the credit entitlement (e.g., "API Calls", "Tokens")"""

    expires_after_days: Optional[int] = None

    low_balance_threshold_percent: Optional[int] = None

    max_rollover_count: Optional[int] = None

    overage_limit: Optional[str] = None

    rollover_percentage: Optional[int] = None

    rollover_timeframe_count: Optional[int] = None

    rollover_timeframe_interval: Optional[TimeInterval] = None
