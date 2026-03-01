# CheckoutSessions

Types:

```python
from dodopayments.types import (
    CheckoutSessionBillingAddress,
    CheckoutSessionCustomization,
    CheckoutSessionFlags,
    CheckoutSessionRequest,
    CheckoutSessionResponse,
    CheckoutSessionStatus,
    CustomField,
    ProductItemReq,
    SubscriptionData,
    ThemeConfig,
    ThemeModeConfig,
    CheckoutSessionPreviewResponse,
)
```

Methods:

- <code title="post /checkouts">client.checkout_sessions.<a href="./src/dodopayments/resources/checkout_sessions.py">create</a>(\*\*<a href="src/dodopayments/types/checkout_session_create_params.py">params</a>) -> <a href="./src/dodopayments/types/checkout_session_response.py">CheckoutSessionResponse</a></code>
- <code title="get /checkouts/{id}">client.checkout_sessions.<a href="./src/dodopayments/resources/checkout_sessions.py">retrieve</a>(id) -> <a href="./src/dodopayments/types/checkout_session_status.py">CheckoutSessionStatus</a></code>
- <code title="post /checkouts/preview">client.checkout_sessions.<a href="./src/dodopayments/resources/checkout_sessions.py">preview</a>(\*\*<a href="src/dodopayments/types/checkout_session_preview_params.py">params</a>) -> <a href="./src/dodopayments/types/checkout_session_preview_response.py">CheckoutSessionPreviewResponse</a></code>

# Payments

Types:

```python
from dodopayments.types import (
    AttachExistingCustomer,
    BillingAddress,
    CreateNewCustomer,
    CustomFieldResponse,
    CustomerLimitedDetails,
    CustomerRequest,
    IntentStatus,
    NewCustomer,
    OneTimeProductCartItem,
    Payment,
    PaymentMethodTypes,
    PaymentRefundStatus,
    RefundListItem,
    PaymentCreateResponse,
    PaymentListResponse,
    PaymentRetrieveLineItemsResponse,
)
```

Methods:

- <code title="post /payments">client.payments.<a href="./src/dodopayments/resources/payments.py">create</a>(\*\*<a href="src/dodopayments/types/payment_create_params.py">params</a>) -> <a href="./src/dodopayments/types/payment_create_response.py">PaymentCreateResponse</a></code>
- <code title="get /payments/{payment_id}">client.payments.<a href="./src/dodopayments/resources/payments.py">retrieve</a>(payment_id) -> <a href="./src/dodopayments/types/payment.py">Payment</a></code>
- <code title="get /payments">client.payments.<a href="./src/dodopayments/resources/payments.py">list</a>(\*\*<a href="src/dodopayments/types/payment_list_params.py">params</a>) -> <a href="./src/dodopayments/types/payment_list_response.py">SyncDefaultPageNumberPagination[PaymentListResponse]</a></code>
- <code title="get /payments/{payment_id}/line-items">client.payments.<a href="./src/dodopayments/resources/payments.py">retrieve_line_items</a>(payment_id) -> <a href="./src/dodopayments/types/payment_retrieve_line_items_response.py">PaymentRetrieveLineItemsResponse</a></code>

# Subscriptions

Types:

```python
from dodopayments.types import (
    AddonCartResponseItem,
    AttachAddon,
    OnDemandSubscription,
    Subscription,
    SubscriptionStatus,
    TimeInterval,
    UpdateSubscriptionPlanReq,
    SubscriptionCreateResponse,
    SubscriptionListResponse,
    SubscriptionChargeResponse,
    SubscriptionPreviewChangePlanResponse,
    SubscriptionRetrieveCreditUsageResponse,
    SubscriptionRetrieveUsageHistoryResponse,
    SubscriptionUpdatePaymentMethodResponse,
)
```

Methods:

