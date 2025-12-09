# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List

from ..._models import BaseModel

__all__ = ["HeaderRetrieveResponse"]


class HeaderRetrieveResponse(BaseModel):
    """The value of the headers is returned in the `headers` field.

    Sensitive headers that have been redacted are returned in the sensitive
    field.
    """

    headers: Dict[str, str]
    """List of headers configured"""

    sensitive: List[str]
    """Sensitive headers without the value"""
