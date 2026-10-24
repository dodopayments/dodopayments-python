# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["MeterUpdateParams"]


class MeterUpdateParams(TypedDict, total=False):
    description: Optional[str]
    """Description of the meter.

    Send `null` to remove the description. Omit it to keep it.
    """

    measurement_unit: Optional[str]
    """Measurement unit"""

    name: Optional[str]
    """Name of the meter"""
