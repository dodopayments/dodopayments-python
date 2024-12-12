# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..types import outgoing_webhook_create_params
from .._utils import PropertyInfo

__all__ = ["OutgoingWebhookCreateParams"]


class OutgoingWebhookCreateParams(TypedDict, total=False):
    business_id: Required[str]

    data: Required[
        Union[
            outgoing_webhook_create_params.DataPayment,
            outgoing_webhook_create_params.DataSubscription,
            outgoing_webhook_create_params.DataRefund,
            outgoing_webhook_create_params.DataDispute,
        ]
    ]

    timestamp: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """
    The timestamp of when the event occurred (not necessarily the same of when it
    was delivered)
    """

    type: Required[
        Literal[
            "payment.succeeded",
            "payment.failed",
            "payment.processing",
            "payment.cancelled",
            "refund.succeeded",
            "refund.failed",
            "dispute.opened",
            "dispute.expired",
            "dispute.accepted",
            "dispute.cancelled",
            "dispute.challenged",
            "dispute.won",
            "dispute.lost",
            "subscription.active",
            "subscription.on_hold",
            "subscription.paused",
            "subscription.cancelled",
            "subscription.failed",
            "subscription.expired",
        ]
    ]
    """Event types for Dodo events"""

    webhook_id: Required[Annotated[str, PropertyInfo(alias="webhook-id")]]

    webhook_signature: Required[Annotated[str, PropertyInfo(alias="webhook-signature")]]

    webhook_timestamp: Required[Annotated[str, PropertyInfo(alias="webhook-timestamp")]]
