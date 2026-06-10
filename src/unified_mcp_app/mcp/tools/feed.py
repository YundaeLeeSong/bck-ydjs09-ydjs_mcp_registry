"""FastMCP Feed Tool Registrations.

This module exposes RSS feed searching capabilities as MCP tools.
"""

from unified_mcp_app.mcp.server import mcp
from unified_mcp_app.core import fcc_news_search, fcc_youtube_search, fcc_secret_message

@mcp.tool(name="fcc_news_search", description="Search FreeCodeCamp news feed via RSS by title/description")
def mcp_fcc_news_search(query: str, max_results: int = 3) -> list:
    """MCP Tool wrapper for core news search logic."""
    return fcc_news_search(query, max_results)

@mcp.tool(name="fcc_youtube_search", description="Search FreeCodeCamp Youtube channel via RSS by title")
def mcp_fcc_youtube_search(query: str, max_results: int = 3) -> list:
    """MCP Tool wrapper for core YouTube search logic."""
    return fcc_youtube_search(query, max_results)

@mcp.tool(name="fcc_secret_message", description="Returns a secret message of FreeCodeCamp")
def mcp_fcc_secret_message() -> str:
    """MCP Tool wrapper for core secret message logic."""
    return fcc_secret_message()
