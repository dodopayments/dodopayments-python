# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .localized_price import LocalizedPrice

__all__ = ["ListLocalizedPricesResponse"]


class ListLocalizedPricesResponse(BaseModel):
    items: List[LocalizedPrice]
