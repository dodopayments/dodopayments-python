# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .entitlement_translation import EntitlementTranslation

__all__ = ["EntitlementTranslationsListResponse"]


class EntitlementTranslationsListResponse(BaseModel):
    """The translations of an entitlement."""

    items: List[EntitlementTranslation]
