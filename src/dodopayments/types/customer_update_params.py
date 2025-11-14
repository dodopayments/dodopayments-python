# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

__all__ = ["CustomerUpdateParams"]


class CustomerUpdateParams(TypedDict, total=False):
    metadata: Optional[Dict[str, str]]
    """Additional metadata for the customer"""

    name: Optional[str]

    phone_number: Optional[str]
