# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["BrandUpdateParams"]


class BrandUpdateParams(TypedDict, total=False):
    description: Optional[str]

    image_id: Optional[str]
    """The UUID you got back from the presigned‐upload call"""

    name: Optional[str]

    statement_descriptor: Optional[str]

    support_email: Optional[str]

    url: Optional[str]
