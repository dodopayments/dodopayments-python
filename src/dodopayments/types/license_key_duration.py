# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .time_interval import TimeInterval

__all__ = ["LicenseKeyDuration"]


class LicenseKeyDuration(BaseModel):
    count: int

    interval: TimeInterval
