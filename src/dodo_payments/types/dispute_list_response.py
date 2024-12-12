# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .dispute import Dispute
from .._models import BaseModel

__all__ = ["DisputeListResponse"]


class DisputeListResponse(BaseModel):
    items: List[Dispute]
