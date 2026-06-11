# mcp-sse-system-status

A custom MCP server demonstrating HTTP/SSE transport instead of STDIO.

## Usage
```bash
uv run --directory server/mcp-sse-system-status python -m mcp_sse_system_status
```

Then point your MCP client to `http://localhost:8000/sse`.
