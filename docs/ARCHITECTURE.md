# Architecture and Design Document

## 1. Overview
This project is a `uv` workspace mono-repo that provides a collection of tools (a math calculator and an RSS feed parser). The application adopts modern Python standards and isolates shared business logic from execution environments. It exposes functionality via **FastAPI** for HTTP/REST and **Model Context Protocol (MCP)** for seamless integration with AI models or other MCP clients.

## 2. Concepts

### API (Application Programming Interface)
An API defines how software components interact. In this project, we implement a **REST API** using **FastAPI** within the `api-feed` server. It exposes HTTP endpoints (`GET`, `POST`, etc.) so clients can easily interact with tools over HTTP.

### MCP (Model Context Protocol)
MCP is an emerging protocol that standardizes how applications can expose "tools," "resources," or "prompts" to AI models and autonomous agents. By integrating MCP via `FastMCP` and `FastApiMCP`, this application allows models to dynamically discover and execute functionalities using structured input.

## 3. Software Design Pattern

The application is structured following the **Workspace Mono-Repo Pattern**:
- **Separation of Concerns:** 
    - **Core Library (`libs/mcp-core`):** Pure business logic, utilities, and integrations (e.g., feed parsing and math functions). Completely decoupled from transport layers.
    - **Isolated Servers (`servers/`):** Each domain is deployed as a standalone service utilizing the shared core logic.
        - **`mcp-calculator`:** A pure `FastMCP` server deployed over STDIO.
        - **`api-feed`:** A dual-interface `FastAPI` and `FastApiMCP` server exposing both REST and MCP endpoints.
- **Isolated Runtimes:** Using `uv --directory`, each server runs in its own context, ensuring dependencies don't conflict across services.

## 4. Directory Structure

```text
.
├── pyproject.toml                 # Root workspace configuration
├── libs/
│   └── mcp-core/                  # Shared core business logic
│       ├── pyproject.toml
│       └── src/
│           └── mcp_core/
│               ├── __init__.py
│               ├── calculator.py  # Pure math logic
│               └── feed.py        # RSS feed parsing
└── servers/
    ├── mcp-calculator/            # Standalone FastMCP server
    │   ├── pyproject.toml
    │   └── src/
    │       └── mcp_calculator/
    │           ├── __init__.py
    │           └── server.py      # MCP tool bindings
    └── api-feed/                  # FastAPI-MCP web app
        ├── pyproject.toml
        └── src/
            └── api_feed/
                ├── __init__.py
                ├── routers.py     # FastAPI endpoints for feed
                └── server.py      # FastAPI application & FastAPI-MCP wrapper
```

## 5. Usage

### HTTP API
To start the FastAPI service for the Feed domain:
```bash
uv run --directory servers/api-feed python -m api_feed.server
```
Visit `http://localhost:8000/docs` for interactive documentation.

### MCP Servers
To start the raw MCP STDIO servers (for AI clients):

**Calculator MCP Server:**
```bash
uv run --directory servers/mcp-calculator python -m mcp_calculator.server
```

**Feed MCP Server:**
```bash
uv run --directory servers/api-feed python -m api_feed.server mcp
```

## 6. Development Lifecycle (uv)
This project is managed using `uv` workspaces for high-performance dependency management and builds.
- **Syncing:** `uv sync` (Syncs the entire workspace)
- **Execution:** `uv run --directory <path> python ...`
