# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .time_interval import TimeInterval

__all__ = ["LicenseKeyDurationParam"]


class LicenseKeyDurationParam(TypedDict, total=False):
    count: Required[int]

    interval: Required[TimeInterval]