- <code title="post /subscriptions">client.subscriptions.<a href="./src/dodopayments/resources/subscriptions.py">create</a>(\*\*<a href="src/dodopayments/types/subscription_create_params.py">params</a>) -> <a href="./src/dodopayments/types/subscription_create_response.py">SubscriptionCreateResponse</a></code>
- <code title="get /subscriptions/{subscription_id}">client.subscriptions.<a href="./src/dodopayments/resources/subscriptions.py">retrieve</a>(subscription_id) -> <a href="./src/dodopayments/types/subscription.py">Subscription</a></code>
- <code title="patch /subscriptions/{subscription_id}">client.subscriptions.<a href="./src/dodopayments/resources/subscriptions.py">update</a>(subscription_id, \*\*<a href="src/dodopayments/types/subscription_update_params.py">params</a>) -> <a href="./src/dodopayments/types/subscription.py">Subscription</a></code>
- <code title="get /subscriptions">client.subscriptions.<a href="./src/dodopayments/resources/subscriptions.py">list</a>(\*\*<a href="src/dodopayments/types/subscription_list_params.py">params</a>) -> <a href="./src/dodopayments/types/subscription_list_response.py">SyncDefaultPageNumberPagination[SubscriptionListResponse]</a></code>
- <code title="post /subscriptions/{subscription_id}/change-plan">client.subscriptions.<a href="./src/dodopayments/resources/subscriptions.py">change_plan</a>(subscription_id, \*\*<a href="src/dodopayments/types/subscription_change_plan_params.py">params</a>) -> None</code>
- <code title="post /subscriptions/{subscription_id}/charge">client.subscriptions.<a href="./src/dodopayments/resources/subscriptions.py">charge</a>(subscription_id, \*\*<a href="src/dodopayments/types/subscription_charge_params.py">params</a>) -> <a href="./src/dodopayments/types/subscription_charge_response.py">SubscriptionChargeResponse</a></code>
- <code title="post /subscriptions/{subscription_id}/change-plan/preview">client.subscriptions.<a href="./src/dodopayments/resources/subscriptions.py">preview_change_plan</a>(subscription_id, \*\*<a href="src/dodopayments/types/subscription_preview_change_plan_params.py">params</a>) -> <a href="./src/dodopayments/types/subscription_preview_change_plan_response.py">SubscriptionPreviewChangePlanResponse</a></code>
- <code title="get /subscriptions/{subscription_id}/credit-usage">client.subscriptions.<a href="./src/dodopayments/resources/subscriptions.py">retrieve_credit_usage</a>(subscription_id) -> <a href="./src/dodopayments/types/subscription_retrieve_credit_usage_response.py">SubscriptionRetrieveCreditUsageResponse</a></code>
- <code title="get /subscriptions/{subscription_id}/usage-history">client.subscriptions.<a href="./src/dodopayments/resources/subscriptions.py">retrieve_usage_history</a>(subscription_id, \*\*<a href="src/dodopayments/types/subscription_retrieve_usage_history_params.py">params</a>) -> <a href="./src/dodopayments/types/subscription_retrieve_usage_history_response.py">SyncDefaultPageNumberPagination[SubscriptionRetrieveUsageHistoryResponse]</a></code>
- <code title="post /subscriptions/{subscription_id}/update-payment-method">client.subscriptions.<a href="./src/dodopayments/resources/subscriptions.py">update_payment_method</a>(subscription_id, \*\*<a href="src/dodopayments/types/subscription_update_payment_method_params.py">params</a>) -> <a href="./src/dodopayments/types/subscription_update_payment_method_response.py">SubscriptionUpdatePaymentMethodResponse</a></code>

# Invoices

## Payments

Methods:

- <code title="get /invoices/payments/{payment_id}">client.invoices.payments.<a href="./src/dodopayments/resources/invoices/payments.py">retrieve</a>(payment_id) -> BinaryAPIResponse</code>
- <code title="get /invoices/refunds/{refund_id}">client.invoices.payments.<a href="./src/dodopayments/resources/invoices/payments.py">retrieve_refund</a>(refund_id) -> BinaryAPIResponse</code>

# Licenses

Types:

```python
from dodopayments.types import LicenseActivateResponse, LicenseValidateResponse
```

Methods:

- <code title="post /licenses/activate">client.licenses.<a href="./src/dodopayments/resources/licenses.py">activate</a>(\*\*<a href="src/dodopayments/types/license_activate_params.py">params</a>) -> <a href="./src/dodopayments/types/license_activate_response.py">LicenseActivateResponse</a></code>
- <code title="post /licenses/deactivate">client.licenses.<a href="./src/dodopayments/resources/licenses.py">deactivate</a>(\*\*<a href="src/dodopayments/types/license_deactivate_params.py">params</a>) -> None</code>
- <code title="post /licenses/validate">client.licenses.<a href="./src/dodopayments/resources/licenses.py">validate</a>(\*\*<a href="src/dodopayments/types/license_validate_params.py">params</a>) -> <a href="./src/dodopayments/types/license_validate_response.py">LicenseValidateResponse</a></code>

# LicenseKeys

Types:

```python
from dodopayments.types import LicenseKey, LicenseKeyStatus
```

Methods:

- <code title="get /license_keys/{id}">client.license_keys.<a href="./src/dodopayments/resources/license_keys.py">retrieve</a>(id) -> <a href="./src/dodopayments/types/license_key.py">LicenseKey</a></code>
- <code title="patch /license_keys/{id}">client.license_keys.<a href="./src/dodopayments/resources/license_keys.py">update</a>(id, \*\*<a href="src/dodopayments/types/license_key_update_params.py">params</a>) -> <a href="./src/dodopayments/types/license_key.py">LicenseKey</a></code>
- <code title="get /license_keys">client.license_keys.<a href="./src/dodopayments/resources/license_keys.py">list</a>(\*\*<a href="src/dodopayments/types/license_key_list_params.py">params</a>) -> <a href="./src/dodopayments/types/license_key.py">SyncDefaultPageNumberPagination[LicenseKey]</a></code>

