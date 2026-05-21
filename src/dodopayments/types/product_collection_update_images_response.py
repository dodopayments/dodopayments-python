# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ProductCollectionUpdateImagesResponse"]


class ProductCollectionUpdateImagesResponse(BaseModel):
    url: str
    """Presigned S3 URL for uploading the image"""

    image_id: Optional[str] = None
    """Optional image ID (present when force_update is true)"""
