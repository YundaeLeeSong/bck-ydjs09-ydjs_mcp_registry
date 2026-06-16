# Project Execution Rules

This document defines the core architectural rules for executing scripts and managing dependencies within this workspace.

## Python Execution (`uv`)
- **ALWAYS** use `uv run` when executing Python scripts or tools. 
- Example: `uv run python script.py` or `uv run pytest`.
- **NEVER** use standard `python`, `python3`, or `pip` directly, as the local machine environment relies on `uv` for isolated and correct dependency management.

## Node.js Execution (`npx`)
- **ALWAYS** use `npx` to execute Node.js binaries and project-specific tools.
- Example: `npx eslint .`, `npx tsc`, or `npx jest`.
- **NEVER** assume that npm packages are installed globally. Always prefix package commands with `npx` to ensure they run against the local `node_modules` installation or fetch the package securely on the fly.

## Search & Research Strategy
To maintain a resilient and comprehensive research workflow, follow this prioritized hierarchy of search capabilities:

1.  **Primary Search:** Utilize the native high-fidelity search engine as the first point of contact for real-time, grounded information and synthesis.
2.  **Specialized AI-Native Fallbacks:** If the primary search is unavailable, restricted, or insufficient for complex queries, pivot to specialized AI-integrated search engines:
    *   **Authoritative Answer Engines (IAsk AI):** Ideal for deep technical, academic, or forum-driven research requiring high-quality synthesis of community knowledge.
    *   **Rapid Summarization Engines (Monica):** Preferred for quick snapshots and summarized real-time web data.
3.  **Privacy-First Web Search (DuckDuckGo):** Use for broad web discovery or as a final fallback for general-purpose queries.
4.  **Error Handling:** In the event of rate-limiting or service-specific blocks (e.g., scraping challenges), do not persist with the failing provider. Immediately rotate to the next tier in the hierarchy to maintain momentum.