# LicenseKeyInstances

Types:

```python
from dodopayments.types import LicenseKeyInstance
```

Methods:

- <code title="get /license_key_instances/{id}">client.license_key_instances.<a href="./src/dodopayments/resources/license_key_instances.py">retrieve</a>(id) -> <a href="./src/dodopayments/types/license_key_instance.py">LicenseKeyInstance</a></code>
- <code title="patch /license_key_instances/{id}">client.license_key_instances.<a href="./src/dodopayments/resources/license_key_instances.py">update</a>(id, \*\*<a href="src/dodopayments/types/license_key_instance_update_params.py">params</a>) -> <a href="./src/dodopayments/types/license_key_instance.py">LicenseKeyInstance</a></code>
- <code title="get /license_key_instances">client.license_key_instances.<a href="./src/dodopayments/resources/license_key_instances.py">list</a>(\*\*<a href="src/dodopayments/types/license_key_instance_list_params.py">params</a>) -> <a href="./src/dodopayments/types/license_key_instance.py">SyncDefaultPageNumberPagination[LicenseKeyInstance]</a></code>

# Customers

Types:

```python
from dodopayments.types import (
    Customer,
    CustomerPortalSession,
    CustomerListCreditEntitlementsResponse,
    CustomerRetrievePaymentMethodsResponse,
)
```

Methods:

- <code title="post /customers">client.customers.<a href="./src/dodopayments/resources/customers/customers.py">create</a>(\*\*<a href="src/dodopayments/types/customer_create_params.py">params</a>) -> <a href="./src/dodopayments/types/customer.py">Customer</a></code>
- <code title="get /customers/{customer_id}">client.customers.<a href="./src/dodopayments/resources/customers/customers.py">retrieve</a>(customer_id) -> <a href="./src/dodopayments/types/customer.py">Customer</a></code>
- <code title="patch /customers/{customer_id}">client.customers.<a href="./src/dodopayments/resources/customers/customers.py">update</a>(customer_id, \*\*<a href="src/dodopayments/types/customer_update_params.py">params</a>) -> <a href="./src/dodopayments/types/customer.py">Customer</a></code>
- <code title="get /customers">client.customers.<a href="./src/dodopayments/resources/customers/customers.py">list</a>(\*\*<a href="src/dodopayments/types/customer_list_params.py">params</a>) -> <a href="./src/dodopayments/types/customer.py">SyncDefaultPageNumberPagination[Customer]</a></code>
- <code title="get /customers/{customer_id}/credit-entitlements">client.customers.<a href="./src/dodopayments/resources/customers/customers.py">list_credit_entitlements</a>(customer_id) -> <a href="./src/dodopayments/types/customer_list_credit_entitlements_response.py">CustomerListCreditEntitlementsResponse</a></code>
- <code title="get /customers/{customer_id}/payment-methods">client.customers.<a href="./src/dodopayments/resources/customers/customers.py">retrieve_payment_methods</a>(customer_id) -> <a href="./src/dodopayments/types/customer_retrieve_payment_methods_response.py">CustomerRetrievePaymentMethodsResponse</a></code>

## CustomerPortal

Methods:

- <code title="post /customers/{customer_id}/customer-portal/session">client.customers.customer_portal.<a href="./src/dodopayments/resources/customers/customer_portal.py">create</a>(customer_id, \*\*<a href="src/dodopayments/types/customers/customer_portal_create_params.py">params</a>) -> <a href="./src/dodopayments/types/customer_portal_session.py">CustomerPortalSession</a></code>

## Wallets

Types:

```python
from dodopayments.types.customers import CustomerWallet, WalletListResponse
```

Methods:

- <code title="get /customers/{customer_id}/wallets">client.customers.wallets.<a href="./src/dodopayments/resources/customers/wallets/wallets.py">list</a>(customer_id) -> <a href="./src/dodopayments/types/customers/wallet_list_response.py">WalletListResponse</a></code>

### LedgerEntries

Types:

```python
from dodopayments.types.customers.wallets import CustomerWalletTransaction
```

Methods:

