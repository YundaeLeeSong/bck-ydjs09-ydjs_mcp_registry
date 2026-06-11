import uvicorn
from fastapi import FastAPI, Request
from mcp.server import Server
from mcp.server.fastapi import FastMcpServer

# 1. Initialize the core MCP Server
mcp_server = Server("sample-http-mcp-server")

# 2. Bind it to the FastMcpServer transport adapter
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


def main():
    """Run the FastAPI application via uvicorn."""
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()
