# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["SubscriptionRetrieveCreditUsageResponse", "Item"]


class Item(BaseModel):
    """Per-entitlement credit usage status for a subscription"""

    balance: str
    """Customer's current credit balance for this entitlement (customer-wide)"""

    credit_entitlement_id: str

    credit_entitlement_name: str

    limit_reached: bool
    """
    True if overage has reached or exceeded the limit. When true, further deductions
    that would increase overage will fail.
    """

    overage: str
    """Current overage amount accrued (customer-wide)"""

    overage_enabled: bool
    """Whether overage is enabled for this entitlement on this subscription"""

    unit: str
    """Unit label for the credit entitlement (e.g. "API Calls", "Tokens")"""

    overage_limit: Optional[str] = None
    """
    Maximum allowed overage before deductions are blocked. None means unlimited
    overage (when overage_enabled is true).
    """

    remaining_headroom: Optional[str] = None
    """
    How much more overage can accumulate before being blocked. None if overage is
    not enabled or there is no limit (unlimited). A value of 0 means the next
    deduction that increases overage will be blocked.
    """


class SubscriptionRetrieveCreditUsageResponse(BaseModel):
    """Credit usage status for all entitlements linked to a subscription"""

    items: List[Item]

    subscription_id: str
