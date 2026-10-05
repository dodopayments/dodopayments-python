# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["RefundNetworkReferenceType"]

RefundNetworkReferenceType: TypeAlias = Literal[
    "acquirer_reference_number", "system_trace_audit_number", "retrieval_reference_number", "other"
]
