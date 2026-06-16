---
name: doc-spec
description: >-
  Formats raw content into a document using an industry spec (GFM, CommonMark,
  LaTeX conventions). Use when input is raw or messy and there is no formatted
  document in the repo to copy layout from. Transform is raw content to one
  formatted doc. Not for raw plus formatted doc (doc-migrate) or merging
  formatted docs (doc-merge).
paths:
  - "docs/**"
  - "**/*.md"
  - "**/*.tex"
---

# Doc Spec

## Transform

```text
raw content -> one formatted doc
```

Layout rules come from an upstream industry spec, not from a file in the repo.

## When to Use

- Raw notes, dumps, or drafts -> formatted document
- Rules from GFM, CommonMark, LaTeX conventions, or org style guide
- No existing formatted document to copy layout from

## Not This Skill

| Situation | Use instead |
|-----------|-------------|
| Raw content + formatted doc | `doc-migrate` |
| Two formatted docs to combine | `doc-merge` |

## Instructions

Pipeline: **Read -> Plan -> Write -> Verify**

### 1. Read

- Read raw content: `read_text_file` or `large-file` if large (~8k+ tokens)
- Find canonical spec URL: `web-search` (e.g. `"GitHub Flavored Markdown spec"`, `"LaTeX article sectioning"`)
- Fetch spec: `fetch-markdown` -> `fetch`
- Search fallback per `analysis-search` rule: `iask-search`, `monica-search`

### 2. Plan

- Run `sequentialthinking` before body text
- Build outline and rules checklist from the fetched spec
- TOC and conventions list; no body text yet

### 3. Write

- Write formatted document section by section
- LaTeX: fetch a minimal upstream example if helpful

### 4. Verify

- Markdown: invoke `md-verify`
- LaTeX: compile or syntax-check

## MCP Servers

| Server | Tools |
|--------|-------|
| `web-search` | `web-search`, `iask-search`, `monica-search` |
| `fetch-markdown` | `fetch` |
| `sequential-thinking` | `sequentialthinking` |
| `large-file` | `get_file_summary`, `read_large_file_chunk` |
| `local-filesystem` | `read_text_file`, `write_file` |

## Anti-Patterns

- Guessing spec rules from memory instead of fetching
- Full document output without a plan
- Using spec when user pointed at a formatted doc to copy (use `doc-migrate`)