- <code title="post /customers/{customer_id}/wallets/ledger-entries">client.customers.wallets.ledger_entries.<a href="./src/dodopayments/resources/customers/wallets/ledger_entries.py">create</a>(customer_id, \*\*<a href="src/dodopayments/types/customers/wallets/ledger_entry_create_params.py">params</a>) -> <a href="./src/dodopayments/types/customers/customer_wallet.py">CustomerWallet</a></code>
- <code title="get /customers/{customer_id}/wallets/ledger-entries">client.customers.wallets.ledger_entries.<a href="./src/dodopayments/resources/customers/wallets/ledger_entries.py">list</a>(customer_id, \*\*<a href="src/dodopayments/types/customers/wallets/ledger_entry_list_params.py">params</a>) -> <a href="./src/dodopayments/types/customers/wallets/customer_wallet_transaction.py">SyncDefaultPageNumberPagination[CustomerWalletTransaction]</a></code>

# Refunds

Types:

```python
from dodopayments.types import Refund, RefundStatus
```

Methods:

- <code title="post /refunds">client.refunds.<a href="./src/dodopayments/resources/refunds.py">create</a>(\*\*<a href="src/dodopayments/types/refund_create_params.py">params</a>) -> <a href="./src/dodopayments/types/refund.py">Refund</a></code>
- <code title="get /refunds/{refund_id}">client.refunds.<a href="./src/dodopayments/resources/refunds.py">retrieve</a>(refund_id) -> <a href="./src/dodopayments/types/refund.py">Refund</a></code>
- <code title="get /refunds">client.refunds.<a href="./src/dodopayments/resources/refunds.py">list</a>(\*\*<a href="src/dodopayments/types/refund_list_params.py">params</a>) -> <a href="./src/dodopayments/types/refund_list_item.py">SyncDefaultPageNumberPagination[RefundListItem]</a></code>

# Disputes

Types:

```python
from dodopayments.types import Dispute, DisputeStage, DisputeStatus, GetDispute, DisputeListResponse
```

Methods:

- <code title="get /disputes/{dispute_id}">client.disputes.<a href="./src/dodopayments/resources/disputes.py">retrieve</a>(dispute_id) -> <a href="./src/dodopayments/types/get_dispute.py">GetDispute</a></code>
- <code title="get /disputes">client.disputes.<a href="./src/dodopayments/resources/disputes.py">list</a>(\*\*<a href="src/dodopayments/types/dispute_list_params.py">params</a>) -> <a href="./src/dodopayments/types/dispute_list_response.py">SyncDefaultPageNumberPagination[DisputeListResponse]</a></code>

# Payouts

Types:

```python
from dodopayments.types import PayoutListResponse
```

Methods:

- <code title="get /payouts">client.payouts.<a href="./src/dodopayments/resources/payouts.py">list</a>(\*\*<a href="src/dodopayments/types/payout_list_params.py">params</a>) -> <a href="./src/dodopayments/types/payout_list_response.py">SyncDefaultPageNumberPagination[PayoutListResponse]</a></code>

# Products

Types:

```python
from dodopayments.types import (
    AddMeterToPrice,
    AttachCreditEntitlement,
    CbbProrationBehavior,
    LicenseKeyDuration,
    Price,
    Product,
    ProductListResponse,
    ProductUpdateFilesResponse,
)
```

Methods:

- <code title="post /products">client.products.<a href="./src/dodopayments/resources/products/products.py">create</a>(\*\*<a href="src/dodopayments/types/product_create_params.py">params</a>) -> <a href="./src/dodopayments/types/product.py">Product</a></code>
- <code title="get /products/{id}">client.products.<a href="./src/dodopayments/resources/products/products.py">retrieve</a>(id) -> <a href="./src/dodopayments/types/product.py">Product</a></code>
- <code title="patch /products/{id}">client.products.<a href="./src/dodopayments/resources/products/products.py">update</a>(id, \*\*<a href="src/dodopayments/types/product_update_params.py">params</a>) -> None</code>
- <code title="get /products">client.products.<a href="./src/dodopayments/resources/products/products.py">list</a>(\*\*<a href="src/dodopayments/types/product_list_params.py">params</a>) -> <a href="./src/dodopayments/types/product_list_response.py">SyncDefaultPageNumberPagination[ProductListResponse]</a></code>
- <code title="delete /products/{id}">client.products.<a href="./src/dodopayments/resources/products/products.py">archive</a>(id) -> None</code>
- <code title="post /products/{id}/unarchive">client.products.<a href="./src/dodopayments/resources/products/products.py">unarchive</a>(id) -> None</code>
- <code title="put /products/{id}/files">client.products.<a href="./src/dodopayments/resources/products/products.py">update_files</a>(id, \*\*<a href="src/dodopayments/types/product_update_files_params.py">params</a>) -> <a href="./src/dodopayments/types/product_update_files_response.py">ProductUpdateFilesResponse</a></code>

## Images

Types:

```python
from dodopayments.types.products import ImageUpdateResponse
```

Methods:

