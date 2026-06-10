# The MCP Ecosystem: Distribution & Discovery

This document explains how MCP servers are published, how you install them, and how AI agents know how to use them.

## 1. Distribution via Package Managers

MCP servers are standard programs typically written in **TypeScript (Node.js)** or **Python**. They are distributed using the same tools developers use for libraries:

*   **NPM (Node Package Manager)**: Used via `npx`. This is the most common way to run TypeScript servers without manual installation.
    *   *Example*: `npx -y @modelcontextprotocol/server-github`
*   **PyPI (Python Package Index)**: Used via `uvx` or `pip`. 
    *   *Example*: `uvx mcp-server-sqlite`

Because they are published packages, the AI Host (like Claude Desktop) can download and run the latest version on-the-fly using these commands.

## 2. Official vs. Community Servers

While the protocol is open to everyone, there are different "tiers" of servers:

*   **Official Servers**: Maintained by the MCP team (Anthropic) and major partners. These are hosted in the [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) repository. They are the "Gold Standard" for services like GitHub, Google Drive, and Slack.
*   **Community Servers**: Built by independent developers. You can find these on GitHub or listed on community galleries like [mcp-get.com](https://mcp-get.com) or [smithery.ai](https://smithery.ai).
*   **Private/Custom Servers**: Like this project! These are tools you build for your specific local workflow.

## 3. The Discovery Mechanism (The "Magic")

How does the AI know what your server can do without you explaining it?

1.  **Handshake**: When the AI Agent (Host) starts an MCP server, it sends a `list_tools` request.
2.  **Self-Description**: The MCP Server replies with a **JSON Schema**. It describes every tool it has, what parameters they need, and what they do.
    *   *Example Server Response*: "I have a tool called `get_weather`. It needs a `city` (string). I use it to find local temperatures."
3.  **Reasoning**: The AI "Brain" reads this schema. If you ask "Is it raining in Tokyo?", the AI sees the `get_weather` tool description, realizes it fits your question, and decides to call it.

## 4. The Power User Workflow

To add any new capability to your AI, the workflow is always the same:

1.  **Find**: Look up the package name for the service you want (e.g., Brave Search, Postgres).
2.  **Auth**: Get the API Key or Connection String for that service.
3.  **Config**: Add the command to your `claude_desktop_config.json`.
4.  **Restart**: Restart your AI Client.

The AI now has "new hands" to interact with that specific part of the world.
