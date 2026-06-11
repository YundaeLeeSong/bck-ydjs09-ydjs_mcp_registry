# Usage Guide

This guide explains how to interact with the servers in the **Unified MCP Workspace**.

## 1. Direct HTTP API (REST)
The HTTP API is provided by the `app-api-feed` app and is best for direct interaction via web browsers, scripts, or traditional applications.

### Start the Service
```bash
uv run --directory apps/app-api-feed python -m app_api_feed
```

### Interactive Documentation
Once the server is running, open your browser and navigate to:
**`http://localhost:8000/docs`**

You will see an interactive Swagger UI. You can expand any endpoint and click **"Try it out"** to send real requests to the server.

### Example curl Request
```bash
curl -X GET "http://localhost:8000/feed/fcc_news_search?query=python"
```

---

## 2. MCP Servers (For AI Agents)
The MCP (Model Context Protocol) interface allows AI models like Claude to discover and use your tools automatically. The workspace currently exposes two MCP servers.

### Start the MCP Servers (STDIO)
To run the servers in a mode compatible with most AI clients:

**Calculator FastMCP Server:**
```bash
uv run --directory servers/mcp-calculator python -m mcp_calculator
```

**Feed FastAPI-MCP Server:**
```bash
uv run --directory servers/mcp-api-feed python -m mcp_api_feed
```

### Verification (Manual Test)
When you run an MCP server manually, it will appear to "stuck" or show no output. This is **expected behavior** as it is waiting for JSON-RPC instructions via `stdin`.

To verify it is working, you must perform the **MCP Handshake** by pasting these lines one by one into your terminal and pressing **Enter** after each:

1. **Initialize Request**:
```json
{"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"capabilities": {}, "clientInfo": {"name": "test", "version": "1.0"}, "protocolVersion": "2024-11-05"}}
```

2. **Initialized Notification**:
```json
{"jsonrpc": "2.0", "method": "notifications/initialized"}
```

3. **List Tools**:
```json
{"jsonrpc": "2.0", "id": 2, "method": "tools/list"}
```

If the server is functioning correctly, the third command will return a JSON object listing all available tools.

### Connect to Claude Desktop
To let Claude Desktop use your tools, add the following to your configuration file:

**File Path:** `%APPDATA%\Claude\claude_desktop_config.json`

**Configuration:**
```
{
  "mcpServers": {
    "mcp-calculator": {
      "command": "uv",
      "args": [
        "--directory",
        "C:/Users/manua/source/repo/_references/_python02-personal_mcp_registry/servers/mcp-calculator",
        "run",
        "python",
        "-m",
        "mcp_calculator"
      ]
    },
    "mcp-api-feed": {
      "command": "uv",
      "args": [
        "--directory",
        "C:/Users/manua/source/repo/_references/_python02-personal_mcp_registry/servers/mcp-api-feed",
        "run",
        "python",
        "-m",
        "mcp_api_feed"
      ]
    }
  }
}
```

## 3. Workspace Maintenance
To keep the project dependencies clean and up-to-date with your source code, use the following commands.

### Automatically Sync Dependencies
If you add new imports to your Python files, run this command to automatically update all `pyproject.toml` files in the workspace:
```bash
uv run poe sync-deps
```

### Manual Workspace Sync
To ensure your local virtual environment matches the lockfile:
```bash
uv sync
```
