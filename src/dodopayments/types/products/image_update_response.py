# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ImageUpdateResponse"]


class ImageUpdateResponse(BaseModel):
    url: str

    image_id: Optional[str] = None
