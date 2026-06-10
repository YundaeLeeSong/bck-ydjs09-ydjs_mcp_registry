# Architecture and Design Document

## 1. Overview
This project unifies disparate tools (a math calculator and an RSS feed parser) into a single, standalone application called **Unified MCP & API Service**. The application adopts modern Python standards and provides a unified interface via **FastAPI** for HTTP/REST and **Model Context Protocol (MCP)** for seamless integration with AI models or other MCP clients.

## 2. Concepts

### API (Application Programming Interface)
An API defines how software components interact. In this project, we implement a **REST API** using **FastAPI**. It exposes HTTP endpoints (`GET`, `POST`, etc.) so clients can easily interact with our tools directly over HTTP.

### MCP (Model Context Protocol)
MCP is an emerging protocol that standardizes how applications can expose "tools," "resources," or "prompts" to AI models and autonomous agents. By integrating MCP, this application allows models to dynamically discover and execute the calculator and feed-searching functionalities using structured input.

## 3. Software Design Pattern

The application is structured following the **Modular Monolith** and **Router-Controller Pattern**:
- **Separation of Concerns:** Features are separated into domains (`calculator` and `feed`). 
    - **Core:** Pure business logic and utilities.
    - **API:** FastAPI routers and server configuration.
    - **MCP:** FastMCP server and tool registrations.
- **Package Entry Point:** The `src/unified_mcp_app/__main__.py` file acts as the primary orchestrator, allowing the package to be run directly via `python -m unified_mcp_app`.
- **Dual-Interface Strategy:** The application can boot as a full HTTP REST server or a raw MCP STDIO server depending on command-line arguments.

## 4. Directory Structure

```text
.
├── main.py                     # Convenience entry point
├── pyproject.toml              # UV dependency & project configuration
├── src/
│   └── unified_mcp_app/
│       ├── __init__.py
│       ├── __main__.py         # Orchestration & CLI entry point
│       ├── api/
│       │   ├── server.py       # FastAPI & FastApiMCP initialization
│       │   └── routers/        # Feature-specific routers
│       │       ├── calculator.py
│       │       └── feed.py
│       ├── core/               # Pure business logic
│       │       ├── calculator.py
│       │       └── feed.py
│       └── mcp/
│           ├── server.py       # FastMCP instance
│           └── tools/          # Tool registration wrappers
```

## 5. Usage

### HTTP API
To start the FastAPI service:
```bash
uv run python main.py
```
Visit `http://localhost:8000/docs` for interactive documentation.

### MCP Server
To start the raw MCP STDIO server (for AI clients):
```bash
uv run python main.py mcp
# OR
python -m unified_mcp_app mcp
```

## 6. Development Lifecycle (uv)
This project is managed using `uv` for high-performance dependency management and builds.
- **Syncing:** `uv sync`
- **Execution:** `uv run python main.py`
