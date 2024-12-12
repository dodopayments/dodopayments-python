# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .refund import Refund
from .._models import BaseModel

__all__ = ["RefundListResponse"]


class RefundListResponse(BaseModel):
    items: List[Refund]
