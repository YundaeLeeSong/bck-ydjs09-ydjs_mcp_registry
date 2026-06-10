"""Main entry point for the Unified MCP & API Service.

This module orchestrates the startup of the application. It acts as a switchboard
between two primary execution modes:
1. HTTP API Mode: Starts a FastAPI server with Uvicorn.
2. MCP Server Mode: Starts a FastMCP server using the STDIO transport.

Design Pattern:
    Orchestrator - Centralizes startup logic and configuration routing.
"""

import sys
import uvicorn

def start():
    """Starts the application service based on command line arguments.

    Default behavior starts the HTTP API. If 'mcp' is passed as the first
    argument, it starts the FastMCP server in STDIO mode.
    """
    # Check for the 'mcp' flag to toggle between API and raw MCP modes
    if len(sys.argv) > 1 and sys.argv[1].lower() == "mcp":
        print("Starting the explicit FastMCP Server via STDIO...")
        
        # Delayed import to avoid initializing unused services
        from unified_mcp_app.mcp import mcp
        
        # mcp.run() defaults to STDIO transport, required by AI clients like Claude
        mcp.run()
    else:
        print("Starting the Unified HTTP API Service...")
        print("Run `uv run python main.py mcp` to start the raw FastMCP STDIO server instead.")
        print("API documentation is available at: http://localhost:8000/docs")
        
        # Uvicorn entry point points to the 'app' instance in the api.server module
        uvicorn.run("unified_mcp_app.api.server:app", host="localhost", port=8000, reload=True)

if __name__ == "__main__":
    start()
