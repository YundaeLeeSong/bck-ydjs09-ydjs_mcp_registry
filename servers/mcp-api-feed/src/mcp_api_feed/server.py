"""Main entry point for the FastMCP Feed Service.

This module imports the FastAPI application from `app_api_feed` and wraps it
in `FastApiMCP` to serve over STDIO for AI agents.
"""

from fastapi_mcp import FastApiMCP
from app_api_feed.server import app

# Wrap the FastAPI app with the MCP adapter
mcp = FastApiMCP(app)

def main():
    """Starts the FastMCP server in STDIO mode."""
    # Note: FastMCP usually handles stdio when run without arguments,
    # but print statements before running mcp could corrupt stdio.
    # So we simply run the MCP server.
    mcp.run()

if __name__ == "__main__":
    main()
