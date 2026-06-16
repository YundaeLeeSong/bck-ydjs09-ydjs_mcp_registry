# Gemini CLI MCP Servers Configuration

This repository uses Model Context Protocol (MCP) servers to extend the capabilities of the Gemini CLI agent. 

## Recent Configuration Updates & Security Fixes

*   **Secure Filesystem Access:** The `local-filesystem` server path argument was updated from `C:/` to `.`. This is a crucial security improvement. Using `.` is cross-platform (works on Windows, macOS, and Linux) and securely scopes the agent's file access exclusively to the current project directory. It prevents the agent from accidentally or maliciously reading/modifying sensitive OS files.
*   **Corrected Fetch Package:** The `fetch` server was failing because `@modelcontextprotocol/server-fetch` does not exist on npm. This was corrected to use the official Python package via `uvx mcp-server-fetch`.

---

## Configured MCP Servers: What They Are & Why They're Great

Here is a breakdown of every MCP server configured in `.gemini/settings.json`, what it does, and why it's a powerful addition to your workspace.

### 1. local-filesystem (`@modelcontextprotocol/server-filesystem`)
*   **What it is:** Provides the AI agent with read and write access to your local files and directories.
*   **Why it's great:** It allows the agent to actively participate in your project. Instead of just giving you code snippets to copy-paste, the agent can explore your codebase, refactor files, write tests, and create new components directly within your scoped workspace.

### 2. fetch (`mcp-server-fetch`)
*   **What it is:** Converts raw HTML web pages into clean, LLM-friendly markdown.
*   **Why it's great:** If you need the agent to use a newly released library, read a specific API reference, or follow an online tutorial, it can fetch the URL, read the documentation, and immediately apply that new knowledge to your code. 

### 3. github (`@modelcontextprotocol/server-github`)
*   **What it is:** Integrates directly with the GitHub API using your Personal Access Token.
*   **Why it's great:** The agent can manage your remote repository. It can read issues to understand bug reports, review Pull Requests, and even create PRs automatically when it finishes a task. It bridges the gap between local coding and remote collaboration.

### 4. git-history (`mcp-server-git`)
*   **What it is:** Reads your local Git repository's history, diffs, branches, and status.
*   **Why it's great:** It gives the AI "time-travel" context. The agent can see what you changed in the last commit, understand the differences between your branch and `main`, or check unstaged changes to understand your current train of thought before offering suggestions.

### 5. Web Search Alternatives (Brave, OneSearch, Web Search)
To give the agent access to real-time internet data, several web search MCP servers can be used depending on your needs regarding API keys and environments:

*   **brave-search (`@modelcontextprotocol/server-brave-search`):**
    *   **What it is:** Allows the agent to perform real-time internet searches using the official Brave Search API.
    *   **Why it's great:** Extremely fast and structured. However, it requires a paid Brave Search API key, which can be a blocker.
*   **OneSearch MCP (`one-search-mcp`):**
    *   **What it is:** A robust, free alternative using a local headless browser (Chromium) via Docker to perform searches locally against engines like Google or DuckDuckGo.
    *   **Why it's great:** It requires no API keys and sidesteps rate limits by acting like a human. It also includes built-in web scraping so the agent can read full pages.
*   **Web Search MCP (`@oevortex/ddg_search`):**
    *   **What it is:** A versatile, privacy-oriented multi-engine search server that provides standard web results and AI-generated answers.
    *   **Engines & Tools:** It aggregates results from several providers into a single interface:
        *   **DuckDuckGo (`web-search`):** Provides standard search snippets and structured "Instant Answers."
        *   **IAsk AI (`iask-search`):** An AI-powered search engine with specialized modes for `academic`, `forums`, `wiki`, and deep `thinking` analysis.
        *   **Monica AI (`monica-search`):** Returns AI-synthesized responses based on real-time web data.
        *   **Brave AI (`brave-search`):** Leverages Brave's privacy-focused AI summarizer.
    *   **Why it's great:**
        *   **Zero Configuration:** Requires **no API keys** or accounts; it works out of the box.
        *   **Privacy-First:** Routes all traffic through privacy-respecting engines and uses rotating user agents to prevent fingerprinting.
        *   **Lightweight & Universal:** Built natively in Node.js, it runs efficiently on any architecture (including Windows, macOS, and Linux/ARM64) without the overhead of Docker.
        *   **Rich Context:** It doesn't just return links; it returns structured snippets, AI-summarized answers, and can even extract page content for the agent to analyze directly.

**⚠️ Important: Only Configure ONE Search Provider**
It is highly inefficient and not recommended to have multiple search MCPs configured in your `settings.json` at the same time:
1. **AI Confusion (Tool Overlap):** Providing multiple tools that do the exact same thing forces the AI to waste reasoning cycles deciding which to use, leading to latency and analysis paralysis.
2. **Context Window Bloat:** Loading multiple search tool schemas wastes precious context window space on redundant instructions.
3. **System Resources:** Running multiple search servers (especially Docker-based ones alongside Node processes) consumes unnecessary RAM and CPU.

