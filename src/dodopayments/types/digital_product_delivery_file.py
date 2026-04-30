# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["DigitalProductDeliveryFile"]


class DigitalProductDeliveryFile(BaseModel):
    download_url: str

    expires_in: int
    """Seconds until `download_url` expires."""

    file_id: str

    filename: str

    content_type: Optional[str] = None

    file_size: Optional[int] = None
