# Checkout

## SupportedCountries

Types:

```python
from dodo_payments.types.checkout import CountryCodeAlpha2, SupportedCountryListResponse
```

Methods:

- <code title="get /checkout/supported_countries">client.checkout.supported_countries.<a href="./src/dodo_payments/resources/checkout/supported_countries.py">list</a>() -> <a href="./src/dodo_payments/types/checkout/supported_country_list_response.py">SupportedCountryListResponse</a></code>

# Customers

Types:

```python
from dodo_payments.types import Customer, CustomerListResponse
```

Methods:

- <code title="get /customers/{customer_id}">client.customers.<a href="./src/dodo_payments/resources/customers.py">retrieve</a>(customer_id) -> <a href="./src/dodo_payments/types/customer.py">Customer</a></code>
- <code title="get /customers">client.customers.<a href="./src/dodo_payments/resources/customers.py">list</a>(\*\*<a href="src/dodo_payments/types/customer_list_params.py">params</a>) -> <a href="./src/dodo_payments/types/customer_list_response.py">CustomerListResponse</a></code>

# Disputes

Types:

```python
from dodo_payments.types import Dispute, DisputeListResponse
```

Methods:

- <code title="get /disputes/{dispute_id}">client.disputes.<a href="./src/dodo_payments/resources/disputes.py">retrieve</a>(dispute_id) -> <a href="./src/dodo_payments/types/dispute.py">Dispute</a></code>
- <code title="get /disputes">client.disputes.<a href="./src/dodo_payments/resources/disputes.py">list</a>(\*\*<a href="src/dodo_payments/types/dispute_list_params.py">params</a>) -> <a href="./src/dodo_payments/types/dispute_list_response.py">DisputeListResponse</a></code>

# Payments

Types:

```python
from dodo_payments.types import Payment, PaymentCreateResponse, PaymentListResponse
```

Methods:

- <code title="post /payments">client.payments.<a href="./src/dodo_payments/resources/payments.py">create</a>(\*\*<a href="src/dodo_payments/types/payment_create_params.py">params</a>) -> <a href="./src/dodo_payments/types/payment_create_response.py">PaymentCreateResponse</a></code>
- <code title="get /payments/{payment_id}">client.payments.<a href="./src/dodo_payments/resources/payments.py">retrieve</a>(payment_id) -> <a href="./src/dodo_payments/types/payment.py">Payment</a></code>
- <code title="get /payments">client.payments.<a href="./src/dodo_payments/resources/payments.py">list</a>(\*\*<a href="src/dodo_payments/types/payment_list_params.py">params</a>) -> <a href="./src/dodo_payments/types/payment_list_response.py">PaymentListResponse</a></code>

# Payouts

Types:

```python
from dodo_payments.types import PayoutListResponse
```

Methods:

- <code title="get /payouts">client.payouts.<a href="./src/dodo_payments/resources/payouts.py">list</a>(\*\*<a href="src/dodo_payments/types/payout_list_params.py">params</a>) -> <a href="./src/dodo_payments/types/payout_list_response.py">PayoutListResponse</a></code>

# Products

Types:

```python
from dodo_payments.types import Product, ProductCreateResponse, ProductListResponse
```

Methods:

- <code title="post /products">client.products.<a href="./src/dodo_payments/resources/products/products.py">create</a>(\*\*<a href="src/dodo_payments/types/product_create_params.py">params</a>) -> <a href="./src/dodo_payments/types/product_create_response.py">ProductCreateResponse</a></code>
- <code title="get /products/{id}">client.products.<a href="./src/dodo_payments/resources/products/products.py">retrieve</a>(id) -> <a href="./src/dodo_payments/types/product.py">Product</a></code>
- <code title="patch /products/{id}">client.products.<a href="./src/dodo_payments/resources/products/products.py">update</a>(id, \*\*<a href="src/dodo_payments/types/product_update_params.py">params</a>) -> None</code>
- <code title="get /products">client.products.<a href="./src/dodo_payments/resources/products/products.py">list</a>(\*\*<a href="src/dodo_payments/types/product_list_params.py">params</a>) -> <a href="./src/dodo_payments/types/product_list_response.py">ProductListResponse</a></code>

