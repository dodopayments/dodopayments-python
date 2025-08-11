# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = ["WebhookListResponse"]


class WebhookListResponse(BaseModel):
    id: str
    """The webhook's ID."""

    created_at: str
    """Created at timestamp"""

    description: str
    """An example webhook name."""

    metadata: Dict[str, str]
    """Metadata of the webhook"""

    updated_at: str
    """Updated at timestamp"""

    url: str
    """Url endpoint of the webhook"""

    disabled: Optional[bool] = None
    """Status of the webhook.

    If true, events are not sent
    """

    filter_types: Optional[List[str]] = None
    """Filter events to the webhook.

    Webhook event will only be sent for events in the list.
    """

    rate_limit: Optional[int] = None
    """Configured rate limit"""
