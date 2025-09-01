# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["AddMeterToPrice"]


class AddMeterToPrice(BaseModel):
    meter_id: str

    price_per_unit: str
    """The price per unit in lowest denomination.

    Must be greater than zero. Supports up to 5 digits before decimal point and 12
    decimal places.
    """

    description: Optional[str] = None
    """Meter description. Will ignored on Request, but will be shown in response"""

    free_threshold: Optional[int] = None

    measurement_unit: Optional[str] = None
    """Meter measurement unit. Will ignored on Request, but will be shown in response"""

    name: Optional[str] = None
    """Meter name. Will ignored on Request, but will be shown in response"""
