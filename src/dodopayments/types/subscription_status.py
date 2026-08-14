# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["SubscriptionStatus"]

SubscriptionStatus: TypeAlias = Literal["pending", "active", "on_hold", "paused", "cancelled", "failed", "expired"]
