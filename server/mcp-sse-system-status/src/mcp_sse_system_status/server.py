import uvicorn
from fastapi import FastAPI, Request
from starlette.responses import Response
from mcp.server import Server
from mcp.server.sse import SseServerTransport

# 1. Initialize the core MCP Server
mcp_server = Server("sample-http-mcp-server")

# 2. Initialize the SSE transport
# The endpoint is where clients will POST their messages after connecting to SSE
app_transport = SseServerTransport("/messages")

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
    async with app_transport.connect_sse(
        request.scope, request.receive, request._send
    ) as streams:
        await mcp_server.run(
            streams[0], streams[1], mcp_server.create_initialization_options()
        )
    return Response()

# Mount the handle_post_message ASGI app to /messages
app.mount("/messages", app_transport.handle_post_message)

def main():
    """Run the FastAPI application via uvicorn."""
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()
