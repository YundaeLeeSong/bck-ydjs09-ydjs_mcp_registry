"""Standalone FastMCP server for calculator functions."""

from fastmcp import FastMCP
from mcp_core.calculator import multiply, add_numbers, subtract, divide

# Initialize the FastMCP server
mcp = FastMCP("CalculatorService")

# Register core logic functions as tools directly
mcp.tool()(multiply)
mcp.tool()(add_numbers)
mcp.tool()(subtract)
mcp.tool()(divide)

if __name__ == "__main__":
    mcp.run()