- <code title="put /products/{id}/images">client.products.images.<a href="./src/dodopayments/resources/products/images.py">update</a>(id, \*\*<a href="src/dodopayments/types/products/image_update_params.py">params</a>) -> <a href="./src/dodopayments/types/products/image_update_response.py">ImageUpdateResponse</a></code>

## ShortLinks

Types:

```python
from dodopayments.types.products import ShortLinkCreateResponse, ShortLinkListResponse
```

Methods:

- <code title="post /products/{id}/short_links">client.products.short_links.<a href="./src/dodopayments/resources/products/short_links.py">create</a>(id, \*\*<a href="src/dodopayments/types/products/short_link_create_params.py">params</a>) -> <a href="./src/dodopayments/types/products/short_link_create_response.py">ShortLinkCreateResponse</a></code>
- <code title="get /products/short_links">client.products.short_links.<a href="./src/dodopayments/resources/products/short_links.py">list</a>(\*\*<a href="src/dodopayments/types/products/short_link_list_params.py">params</a>) -> <a href="./src/dodopayments/types/products/short_link_list_response.py">SyncDefaultPageNumberPagination[ShortLinkListResponse]</a></code>

# Misc

Types:

```python
from dodopayments.types import (
    CountryCode,
    Currency,
    TaxCategory,
    MiscListSupportedCountriesResponse,
)
```

Methods:

- <code title="get /checkout/supported_countries">client.misc.<a href="./src/dodopayments/resources/misc.py">list_supported_countries</a>() -> <a href="./src/dodopayments/types/misc_list_supported_countries_response.py">MiscListSupportedCountriesResponse</a></code>

# Discounts

Types:

```python
from dodopayments.types import Discount, DiscountType
```

Methods:

- <code title="post /discounts">client.discounts.<a href="./src/dodopayments/resources/discounts.py">create</a>(\*\*<a href="src/dodopayments/types/discount_create_params.py">params</a>) -> <a href="./src/dodopayments/types/discount.py">Discount</a></code>
- <code title="get /discounts/{discount_id}">client.discounts.<a href="./src/dodopayments/resources/discounts.py">retrieve</a>(discount_id) -> <a href="./src/dodopayments/types/discount.py">Discount</a></code>
- <code title="patch /discounts/{discount_id}">client.discounts.<a href="./src/dodopayments/resources/discounts.py">update</a>(discount_id, \*\*<a href="src/dodopayments/types/discount_update_params.py">params</a>) -> <a href="./src/dodopayments/types/discount.py">Discount</a></code>
- <code title="get /discounts">client.discounts.<a href="./src/dodopayments/resources/discounts.py">list</a>(\*\*<a href="src/dodopayments/types/discount_list_params.py">params</a>) -> <a href="./src/dodopayments/types/discount.py">SyncDefaultPageNumberPagination[Discount]</a></code>
- <code title="delete /discounts/{discount_id}">client.discounts.<a href="./src/dodopayments/resources/discounts.py">delete</a>(discount_id) -> None</code>
- <code title="get /discounts/code/{code}">client.discounts.<a href="./src/dodopayments/resources/discounts.py">retrieve_by_code</a>(code) -> <a href="./src/dodopayments/types/discount.py">Discount</a></code>

# Addons

Types:

```python
from dodopayments.types import AddonResponse, AddonUpdateImagesResponse
```

Methods:

- <code title="post /addons">client.addons.<a href="./src/dodopayments/resources/addons.py">create</a>(\*\*<a href="src/dodopayments/types/addon_create_params.py">params</a>) -> <a href="./src/dodopayments/types/addon_response.py">AddonResponse</a></code>
- <code title="get /addons/{id}">client.addons.<a href="./src/dodopayments/resources/addons.py">retrieve</a>(id) -> <a href="./src/dodopayments/types/addon_response.py">AddonResponse</a></code>
- <code title="patch /addons/{id}">client.addons.<a href="./src/dodopayments/resources/addons.py">update</a>(id, \*\*<a href="src/dodopayments/types/addon_update_params.py">params</a>) -> <a href="./src/dodopayments/types/addon_response.py">AddonResponse</a></code>
- <code title="get /addons">client.addons.<a href="./src/dodopayments/resources/addons.py">list</a>(\*\*<a href="src/dodopayments/types/addon_list_params.py">params</a>) -> <a href="./src/dodopayments/types/addon_response.py">SyncDefaultPageNumberPagination[AddonResponse]</a></code>
- <code title="put /addons/{id}/images">client.addons.<a href="./src/dodopayments/resources/addons.py">update_images</a>(id) -> <a href="./src/dodopayments/types/addon_update_images_response.py">AddonUpdateImagesResponse</a></code>

# Brands

Types:

```python
from dodopayments.types import Brand, BrandListResponse, BrandUpdateImagesResponse
```

Methods:

