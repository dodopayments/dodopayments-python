from fastapi import Request, HTTPException
import hmac
import hashlib

class DodoWebhookGuard:
    """
    FastAPI dependency to verify Dodo Payments webhook signatures.
    """
    def __init__(self, secret: str):
        self.secret = secret.encode()

    async def __call__(self, request: Request):
        signature = request.headers.get("Dodo-Signature")
        if not signature:
            raise HTTPException(status_code=400, detail="Missing signature header")

        body = await request.body()
        expected_signature = hmac.new(self.secret, body, hashlib.sha256).hexdigest()

        if not hmac.compare_digest(signature, expected_signature):
            raise HTTPException(status_code=400, detail="Invalid webhook signature")

        return True