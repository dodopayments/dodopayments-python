# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .refund_param import RefundParam
from .payment_param import PaymentParam
from .get_dispute_param import GetDisputeParam
from .license_key_param import LicenseKeyParam
from .subscription_param import SubscriptionParam
from .webhook_event_type import WebhookEventType

__all__ = [
    "YourWebhookURLCreateParams",
    "DataPayment",
    "DataSubscription",
    "DataRefund",
    "DataDispute",
    "DataLicenseKey",
]


class YourWebhookURLCreateParams(TypedDict, total=False):
    business_id: Required[str]

    data: Required[Union[DataPayment, DataSubscription, DataRefund, DataDispute, DataLicenseKey]]
    """The latest data at the time of delivery attempt"""

    timestamp: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """
    The timestamp of when the event occurred (not necessarily the same of when it
    was delivered)
    """

    type: Required[WebhookEventType]
    """Event types for Dodo events"""

    webhook_id: Required[Annotated[str, PropertyInfo(alias="webhook-id")]]

    webhook_signature: Required[Annotated[str, PropertyInfo(alias="webhook-signature")]]

    webhook_timestamp: Required[Annotated[str, PropertyInfo(alias="webhook-timestamp")]]


class DataPayment(PaymentParam, total=False):
    payload_type: Required[Literal["Payment"]]


class DataSubscription(SubscriptionParam, total=False):
    payload_type: Required[Literal["Subscription"]]


class DataRefund(RefundParam, total=False):
    payload_type: Required[Literal["Refund"]]


class DataDispute(GetDisputeParam, total=False):
    payload_type: Required[Literal["Dispute"]]


class DataLicenseKey(LicenseKeyParam, total=False):
    payload_type: Required[Literal["LicenseKey"]]
