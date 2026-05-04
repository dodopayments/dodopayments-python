# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["DigitalProductDeliveryFile"]


class DigitalProductDeliveryFile(BaseModel):
    """One file in a digital-product delivery payload."""

    download_url: str
    """Short-lived presigned URL for downloading the file."""

    expires_in: int
    """Seconds until `download_url` expires."""

    file_id: str
    """Identifier of the attached file."""

    filename: str
    """Original filename of the attached file."""

    content_type: Optional[str] = None
    """Optional content-type declared at upload."""

    file_size: Optional[int] = None
    """Optional size of the file in bytes."""