- <code title="post /brands">client.brands.<a href="./src/dodopayments/resources/brands.py">create</a>(\*\*<a href="src/dodopayments/types/brand_create_params.py">params</a>) -> <a href="./src/dodopayments/types/brand.py">Brand</a></code>
- <code title="get /brands/{id}">client.brands.<a href="./src/dodopayments/resources/brands.py">retrieve</a>(id) -> <a href="./src/dodopayments/types/brand.py">Brand</a></code>
- <code title="patch /brands/{id}">client.brands.<a href="./src/dodopayments/resources/brands.py">update</a>(id, \*\*<a href="src/dodopayments/types/brand_update_params.py">params</a>) -> <a href="./src/dodopayments/types/brand.py">Brand</a></code>
- <code title="get /brands">client.brands.<a href="./src/dodopayments/resources/brands.py">list</a>() -> <a href="./src/dodopayments/types/brand_list_response.py">BrandListResponse</a></code>
- <code title="put /brands/{id}/images">client.brands.<a href="./src/dodopayments/resources/brands.py">update_images</a>(id) -> <a href="./src/dodopayments/types/brand_update_images_response.py">BrandUpdateImagesResponse</a></code>

# Webhooks

Types:

```python
from dodopayments.types import (
    WebhookDetails,
    WebhookRetrieveSecretResponse,
    CreditAddedWebhookEvent,
    CreditBalanceLowWebhookEvent,
    CreditDeductedWebhookEvent,
    CreditExpiredWebhookEvent,
    CreditManualAdjustmentWebhookEvent,
    CreditOverageChargedWebhookEvent,
    CreditRolledOverWebhookEvent,
    CreditRolloverForfeitedWebhookEvent,
    DisputeAcceptedWebhookEvent,
    DisputeCancelledWebhookEvent,
    DisputeChallengedWebhookEvent,
    DisputeExpiredWebhookEvent,
    DisputeLostWebhookEvent,
    DisputeOpenedWebhookEvent,
    DisputeWonWebhookEvent,
    LicenseKeyCreatedWebhookEvent,
    PaymentCancelledWebhookEvent,
    PaymentFailedWebhookEvent,
    PaymentProcessingWebhookEvent,
    PaymentSucceededWebhookEvent,
    RefundFailedWebhookEvent,
    RefundSucceededWebhookEvent,
    SubscriptionActiveWebhookEvent,
    SubscriptionCancelledWebhookEvent,
    SubscriptionExpiredWebhookEvent,
    SubscriptionFailedWebhookEvent,
    SubscriptionOnHoldWebhookEvent,
    SubscriptionPlanChangedWebhookEvent,
    SubscriptionRenewedWebhookEvent,
    SubscriptionUpdatedWebhookEvent,
    CreditAddedWebhookEvent,
    CreditBalanceLowWebhookEvent,
    CreditDeductedWebhookEvent,
    CreditExpiredWebhookEvent,
    CreditManualAdjustmentWebhookEvent,
    CreditOverageChargedWebhookEvent,
    CreditRolledOverWebhookEvent,
    CreditRolloverForfeitedWebhookEvent,
    DisputeAcceptedWebhookEvent,
    DisputeCancelledWebhookEvent,
    DisputeChallengedWebhookEvent,
    DisputeExpiredWebhookEvent,
    DisputeLostWebhookEvent,
    DisputeOpenedWebhookEvent,
    DisputeWonWebhookEvent,
    LicenseKeyCreatedWebhookEvent,
    PaymentCancelledWebhookEvent,
    PaymentFailedWebhookEvent,
    PaymentProcessingWebhookEvent,
    PaymentSucceededWebhookEvent,
    RefundFailedWebhookEvent,
    RefundSucceededWebhookEvent,
    SubscriptionActiveWebhookEvent,
    SubscriptionCancelledWebhookEvent,
    SubscriptionExpiredWebhookEvent,
    SubscriptionFailedWebhookEvent,
    SubscriptionOnHoldWebhookEvent,
    SubscriptionPlanChangedWebhookEvent,
    SubscriptionRenewedWebhookEvent,
    SubscriptionUpdatedWebhookEvent,
    UnsafeUnwrapWebhookEvent,
    UnwrapWebhookEvent,
)
```

Methods:

