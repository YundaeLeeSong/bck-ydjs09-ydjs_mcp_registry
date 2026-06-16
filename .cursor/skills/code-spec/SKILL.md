---
name: code-spec
description: >-
  Scaffolds unorganized code into a proper build-tool or framework project with
  official directory layout (uv workspace, hatchling src layout, npm, Maven, etc.).
  Use when code is a loose segment not yet in a real project structure. Not for
  integrating into an existing repo (code-migrate) or writing API docs
  (code-document).
paths:
  - "**/*.py"
  - "**/*.ts"
  - "**/*.tsx"
  - "**/*.js"
  - "**/*.jsx"
  - "**/*.java"
  - "**/pyproject.toml"
  - "**/package.json"
---

# Code Spec

## Transform

```text
unorganized code segment -> project with official build layout
```

Output is a real project skeleton: config files, `src/` (or framework equivalent), entry points, and the code placed in the right paths.

## When to Use

- Loose scripts, pasted snippets, or prototypes with no project structure
- Need a **uv** workspace member, **npm** package, **Maven/Gradle** module, or similar
- User asks to "set up a proper project", "scaffold", or "put this in standard layout"

## Not This Skill

| Situation | Use instead |
|-----------|-------------|
| Snippet belongs inside an existing project | `code-migrate` |
| Add docstrings, Javadoc, or API docs to existing code | `code-document` |
| User-facing Markdown or README | `doc-spec` |

## Instructions

Pipeline: **Read -> Plan -> Write -> Verify**

### 1. Read

- Read the unorganized code (`read_text_file` or `large-file` if large)
- Detect language and intended stack
- Fetch official layout docs: `web-search` + `fetch-markdown` (e.g. `"uv workspace layout"`, `"hatchling src layout"`, `"npm package.json structure"`, `"Maven standard directory layout"`)
- Search fallback per `analysis-search` rule

### 2. Plan

- Run `sequentialthinking` before creating files
- List target tree: config (`pyproject.toml`, `package.json`, `pom.xml`), `src/`, tests, `README` stub
- Map code segments to modules/packages; no bulk file dump yet

### 3. Write

- Create directory structure and config first, then place code
- Follow the stack's official layout and toolchain (e.g. Python `uv` workspace with `hatchling` and `src/<package>/` per `execute-python` rule, Node `package.json` with `npx` tooling per `execute-node` rule)

### 4. Verify

- Install dependencies and run an import or test entry point with the stack's tooling (e.g. Python `uv sync` then `uv run`, Node `npm install` then `npx tsc` or a test script)
- Project must build or run minimally

## MCP Servers

| Server | Tools |
|--------|-------|
| `web-search` | `web-search`, `iask-search`, `monica-search` |
| `fetch-markdown` | `fetch` |
| `sequential-thinking` | `sequentialthinking` |
| `large-file` | `get_file_summary`, `read_large_file_chunk` |
| `local-filesystem` | `read_text_file`, `write_file`, `create_directory`, `search_files` |

## Anti-Patterns

- Placing loose code in repo root without package layout
- Guessing directory layout instead of fetching framework docs
- Using spec when the target repo already exists (use `code-migrate`)
