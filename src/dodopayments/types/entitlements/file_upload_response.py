# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["FileUploadResponse"]


class FileUploadResponse(BaseModel):
    file_id: str
    """Identifier of the attached file.

    Pass it to `DELETE /entitlements/{id}/files/{file_id}` to detach the file later.
    """
