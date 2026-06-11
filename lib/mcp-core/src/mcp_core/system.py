"""System utilities."""

def fetch_system_status() -> list[dict]:
    """Returns the current operational status of the server."""
    return [{"type": "text", "text": "All systems operational over HTTP/SSE."}]
