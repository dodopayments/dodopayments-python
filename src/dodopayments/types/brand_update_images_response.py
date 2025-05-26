# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["BrandUpdateImagesResponse"]


class BrandUpdateImagesResponse(BaseModel):
    image_id: str
    """UUID that will be used as the image identifier/key suffix"""

    url: str
    """Presigned URL to upload the image"""
