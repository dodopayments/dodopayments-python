# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["LicenseKeyUpdateParams"]


class LicenseKeyUpdateParams(TypedDict, total=False):
    activations_limit: Optional[int]

    disabled: Optional[bool]

    expires_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
