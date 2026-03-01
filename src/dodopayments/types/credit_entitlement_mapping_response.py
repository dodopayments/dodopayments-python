# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .currency import Currency
from .time_interval import TimeInterval
from .cbb_overage_behavior import CbbOverageBehavior
from .cbb_proration_behavior import CbbProrationBehavior

__all__ = ["CreditEntitlementMappingResponse"]


class CreditEntitlementMappingResponse(BaseModel):
    """Response struct for credit entitlement mapping"""

    id: str
    """Unique ID of this mapping"""

    credit_entitlement_id: str
    """ID of the credit entitlement"""

    credit_entitlement_name: str
    """Name of the credit entitlement"""

    credit_entitlement_unit: str
    """Unit label for the credit entitlement"""

    credits_amount: str
    """Number of credits granted"""

    overage_behavior: CbbOverageBehavior
    """Controls how overage is handled at billing cycle end."""

    overage_enabled: bool
    """Whether overage is enabled"""

    proration_behavior: CbbProrationBehavior
    """Proration behavior for credit grants during plan changes"""

    rollover_enabled: bool
    """Whether rollover is enabled"""

    trial_credits_expire_after_trial: bool
    """Whether trial credits expire after trial"""

    currency: Optional[Currency] = None
    """Currency"""

    expires_after_days: Optional[int] = None
    """Days until credits expire"""

    low_balance_threshold_percent: Optional[int] = None
    """Low balance threshold percentage"""

    max_rollover_count: Optional[int] = None
    """Maximum rollover cycles"""

    overage_limit: Optional[str] = None
    """Overage limit"""

    price_per_unit: Optional[str] = None
    """Price per unit"""

    rollover_percentage: Optional[int] = None
    """Rollover percentage"""

    rollover_timeframe_count: Optional[int] = None
    """Rollover timeframe count"""

    rollover_timeframe_interval: Optional[TimeInterval] = None
    """Rollover timeframe interval"""

    trial_credits: Optional[str] = None
    """Trial credits"""
