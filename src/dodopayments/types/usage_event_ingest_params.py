# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .event_input_param import EventInputParam

__all__ = ["UsageEventIngestParams"]


class UsageEventIngestParams(TypedDict, total=False):
    events: Required[Iterable[EventInputParam]]
    """List of events to be pushed"""
