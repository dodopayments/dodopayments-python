# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import Required, TypedDict

from .webhook_event_type import WebhookEventType

__all__ = ["WebhookCreateParams"]


class WebhookCreateParams(TypedDict, total=False):
    url: Required[str]
    """Url of the webhook"""

    description: Optional[str]

    disabled: Optional[bool]
    """Create the webhook in a disabled state.

    Default is false
    """

    filter_types: List[WebhookEventType]
    """Filter events to the webhook.

    Webhook event will only be sent for events in the list.
    """

    headers: Optional[Dict[str, str]]
    """Custom headers to be passed"""

    idempotency_key: Optional[str]
    """The request's idempotency key"""

    metadata: Optional[Dict[str, str]]
    """Metadata to be passed to the webhook Defaut is {}"""

    rate_limit: Optional[int]