## Images

Types:

```python
from dodo_payments.types.products import ImageUpdateResponse
```

Methods:

- <code title="put /products/{id}/images">client.products.images.<a href="./src/dodo_payments/resources/products/images.py">update</a>(id) -> <a href="./src/dodo_payments/types/products/image_update_response.py">ImageUpdateResponse</a></code>

# Refunds

Types:

```python
from dodo_payments.types import Refund, RefundListResponse
```

Methods:

- <code title="post /refunds">client.refunds.<a href="./src/dodo_payments/resources/refunds.py">create</a>(\*\*<a href="src/dodo_payments/types/refund_create_params.py">params</a>) -> <a href="./src/dodo_payments/types/refund.py">Refund</a></code>
- <code title="get /refunds/{refund_id}">client.refunds.<a href="./src/dodo_payments/resources/refunds.py">retrieve</a>(refund_id) -> <a href="./src/dodo_payments/types/refund.py">Refund</a></code>
- <code title="get /refunds">client.refunds.<a href="./src/dodo_payments/resources/refunds.py">list</a>(\*\*<a href="src/dodo_payments/types/refund_list_params.py">params</a>) -> <a href="./src/dodo_payments/types/refund_list_response.py">RefundListResponse</a></code>

# Subscriptions

Types:

```python
from dodo_payments.types import Subscription, SubscriptionCreateResponse, SubscriptionListResponse
```

Methods:

- <code title="post /subscriptions">client.subscriptions.<a href="./src/dodo_payments/resources/subscriptions.py">create</a>(\*\*<a href="src/dodo_payments/types/subscription_create_params.py">params</a>) -> <a href="./src/dodo_payments/types/subscription_create_response.py">SubscriptionCreateResponse</a></code>
- <code title="get /subscriptions/{subscription_id}">client.subscriptions.<a href="./src/dodo_payments/resources/subscriptions.py">retrieve</a>(subscription_id) -> <a href="./src/dodo_payments/types/subscription.py">Subscription</a></code>
- <code title="patch /subscriptions/{subscription_id}">client.subscriptions.<a href="./src/dodo_payments/resources/subscriptions.py">update</a>(subscription_id, \*\*<a href="src/dodo_payments/types/subscription_update_params.py">params</a>) -> <a href="./src/dodo_payments/types/subscription.py">Subscription</a></code>
- <code title="get /subscriptions">client.subscriptions.<a href="./src/dodo_payments/resources/subscriptions.py">list</a>(\*\*<a href="src/dodo_payments/types/subscription_list_params.py">params</a>) -> <a href="./src/dodo_payments/types/subscription_list_response.py">SubscriptionListResponse</a></code>

# WebhookEvents

Types:

```python
from dodo_payments.types import WebhookEventLog, WebhookEventListResponse
```

Methods:

- <code title="get /webhook_events/{webhook_event_id}">client.webhook_events.<a href="./src/dodo_payments/resources/webhook_events.py">retrieve</a>(webhook_event_id) -> <a href="./src/dodo_payments/types/webhook_event_log.py">WebhookEventLog</a></code>
- <code title="get /webhook_events">client.webhook_events.<a href="./src/dodo_payments/resources/webhook_events.py">list</a>(\*\*<a href="src/dodo_payments/types/webhook_event_list_params.py">params</a>) -> <a href="./src/dodo_payments/types/webhook_event_list_response.py">WebhookEventListResponse</a></code>

# OutgoingWebhooks

Methods:

- <code title="post /your-webhook-url">client.outgoing_webhooks.<a href="./src/dodo_payments/resources/outgoing_webhooks.py">create</a>(\*\*<a href="src/dodo_payments/types/outgoing_webhook_create_params.py">params</a>) -> None</code>
