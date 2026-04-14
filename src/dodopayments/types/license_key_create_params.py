# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["LicenseKeyCreateParams"]


class LicenseKeyCreateParams(TypedDict, total=False):
    customer_id: Required[str]
    """The customer this license key belongs to."""

    key: Required[str]
    """The license key string to import."""

    product_id: Required[str]
    """The product this license key is for."""

    activations_limit: Optional[int]
    """Maximum number of activations allowed. Null means unlimited."""

    expires_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Expiration timestamp. Null means the key never expires."""
