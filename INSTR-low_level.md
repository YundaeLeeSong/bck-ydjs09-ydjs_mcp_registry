# Low-Level Server Interaction (Shell & Scripts)

**Use Case:** Debugging network layers, capturing raw protocol data (HTTP headers, exact JSON-RPC payloads, SSE streams), and documenting byte-for-byte server behaviors.

Yes, I have full capability to run servers in the background and act as a client without freezing my execution loop. I accomplish this using my built-in background shell process management tools.

## 1. Running the Server in the Background

I can use the `run_shell_command` tool with the parameter `is_background=true`. This starts the process, checks for immediate errors, and then detaches it to run asynchronously.

**Example Command (starting SSE server):**
```bash
uv run --directory server/mcp-sse-system-status python -m mcp_sse_system_status
```
*(Executed with `is_background: true`)*

## 2. Managing the Background Server

Once running, I receive a Process ID (PID). I can use two dedicated tools to manage this:
- **`list_background_processes`**: To see all active processes and their status.
- **`read_background_output`**: To read the server logs (like Uvicorn startup logs) and confirm the server is listening on the correct port (e.g., `http://localhost:8000`).

## 3. Acting as a Client

While the server is running in the background, I can run synchronous `run_shell_command` calls to act as a client and interact with it.

### Inspecting HTTP Metadata and JSON
To see the exact HTTP requests, headers, and JSON responses, I can use `curl` with verbose or header-only flags.

**Example: Inspecting the SSE stream handshake (GET)**
```bash
curl -i -N http://localhost:8000/sse
```
*(`-i` includes the HTTP response headers. `-N` disables buffering to stream the response.)*

**Example: Sending a JSON-RPC request (POST)**
```bash
curl -i -X POST http://localhost:8000/messages?sessionId=<id> \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc": "2.0", "id": 1, "method": "tools/list"}'
```

### Advanced Testing with Python Scripts
For complex interactions, like holding an SSE connection open while simultaneously sending POST requests, I can write a temporary Python script that uses `httpx` or `requests` to perform the interaction, capture the metadata/JSON, and print it to standard output. I then run this script using `run_shell_command`.

## 4. Documenting the Results

Once I've captured the exact HTTP exchanges (headers, status codes, JSON payloads), I can use my file editing tools to inject these real-world traces directly into documentation files to make them accurate and thorough.