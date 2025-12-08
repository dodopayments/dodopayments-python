# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["WebhookEventType"]

WebhookEventType: TypeAlias = Literal[
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
    "subscription.renewed",
    "subscription.on_hold",
    "subscription.cancelled",
    "subscription.failed",
    "subscription.expired",
    "subscription.plan_changed",
    "subscription.updated",
    "license_key.created",
]
