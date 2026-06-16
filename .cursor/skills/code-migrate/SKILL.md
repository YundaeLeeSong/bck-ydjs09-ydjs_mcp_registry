---
name: code-migrate
description: >-
  Formats a code snippet to match an existing build environment and integrates it
  into the project. Use when the repo already has project structure and a snippet
  must land in the right module with consistent style. Not for greenfield scaffold
  (code-spec) or API documentation (code-document).
paths:
  - "**/*.py"
  - "**/*.ts"
  - "**/*.tsx"
  - "**/*.js"
  - "**/*.jsx"
  - "**/*.java"
  - "**/src/**"
---

# Code Migrate

## Transform

```text
code snippet + existing project -> snippet integrated in project
```

The project already has build config, layout, and conventions. The snippet is formatted to match, then placed in the correct module with imports, tests, and wiring.

## When to Use

- Add a function, class, or module into an **existing** codebase
- "Put this snippet in `mcp_core`", "Wire this handler like the others"
- Snippet must match naming, imports, types, error handling, and test patterns already in the repo

## Not This Skill

| Situation | Use instead |
|-----------|-------------|
| No project structure yet | `code-spec` |
| Document functions/classes (docstrings, Javadoc) | `code-document` |
| Prose or Markdown files | `doc-migrate` |

## Instructions

Pipeline: **Read -> Plan -> Write -> Verify**

### 1. Read

- Read target area of the **existing project**: sibling modules, `pyproject.toml` / `package.json`, tests
- Read the **snippet** to integrate
- Optional: `git-history` for recent changes in the target package

### 2. Plan

- Run `sequentialthinking` before edits
- Decide: target file (new vs existing), package path, public API, imports, tests to add or update
- Extract conventions from neighbors (not from generic style guides alone)

### 3. Write

- Format snippet to match project conventions
- Integrate by updating package exports or index files, registry tables, routes, or workspace deps as needed (e.g. Python `__init__.py`)
- Sync dependencies if new third-party imports appear (e.g. Python `uv run poe sync-deps`)

### 4. Verify

- Run the touched package's tests or linter with the language's toolchain (e.g. Python per `execute-python` rule, TypeScript/JavaScript per `execute-node` rule)
- Confirm snippet is reachable from intended entry point

## MCP Servers

| Server | Tools |
|--------|-------|
| `local-filesystem` | `read_text_file`, `write_file`, `search_files`, `edit_file` |
| `sequential-thinking` | `sequentialthinking` |
| `git-history` | history/blame when integration context matters |

## Anti-Patterns

- Creating a parallel folder layout instead of using the existing package tree
- Dropping a snippet without tests when neighbors have tests
- Using migrate for greenfield scaffold (use `code-spec`)
