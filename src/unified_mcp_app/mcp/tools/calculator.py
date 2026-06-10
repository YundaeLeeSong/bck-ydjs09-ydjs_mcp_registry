"""FastMCP Server Tool Registrations.

This module acts as a registration layer that wraps core domain logic
with FastMCP tool decorators.

Design Pattern:
    Proxy/Wrapper - Wraps core functions with MCP-specific metadata.
"""

from unified_mcp_app.mcp.server import mcp
from unified_mcp_app.core import multiply, add_numbers, subtract, divide

@mcp.tool(name="multiply", description="Multiply two numbers.")
def mcp_multiply(a: float, b: float) -> float:
    """MCP Tool wrapper for core multiplication logic."""
    return multiply(a, b)

@mcp.tool(name="add", description="Add two numbers.", tags={"math", "arithmetic"})
def mcp_add_numbers(x: float, y: float) -> float:
    """MCP Tool wrapper for core addition logic."""
    return add_numbers(x, y)

@mcp.tool(name="subtract", description="Subtract two numbers.")
def mcp_subtract(a: float, b: float) -> float:
    """MCP Tool wrapper for core subtraction logic."""
    return subtract(a, b)

@mcp.tool(name="divide", description="Divide two numbers.")
def mcp_divide(a: float, b: float) -> float:
    """MCP Tool wrapper for core division logic."""
    return divide(a, b)
