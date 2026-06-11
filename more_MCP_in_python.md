To understand HTTP/SSE (Server-Sent Events) in the context of MCP, it helps to contrast it with STDIO.

With STDIO, the AI client launches your python script as a child process and talks to it via standard input/output. This means the server must run on the same machine as the client.

With HTTP/SSE, your MCP server runs as a standalone web server.

The AI client connects to it over standard HTTP to send commands (requests).

The server uses SSE (Server-Sent Events) to maintain an open, one-way streaming connection back to the client to push data.
This allows your MCP server to run in a Docker container, on a cloud instance, or anywhere on your network.

Here is how you can implement an MCP server in Python utilizing HTTP/SSE using the official mcp SDK and fastapi with uvicorn.

Prerequisites
You will need the MCP Python SDK and an asynchronous web framework package.

Bash
pip install mcp fastapi uvicorn
Python Implementation (server.py)
Python
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import Response
from mcp.server import Server
from mcp.server.fastapi import FastMcpServer

# 1. Initialize the core MCP Server
mcp_server = Server("sample-http-mcp-server")

# 2. Bind it to the FastMcpServer transport adapter
# This handles the complex SSE routing logic under the hood
app_transport = FastMcpServer(mcp_server)


# 3. Define a sample tool that the AI can use
@mcp_server.list_tools()
async def handle_list_tools():
    """List available tools for the LLM."""
    return [
        {
            "name": "fetch_system_status",
            "description": "Returns the current operational status of the server.",
            "inputSchema": {
                "type": "object",
                "properties": {},
            },
        }
    ]


@mcp_server.call_tool()
async def handle_call_tool(name: str, arguments: dict):
    """Execute the tool requested by the LLM."""
    if name == "fetch_system_status":
        return [{"type": "text", "text": "All systems operational over HTTP/SSE."}]
    raise ValueError(f"Tool not found: {name}")


# 4. Expose the required MCP endpoints via FastAPI
app = FastAPI()


@app.get("/sse")
async def sse_endpoint(request: Request):
    """The client connects here first to establish the SSE stream."""
    async with app_transport.sse_endpoint(request) as sse:
        return sse


@app.post("/messages")
async def messages_endpoint(request: Request):
    """The client sends HTTP POST commands back to this endpoint."""
    return await app_transport.handle_post_message(request)


if __name__ == "__main__":
    # Run the server locally on port 8000
    uvicorn.run(app, host="0.0.0.0", port=8000)
How the Client Connects
Instead of configuring your AI client (like Claude Desktop) with a command-line execution string, you configure it with a URL pointing to your server's SSE endpoint.

An example configuration snippet for your client settings would look like this:

JSON
{
  "mcpServers": {
    "my-remote-server": {
      "url": "http://localhost:8000/sse"
    }
  }
}
When the client starts up, it hits http://localhost:8000/sse, establishes a persistent downward stream for events, and fires off JSON-RPC payloads via POST requests to /messages.




Packages like fastapi-mcp or FastMCP (via its FastAPI integrations) are specifically designed to expose your tools over network protocols—primarily HTTP/SSE.Here is how fastapi-mcp is different and how it handles communication.How is it different?The boilerplate code provided earlier used the official mcp core SDK, requiring you to manually define tools, wrap them, and build the routing paths (/sse and /messages).fastapi-mcp acts as a high-level automation wrapper. Instead of forcing you to rewrite your logic for an AI, it hooks into an existing FastAPI application, reads your standard API routes, and automatically translates them into MCP tools using your Pydantic schemas and Swagger documentation.  Is it STDIO?No, it runs over HTTP/SSE. When you use fastapi-mcp or mount an MCP application onto FastAPI, it spins up an ASGI-compliant web server (typically via Uvicorn).The Transport: It explicitly exposes an event stream endpoint (usually under /mcp or /sse).The Benefit: Because it uses HTTP/SSE, you do not need to keep the Python script running locally on the same machine as your AI client. Your FastAPI app can be hosted remotely on a server, inside a Kubernetes cluster, or on a cloud instance, and any compatible AI client can connect to it over the network.Basic Implementation with fastapi-mcpTo achieve the exact same HTTP/SSE behavior we built manually before, fastapi-mcp reduces the code down to just a few lines:Pythonfrom fastapi import FastAPI
from fastapi_mcp import FastApiMCP
import uvicorn

app = FastAPI(title="My Production API")


# Define a standard FastAPI endpoint just like you normally would
@app.get("/items/{item_id}", operation_id="fetch_item_details")
async def read_item(item_id: int, q: str = None):
    """Fetch item details from the database.

    The LLM will read this docstring to understand what the tool does.
    """
    return {"item_id": item_id, "query": q, "status": "active"}


# Initialize the MCP wrapper and point it to your FastAPI app
mcp = FastApiMCP(
    app,
    name="Automated API MCP",
    description="Exposes production endpoints to LLM clients",
    base_url="http://localhost:8000",
)

# Automatically register routes and mount the /mcp endpoint
mcp.mount()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
Connecting the ClientBecause this setup uses HTTP/SSE via the mounted wrapper, your claude_desktop_config.json doesn't run a command. It targets the URL exposed by FastAPI:JSON{
  "mcpServers": {
    "fastapi-mcp-server": {
      "url": "http://localhost:8000/mcp/sse"
    }
  }
}
The AI client hits the endpoint, reads the generated OpenAPI schema, and immediately understands how to execute /items/{item_id} as a native tool over the network.For a step-by-step visual demonstration of setting up this workflow, you can watch How to Convert FastAPI to an MCP Server. This video walks through transforming your endpoints and verifying that local AI agents recognize them over Server-Sent Events instead of standard IO