# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["GrantFulfillLicenseKeyParams"]


class GrantFulfillLicenseKeyParams(TypedDict, total=False):
    key: Required[str]
    """The license key value to deliver to the customer."""

    activations_limit: Optional[int]
    """Per-key activation limit.

    Defaults to the entitlement's license-key configuration.
    """

    expires_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """When the key expires.

    Defaults to the duration in the entitlement's license-key configuration.
    """
