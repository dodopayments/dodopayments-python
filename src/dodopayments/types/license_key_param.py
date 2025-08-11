# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .license_key_status import LicenseKeyStatus

__all__ = ["LicenseKeyParam"]


class LicenseKeyParam(TypedDict, total=False):
    id: Required[str]
    """The unique identifier of the license key."""

    business_id: Required[str]
    """The unique identifier of the business associated with the license key."""

    created_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """The timestamp indicating when the license key was created, in UTC."""

    customer_id: Required[str]
    """The unique identifier of the customer associated with the license key."""

    instances_count: Required[int]
    """The current number of instances activated for this license key."""

    key: Required[str]
    """The license key string."""

    payment_id: Required[str]
    """The unique identifier of the payment associated with the license key."""

    product_id: Required[str]
    """The unique identifier of the product associated with the license key."""

    status: Required[LicenseKeyStatus]
    """The current status of the license key (e.g., active, inactive, expired)."""

    activations_limit: Optional[int]
    """The maximum number of activations allowed for this license key."""

    expires_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The timestamp indicating when the license key expires, in UTC."""

    subscription_id: Optional[str]
    """
    The unique identifier of the subscription associated with the license key, if
    any.
    """
