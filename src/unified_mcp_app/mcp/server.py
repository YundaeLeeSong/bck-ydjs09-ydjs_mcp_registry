"""FastMCP Server Instance.

This module initializes the standalone FastMCP server used for
direct STDIO communication with AI clients.
"""

from fastmcp import FastMCP

# Initialize the FastMCP server instance
mcp = FastMCP(name="Unified FastMCP Server")
