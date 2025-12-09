# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["AddonCartResponseItem"]


class AddonCartResponseItem(BaseModel):
    """Response struct representing subscription details"""

    addon_id: str

    quantity: int
