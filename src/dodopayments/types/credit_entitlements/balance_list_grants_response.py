# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["BalanceListGrantsResponse"]


class BalanceListGrantsResponse(BaseModel):
    """Response for a credit grant"""

    id: str

    created_at: datetime

    credit_entitlement_id: str

    customer_id: str

    initial_amount: str

    is_expired: bool

    is_rolled_over: bool

    remaining_amount: str

    rollover_count: int

    source_type: Literal["subscription", "one_time", "addon", "api", "rollover"]

    updated_at: datetime

    expires_at: Optional[datetime] = None

    metadata: Optional[Dict[str, str]] = None

    parent_grant_id: Optional[str] = None

    source_id: Optional[str] = None
