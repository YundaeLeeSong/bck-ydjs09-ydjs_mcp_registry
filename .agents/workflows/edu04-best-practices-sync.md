---
description: Reconciles theoretical documentation and implementation contexts against strict, project-specific architectural constraints and best practices.
---

# Workflow: edu04-best-practices-sync

## Core Principle: Context Preservation
> [!IMPORTANT]
> **Zero-Destructive Editing:** During any synchronization phase, you must ensure a reasonable level of modification that **minimizes the dramatic deletion of existing contexts**. Do not outright delete legacy or pre-existing theoretical explanations; instead, encapsulate them under "Legacy" headings or warning blocks to preserve the historical or broader context of the document.

> [!IMPORTANT]
> **Unconditional Deep Processing:** To handle massive source files securely without token limits, you MUST use the `large-file` MCP (e.g., `read_large_file_chunk`, `search_in_large_file`) and the `sequential-thinking` MCP for deep processing **every single time**, regardless of your assumptions about the file size. This guarantees exhaustive context extraction and safe file handling.

## Trigger
Use this workflow when a repository contains explicit architectural guidelines or AI directives (e.g., `AGENTS.md`) that supersede standard framework conventions, requiring the existing partitioned documentation to be retroactively updated to match strict project standards.

## Steps

Pipeline: **Discover -> Audit -> Reconcile -> Verify -> Report**

### 1. Discover
- Use the `local-filesystem` MCP to identify and read project-specific rule-based files (e.g., `AGENTS.md`, `README.md`, `.prettierrc`, `.editorconfig`, `eslint.json`).
- Extract the core architectural mandates, specifically focusing on modern paradigm shifts that contradict legacy framework conventions (e.g., replacing decorators with functional APIs, state management rules, strict change detection policies).

### 2. Audit
- Systematically cross-reference the extracted mandates against the existing `topic[N]-*.md` partitioned documents.
- Identify specific sections where legacy implementations conflict with the enforced rules. Common examples include:
  - Class-based components vs. modern functional components.
  - Legacy state management (e.g., heavy boilerplates) vs. modern lightweight stores.
  - Custom framework directives vs. native HTML bindings.
  - Default rendering vs. optimized performance strategies.

### 3. Reconcile
- Utilize native file manipulation tools to edit the partitioned documents.
- **Do Not Erase History:** The workflow must not merely delete the old concepts. Instead, explicitly note legacy syntaxes as "Legacy/Deprecated (Project Context)" and introduce the mandated standard as the primary, preferred implementation.
- Refactor the injected implementation code blocks to strictly comply with the newly audited best practices.

### 4. Verify
- Review the modified documents to ensure no markdown formatting was broken during the updates.
- Ensure that the documentation clearly distinguishes between standard framework capabilities and strict project-level constraints.

### 5. Report
- Generate a summary artifact detailing the specific paradigm shifts applied to the documentation, providing a clear overview of the enforced best practices.

## Required MCP Servers
| Server | Purpose |
|--------|---------|
| `local-filesystem` | Scanning for and reading configuration and constraint files. |
| `large-file` | Safely reading and navigating massive architectural mandates and partitioned markdown documents. |
| `sequential-thinking` | Managing the complex audit and synthesis of conflicting structural patterns. |
