---
name: server-test
description: >-
  Use when debugging or interacting with local servers, capturing raw protocol
  data, or when you need to start a server and act as a client without freezing
  your execution loop.
---

# Server Test

This skill outlines the universal pattern for AI agents to interact with local servers. To prevent freezing your main execution loop and getting stuck in a hanging prompt session, you must **never** run a blocking server process directly in the foreground.

## 1. Starting the Server Non-Blocking

When starting a server, you must ensure it runs asynchronously. Depending on your specific agent capabilities, use one of the following methods:

- **Agent-Specific Tools:** If you have built-in background process tools (e.g., an `is_background: true` parameter for your shell command tool), use them.
- **Universal Shell Methods:** If no built-in tool exists, redirect the server output to a log file and run it in the background using standard shell features (e.g., appending `&` in Bash, using `nohup`, or using `Start-Process` in PowerShell).

**Example (Universal Bash):**
```bash
python -m my_server > server_logs.txt 2>&1 &
```

## 2. Verifying the Server State

Do not assume the server started instantly. You must verify it is ready to accept connections before acting as a client:
- Read the redirected log file (e.g., `cat server_logs.txt`) or use your agent's log reading tool.
- Wait for the specific log message indicating the port is bound and listening (e.g., `Uvicorn running on http://127.0.0.1:8000`).
- If the server crashes, read the logs to diagnose why.

## 3. Acting as a Client

Once the server is verified as running, use synchronous shell commands to act as a client.

### Inspecting Raw Protocols
To see exact HTTP requests, headers, and responses, use `curl` with verbose flags.

**Example: Inspecting a Server-Sent Events (SSE) stream**
```bash
curl -i -N http://localhost:8000/stream
```
*(`-i` includes headers, `-N` disables buffering to stream the response.)*

**Example: Sending a POST request**
```bash
curl -i -X POST http://localhost:8000/api \
  -H "Content-Type: application/json" \
  -d '{"data": "test"}'
```

### Advanced Complex Interactions
For multi-step interactions (like holding a stream open while simultaneously sending POST requests), write a temporary test script (e.g., in Python using `httpx` or `requests`) that performs the interaction, captures the exact output, and prints it to standard output. Run this temporary script synchronously.

## 4. Cleanup and Documentation

- **Cleanup:** Always ensure you terminate the background process when testing is complete to free up the port. Use your agent's process management tools or standard shell kill commands (e.g., `kill <PID>`).
- **Documentation:** Inject the captured raw HTTP exchanges and traces into your documentation to accurately reflect the server's real-world behavior.
