import hmac
import hashlib
import time
from typing import Optional
from fastapi import Request, HTTPException

class DodoWebhookGuard:
    """
    FastAPI Dependency that verifies Dodo Payments webhook signatures.
    
    It validates the 'webhook-signature' header according to the Standard Webhooks 
    specification (HMAC-SHA256 with timestamp protection) to prevent replay attacks.
    
    Usage:
        @app.post("/webhook")
        async def handle_webhook(payload: bytes = Depends(DodoWebhookGuard("whsec_..."))):
            # payload is verified and safe to process
            process_event(payload)
    """

    def __init__(self, secret: str, tolerance: int = 300):
        """
        Args:
            secret: The webhook secret (starts with 'whsec_').
            tolerance: Time in seconds to allow for clock drift (default 5 mins).
        """
        self.secret = secret
        self.tolerance = tolerance

    async def __call__(self, request: Request) -> bytes:
        # 1. Extract the signature header
        header = request.headers.get("webhook-signature")
        if not header:
            raise HTTPException(status_code=400, detail="Missing webhook-signature header")

        # 2. Parse the header (Format: t=TIMESTAMP,v1=SIGNATURE)
        # Example: t=1698765432,v1=d6a...
        try:
            parts = {k: v for k, v in [item.split("=") for item in header.split(",")]}
            timestamp = parts.get("t")
            signature = parts.get("v1")
        except ValueError:
            raise HTTPException(status_code=400, detail="Invalid signature header format")

        if not timestamp or not signature:
            raise HTTPException(status_code=400, detail="Missing timestamp or signature")

        # 3. Prevent Replay Attacks (Check Timestamp)
        now = int(time.time())
        try:
            timestamp_int = int(timestamp)
        except ValueError:
             raise HTTPException(status_code=400, detail="Invalid timestamp")

        if now - timestamp_int > self.tolerance:
             raise HTTPException(status_code=400, detail="Webhook timestamp too old")

        # 4. Verify Signature
        # The string to sign is: "{timestamp}.{payload}"
        payload_bytes = await request.body()
        payload_str = payload_bytes.decode("utf-8")
        to_sign = f"{timestamp}.{payload_str}"

        # Calculate expected HMAC
        # Note: If the secret starts with 'whsec_', some systems expect it decoded, 
        # but usually for these SDKs it is used as a raw string key. 
        # We assume standard string key usage here.
        expected_signature = hmac.new(
            self.secret.encode("utf-8"),
            to_sign.encode("utf-8"),
            hashlib.sha256
        ).hexdigest()

        if not hmac.compare_digest(expected_signature, signature):
            raise HTTPException(status_code=400, detail="Invalid webhook signature")

        # Return the raw bytes so the user can parse it with the SDK or json
        return payload_bytes