# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .webhook_event_log import WebhookEventLog

__all__ = ["WebhookEventListResponse"]


class WebhookEventListResponse(BaseModel):
    items: List[WebhookEventLog]
