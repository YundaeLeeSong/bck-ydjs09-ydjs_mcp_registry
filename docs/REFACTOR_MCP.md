For a personal collection of custom Model Context Protocol (MCP) servers, an ultra-clean uv workspace setup using the hatchling backend and the src/ layout is perfect.

Since MCP servers often share logic (like custom logging, auth handlers, or payload parsing) but run as independent processes when called by Claude Desktop or Cursor, you should design the layout to support a shared internal library alongside isolated server tools.

The ideal directory structure and step-by-step setup are detailed below.

1. The Ideal Layout
Plaintext
my-mcp-registry/
├── pyproject.toml             # Root workspace manager
├── uv.lock                    # Global lockfile (guarantees fast installs)
├── README.md
│
├── libs/
│   └── mcp-core/              # Shared helper library (optional)
│       ├── pyproject.toml
│       └── src/
│           └── mcp_core/
│               └── helpers.py
│
└── servers/                   # Your individual MCP tools
    ├── mcp-weather/           # Server 1
    │   ├── pyproject.toml
    │   └── src/
    │       └── mcp_weather/
    │           └── server.py  # <-- Server entry point
    │
    └── mcp-github-utils/      # Server 2
        ├── pyproject.toml
        └── src/
            └── mcp_github_utils/
                └── server.py
2. File Configurations
Step A: Root Configuration (my-mcp-registry/pyproject.toml)
This configuration defines the layout explicitly so that uv and Workspace Mode immediately recognize the repository boundaries.

Ini, TOML
[tool.uv.workspace]
members = ["servers/*", "libs/*"]
Step B: The Shared Core Library (libs/mcp-core/pyproject.toml)
If your servers need a standardized format for logging or API configurations, place those files here.

Ini, TOML
[project]
name = "mcp-core"
version = "0.1.0"
description = "Shared core utilities for my MCP servers"
dependencies = [
    "mcp[cli]>=0.1.0", # Ensure MCP SDK is globally baseline accessible
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
Step C: An Individual MCP Server (servers/mcp-weather/pyproject.toml)
Each individual server has its own dependency list. If it requires external tools or libraries (like htmx or httpx), declare them here. It will pull the internal mcp-core directly from your workspace.

Ini, TOML
[project]
name = "mcp-weather"
version = "0.1.0"
description = "MCP Server for tracking local weather forecasts"
dependencies = [
    "mcp[cli]>=0.1.0",
    "httpx>=0.27.0",
    "mcp-core",        # <-- Depend on your shared code
]

[tool.uv.sources]
mcp-core = { workspace = true } # <-- Direct uv to find it locally

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
3. Code Implementation Example
In your core library:
Python
# libs/mcp-core/src/mcp_core/helpers.py
def custom_mcp_logger(server_name: str, message: str):
    print(f"[{server_name.upper()}] MCP Log: {message}")
In your dedicated server:
Python
# servers/mcp-weather/src/mcp_weather/server.py
from mcp.server.fastmcp import FastMCP
from mcp_core.helpers import custom_mcp_logger # Resolves flawlessly!

mcp = FastMCP("WeatherService")

@mcp.tool()
def get_temperature(location: str) -> str:
    """Gets current temperature for a given city."""
    custom_mcp_logger("Weather", f"Fetching info for {location}")
    return f"The weather in {location} is currently 72°F and sunny."

if __name__ == "__main__":
    mcp.run()
4. Why This Layout is Perfect for your LLM / Client Config
When configuring an ecosystem like Claude Desktop or Cursor to load these servers via stdio, referencing them is incredibly streamlined. You point the configuration directly to the project folder using the global uv command:

claude_desktop_config.json Example:

JSON
{
  "mcpServers": {
    "my-weather-tool": {
      "command": "uv",
      "args": [
        "--directory",
        "/absolute/path/to/my-mcp-registry/servers/mcp-weather",
        "run",
        "src/mcp_weather/server.py"
      ]
    }
  }
}
Benefits of this approach:
Isolated runtimes: When Claude boots up my-weather-tool, uv --directory ensures it spins up using the exact package context required for that server.

Instant IDE Mapping: Turning on Workspace Mode allows navigation between the mcp-weather server logic and the mcp-core shared code seamlessly, with no broken paths or missing lint definitions