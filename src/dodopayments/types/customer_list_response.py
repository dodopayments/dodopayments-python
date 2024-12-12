# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .customer import Customer

__all__ = ["CustomerListResponse"]


class CustomerListResponse(BaseModel):
    items: List[Customer]
