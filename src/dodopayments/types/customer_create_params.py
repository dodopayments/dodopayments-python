# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .metadata_param import MetadataParam

__all__ = ["CustomerCreateParams"]


class CustomerCreateParams(TypedDict, total=False):
    email: Required[str]

    name: Required[str]

    metadata: MetadataParam
    """Additional metadata for the customer"""

    phone_number: Optional[str]
