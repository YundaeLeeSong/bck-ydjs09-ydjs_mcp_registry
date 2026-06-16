---
name: doc-migrate
description: >-
  Reformats raw content to match an existing formatted document's layout. Use
  when the user has raw or messy content plus a formatted file to copy layout
  from. Transform is raw content plus formatted doc to one formatted doc. Not
  for raw-only (doc-spec) or merging two formatted docs (doc-merge).
---

# Doc Migrate

## Transform

```text
raw content + formatted doc -> one formatted doc
```

Raw content keeps its meaning. Output uses the formatted doc's layout (headings, spacing, structure). Do not copy the formatted doc's text.

## When to Use

- User has **raw content** and a **formatted doc** that defines target layout
- "Make this raw data look like `guide.md`"
- "Format my notes the same way as `docs/module/01-intro.tex`"

## Not This Skill

| Situation | Use instead |
|-----------|-------------|
| Raw content only, no formatted doc | `doc-spec` |
| Two formatted docs to combine | `doc-merge` |

## Instructions

Pipeline: **Read -> Plan -> Write -> Verify**

### 1. Read

- Read the **formatted doc** first (`read_text_file`) - layout to copy
- Then read **raw content** (`read_text_file` or `large-file` if large)
- Large raw input (~8k+ tokens): `large-file` -> `get_file_summary`, `read_large_file_chunk`, `search_in_large_file`

### 2. Plan

- Run `sequentialthinking` before body text
- Extract layout rules from the formatted doc: headings, punctuation, spacing, line breaks, tables, LaTeX environments
- Map raw segments to sections
- No reformatted prose in this step

### 3. Write

- Reformat raw content section by section
- Formatted doc wins over markdownlint defaults

### 4. Verify

- Markdown: invoke `md-verify` (keep formatted doc layout if lint conflicts)
- LaTeX: compile or syntax-check

## MCP Servers

| Server | Tools |
|--------|-------|
| `local-filesystem` | `read_text_file`, `write_file` |
| `large-file` | `get_file_summary`, `read_large_file_chunk`, `search_in_large_file` |
| `sequential-thinking` | `sequentialthinking` |

## Anti-Patterns

- Reading raw content before the formatted doc
- Outputting the full document without a plan
- Using migrate when there is no formatted doc (use `doc-spec`)
