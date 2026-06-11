# Unified MCP Registry Project
This project is a `uv` workspace mono-repo that provides a collection of tools (a math calculator and an RSS feed parser). The application adopts modern Python standards and isolates shared business logic from execution environments. It exposes functionality via **FastAPI** for HTTP/REST and **Model Context Protocol (MCP)** for seamless integration with AI models or other MCP clients.

## Development (uv)

This project is managed using `uv` workspaces for high-performance dependency management and builds. Dependencies are kept in sync through isolated maintenance scripts and workspace-aware local source resolution.

### Standard Commands

**Automatically sync dependencies** — if you add new imports to your Python files, run this to update all `pyproject.toml` files in the workspace:
```bash
uv run poe sync-deps
```

**Manual workspace sync** — ensure your local virtual environment matches the lockfile:
```bash
uv sync
```

**Execution:** `uv run --directory <path> python ...`

### Dependency Sync (`poe sync-deps`)

The `sync-deps` task is defined in the root `pyproject.toml` and runs via **poethepoet** (aliased as `poe`). It triggers the isolated script at `uv/pipreqs.uv.py`, which orchestrates dependency discovery and synchronization across all workspace members.

### Isolated Maintenance Scripts (PEP 723)

The script at `uv/pipreqs.uv.py` uses **PEP 723 Inline Script Metadata** to declare its own dependencies independently of the project's `pyproject.toml`:

```python
# /// script
# dependencies = ["tomlkit"]
# ///
```

When you run `uv run uv/pipreqs.uv.py`, `uv`:
1. **Transient environment** — creates a temporary, isolated virtual environment for that execution.
2. **On-the-fly installation** — installs `tomlkit` (and any other declared dependencies) into that environment.
3. **Zero clutter** — does **not** add those dependencies to your `pyproject.toml` or main `.venv`; once the script finishes, the environment is managed by `uv`'s cache.

### Smart Dependency Discovery (`uvx pipreqs`)

The maintenance script discovers dependencies using `pipreqs`, invoked via `uvx` rather than installed as a project dependency:

```python
subprocess.run(["uvx", "pipreqs", ...])
```

**`uvx`** is the `uv` equivalent of `npx` — it downloads and runs a tool in a temporary environment, keeping utility tools out of your application's runtime dependencies.

### Local Source Resolution

Workspace members often depend on each other (e.g., `app-api-feed` depends on `mcp-core`). `uv` resolves this through the `[tool.uv.sources]` table in each member's `pyproject.toml`.

When the maintenance script runs `uv add --package <member-name> -r requirements.txt`:
1. **Workspace check** — `uv` checks whether discovered imports (like `mcp_core`) match a workspace member.
2. **Source mapping** — it uses the local mapping in `pyproject.toml`:
   ```toml
   [tool.uv.sources]
   mcp-core = { workspace = true }
   ```
3. **Isolation** — because `uv` is workspace-aware, it treats `mcp-core` as a local directory rather than a PyPI package, preventing version conflicts and ensuring you always code against local changes.

### Package Layout (`[build-system]`)

Each workspace member is a **Python package** — not just a folder of scripts. The `[build-system]` block in its `pyproject.toml` tells installers how to build and install it:

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

- **`[build-system]`** — standard Python metadata (PEP 517): "use hatchling to turn this project into an installable package."
- **`hatchling`** — the build tool that finds your source code and packages it. When `uv sync` installs a workspace member, it calls hatchling under the hood.
- **`src/` layout** — hatchling's default convention: if a `src/` folder exists, look inside it for the package directory. The folder name matches the project name with hyphens turned to underscores — e.g. project `mcp-calculator` → code in `src/mcp_calculator/`.

So `uv` does not guess paths on its own — it installs each member as a package, and hatchling knows to look in `src/<package_name>/`. That is why `python -m mcp_calculator` works after sync: the package is installed into `.venv` from that `src/` tree.










## Concepts

### API (Application Programming Interface)
An API defines how software components interact. In this project, we implement a **REST API** using **FastAPI**. It exposes HTTP endpoints (`GET`, `POST`, etc.) so clients can easily interact with tools over HTTP.

### MCP (Model Context Protocol)
Model Context Protocol (MCP) is a standardized communication **protocol** that securely connects AI large language **models** (LLMs) to external **contexts** like codebases, databases, and files, frequently using either standardized input and output (STDIO) for local integration or Server-Sent Events (HTTP/SSE) for network-based remote communication.

Regardless of the transport, all MCP clients and servers exchange messages using **JSON-RPC 2.0** — structured request/response and notification payloads sent over the chosen channel.











## Software Design

This project uses two Python MCP libraries — each suited to a different layer of the stack:

### FastMCP — native MCP server

Built specifically for MCP. Decorator-based syntax (inspired by FastAPI), dedicated to defining MCP tools, resources, and prompts.

- **Lightweight** — no full HTTP server or web framework required.
- **Direct** — focuses on standard MCP transports (STDIO, SSE).
- **Tool-centric** — designed around LLM tool calling.

Use **FastMCP** when building something new and dedicated to an AI agent — e.g. a local utility toolkit or script runner. In this repo: `server/mcp-calculator`.