### 6. postgres-db (`@modelcontextprotocol/server-postgres`)
*   **What it is:** Connects to a local or remote PostgreSQL database instance.
*   **Why it's great:** It turns the agent into a DBA. The agent can inspect your database schema, write complex SQL queries, debug data inconsistencies, and ensure your backend code perfectly aligns with your actual database structure.

### 7. memory (`@modelcontextprotocol/server-memory`)
*   **What it is:** A local Knowledge Graph that stores entities, relations, and observations.
*   **Why it's great:** It gives the agent long-term memory across sessions. If you tell it about your preferred coding style, complex architectural decisions, or how specific internal services communicate, it remembers and applies this context in future tasks without you having to repeat yourself.

### 8. sequential-thinking (`@modelcontextprotocol/server-sequential-thinking`)
*   **What it is:** A specialized reasoning tool that forces the agent to break complex problems into sequential, revisable steps.
*   **Why it's great:** For incredibly difficult architectural challenges or deep bug hunts, this tool prevents the AI from rushing to a wrong conclusion. It allows the agent to hypothesize, test, realize it's wrong, backtrack, and formulate a better plan before touching your code.

### 9. large-file (`@willianpinho/large-file-mcp`)
*   **What it is:** Efficiently reads, chunks, and searches through massive files.
*   **Why it's great:** Standard AI context windows get overwhelmed by huge files (like massive production log dumps, heavy SQL seeds, or giant legacy monolithic files). This tool lets the agent intelligently search and page through these giants without crashing or losing context.

---

## 🛠️ Troubleshooting & Known Limitations

Even the best MCP servers can encounter issues due to external service changes or security protections. Here is how to handle common failures:

### 1. Web Search MCP: The "HTTP 202" Error
*   **The Issue:** Sometimes the `web-search` tool returns `HTTP 202: Failed to fetch search results`.
*   **The Cause:** This is an **anti-bot / rate-limit response** from DuckDuckGo. It means the scraper has been detected or the engine is overloaded.
*   **The Fix:** 
    *   **Switch Tools:** The `@oevortex/ddg_search` server includes multiple tools. If `web-search` fails, immediately try **`iask-search`** or **`monica-search`**. These use different upstream providers and are often unaffected.
    *   **Wait:** If you've been searching heavily, wait 1-2 minutes for the rate limit to reset.
    *   **Alternative:** If you have a Brave API key, switch to the official `brave-search` MCP for 100% reliable, non-scraped results.

### 2. File Access Errors
*   **The Issue:** `local-filesystem` reports "Path not found" or "Access denied."
*   **The Fix:** Ensure the path in your `settings.json` is set to `.` (current directory). If you recently opened a new folder, you may need to run `gemini trust` to authorize the agent's file access.

### 3. Missing Tools
*   **The Issue:** A server is configured in `settings.json` but its tools don't appear in `/mcp list`.
*   **The Fix:** Check your terminal for initialization errors. If a required environment variable (like `GITHUB_PERSONAL_ACCESS_TOKEN`) is missing, the server will silently fail to start.

---

## How the Agent Uses These Tools

You **do not** need to use any special "trigger words" to activate these tools. Here is how it works under the hood:

1. When the agent starts, it connects to these MCP servers and receives a "menu" of tools, along with a plain-English description of what each tool does.
2. When you provide a natural language prompt (e.g., "What did I change in my last commit?"), the agent's reasoning engine evaluates its toolbox and automatically selects the most appropriate tool (`mcp_git-history_git_log` in this case).
3. **Note on Authentication:** If an environment variable (like `BRAVE_API_KEY` or `PGPASSWORD`) is missing, that specific server will fail to initialize, and its tools simply won't appear in the agent's toolbox.

## Built-in Tools vs. MCP Tools

You might notice that `local-filesystem` and `fetch` overlap with the Gemini CLI's native, built-in abilities (like its native file reader and web fetcher). If the built-in tools are faster and use fewer tokens, why include the MCP versions?

*   **The Sandboxing Factor (Claude Desktop):** MCP was created by Anthropic, and the primary client is the Claude Desktop GUI. GUI apps run in strict security sandboxes and *cannot* access your hard drive natively. They strictly require the `local-filesystem` MCP. Many developers simply copy their config from Claude Desktop to the CLI. While the CLI doesn't strictly *need* it (since it runs directly in your terminal), it doesn't hurt to include it.
*   **Fallback Implementations:** Built-in tools and MCP tools might solve the same problem using different underlying code. For instance, if the built-in web fetcher gets blocked by a website's anti-bot protection, the `fetch` MCP might use a different library (like `httpx`) that succeeds. It acts as a helpful backup wrench.
*   **Standardization:** Some teams prefer to use a standardized set of MCP servers to ensure uniform behavior across different AI clients (Cursor, Windsurf, Claude Desktop, Gemini CLI).

For Gemini CLI, the agent will generally prioritize its native, highly-optimized tools, but will autonomously fall back to MCP tools if they offer a better path to success.