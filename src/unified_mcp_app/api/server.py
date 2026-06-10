"""API Server Configuration and Initialization.

This module initializes the FastAPI application, mounts the routers, and
wraps the application with FastApiMCP to bridge the gap between REST and MCP.

Design Patterns:
    Modular Monolith - Encapsulates API configuration.
    Facade/Adapter - FastApiMCP adapts REST endpoints to the MCP protocol.
"""

from fastapi import FastAPI
from fastapi_mcp import FastApiMCP
from unified_mcp_app.api.routers import api_router

# Initialize the core FastAPI application
app = FastAPI(
    title="Unified API",
    description="This is the explicit API implementation using FastAPI."
)

# Register the aggregated feature routers
app.include_router(api_router)

# Mount the FastApiMCP adapter
# This automatically exposes all standard FastAPI endpoints as MCP-compliant tools
mcp_api = FastApiMCP(app, name="Unified App HTTP MCP")
mcp_api.mount_http()
