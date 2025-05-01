# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["AddonCartResponseItem"]


class AddonCartResponseItem(BaseModel):
    addon_id: str

    quantity: int
