import pytest
from fastapi.testclient import TestClient
from fastapi import FastAPI, Depends
import hmac, hashlib, json
from dodopayments.integrations.fastapi.webhook_guard import DodoWebhookGuard

app = FastAPI()
guard = DodoWebhookGuard(secret="secret")

@app.post("/webhook")
async def webhook(payload: dict, guard_ok: bool = Depends(guard)):
    return {"status": "ok"}

client = TestClient(app)

def test_valid_signature():
    # Create the exact payload that will be sent
    payload_str = '{"event": "payment_succeeded"}'
    body = payload_str.encode()
    signature = hmac.new(b"secret", body, hashlib.sha256).hexdigest()
    
    # Send raw data with proper content type
    response = client.post(
        "/webhook", 
        content=payload_str,
        headers={
            "Dodo-Signature": signature,
            "Content-Type": "application/json"
        }
    )
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_invalid_signature():
    payload_str = '{"event": "payment_succeeded"}'
    response = client.post(
        "/webhook", 
        content=payload_str,
        headers={
            "Dodo-Signature": "wrong",
            "Content-Type": "application/json"
        }
    )
    assert response.status_code == 400

def test_missing_signature():
    payload_str = '{"event": "payment_succeeded"}'
    response = client.post(
        "/webhook", 
        content=payload_str,
        headers={"Content-Type": "application/json"}
    )
    assert response.status_code == 400