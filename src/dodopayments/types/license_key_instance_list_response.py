# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .._models import BaseModel
from .license_key_instance import LicenseKeyInstance

__all__ = ["LicenseKeyInstanceListResponse", "LicenseKeyInstanceListResponseItem"]


class LicenseKeyInstanceListResponseItem(BaseModel):
    items: List[LicenseKeyInstance]


LicenseKeyInstanceListResponse: TypeAlias = List[LicenseKeyInstanceListResponseItem]
