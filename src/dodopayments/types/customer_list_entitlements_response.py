# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CustomerListEntitlementsResponse", "Item"]


class Item(BaseModel):
    created_at: datetime

    entitlement_id: str
    """The entitlement this grant belongs to."""

    entitlement_name: str

    grant_id: str
    """Grant id (the per-customer row in `entitlement_grants`)."""

    integration_type: Literal[
        "discord", "telegram", "github", "figma", "framer", "notion", "digital_files", "license_key"
    ]

    status: Literal["pending", "delivered", "failed", "revoked"]

    updated_at: datetime

    delivered_at: Optional[datetime] = None

    entitlement_description: Optional[str] = None

    revoked_at: Optional[datetime] = None


class CustomerListEntitlementsResponse(BaseModel):
    items: List[Item]
