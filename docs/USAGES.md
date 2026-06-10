# Usage Guide

This guide explains how to interact with the **Unified MCP & API Service**.

## 1. Direct HTTP API (REST)
The HTTP API is best for direct interaction via web browsers, scripts, or traditional applications.

### Start the Service
```bash
uv run python main.py
```

### Interactive Documentation
Once the server is running, open your browser and navigate to:
**`http://localhost:8000/docs`**

You will see an interactive Swagger UI. You can expand any endpoint (e.g., `/calculator/multiply`) and click **"Try it out"** to send real requests to the server.

### Example curl Request
```bash
curl -X POST "http://localhost:8000/calculator/multiply?a=10&b=5"
```

---

## 2. MCP Server (For AI Agents)
The MCP (Model Context Protocol) interface allows AI models like Claude to discover and use your tools automatically.

### Start the MCP Server (STDIO)
To run the server in a mode compatible with most AI clients:
```bash
uv run python main.py mcp
```
*Note: This starts a dashboard for monitoring. The actual communication happens over standard input/output.*

### Connect to Claude Desktop
To let Claude Desktop use your tools, add the following to your configuration file:

**File Path:** `%APPDATA%\Claude\claude_desktop_config.json`

**Configuration:**
```json
{
  "mcpServers": {
    "unified-mcp-app": {
      "command": "uv",
      "args": [
        "--directory",
        "C:/Users/manua/source/repo/_references/_empty",
        "run",
        "python",
        "main.py",
        "mcp"
      ]
    }
  }
}
```

### Example AI Prompt
Once connected, you can ask Claude:
- *"Multiply 1234 by 5678."*
- *"What is the latest news from FreeCodeCamp?"*
- *"Search the FreeCodeCamp YouTube channel for 'Python tutorial'."*

The AI will automatically choose the correct tool, execute your Python code, and report the results back to you.
