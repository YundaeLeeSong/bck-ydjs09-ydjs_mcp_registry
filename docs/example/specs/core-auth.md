# Spec: Core Authentication Boundary

## Requirements
Implement an internal cryptographic header validation system within the web routing layout to ensure incoming client tasks originate from the trusted local controller.

## Steps
1. Capture the incoming `X-Agent-Signature` verification string from headers.
2. Formulate a SHA256 HMAC digest based on system parameters configured via `MCP_ALLOWED_CLIENT`.
3. Halt execution with an HTTP 403 response if the signature fails confirmation matches.

## Expected Targets
* Logic implementation: `src/core/security.py`
* Routing deployment: `src/mcp_server/app.py`