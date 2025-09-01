# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EventInputParam"]


class EventInputParam(TypedDict, total=False):
    customer_id: Required[str]
    """customer_id of the customer whose usage needs to be tracked"""

    event_id: Required[str]
    """Event Id acts as an idempotency key.

    Any subsequent requests with the same event_id will be ignored
    """

    event_name: Required[str]
    """Name of the event"""

    metadata: Optional[Dict[str, object]]
    """Custom metadata.

    Only key value pairs are accepted, objects or arrays submitted will be rejected.
    """

    timestamp: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Custom Timestamp.

    Defaults to current timestamp in UTC. Timestamps that are older that 1 hour or
    after 5 mins, from current timestamp, will be rejected.
    """
