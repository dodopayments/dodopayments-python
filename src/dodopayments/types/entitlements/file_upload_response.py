# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["FileUploadResponse"]


class FileUploadResponse(BaseModel):
    file_id: str
    """
    EE-issued digital file id; appended to
    `entitlements.integration_config.digital_file_ids`.
    """
