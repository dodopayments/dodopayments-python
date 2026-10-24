# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .credit_entitlement_translation import CreditEntitlementTranslation

__all__ = ["CreditEntitlementTranslationsListResponse"]


class CreditEntitlementTranslationsListResponse(BaseModel):
    """The translations of a credit entitlement."""

    items: List[CreditEntitlementTranslation]
