# Payments

Types:

```python
from dodopayments.types import Payment, PaymentCreateResponse, PaymentListResponse
```

Methods:

- <code title="post /payments">client.payments.<a href="./src/dodopayments/resources/payments.py">create</a>(\*\*<a href="src/dodopayments/types/payment_create_params.py">params</a>) -> <a href="./src/dodopayments/types/payment_create_response.py">PaymentCreateResponse</a></code>
- <code title="get /payments/{payment_id}">client.payments.<a href="./src/dodopayments/resources/payments.py">retrieve</a>(payment_id) -> <a href="./src/dodopayments/types/payment.py">Payment</a></code>
- <code title="get /payments">client.payments.<a href="./src/dodopayments/resources/payments.py">list</a>(\*\*<a href="src/dodopayments/types/payment_list_params.py">params</a>) -> <a href="./src/dodopayments/types/payment_list_response.py">SyncDefaultPageNumberPagination[PaymentListResponse]</a></code>

# Subscriptions

Types:

```python
from dodopayments.types import Subscription, SubscriptionCreateResponse
```

Methods:

- <code title="post /subscriptions">client.subscriptions.<a href="./src/dodopayments/resources/subscriptions.py">create</a>(\*\*<a href="src/dodopayments/types/subscription_create_params.py">params</a>) -> <a href="./src/dodopayments/types/subscription_create_response.py">SubscriptionCreateResponse</a></code>
- <code title="get /subscriptions/{subscription_id}">client.subscriptions.<a href="./src/dodopayments/resources/subscriptions.py">retrieve</a>(subscription_id) -> <a href="./src/dodopayments/types/subscription.py">Subscription</a></code>
- <code title="patch /subscriptions/{subscription_id}">client.subscriptions.<a href="./src/dodopayments/resources/subscriptions.py">update</a>(subscription_id, \*\*<a href="src/dodopayments/types/subscription_update_params.py">params</a>) -> <a href="./src/dodopayments/types/subscription.py">Subscription</a></code>
- <code title="get /subscriptions">client.subscriptions.<a href="./src/dodopayments/resources/subscriptions.py">list</a>(\*\*<a href="src/dodopayments/types/subscription_list_params.py">params</a>) -> <a href="./src/dodopayments/types/subscription.py">SyncDefaultPageNumberPagination[Subscription]</a></code>

# Customers

Types:

```python
from dodopayments.types import Customer
```

Methods:

- <code title="post /customers">client.customers.<a href="./src/dodopayments/resources/customers.py">create</a>(\*\*<a href="src/dodopayments/types/customer_create_params.py">params</a>) -> <a href="./src/dodopayments/types/customer.py">Customer</a></code>
- <code title="get /customers/{customer_id}">client.customers.<a href="./src/dodopayments/resources/customers.py">retrieve</a>(customer_id) -> <a href="./src/dodopayments/types/customer.py">Customer</a></code>
- <code title="patch /customers/{customer_id}">client.customers.<a href="./src/dodopayments/resources/customers.py">update</a>(customer_id, \*\*<a href="src/dodopayments/types/customer_update_params.py">params</a>) -> <a href="./src/dodopayments/types/customer.py">Customer</a></code>
- <code title="get /customers">client.customers.<a href="./src/dodopayments/resources/customers.py">list</a>(\*\*<a href="src/dodopayments/types/customer_list_params.py">params</a>) -> <a href="./src/dodopayments/types/customer.py">SyncDefaultPageNumberPagination[Customer]</a></code>

# Refunds

Types:

```python
from dodopayments.types import Refund
```

Methods:

- <code title="post /refunds">client.refunds.<a href="./src/dodopayments/resources/refunds.py">create</a>(\*\*<a href="src/dodopayments/types/refund_create_params.py">params</a>) -> <a href="./src/dodopayments/types/refund.py">Refund</a></code>
- <code title="get /refunds/{refund_id}">client.refunds.<a href="./src/dodopayments/resources/refunds.py">retrieve</a>(refund_id) -> <a href="./src/dodopayments/types/refund.py">Refund</a></code>
- <code title="get /refunds">client.refunds.<a href="./src/dodopayments/resources/refunds.py">list</a>(\*\*<a href="src/dodopayments/types/refund_list_params.py">params</a>) -> <a href="./src/dodopayments/types/refund.py">SyncDefaultPageNumberPagination[Refund]</a></code>

