# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["LicenseKeyUpdateParams"]


class LicenseKeyUpdateParams(TypedDict, total=False):
    activations_limit: Optional[int]
    """
    The updated activation limit for the license key. Use `null` to remove the
    limit, or omit this field to leave it unchanged.
    """

    disabled: Optional[bool]
    """
    Indicates whether the license key should be disabled. A value of `true` disables
    the key, while `false` enables it. Omit this field to leave it unchanged.
    """

    expires_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """
    The updated expiration timestamp for the license key in UTC. Use `null` to
    remove the expiration date, or omit this field to leave it unchanged.
    """
