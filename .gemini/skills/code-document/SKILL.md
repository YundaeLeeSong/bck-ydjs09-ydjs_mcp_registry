---
name: code-document
description: >-
  Adds or finalizes formal in-code API documentation: Python docstrings, Javadoc,
  JSDoc/TSDoc, XML docs. Use when existing code needs official API docs, not
  user-facing Markdown. Not for README or guides (doc-*) or project scaffold
  (code-spec).
---

# Code Document

## Transform

```text
undocumented code -> code with formal API documentation
```

Documentation lives **in source**: docstrings, Javadoc, JSDoc/TSDoc, XML doc comments. Not README or external Markdown.

## When to Use

- Add or complete **docstrings** (Python: Google, NumPy, or project style)
- Add **Javadoc** for Java public API
- Add **JSDoc/TSDoc** for TypeScript/JavaScript exports
- "Document this module", "add API docs", "finalize docstrings before release"

## Not This Skill

| Situation | Use instead |
|-----------|-------------|
| User-facing docs (README, guides, specs) | `doc-spec`, `doc-migrate`, or `doc-merge` |
| Scaffold new project from loose code | `code-spec` |
| Integrate snippet into codebase | `code-migrate` |
| Inline design or pattern reasoning, not API contracts | `code-develop` |

## Instructions

Pipeline: **Read -> Plan -> Write -> Verify**

### 1. Read

- Read the code to document and **neighboring documented modules** for style to match
- Fetch style spec if needed: PEP 257, Google Python Style docstrings, Oracle Javadoc conventions (`web-search`, `fetch-markdown`)
- List public API surface: modules, classes, functions, parameters, returns, raises/errors

### 2. Plan

- Run `sequentialthinking` before editing
- Choose doc format consistent with the project (match existing docstrings first)
- Plan coverage: every public symbol; skip obvious private `_` helpers unless project requires them

### 3. Write

- Add or revise doc comments section by section
- Include: summary, args/parameters, returns, raises/exceptions, examples only when project uses them
- Do not change behavior; documentation-only diff unless types need fixing for clarity

### 4. Verify

- Run the project's doc tooling or doc linter if configured, then read the rendered help output (e.g. Python `uv run python -c "help(module)"`, TypeScript `npx typedoc`)
- Re-check with the language's type checker wherever types were adjusted (e.g. `tsc`)
- Invoke `md-verify` only for `.md` files touched alongside code

## MCP Servers

| Server | Tools |
|--------|-------|
| `local-filesystem` | `read_text_file`, `write_file`, `edit_file`, `search_files` |
| `sequential-thinking` | `sequentialthinking` |
| `web-search` | style guide lookup |
| `fetch-markdown` | `fetch` |

## Anti-Patterns

- Restating the function name with no semantic value ("returns x" with no type context)
- User-facing tutorials in docstrings (belongs in `doc-*`)
- Documenting without reading how siblings in the same package are documented
- Writing inline design or pattern reasoning here (belongs in `code-develop`)
