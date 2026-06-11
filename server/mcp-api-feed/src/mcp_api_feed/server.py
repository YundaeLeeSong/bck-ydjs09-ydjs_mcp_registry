"""Main entry point for the FastMCP Feed Service.

This module imports the FastAPI application from `app_api_feed` and wraps it
in `FastApiMCP` to serve over STDIO for AI agents.
"""

import asyncio
from mcp.server.stdio import stdio_server
from fastapi_mcp import FastApiMCP
from app_api_feed.server import app

# Wrap the FastAPI app with the MCP adapter
mcp = FastApiMCP(app)

def run_stdio():
    """Helper to run the underlying MCP server via STDIO."""
    async def _run():
        async with stdio_server() as (read, write):
            await mcp.server.run(read, write, mcp.server.create_initialization_options())
    asyncio.run(_run())

# Restore the .run() method to the instance to match original expected behavior
mcp.run = run_stdio

def main():
    """Starts the FastMCP server in STDIO mode."""
    mcp.run()

if __name__ == "__main__":
    main()
