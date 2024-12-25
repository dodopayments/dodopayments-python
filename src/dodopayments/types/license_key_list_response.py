# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .._models import BaseModel
from .license_key import LicenseKey

__all__ = ["LicenseKeyListResponse", "LicenseKeyListResponseItem"]


class LicenseKeyListResponseItem(BaseModel):
    items: List[LicenseKey]


LicenseKeyListResponse: TypeAlias = List[LicenseKeyListResponseItem]
