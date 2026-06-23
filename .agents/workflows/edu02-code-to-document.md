---
description: Extracts deep context and concepts from heavily commented source code files and maps them to previously partitioned markdown documents.
---

# Workflow: edu02-code-to-document

## Core Principle: Context Preservation
> [!IMPORTANT]
> **Zero-Destructive Editing:** During any modification or mapping phase, you must ensure a reasonable level of modification that **minimizes the dramatic deletion of existing contexts**. Do not outright delete legacy or pre-existing theoretical explanations; instead, encapsulate them under "Legacy" headings or warning blocks to preserve the historical or broader context of the document.

> [!IMPORTANT]
> **Unconditional Deep Processing:** To handle massive source files securely without token limits, you MUST use the `large-file` MCP (e.g., `read_large_file_chunk`, `search_in_large_file`) and the `sequential-thinking` MCP for deep processing **every single time**, regardless of your assumptions about the file size. This guarantees exhaustive context extraction and safe file handling.

## Trigger
Use this workflow when requested to enrich partitioned study notes or documentation using an existing project directory containing heavily commented source code.

## Steps

Pipeline: **Discover -> Think -> Map -> Update -> Verify**

### 1. Discover
- **The Discovery Ledger Mandate:** You MUST perform a 100% exhaustive scan of the target directory. Before analyzing any code, you must:
  1. Use the `local-filesystem` MCP or terminal commands (e.g., `tree`, `find`) to map every single source file (`.ts`, `.html`, `.css`, configurations) in the project.
  2. Create a **Discovery Ledger** checklist in `task.md` enumerating every single discovered file.
  3. You are strictly forbidden from completing the workflow until every file in the ledger has been opened, read, and explicitly checked off (`[x]`). This mechanically guarantees no context is missed.
- **Focus:** While sequentially iterating through your ledger, focus strictly on extracting inline comments, docstrings, build configurations, and structural context. Identify architectural files such as entry points (`main.ts`), routing (`*.routes.ts`), and global setups (`*.config.ts`).

### 2. Think
- Invoke the `sequentialthinking` MCP to break down and synthesize complex architectural patterns and contextual explanations found within the code comments.
- Utilize the `memory` MCP server to construct a knowledge graph mapping relationships between components, services, and modules across multiple files, if applicable.

### 3. Map
- Analyze the extracted concepts and cross-reference them against the existing partitioned markdown documents.
- Determine the correct target document for each concept (e.g., matching routing logic to a `routing` partition).
- **Dependency Context Resolution:** If an extracted implementation block relies heavily on a custom imported file (e.g., a specific Service, Interface, or related Component) to function logically, you MUST recursively extract or summarize that imported dependency. This ensures the reader is provided a complete, unbroken logical chain rather than a fragmented context.
- **Gap Analysis & Dynamic Partition Generation:** If the exhaustive discovery unearths major concepts (e.g., Application Bootstrapping, Routing, Unit Testing) that lack a corresponding partitioned document, you MUST automatically generate a new partition document. Do not discard discovered logic simply because a pre-existing partition does not exist.
- **Enumeration Safety Check:** Before creating any new file, you MUST explicitly scan the root directory to determine the highest existing enumeration integer (e.g., `topic07-testing.md`). The newly generated document must increment this integer sequentially (`prefix[N+1]-new-concept.md`) to strictly avoid enumeration clashes with pre-existing documentation.

### 4. Update
- Edit the target partitioned documents using native file manipulation tools.
- Weave the extracted code examples and conceptual explanations seamlessly into the existing content.
- **Context & Provenance:** Translate the original source code comments into the primary contextual explanations within the document. Every injected code block must explicitly note its original file path to anchor the example in real-world code.
- **Configuration & Dependencies:** Incorporate build configurations and dependency details into foundational partitions (e.g., core). When an injected code example relies on specific configurations or external libraries, explicitly cite that dependency requirement alongside the source code.
- **Multi-File Examples:** When a concept spans multiple files, combine multiple code blocks from those different files to illustrate the complete interaction.
- **Multi-Concept Code:** If a single chunk of source code demonstrates multiple distinct concepts, replicate and inject that same code example into all applicable contexts or partitions.
- Ensure the injection aligns with existing markdown structures, appending under relevant headers (such as `## Implementation Context`) rather than overwriting existing theory.

### 5. Verify
- Review the modified documents to ensure no markdown formatting (e.g., nested lists, code blocks, tables) was broken during the update.
- Ensure that the resulting documents remain self-explanatory, combining the original theoretical notes with practical code implementation.

## Required MCP Servers
| Server | Purpose |
|--------|---------|
| `local-filesystem` | Directory scanning and file reading. |
| `large-file` | Efficient reading and streaming of large source files. |
| `sequential-thinking` | Synthesizing multi-step context and relationships. |
| `memory` | Storing and querying cross-file architectural patterns. |
