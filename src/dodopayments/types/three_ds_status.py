# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["ThreeDSStatus"]

ThreeDSStatus: TypeAlias = Literal[
    "authenticated", "attempt_acknowledged", "exempted", "failed", "not_supported", "processing_error"
]
