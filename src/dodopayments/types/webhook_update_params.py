# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import TypedDict

from .webhook_event_type import WebhookEventType

__all__ = ["WebhookUpdateParams"]


class WebhookUpdateParams(TypedDict, total=False):
    description: Optional[str]
    """Description of the webhook"""

    disabled: Optional[bool]
    """To Disable the endpoint, set it to true."""

    filter_types: Optional[List[WebhookEventType]]
    """Filter events to the endpoint.

    Webhook event will only be sent for events in the list.
    """

    metadata: Optional[Dict[str, str]]
    """Metadata"""

    rate_limit: Optional[int]
    """Rate limit"""

    url: Optional[str]
    """Url endpoint"""
