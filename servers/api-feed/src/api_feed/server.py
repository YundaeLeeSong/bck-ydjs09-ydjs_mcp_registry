"""Main entry point for the FastAPI-MCP Feed Service.

This module orchestrates the startup of the application. It acts as a switchboard
between two primary execution modes:
1. HTTP API Mode: Starts a FastAPI server with Uvicorn.
2. MCP Server Mode: Starts a FastMCP server using the STDIO transport.
"""

import sys
import uvicorn
from fastapi import FastAPI
from fastapi_mcp import FastApiMCP
from api_feed.routers import router as feed_router

# Create the standard FastAPI application
app = FastAPI(
    title="Feed Service API",
    description="Unified HTTP API and MCP Service for Feed operations.",
    version="1.0.0"
)

# Include the domain-specific router
app.include_router(feed_router)

# Wrap the FastAPI app with the MCP adapter
mcp = FastApiMCP(app)

def main():
    """Starts the application service based on command line arguments.

    Default behavior starts the HTTP API. If 'mcp' is passed as the first
    argument, it starts the FastMCP server in STDIO mode.
    """
    if len(sys.argv) > 1 and sys.argv[1].lower() == "mcp":
        print("Starting the explicit FastMCP Server via STDIO...")
        mcp.run()
    else:
        print("Starting the Unified HTTP API Service...")
        print("Run `uv run python -m api_feed.server mcp` to start the raw FastMCP STDIO server instead.")
        print("API documentation is available at: http://localhost:8000/docs")
        
        # Uvicorn entry point points to the 'app' instance
        uvicorn.run("api_feed.server:app", host="localhost", port=8000, reload=True)

if __name__ == "__main__":
    main()
