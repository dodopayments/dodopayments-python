# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .translation import Translation

__all__ = ["TranslationsListResponse"]


class TranslationsListResponse(BaseModel):
    """The translations of a product, an add-on, a product collection or a meter."""

    items: List[Translation]
