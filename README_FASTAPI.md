# Dodo Payments FastAPI Integration

This package provides a FastAPI integration for verifying Dodo Payments webhook signatures.

## Installation

To use the FastAPI integration, you need to install the `fastapi` extra:

```bash
pip install "dodopayments[fastapi]"
```

## Usage

### 1. Import the Webhook Guard

```python
from dodopayments.integrations.fastapi.webhook_guard import DodoWebhookGuard
```

### 2. Create a Webhook Guard Instance

```python
# Using your webhook secret
webhook_guard = DodoWebhookGuard(secret="whsec_your_webhook_secret")
```

### 3. Protect Your Webhook Endpoints

```python
from fastapi import FastAPI, Depends

app = FastAPI()

@app.post("/webhook")
async def handle_webhook(payload: dict, verified: bool = Depends(webhook_guard)):
    # If we reach this point, the webhook signature has been verified
    # Process your webhook here
    return {"status": "success"}
```

### 4. How It Works

The `DodoWebhookGuard` verifies the signature in the `Dodo-Signature` header against the request body using HMAC-SHA256. 

- If the signature is missing, it raises an HTTP 400 error with "Missing signature header"
- If the signature is invalid, it raises an HTTP 400 error with "Invalid webhook signature"
- If the signature is valid, it returns `True` and allows the request to proceed

## Example

```python
from fastapi import FastAPI, Depends
from dodopayments.integrations.fastapi.webhook_guard import DodoWebhookGuard

app = FastAPI()
webhook_guard = DodoWebhookGuard(secret="whsec_your_webhook_secret")

@app.post("/webhook/payment")
async def handle_payment_webhook(payload: dict, verified: bool = Depends(webhook_guard)):
    # Process payment webhook
    print(f"Received payment event: {payload}")
    return {"status": "processed"}
```

## Testing

To test your webhook endpoints, you'll need to generate a valid signature:

```python
import hmac
import hashlib
import json

def generate_signature(secret: str, payload: dict) -> str:
    body = json.dumps(payload).encode()
    return hmac.new(secret.encode(), body, hashlib.sha256).hexdigest()

# Usage
payload = {"event": "payment.succeeded", "data": {"amount": 100}}
signature = generate_signature("whsec_your_webhook_secret", payload)

# Send request with header
# headers = {"Dodo-Signature": signature}
```

## Security Notes

- Keep your webhook secret secure and never expose it in client-side code
- Use environment variables to store your webhook secret in production
- The webhook guard protects against unauthorized webhook requests