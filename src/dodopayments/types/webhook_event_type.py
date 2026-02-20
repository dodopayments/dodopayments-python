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
    "payout.not_initiated",
    "payout.on_hold",
    "payout.in_progress",
    "payout.failed",
    "payout.success",
    "credit.added",
    "credit.deducted",
    "credit.expired",
    "credit.rolled_over",
    "credit.rollover_forfeited",
    "credit.overage_charged",
    "credit.manual_adjustment",
    "credit.balance_low",
]
