# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .dispute_won_webhook_event import DisputeWonWebhookEvent
from .credit_added_webhook_event import CreditAddedWebhookEvent
from .dispute_lost_webhook_event import DisputeLostWebhookEvent
from .refund_failed_webhook_event import RefundFailedWebhookEvent
from .credit_expired_webhook_event import CreditExpiredWebhookEvent
from .dispute_opened_webhook_event import DisputeOpenedWebhookEvent
from .payment_failed_webhook_event import PaymentFailedWebhookEvent
from .credit_deducted_webhook_event import CreditDeductedWebhookEvent
from .dispute_expired_webhook_event import DisputeExpiredWebhookEvent
from .dispute_accepted_webhook_event import DisputeAcceptedWebhookEvent
from .refund_succeeded_webhook_event import RefundSucceededWebhookEvent
from .dispute_cancelled_webhook_event import DisputeCancelledWebhookEvent
from .payment_cancelled_webhook_event import PaymentCancelledWebhookEvent
from .payment_succeeded_webhook_event import PaymentSucceededWebhookEvent
from .credit_balance_low_webhook_event import CreditBalanceLowWebhookEvent
from .credit_rolled_over_webhook_event import CreditRolledOverWebhookEvent
from .dispute_challenged_webhook_event import DisputeChallengedWebhookEvent
from .payment_processing_webhook_event import PaymentProcessingWebhookEvent
from .license_key_created_webhook_event import LicenseKeyCreatedWebhookEvent
from .subscription_active_webhook_event import SubscriptionActiveWebhookEvent
from .subscription_failed_webhook_event import SubscriptionFailedWebhookEvent
from .subscription_expired_webhook_event import SubscriptionExpiredWebhookEvent
from .subscription_on_hold_webhook_event import SubscriptionOnHoldWebhookEvent
from .subscription_renewed_webhook_event import SubscriptionRenewedWebhookEvent
from .subscription_updated_webhook_event import SubscriptionUpdatedWebhookEvent
from .credit_overage_charged_webhook_event import CreditOverageChargedWebhookEvent
from .subscription_cancelled_webhook_event import SubscriptionCancelledWebhookEvent
from .credit_manual_adjustment_webhook_event import CreditManualAdjustmentWebhookEvent
from .credit_rollover_forfeited_webhook_event import CreditRolloverForfeitedWebhookEvent
from .subscription_plan_changed_webhook_event import SubscriptionPlanChangedWebhookEvent

__all__ = ["UnwrapWebhookEvent"]

UnwrapWebhookEvent: TypeAlias = Union[
    CreditAddedWebhookEvent,
    CreditBalanceLowWebhookEvent,
    CreditDeductedWebhookEvent,
    CreditExpiredWebhookEvent,
    CreditManualAdjustmentWebhookEvent,
    CreditOverageChargedWebhookEvent,
    CreditRolledOverWebhookEvent,
    CreditRolloverForfeitedWebhookEvent,
    DisputeAcceptedWebhookEvent,
    DisputeCancelledWebhookEvent,
    DisputeChallengedWebhookEvent,
    DisputeExpiredWebhookEvent,
    DisputeLostWebhookEvent,
    DisputeOpenedWebhookEvent,
    DisputeWonWebhookEvent,
    LicenseKeyCreatedWebhookEvent,
    PaymentCancelledWebhookEvent,
    PaymentFailedWebhookEvent,
    PaymentProcessingWebhookEvent,
    PaymentSucceededWebhookEvent,
    RefundFailedWebhookEvent,
    RefundSucceededWebhookEvent,
    SubscriptionActiveWebhookEvent,
    SubscriptionCancelledWebhookEvent,
    SubscriptionExpiredWebhookEvent,
    SubscriptionFailedWebhookEvent,
    SubscriptionOnHoldWebhookEvent,
    SubscriptionPlanChangedWebhookEvent,
    SubscriptionRenewedWebhookEvent,
    SubscriptionUpdatedWebhookEvent,
]
