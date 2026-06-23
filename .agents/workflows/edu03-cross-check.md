---
description: Validates partitioned documentation against official online sources, automatically correcting terminology and syntax discrepancies.
---

# Workflow: edu03-cross-check

## Core Principle: Context Preservation
> [!IMPORTANT]
> **Zero-Destructive Editing:** During any validation or cross-check phase, you must ensure a reasonable level of modification that **minimizes the dramatic deletion of existing contexts**. If official documentation contradicts the local file, do not outright delete the local context; instead, encapsulate it under "Legacy" headings or warning blocks to preserve the historical evolution of the document.

> [!IMPORTANT]
> **Unconditional Deep Processing:** To handle massive source files securely without token limits, you MUST use the `large-file` MCP (e.g., `read_large_file_chunk`, `search_in_large_file`) and the `sequential-thinking` MCP for deep processing **every single time**, regardless of your assumptions about the file size. This guarantees exhaustive context extraction and safe file handling.

## Trigger
Use this workflow to finalize documentation by cross-referencing partitioned documents against their authoritative online counterparts (e.g., verifying framework concepts against their official site).

## Steps

Pipeline: **Analyze -> Search -> Fetch -> Compare -> Correct -> Report**

### 1. Analyze
- Read the target partitioned markdown documents using native file tools.
- Isolate core terminologies, code syntax, API usages, and naming conventions described within the text.
- Determine the appropriate official domain to validate against based on the project context (e.g., if the topic is React, dynamically restrict searches to `react.dev`).

### 2. Search
- Formulate precise search queries targeted at the identified official sources (e.g., `site:react.dev state management`).
- Utilize the `web-search`, `iask-search`, or `monica-search` MCP servers to locate the specific, authoritative documentation pages.

### 3. Fetch
- Retrieve the full text of the identified official documentation using the `fetch` MCP server or native `read_url_content` capabilities.
- Ensure the retrieved context specifically covers the API version relevant to the project (or the latest stable version if unspecified).

### 4. Compare
- Employ the `sequentialthinking` MCP to systematically compare the local document's terminology, syntax, and conceptual explanations against the fetched official documentation.
- Detect discrepancies such as deprecated syntax, incorrect naming conventions, trivial typos, or logical inconsistencies.

### 5. Correct
- Utilize native file manipulation tools to rewrite the erroneous sections within the partitioned document.
- Ensure the edits align the local document flawlessly with the official standard without breaking the existing markdown structures (e.g., nested lists, code blocks, tables).
- **Verification Tagging:** Upon successful correction or validation, append a `> [!NOTE]` block at the bottom of the relevant section or document stating: "Verified against official documentation: [URL]".

### 6. Report
- Generate a summary detailing exactly what terminologies, conventions, or code blocks were modified during the cross-check process.

## Required MCP Servers & Tools
| Server / Tool | Purpose |
|---------------|---------|
| `web-search` / `iask-search` / `monica-search` | Querying the web to locate official documentation URLs. |
| `fetch` / `read_url_content` | Pulling the actual text from the official documentation pages. |
| `large-file` | Safely reading and navigating massive local documents and fetched official specs without context truncation. |
| `sequential-thinking` | Managing the cognitive load of verifying technical documentation. |
| Native File Tools | Editing the partitioned markdown files to apply corrections. |
