# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable, Optional
from typing_extensions import Required, TypedDict

from .currency import Currency
from .custom_field_param import CustomFieldParam
from .payment_method_types import PaymentMethodTypes
from .customer_request_param import CustomerRequestParam
from .product_item_req_param import ProductItemReqParam
from .subscription_data_param import SubscriptionDataParam
from .checkout_session_flags_param import CheckoutSessionFlagsParam
from .checkout_session_customization_param import CheckoutSessionCustomizationParam
from .checkout_session_billing_address_param import CheckoutSessionBillingAddressParam

__all__ = ["CheckoutSessionCreateParams"]


class CheckoutSessionCreateParams(TypedDict, total=False):
    product_cart: Required[Iterable[ProductItemReqParam]]

    allowed_payment_method_types: Optional[List[PaymentMethodTypes]]
    """
    Customers will never see payment methods that are not in this list. However,
    adding a method here does not guarantee customers will see it. Availability
    still depends on other factors (e.g., customer location, merchant settings).

    Disclaimar: Always provide 'credit' and 'debit' as a fallback. If all payment
    methods are unavailable, checkout session will fail.
    """

    billing_address: Optional[CheckoutSessionBillingAddressParam]
    """Billing address information for the session"""

    billing_currency: Optional[Currency]
    """This field is ingored if adaptive pricing is disabled"""

    confirm: bool
    """If confirm is true, all the details will be finalized.

    If required data is missing, an API error is thrown.
    """

    custom_fields: Optional[Iterable[CustomFieldParam]]
    """Custom fields to collect from customer during checkout (max 5 fields)"""

    customer: Optional[CustomerRequestParam]
    """Customer details for the session"""

    customization: CheckoutSessionCustomizationParam
    """Customization for the checkout session page"""

    discount_code: Optional[str]

    feature_flags: CheckoutSessionFlagsParam

    force_3ds: Optional[bool]
    """Override merchant default 3DS behaviour for this session"""

    metadata: Optional[Dict[str, str]]
    """Additional metadata associated with the payment.

    Defaults to empty if not provided.
    """

    minimal_address: bool
    """
    If true, only zipcode is required when confirm is true; other address fields
    remain optional
    """

    payment_method_id: Optional[str]
    """
    Optional payment method ID to use for this checkout session. Only allowed when
    `confirm` is true. If provided, existing customer id must also be provided.
    """

    product_collection_id: Optional[str]
    """Product collection ID for collection-based checkout flow"""

    return_url: Optional[str]
    """The url to redirect after payment failure or success."""

    short_link: bool
    """If true, returns a shortened checkout URL. Defaults to false if not specified."""

    show_saved_payment_methods: bool
    """Display saved payment methods of a returning customer False by default"""

    subscription_data: Optional[SubscriptionDataParam]
