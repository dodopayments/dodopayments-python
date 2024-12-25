# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["LicenseKeyInstance"]


class LicenseKeyInstance(BaseModel):
    id: str

    business_id: str

    created_at: datetime

    license_key_id: str

    name: str
