# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["LicenseDeactivateParams"]


class LicenseDeactivateParams(TypedDict, total=False):
    license_key: Required[str]

    license_key_instance_id: Required[str]
