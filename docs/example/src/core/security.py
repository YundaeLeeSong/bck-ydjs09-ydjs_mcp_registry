"""
Security filter systems parsing incoming validation headers.
"""
import hmac
import hashlib
import os

def verify_agent_signature(payload: bytes, signature: str) -> bool:
    # Retrieve configuration key from localized environment boundary
    secret = os.getenv("MCP_ALLOWED_CLIENT", "").encode("utf-8")
    if not secret:
        return False
    
    # Compute mathematical checksum cleanly
    expected = hmac.new(secret, payload, hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected, signature)