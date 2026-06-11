import sys
from rich.console import Console
from rich.prompt import Prompt

console = Console()

def main():
    console.print("[bold cyan]Welcome to the YDJS MCP Registry![/bold cyan]\n")
    console.print("Please select a service to run:")
    console.print("  [bold]1.[/bold] FastAPI Web Server (app-api-feed)")
    console.print("  [bold]2.[/bold] FastAPI MCP Bridge (mcp-api-feed) - STDIO")
    console.print("  [bold]3.[/bold] FastMCP Calculator (mcp-stdio-calculator) - STDIO")
    console.print("  [bold]4.[/bold] Custom HTTP/SSE System Status (mcp-sse-system-status)")
    
    choice = Prompt.ask("\nEnter the number of the service you want to start", choices=["1", "2", "3", "4"], default="1")
    
    if choice == "1":
        console.print("[green]Starting FastAPI Web Server...[/green]")
        from app_api_feed.server import main as run_app
        run_app()
    elif choice == "2":
        console.print("[green]Starting FastAPI MCP Bridge (STDIO)...[/green]")
        from mcp_api_feed.server import main as run_mcp_api
        run_mcp_api()
    elif choice == "3":
        console.print("[green]Starting FastMCP Calculator (STDIO)...[/green]")
        from mcp_stdio_calculator.server import mcp
        mcp.run()
    elif choice == "4":
        console.print("[green]Starting HTTP/SSE System Status...[/green]")
        from mcp_sse_system_status.server import main as run_sse
        run_sse()

if __name__ == "__main__":
    main()