# High-Level Server Interaction (Native MCP Integration)

**Use Case:** Testing business logic, utilizing tools, and seamlessly interacting with server capabilities without writing custom client code or managing network transport.

When you configure my host environment (Gemini CLI) to connect directly to an MCP server, the workflow changes completely compared to low-level script testing.

## How It Works

Instead of me running the server in the background and sending manual HTTP or STDIO requests via shell scripts, the **host environment** handles the connection automatically.

1. **Orchestration:** The host starts the server process (if local STDIO) or connects to the URL (if remote SSE).
2. **Transport:** The host completely manages the STDIO pipes or SSE event streams.
3. **Serialization:** The host handles wrapping and unwrapping the JSON-RPC 2.0 messages.

The tools provided by the MCP server seamlessly appear in my native tool list, exactly like my built-in tools (`read_file`, `run_shell_command`, etc.).

## Workflow Comparison

| Feature | Low-Level Shell/Scripts (`INSTR-low_level.md`) | Native MCP Configuration |
| :--- | :--- | :--- |
| **Execution** | I start the server via `run_shell_command` (`is_background=true`) | The host automatically runs/connects to the server in the background |
| **Client** | I use `curl`, `httpx`, or pipe `stdin` via custom Python scripts | I simply call the tool natively (e.g., `multiply(a=5, b=3)`) |
| **Visibility** | I see HTTP headers, chunked encoding, and raw JSON-RPC bytes | I only see the parsed inputs and outputs of the tool |
| **Best For** | Protocol documentation, debugging transport issues | End-to-end testing, utilizing the actual tool features |

## Why Native MCP Hides the Network

The Model Context Protocol is explicitly designed to abstract the transport layer away from the AI agent. 

Even if you use off-the-shelf, community-provided MCP servers from public registries (via `npx` or `uvx`), they operate on this high-level paradigm. For example, the official `@modelcontextprotocol/server-fetch` gives me the *meaning* of a webpage (parsing HTML to Markdown), but intentionally strips away the HTTP headers (`Transfer-Encoding`, `Date`, etc.).

**Rule of Thumb:**
- Use **Native MCP Configuration** when you want me to *use* the tools.
- Use **Low-Level Shell Scripts** when you want me to *document or debug* how the tools communicate over the wire.