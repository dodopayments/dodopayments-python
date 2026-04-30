# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["ScheduledPlanChange", "Addon"]


class Addon(BaseModel):
    addon_id: str
    """The addon ID"""

    name: str
    """Name of the addon"""

    quantity: int
    """Quantity of the addon"""


class ScheduledPlanChange(BaseModel):
    id: str
    """The scheduled plan change ID"""

    addons: List[Addon]
    """Addons included in the scheduled change"""

    created_at: datetime
    """When this scheduled change was created"""

    effective_at: datetime
    """When the change will be applied"""

    product_id: str
    """The product ID the subscription will change to"""

    quantity: int
    """Quantity for the new plan"""

    product_description: Optional[str] = None
    """Description of the product being changed to"""

    product_name: Optional[str] = None
    """Name of the product being changed to"""
