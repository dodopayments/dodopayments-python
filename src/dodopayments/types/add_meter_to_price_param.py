# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["AddMeterToPriceParam"]


class AddMeterToPriceParam(TypedDict, total=False):
    meter_id: Required[str]

    credit_entitlement_id: Optional[str]
    """Optional credit entitlement ID to link this meter to for credit-based billing"""

    description: Optional[str]
    """Meter description. Will ignored on Request, but will be shown in response"""

    free_threshold: Optional[int]

    measurement_unit: Optional[str]
    """Meter measurement unit. Will ignored on Request, but will be shown in response"""

    meter_units_per_credit: Optional[str]
    """Number of meter units that equal one credit.

    Required when credit_entitlement_id is set.
    """

    name: Optional[str]
    """Meter name. Will ignored on Request, but will be shown in response"""

    price_per_unit: Optional[str]
    """The price per unit in lowest denomination.

    Must be greater than zero. Supports up to 5 digits before decimal point and 12
    decimal places.
    """
