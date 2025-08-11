# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List

from ..._models import BaseModel

__all__ = ["HeaderRetrieveResponse"]


class HeaderRetrieveResponse(BaseModel):
    headers: Dict[str, str]
    """List of headers configured"""

    sensitive: List[str]
    """Sensitive headers without the value"""
