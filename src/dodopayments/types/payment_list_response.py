# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel
from .currency import Currency
from .intent_status import IntentStatus
from .customer_limited_details import CustomerLimitedDetails

__all__ = ["PaymentListResponse"]


class PaymentListResponse(BaseModel):
    brand_id: str

    created_at: datetime

    currency: Currency

    customer: CustomerLimitedDetails

    metadata: Dict[str, str]

    payment_id: str

    total_amount: int

    payment_method: Optional[str] = None

    payment_method_type: Optional[str] = None

    status: Optional[IntentStatus] = None

    subscription_id: Optional[str] = None
