# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["AddMeterToPrice"]


class AddMeterToPrice(BaseModel):
    meter_id: str

    credit_entitlement_id: Optional[str] = None
    """Optional credit entitlement ID to link this meter to for credit-based billing"""

    description: Optional[str] = None
    """Meter description. Will ignored on Request, but will be shown in response"""

    free_threshold: Optional[int] = None

    measurement_unit: Optional[str] = None
    """Meter measurement unit. Will ignored on Request, but will be shown in response"""

    meter_units_per_credit: Optional[str] = None
    """Number of meter units that equal one credit.

    Required when credit_entitlement_id is set.
    """

    name: Optional[str] = None
    """Meter name. Will ignored on Request, but will be shown in response"""

    price_per_unit: Optional[str] = None
    """The price per unit in lowest denomination.

    Must be greater than zero. Supports up to 5 digits before decimal point and 12
    decimal places.
    """