- <code title="post /webhooks">client.webhooks.<a href="./src/dodopayments/resources/webhooks/webhooks.py">create</a>(\*\*<a href="src/dodopayments/types/webhook_create_params.py">params</a>) -> <a href="./src/dodopayments/types/webhook_details.py">WebhookDetails</a></code>
- <code title="get /webhooks/{webhook_id}">client.webhooks.<a href="./src/dodopayments/resources/webhooks/webhooks.py">retrieve</a>(webhook_id) -> <a href="./src/dodopayments/types/webhook_details.py">WebhookDetails</a></code>
- <code title="patch /webhooks/{webhook_id}">client.webhooks.<a href="./src/dodopayments/resources/webhooks/webhooks.py">update</a>(webhook_id, \*\*<a href="src/dodopayments/types/webhook_update_params.py">params</a>) -> <a href="./src/dodopayments/types/webhook_details.py">WebhookDetails</a></code>
- <code title="get /webhooks">client.webhooks.<a href="./src/dodopayments/resources/webhooks/webhooks.py">list</a>(\*\*<a href="src/dodopayments/types/webhook_list_params.py">params</a>) -> <a href="./src/dodopayments/types/webhook_details.py">SyncCursorPagePagination[WebhookDetails]</a></code>
- <code title="delete /webhooks/{webhook_id}">client.webhooks.<a href="./src/dodopayments/resources/webhooks/webhooks.py">delete</a>(webhook_id) -> None</code>
- <code title="get /webhooks/{webhook_id}/secret">client.webhooks.<a href="./src/dodopayments/resources/webhooks/webhooks.py">retrieve_secret</a>(webhook_id) -> <a href="./src/dodopayments/types/webhook_retrieve_secret_response.py">WebhookRetrieveSecretResponse</a></code>

## Headers

Types:

```python
from dodopayments.types.webhooks import HeaderRetrieveResponse
```

Methods:

- <code title="get /webhooks/{webhook_id}/headers">client.webhooks.headers.<a href="./src/dodopayments/resources/webhooks/headers.py">retrieve</a>(webhook_id) -> <a href="./src/dodopayments/types/webhooks/header_retrieve_response.py">HeaderRetrieveResponse</a></code>
- <code title="patch /webhooks/{webhook_id}/headers">client.webhooks.headers.<a href="./src/dodopayments/resources/webhooks/headers.py">update</a>(webhook_id, \*\*<a href="src/dodopayments/types/webhooks/header_update_params.py">params</a>) -> None</code>

# WebhookEvents

Types:

```python
from dodopayments.types import WebhookEventType, WebhookPayload
```

# UsageEvents

Types:

```python
from dodopayments.types import Event, EventInput, UsageEventIngestResponse
```

Methods:

- <code title="get /events/{event_id}">client.usage_events.<a href="./src/dodopayments/resources/usage_events.py">retrieve</a>(event_id) -> <a href="./src/dodopayments/types/event.py">Event</a></code>
- <code title="get /events">client.usage_events.<a href="./src/dodopayments/resources/usage_events.py">list</a>(\*\*<a href="src/dodopayments/types/usage_event_list_params.py">params</a>) -> <a href="./src/dodopayments/types/event.py">SyncDefaultPageNumberPagination[Event]</a></code>
- <code title="post /events/ingest">client.usage_events.<a href="./src/dodopayments/resources/usage_events.py">ingest</a>(\*\*<a href="src/dodopayments/types/usage_event_ingest_params.py">params</a>) -> <a href="./src/dodopayments/types/usage_event_ingest_response.py">UsageEventIngestResponse</a></code>

# Meters

Types:

```python
from dodopayments.types import Conjunction, FilterOperator, Meter, MeterAggregation, MeterFilter
```

Methods:

- <code title="post /meters">client.meters.<a href="./src/dodopayments/resources/meters.py">create</a>(\*\*<a href="src/dodopayments/types/meter_create_params.py">params</a>) -> <a href="./src/dodopayments/types/meter.py">Meter</a></code>
- <code title="get /meters/{id}">client.meters.<a href="./src/dodopayments/resources/meters.py">retrieve</a>(id) -> <a href="./src/dodopayments/types/meter.py">Meter</a></code>
- <code title="get /meters">client.meters.<a href="./src/dodopayments/resources/meters.py">list</a>(\*\*<a href="src/dodopayments/types/meter_list_params.py">params</a>) -> <a href="./src/dodopayments/types/meter.py">SyncDefaultPageNumberPagination[Meter]</a></code>
- <code title="delete /meters/{id}">client.meters.<a href="./src/dodopayments/resources/meters.py">archive</a>(id) -> None</code>
- <code title="post /meters/{id}/unarchive">client.meters.<a href="./src/dodopayments/resources/meters.py">unarchive</a>(id) -> None</code>

# Balances

Types:

```python
from dodopayments.types import BalanceLedgerEntry
```

Methods:

- <code title="get /balances/ledger">client.balances.<a href="./src/dodopayments/resources/balances.py">retrieve_ledger</a>(\*\*<a href="src/dodopayments/types/balance_retrieve_ledger_params.py">params</a>) -> <a href="./src/dodopayments/types/balance_ledger_entry.py">SyncDefaultPageNumberPagination[BalanceLedgerEntry]</a></code>

