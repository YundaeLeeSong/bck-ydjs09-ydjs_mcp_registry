# MCP Mechanics & Real-World Examples

This document clarifies how the Model Context Protocol (MCP) works, specifically addressing the confusion between local execution and external services like GitHub or Postgres.

## 1. The Core Concept: The "Local Translator"

The most important thing to understand is: **The MCP Server almost always runs on your local machine.**

Think of the MCP Server as a **Translator** or a **Proxy**. The AI Agent (like Claude) doesn't know how to "talk" to GitHub's complex API or your local math functions. It only knows how to "talk" MCP.

### The Flow of Control:
1.  **You:** "Claude, list my last 3 GitHub commits."
2.  **AI Agent (Claude):** Looks at its list of connected MCP servers. It sees one called `github-mcp`.
3.  **AI Agent:** Sends a standardized MCP request to the **local process** running on your machine: `execute_tool("list_commits", {repo: "..."})`.
4.  **Local MCP Server:** Receives this request. It then executes its own internal Python/TypeScript code.
5.  **Local MCP Server:** Makes a standard HTTPS API call to `api.github.com` using **your** stored API key.
6.  **Local MCP Server:** Receives the JSON from GitHub, simplifies it, and sends it back to Claude in the MCP format.
7.  **AI Agent:** Reads the simplified text and answers you.

---

## 2. Comparison: Local vs. Cloud Services

| Service Type | Where the MCP Server Runs | What it does behind the scenes |
| :--- | :--- | :--- |
| **Local File System** | Your Machine | Uses standard OS commands (`os.listdir`, `open`) to read your hard drive. |
| **This Project (Math)** | Your Machine | Runs the `multiply(a, b)` function in your local CPU. |
| **GitHub / Google** | Your Machine | Acts as a bridge. It takes the AI's request and makes a **Web API Call** to GitHub/Google. |
| **Postgres / SQL** | Your Machine | Acts as a bridge. It takes the AI's request and runs a **Database Query** against your DB server. |

---

## 3. How do I actually run them? (Configuration)

You don't "install" MCP servers like traditional apps. Instead, you tell an **MCP Host** (like Claude Desktop) which **command** it should run to start the server as a background process.

### The Claude Desktop Example
On Windows, you edit `%APPDATA%\Claude\claude_desktop_config.json`. Every time you open Claude, it looks at this file and starts these processes for you.

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "your_token_here"
      }
    },
    "postgres": {
      "command": "npx",
      "args": [
        "-y", 
        "@modelcontextprotocol/server-postgres", 
        "postgresql://localhost/my_database"
      ]
    },
    "my-local-tool": {
      "command": "uv",
      "args": [
        "--directory", "C:/path/to/this/project",
        "run", "python", "main.py", "mcp"
      ]
    }
  }
}
```

### Key Takeaways:
- **`command`**: The executable to run (e.g., `npx`, `uv`, `docker`, `python`).
- **`args`**: The specific arguments to start that server.
- **`env`**: This is where you store your **Secrets**. Because the MCP server runs on your machine, your API keys stay on your machine—they are never sent to the AI's cloud.

---

## 4. Why is it designed this way?

You might wonder: *"Why doesn't the AI just call the GitHub API directly?"*

1.  **Security/Privacy**: You never give your GitHub API Key or Database Password to the AI company (Anthropic/OpenAI). You only give them to the **local MCP process** running on your own computer.
2.  **Standardization**: Every API in the world is different. MCP forces every service (GitHub, Postgres, Calculator) to look exactly the same to the AI: a simple list of "Tools."
3.  **Context Management**: MCP servers can "clean up" massive API responses. GitHub might return 50KB of JSON for one commit; the MCP server can trim that down to just the message and date, saving the AI from being overwhelmed.

## 5. Summary

*   **MCP GitHub** = A small program running **on your machine** that knows how to call GitHub's web service.
*   **MCP Postgres** = A small program running **on your machine** that knows how to log into your local or remote database.
*   **This Project** = A small program running **on your machine** that knows how to calculate math and search FreeCodeCamp.

The AI Agent is the **Brain**, and the local MCP Servers are the **Hands** that reach out to the world (Local Files, Local Databases, or Remote Cloud APIs).
