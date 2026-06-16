---
name: code-develop
description: >-
  Applies official software design principles and design patterns to an existing
  built project's source, refactoring or implementing each according to its true
  purpose, and recording the implementation reasoning as concise numbered inline
  comments. Use when developing, designing, or refactoring code in a project that
  already has structure. Not for greenfield scaffold (code-spec), integrating a
  snippet (code-migrate), or formal API docs (code-document).
paths:
  - "**/*.py"
  - "**/*.ts"
  - "**/*.tsx"
  - "**/*.js"
  - "**/*.jsx"
  - "**/*.java"
  - "**/src/**"
---

# Code Develop

## Transform

```text
built project -> same project with design principles and patterns soundly applied, reasoning in inline comments
```

Design and implementation reasoning lives **inline**: concepts, logic, principles, patterns. Formal API documentation is `code-document`. A principle or pattern is applied only where it fits its real purpose, never for its own sake.

## When to Use

- Apply design principles (e.g. SOLID, DRY, KISS, separation of concerns) to existing code
- Introduce or correct a design pattern (e.g. Strategy, Factory, Observer, Singleton) where its intent matches the problem
- Refactor a built project's structure while preserving behavior
- "Refactor this into a Strategy", "apply SOLID here", "clean up this module's design"

## Not This Skill

| Situation | Use instead |
|-----------|-------------|
| No project structure yet (loose code) | `code-spec` |
| Drop a snippet into an existing project | `code-migrate` |
| Formal API docs (docstrings, Javadoc, JSDoc) | `code-document` |
| Prose or Markdown files | `doc-*` |

## Scope and Position

- Default scope is an **already-built project**; apply to loose code only when explicitly requested
- Often follows `code-spec` (scaffold, then develop the design)
- Often precedes `code-migrate` (develop, then integrate the result elsewhere)

## Instructions

Pipeline: **Read -> Plan -> Write -> Verify**

### 1. Read

- Read the target area and **neighboring modules** to learn existing architecture and conventions
- Identify the design problem: responsibilities, coupling, duplication, missing extension points
- Confirm the intended principle or pattern against its official definition (`web-search`, `fetch-markdown`; search fallback per `analysis-search` rule) so usage matches purpose
- Optional: `git-history` for why the current design exists

### 2. Plan

- Run `sequentialthinking` before editing
- Select only principles and patterns whose **intent fits** the problem; reject any that add structure without benefit
- Map each pattern to concrete code changes and a numbered step sequence
- Plan a behavior-preserving path for refactors

### 3. Write

- Apply the design change incrementally, one principle or pattern at a time
- Tag each step of a pattern with a concise numbered inline comment naming the pattern and the step, for example:

```text
// [1] Singleton: define private constructor
// [2] Singleton: hold the single static instance
// [3] Singleton: expose static accessor
```

- Keep comments short and intent-focused: comment the **why**, not a restatement of the line
- Leave formal API documentation to `code-document`; do not duplicate it inline

### 4. Verify

- Run the project's tests and linter with the language's toolchain (e.g. per `execute-python` or `execute-node` rule) to confirm behavior is preserved
- Check that each numbered comment still matches the code it annotates
- Confirm the applied pattern reads as its canonical form, not a partial imitation

## MCP Servers

| Server | Tools |
|--------|-------|
| `local-filesystem` | `read_text_file`, `write_file`, `edit_file`, `search_files` |
| `sequential-thinking` | `sequentialthinking` |
| `git-history` | history/blame for existing design context |
| `web-search` | principle and pattern definitions |
| `fetch-markdown` | `fetch` |
| `large-file` | `get_file_summary`, `read_large_file_chunk` |

## Anti-Patterns

- Forcing a pattern where its intent does not match the problem (pattern for its own sake)
- Over-complicated inline comments, or comments that restate the code instead of the reasoning
- Changing behavior during a refactor without tests to prove equivalence
- Writing formal API documentation inline (belongs in `code-document`)
- Applying several patterns at once with no plan or step numbering
