MCP stands for Model Context Protocol. It is an open-source standard created by Anthropic that has rapidly become the universal integration standard for AI—essentially acting as the "USB-C port for AI assistants."  Before MCP, if a company built a new developer tool, database, or API, they had to write a custom plugin for OpenAI, a separate custom plugin for Claude, another for Gemini, and another for Cursor. This created a massive, messy integration problem.  MCP solves this by creating a uniform, client-server architecture: 
┌──────────────────────────────┐
│          AI Host             │
│ (Kiro, Cursor, Claude Code)  │
└──────────────┬───────────────┘
               │ (Standardized MCP Client)
               ▼
┌──────────────────────────────┐
│          MCP Server          │
│ (Postgres, Git, Docker, etc.)│
└──────────────────────────────┘
Why You See It in Kiro and Other IDEsWhen an IDE like Amazon's Kiro supports MCP, it means the IDE acts as an MCP Client. You can plug any pre-made or custom MCP Server directly into it.Instead of waiting for Amazon or Cursor to build a specific feature, you can grab an open-source MCP server off GitHub and instantly give the AI native abilities to:Query your local PostgreSQL or MySQL databases.  Read and edit files inside a Docker container.Interact with Slack, Google Drive, or Jira.  Run terminal commands or execute code in a secure sandbox.  The Three Core Primitives of MCPEvery MCP server exposes three main things to the AI host:Resources: Read-only data data streams (like log files, database schemas, or API docs).Tools: Executable functions that the AI can trigger (like running a test suite, creating a Git commit, or updating a database row).  Prompts: Pre-designed templates that help guide the AI through specific complex tasks.  Because it's an open standard, it prevents vendor lock-in. If you build an MCP server to connect to an internal company API, that exact same server will work perfectly whether you feed it into Kiro, Cursor, Windsurf, or Claude Code.  


Realistically and technically, Model Context Protocol (MCP) is an open-source, client-server stateful protocol built on top of JSON-RPC 2.0.

Instead of hard-coding unique API integrations for every different AI model or application, MCP standardizes how an AI application (the client/host) and an external data source or tool (the server) send structured messages to each other.

1. The Core Architecture
The architecture consists of three main participants:

┌────────────────────────────────────────┐
│               MCP Host                 │
│      (The IDE: Kiro, Cursor, etc.)     │
│   ┌────────────────────────────────┐   │
│   │           MCP Client           │   │
│   └───────────────┬────────────────┘   │
└───────────────────┼────────────────────┘
                    │ 
                    │  JSON-RPC 2.0 Messages via
                    │  Local Stdio or HTTP / SSE
                    ▼
┌────────────────────────────────────────┐
│              MCP Server                │
│    (Database, Git, local script)       │
└────────────────────────────────────────┘
MCP Host: The runtime environment where the AI model lives (such as Kiro, Cursor, or Claude Desktop).

MCP Client: A lightweight component embedded inside the host application. It maintains a 1:1, stateful session with a specific server.

MCP Server: A standalone program or process that wraps around a local or remote resource (like a PostgreSQL database, a file system, or a third-party API) and exposes its capabilities.

2. Real-Time Communication & Transport
When an IDE starts an MCP server, they perform a protocol handshake to negotiate capabilities and API versions. Once initialized, they communicate using standard JSON-RPC 2.0 messages across two primary transport methods:

Stdio (Standard Input/Output): Typically used for local tools running on the same machine. The IDE spins up the server as a background subprocess and pipes data back and forth.

HTTP with SSE (Server-Sent Events): Used for remote or networked microservices.

3. The 3 Technical Primitives
An MCP server exposes data and actions to the AI using exactly three structured primitives, defined explicitly by JSON schemas:

A. Resources (Read-Only Data)
A resource is a passive data stream that the AI can read to gain context. Each resource is identified using a unique Uniform Resource Identifier (URI).

Real-world example: A server schema definition like postgres://localhost:5432/db/schema that exposes application database tables to the model.

B. Tools (Executable Actions)
Tools are executable functions that the AI model can choose to call. The server provides a JSON Schema defining the tool's name, description, and strict parameter requirements.

Real-world example: A tool called execute_query with a parameter schema requiring a validated SQL string. When the AI decides to call it, the client sends a tools/call JSON-RPC request:

JSON
{
  "jsonrpc": "2.0",
  "id": 42,
  "method": "tools/call",
  "params": {
    "name": "execute_query",
    "arguments": {
      "sql": "SELECT * FROM users WHERE status = 'active';"
    }
  }
}
C. Prompts (Templates)
Pre-defined, server-side prompt engineering templates that help guide the user and the model through complex tasks (like structured code review configurations).

Why this matters to the code
Without MCP, if you write a custom script to inspect cloud resources or query a specialized database, you have to write custom integration code specifically for Cursor's API format, then completely rewrite it if you want Kiro or a Python agent framework to use it.

With MCP, you write a single, lightweight backend script that conforms to the MCP JSON-RPC specification. Once it satisfies the specification, any IDE or AI client that supports MCP can instantly parse your tool's schema, validate inputs against it, and execute it natively.









https://modelcontextprotocol.io/docs/getting-started/intro

https://mcpservers.org/servers/modelcontextprotocol/fetch

https://mcpservers.org/servers/tverney/mcp-agent-memory