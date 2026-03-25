# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["CustomerLimitedDetailsParam"]


class CustomerLimitedDetailsParam(TypedDict, total=False):
    customer_id: Required[str]
    """Unique identifier for the customer"""

    email: Required[str]
    """Email address of the customer"""

    name: Required[str]
    """Full name of the customer"""

    metadata: Dict[str, str]
    """Additional metadata associated with the customer"""

    phone_number: Optional[str]
    """Phone number of the customer"""
