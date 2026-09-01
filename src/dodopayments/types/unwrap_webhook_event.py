# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .dispute_won_webhook_event import DisputeWonWebhookEvent
from .credit_added_webhook_event import CreditAddedWebhookEvent
from .dispute_lost_webhook_event import DisputeLostWebhookEvent
from .payout_failed_webhook_event import PayoutFailedWebhookEvent
from .refund_failed_webhook_event import RefundFailedWebhookEvent
from .credit_expired_webhook_event import CreditExpiredWebhookEvent
from .dispute_opened_webhook_event import DisputeOpenedWebhookEvent
from .payment_failed_webhook_event import PaymentFailedWebhookEvent
from .payout_created_webhook_event import PayoutCreatedWebhookEvent
from .payout_on_hold_webhook_event import PayoutOnHoldWebhookEvent
from .payout_success_webhook_event import PayoutSuccessWebhookEvent
from .credit_deducted_webhook_event import CreditDeductedWebhookEvent
from .dispute_expired_webhook_event import DisputeExpiredWebhookEvent
from .dunning_started_webhook_event import DunningStartedWebhookEvent
from .dispute_accepted_webhook_event import DisputeAcceptedWebhookEvent
from .refund_succeeded_webhook_event import RefundSucceededWebhookEvent
from .dispute_cancelled_webhook_event import DisputeCancelledWebhookEvent
from .dunning_recovered_webhook_event import DunningRecoveredWebhookEvent
from .payment_cancelled_webhook_event import PaymentCancelledWebhookEvent
from .payment_succeeded_webhook_event import PaymentSucceededWebhookEvent
from .credit_balance_low_webhook_event import CreditBalanceLowWebhookEvent
from .credit_rolled_over_webhook_event import CreditRolledOverWebhookEvent
from .dispute_challenged_webhook_event import DisputeChallengedWebhookEvent
from .payment_processing_webhook_event import PaymentProcessingWebhookEvent
from .payout_in_progress_webhook_event import PayoutInProgressWebhookEvent
from .license_key_created_webhook_event import LicenseKeyCreatedWebhookEvent
from .subscription_active_webhook_event import SubscriptionActiveWebhookEvent
from .subscription_failed_webhook_event import SubscriptionFailedWebhookEvent
from .subscription_paused_webhook_event import SubscriptionPausedWebhookEvent
from .credit_overage_reset_webhook_event import CreditOverageResetWebhookEvent
from .subscription_expired_webhook_event import SubscriptionExpiredWebhookEvent
from .subscription_on_hold_webhook_event import SubscriptionOnHoldWebhookEvent
from .subscription_renewed_webhook_event import SubscriptionRenewedWebhookEvent
from .subscription_updated_webhook_event import SubscriptionUpdatedWebhookEvent
from .subscription_past_due_webhook_event import SubscriptionPastDueWebhookEvent
from .subscription_unpaused_webhook_event import SubscriptionUnpausedWebhookEvent
from .credit_overage_charged_webhook_event import CreditOverageChargedWebhookEvent
from .subscription_cancelled_webhook_event import SubscriptionCancelledWebhookEvent
from .credit_manual_adjustment_webhook_event import CreditManualAdjustmentWebhookEvent
from .entitlement_grant_failed_webhook_event import EntitlementGrantFailedWebhookEvent
from .credit_rollover_forfeited_webhook_event import CreditRolloverForfeitedWebhookEvent
from .entitlement_grant_created_webhook_event import EntitlementGrantCreatedWebhookEvent
from .entitlement_grant_revoked_webhook_event import EntitlementGrantRevokedWebhookEvent
from .subscription_plan_changed_webhook_event import SubscriptionPlanChangedWebhookEvent
from .abandoned_checkout_detected_webhook_event import AbandonedCheckoutDetectedWebhookEvent
from .entitlement_grant_delivered_webhook_event import EntitlementGrantDeliveredWebhookEvent
from .abandoned_checkout_recovered_webhook_event import AbandonedCheckoutRecoveredWebhookEvent
from .subscription_update_payment_method_webhook_event import SubscriptionUpdatePaymentMethodWebhookEvent

__all__ = ["UnwrapWebhookEvent"]

UnwrapWebhookEvent: TypeAlias = Annotated[
    Union[
        AbandonedCheckoutDetectedWebhookEvent,
        AbandonedCheckoutRecoveredWebhookEvent,
        CreditAddedWebhookEvent,
        CreditBalanceLowWebhookEvent,
        CreditDeductedWebhookEvent,
        CreditExpiredWebhookEvent,
        CreditManualAdjustmentWebhookEvent,
        CreditOverageChargedWebhookEvent,
        CreditOverageResetWebhookEvent,
        CreditRolledOverWebhookEvent,
        CreditRolloverForfeitedWebhookEvent,
        DisputeAcceptedWebhookEvent,
        DisputeCancelledWebhookEvent,
        DisputeChallengedWebhookEvent,
        DisputeExpiredWebhookEvent,
        DisputeLostWebhookEvent,
        DisputeOpenedWebhookEvent,
        DisputeWonWebhookEvent,
        DunningRecoveredWebhookEvent,
        DunningStartedWebhookEvent,
        EntitlementGrantCreatedWebhookEvent,
        EntitlementGrantDeliveredWebhookEvent,
        EntitlementGrantFailedWebhookEvent,
        EntitlementGrantRevokedWebhookEvent,
        LicenseKeyCreatedWebhookEvent,
        PaymentCancelledWebhookEvent,
        PaymentFailedWebhookEvent,
        PaymentProcessingWebhookEvent,
        PaymentSucceededWebhookEvent,
        PayoutCreatedWebhookEvent,
        PayoutFailedWebhookEvent,
        PayoutInProgressWebhookEvent,
        PayoutOnHoldWebhookEvent,
        PayoutSuccessWebhookEvent,
        RefundFailedWebhookEvent,
        RefundSucceededWebhookEvent,
        SubscriptionActiveWebhookEvent,
        SubscriptionCancelledWebhookEvent,
        SubscriptionExpiredWebhookEvent,
        SubscriptionFailedWebhookEvent,
        SubscriptionOnHoldWebhookEvent,
        SubscriptionPastDueWebhookEvent,
        SubscriptionPausedWebhookEvent,
        SubscriptionPlanChangedWebhookEvent,
        SubscriptionRenewedWebhookEvent,
        SubscriptionUnpausedWebhookEvent,
        SubscriptionUpdatePaymentMethodWebhookEvent,
        SubscriptionUpdatedWebhookEvent,
    ],
    PropertyInfo(discriminator="type"),
]