# CreditEntitlements

Types:

```python
from dodopayments.types import CbbOverageBehavior, CreditEntitlement
```

Methods:

- <code title="post /credit-entitlements">client.credit_entitlements.<a href="./src/dodopayments/resources/credit_entitlements/credit_entitlements.py">create</a>(\*\*<a href="src/dodopayments/types/credit_entitlement_create_params.py">params</a>) -> <a href="./src/dodopayments/types/credit_entitlement.py">CreditEntitlement</a></code>
- <code title="get /credit-entitlements/{id}">client.credit_entitlements.<a href="./src/dodopayments/resources/credit_entitlements/credit_entitlements.py">retrieve</a>(id) -> <a href="./src/dodopayments/types/credit_entitlement.py">CreditEntitlement</a></code>
- <code title="patch /credit-entitlements/{id}">client.credit_entitlements.<a href="./src/dodopayments/resources/credit_entitlements/credit_entitlements.py">update</a>(id, \*\*<a href="src/dodopayments/types/credit_entitlement_update_params.py">params</a>) -> None</code>
- <code title="get /credit-entitlements">client.credit_entitlements.<a href="./src/dodopayments/resources/credit_entitlements/credit_entitlements.py">list</a>(\*\*<a href="src/dodopayments/types/credit_entitlement_list_params.py">params</a>) -> <a href="./src/dodopayments/types/credit_entitlement.py">SyncDefaultPageNumberPagination[CreditEntitlement]</a></code>
- <code title="delete /credit-entitlements/{id}">client.credit_entitlements.<a href="./src/dodopayments/resources/credit_entitlements/credit_entitlements.py">delete</a>(id) -> None</code>
- <code title="post /credit-entitlements/{id}/undelete">client.credit_entitlements.<a href="./src/dodopayments/resources/credit_entitlements/credit_entitlements.py">undelete</a>(id) -> None</code>

## Balances

Types:

```python
from dodopayments.types.credit_entitlements import (
    CreditLedgerEntry,
    CustomerCreditBalance,
    LedgerEntryType,
    BalanceCreateLedgerEntryResponse,
    BalanceListGrantsResponse,
)
```

Methods:

- <code title="get /credit-entitlements/{credit_entitlement_id}/balances/{customer_id}">client.credit_entitlements.balances.<a href="./src/dodopayments/resources/credit_entitlements/balances.py">retrieve</a>(customer_id, \*, credit_entitlement_id) -> <a href="./src/dodopayments/types/credit_entitlements/customer_credit_balance.py">CustomerCreditBalance</a></code>
- <code title="get /credit-entitlements/{credit_entitlement_id}/balances">client.credit_entitlements.balances.<a href="./src/dodopayments/resources/credit_entitlements/balances.py">list</a>(credit_entitlement_id, \*\*<a href="src/dodopayments/types/credit_entitlements/balance_list_params.py">params</a>) -> <a href="./src/dodopayments/types/credit_entitlements/customer_credit_balance.py">SyncDefaultPageNumberPagination[CustomerCreditBalance]</a></code>
- <code title="post /credit-entitlements/{credit_entitlement_id}/balances/{customer_id}/ledger-entries">client.credit_entitlements.balances.<a href="./src/dodopayments/resources/credit_entitlements/balances.py">create_ledger_entry</a>(customer_id, \*, credit_entitlement_id, \*\*<a href="src/dodopayments/types/credit_entitlements/balance_create_ledger_entry_params.py">params</a>) -> <a href="./src/dodopayments/types/credit_entitlements/balance_create_ledger_entry_response.py">BalanceCreateLedgerEntryResponse</a></code>
- <code title="get /credit-entitlements/{credit_entitlement_id}/balances/{customer_id}/grants">client.credit_entitlements.balances.<a href="./src/dodopayments/resources/credit_entitlements/balances.py">list_grants</a>(customer_id, \*, credit_entitlement_id, \*\*<a href="src/dodopayments/types/credit_entitlements/balance_list_grants_params.py">params</a>) -> <a href="./src/dodopayments/types/credit_entitlements/balance_list_grants_response.py">SyncDefaultPageNumberPagination[BalanceListGrantsResponse]</a></code>
- <code title="get /credit-entitlements/{credit_entitlement_id}/balances/{customer_id}/ledger">client.credit_entitlements.balances.<a href="./src/dodopayments/resources/credit_entitlements/balances.py">list_ledger</a>(customer_id, \*, credit_entitlement_id, \*\*<a href="src/dodopayments/types/credit_entitlements/balance_list_ledger_params.py">params</a>) -> <a href="./src/dodopayments/types/credit_entitlements/credit_ledger_entry.py">SyncDefaultPageNumberPagination[CreditLedgerEntry]</a></code>
