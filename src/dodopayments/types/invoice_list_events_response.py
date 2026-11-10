# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .invoice_event import InvoiceEvent

__all__ = ["InvoiceListEventsResponse"]


class InvoiceListEventsResponse(BaseModel):
    items: List[InvoiceEvent]
