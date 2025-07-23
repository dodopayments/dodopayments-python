# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .brand import Brand
from .._models import BaseModel

__all__ = ["BrandListResponse"]


class BrandListResponse(BaseModel):
    items: List[Brand]
    """List of brands for this business"""
