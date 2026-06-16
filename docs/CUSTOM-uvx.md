In uv, you don't need a separate global linking step because uv natively understands local editable development and workspaces.

The uv Solution: Editable Installations
Instead of publishing your packages or managing a global symlink state on your machine, you can tell uvx to run your local packages directly in editable mode via their file paths.

When an agent triggers the server, uv will instantly run the live code from your directory. If you change a line of code in your editor, the AI agent gets the updated behavior on its very next request—no rebuilding or re-linking required.

Here is how you structure your mcpServers configuration using your uv workspace subdirectories:

JSON
{
  "mcpServers": {
    "my-uv-filesystem": {
      "command": "uvx",
      "args": [
        "--with",
        "editable+/absolute/path/to/my-mcp-suite/packages/service-filesystem",
        "my-filesystem-package-name"
      ]
    },
    "my-uv-database": {
      "command": "uvx",
      "args": [
        "--with",
        "editable+/absolute/path/to/my-mcp-suite/packages/service-database",
        "my-database-package-name"
      ]
    }
  }
}
How This Command Works Under the Hood
The arguments passed to uvx break down like this:

--with editable+/path/to/package: This flags the local subdirectory as a dependency and installs it dynamically into a transient, isolated virtual environment in editable mode.

my-filesystem-package-name: This is the actual name of the package/executable defined inside that subdirectory's pyproject.toml (under [project] or [project.scripts]).

Setting Up Your Workspace pyproject.toml
To make sure uv handles everything perfectly across your suite, your root project directory should explicitly declare the subdirectories as part of a uv workspace.

Here is how your root pyproject.toml should look:

Ini, TOML
[project]
name = "my-mcp-suite"
version = "0.1.0"
description = "Universal MCP Monorepo Suite"
readme = "README.md"
requires-python = ">=3.10"

# Declare your subdirectories as members of the workspace
[tool.uv.workspace]
members = ["packages/*"]
And inside each individual subdirectory (e.g., packages/service-filesystem/pyproject.toml), ensure you expose the script entry point so uvx knows what command to execute:

Ini, TOML
[project]
name = "my-filesystem-package-name"
version = "0.1.0"
dependencies = [
    "mcp>=0.1.0", # Dependencies for your MCP server code
]

# This maps the executable command name to your main function loop
[project.scripts]
my-filesystem-package-name = "service_filesystem.main:run"