### FastAPI-MCP — bridge for existing web apps

An adapter for FastAPI. Takes an existing app — routes, Pydantic models, dependencies — and translates REST endpoints into MCP tools.

- **Dual interface** — runs as both a REST API and an MCP server.
- **Automatic translation** — converts OpenAPI/Swagger definitions into MCP tool schemas.
- **Reuses architecture** — same routing, auth, and business logic for web and AI clients.

Use **FastAPI-MCP** when you already have a web backend and want to expose it to AI agents without rewriting it — or when both traditional clients and AI agents need the same API. In this repo: `server/mcp-api-feed` wraps `app/app-api-feed`.

| | FastMCP | FastAPI-MCP |
| :--- | :--- | :--- |
| **Goal** | Native MCP server | Adapt REST APIs to MCP |
| **Foundation** | Standalone | Requires FastAPI |
| **Best for** | Greenfield AI-only tools | Existing or hybrid web backends |
| **Duplication** | High if you also need a web API | None — routes are reused |

### Workspace Mono-Repo Pattern

The application is structured following the **Workspace Mono-Repo Pattern**:
- **Separation of Concerns:**
    - **Core Library (`lib/mcp-core`):** Pure business logic, utilities, and integrations (e.g., feed parsing and math functions). Completely decoupled from transport layers.
    - **Isolated Apps (`app/`):** Hosting the primary user-facing services (e.g., FastAPI backend).
    - **Isolated Servers (`server/`):** Exposing functionalities to AI agents via MCP.
- **Isolated Runtimes:** Using `uv --directory`, each server runs in its own context, ensuring dependencies don't conflict across services.

### Repository Structure

```text
.
├── pyproject.toml                 # Root workspace configuration
├── app/
│   └── app-api-feed/              # FastAPI backend for feed functions
│       ├── pyproject.toml
│       └── src/
│           └── app_api_feed/
│               ├── __init__.py
│               ├── routers.py     # FastAPI endpoints for feed
│               └── server.py      # FastAPI application
├── lib/
│   └── mcp-core/                  # Shared core business logic
│       ├── pyproject.toml
│       └── src/
│           └── mcp_core/
│               ├── __init__.py
│               ├── calculator.py  # Pure math logic
│               └── feed.py        # RSS feed parsing
└── server/
    ├── mcp-calculator/            # Standalone FastMCP server
    │   ├── pyproject.toml
    │   └── src/
    │       └── mcp_calculator/
    │           ├── __init__.py
    │           └── server.py      # MCP tool bindings
    └── mcp-api-feed/              # MCP wrapper for FastAPI backend
        ├── pyproject.toml
        └── src/
            └── mcp_api_feed/
                ├── __init__.py
                └── server.py      # FastAPI-MCP wrapper
```




















## Usage



### HTTP API (REST)
The HTTP API is provided by the `app-api-feed` app and is best for direct interaction via web browsers, scripts, or traditional applications.

**Start the service:**
```bash
uv run --directory app/app-api-feed python -m app_api_feed
```

**Interactive documentation:** Once the server is running, open **`http://localhost:8000/docs`** in your browser. You will see an interactive Swagger UI where you can expand any endpoint and click **"Try it out"** to send real requests.

**Example curl request:**
```bash
curl -X GET "http://localhost:8000/feed/fcc_news_search?query=python"
```





### MCP Servers (For AI Agents)
The MCP interface allows AI models like Claude to discover and use your tools automatically. The workspace exposes two MCP servers.

**Start the MCP servers (STDIO):**
```bash
# Calculator FastMCP server
uv run --directory server/mcp-calculator python -m mcp_calculator

# Feed FastAPI-MCP server
uv run --directory server/mcp-api-feed python -m mcp_api_feed
```

**Verification (manual test):** When you run an MCP server manually, it will appear stuck or show no output. This is **expected behavior** — it is waiting for JSON-RPC instructions via `stdin`. To verify it is working, perform the **MCP handshake** by pasting these lines one at a time and pressing **Enter** after each:

1. Initialize request:
```json
{"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"capabilities": {}, "clientInfo": {"name": "test", "version": "1.0"}, "protocolVersion": "2024-11-05"}}
```

2. Initialized notification:
```json
{"jsonrpc": "2.0", "method": "notifications/initialized"}
```

3. List tools:
```json
{"jsonrpc": "2.0", "id": 2, "method": "tools/list"}
```

If the server is functioning correctly, the third command will return a JSON object listing all available tools.

**Connect to Claude Desktop:** Add the following to `%APPDATA%\Claude\claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "mcp-calculator": {
      "command": "uv",
      "args": [
        "--directory",
        "C:/Users/manua/source/repo/_references/_python02-personal_mcp_registry/server/mcp-calculator",
        "run",
        "python",
        "-m",
        "mcp_calculator"
      ]
    },
    "mcp-api-feed": {
      "command": "uv",
      "args": [
        "--directory",
        "C:/Users/manua/source/repo/_references/_python02-personal_mcp_registry/server/mcp-api-feed",
        "run",
        "python",
        "-m",
        "mcp_api_feed"
      ]
    }
  }
}
```