# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Event"]


class Event(BaseModel):
    business_id: str

    customer_id: str

    event_id: str

    event_name: str

    timestamp: datetime

    metadata: Optional[Dict[str, Union[str, float, bool]]] = None
    """Arbitrary key-value metadata.

    Values can be string, integer, number, or boolean.
    """