# Disputes

Types:

```python
from dodopayments.types import Dispute
```

Methods:

- <code title="get /disputes/{dispute_id}">client.disputes.<a href="./src/dodopayments/resources/disputes.py">retrieve</a>(dispute_id) -> <a href="./src/dodopayments/types/dispute.py">Dispute</a></code>
- <code title="get /disputes">client.disputes.<a href="./src/dodopayments/resources/disputes.py">list</a>(\*\*<a href="src/dodopayments/types/dispute_list_params.py">params</a>) -> <a href="./src/dodopayments/types/dispute.py">SyncDefaultPageNumberPagination[Dispute]</a></code>

# Payouts

Types:

```python
from dodopayments.types import PayoutListResponse
```

Methods:

- <code title="get /payouts">client.payouts.<a href="./src/dodopayments/resources/payouts.py">list</a>(\*\*<a href="src/dodopayments/types/payout_list_params.py">params</a>) -> <a href="./src/dodopayments/types/payout_list_response.py">SyncDefaultPageNumberPagination[PayoutListResponse]</a></code>

# WebhookEvents

Types:

```python
from dodopayments.types import WebhookEvent
```

Methods:

- <code title="get /webhook_events/{webhook_event_id}">client.webhook_events.<a href="./src/dodopayments/resources/webhook_events.py">retrieve</a>(webhook_event_id) -> <a href="./src/dodopayments/types/webhook_event.py">WebhookEvent</a></code>
- <code title="get /webhook_events">client.webhook_events.<a href="./src/dodopayments/resources/webhook_events.py">list</a>(\*\*<a href="src/dodopayments/types/webhook_event_list_params.py">params</a>) -> <a href="./src/dodopayments/types/webhook_event.py">SyncDefaultPageNumberPagination[WebhookEvent]</a></code>

# Products

Types:

```python
from dodopayments.types import Product, ProductCreateResponse, ProductListResponse
```

Methods:

- <code title="post /products">client.products.<a href="./src/dodopayments/resources/products/products.py">create</a>(\*\*<a href="src/dodopayments/types/product_create_params.py">params</a>) -> <a href="./src/dodopayments/types/product_create_response.py">ProductCreateResponse</a></code>
- <code title="get /products/{id}">client.products.<a href="./src/dodopayments/resources/products/products.py">retrieve</a>(id) -> <a href="./src/dodopayments/types/product.py">Product</a></code>
- <code title="patch /products/{id}">client.products.<a href="./src/dodopayments/resources/products/products.py">update</a>(id, \*\*<a href="src/dodopayments/types/product_update_params.py">params</a>) -> None</code>
- <code title="get /products">client.products.<a href="./src/dodopayments/resources/products/products.py">list</a>(\*\*<a href="src/dodopayments/types/product_list_params.py">params</a>) -> <a href="./src/dodopayments/types/product_list_response.py">SyncDefaultPageNumberPagination[ProductListResponse]</a></code>

## Images

Types:

```python
from dodopayments.types.products import ImageUpdateResponse
```

Methods:

- <code title="put /products/{id}/images">client.products.images.<a href="./src/dodopayments/resources/products/images.py">update</a>(id) -> <a href="./src/dodopayments/types/products/image_update_response.py">ImageUpdateResponse</a></code>

# Misc

## SupportedCountries

Types:

```python
from dodopayments.types.misc import CountryCode, SupportedCountryListResponse
```

Methods:

- <code title="get /checkout/supported_countries">client.misc.supported_countries.<a href="./src/dodopayments/resources/misc/supported_countries.py">list</a>() -> <a href="./src/dodopayments/types/misc/supported_country_list_response.py">SupportedCountryListResponse</a></code>
