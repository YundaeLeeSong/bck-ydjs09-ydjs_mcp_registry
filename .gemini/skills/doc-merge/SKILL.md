---
name: doc-merge
description: >-
  Combines two or more formatted documents into one formatted document. Use when
  both inputs are already formatted (README plus guide, draft plus appendix).
  Transform is formatted doc A plus formatted doc B to one formatted doc. Not
  for raw content (use doc-spec or doc-migrate).
---

# Doc Merge

## Transform

```text
formatted doc A + formatted doc B -> one formatted doc
```

## When to Use

- Combine two or more **already formatted** documents into one file
- README + guide, draft + appendix, old + new version

## Not This Skill

| Situation | Use instead |
|-----------|-------------|
| Raw content only | `doc-spec` |
| Raw content + formatted doc | `doc-migrate` |

## Instructions

Pipeline: **Read -> Plan -> Write -> Verify**

### 1. Read

- `local-filesystem` -> `read_multiple_files` or sequential `read_text_file`
- Per source: title, heading tree, macros/environments, link scheme

### 2. Plan

- Run `sequentialthinking` before any merged prose
- Agree on one layout: heading levels, duplicate sections, terminology, cross-references, front matter
- Output of this step is a merge plan, not merged text

### 3. Write

- Write one combined document, section by section
- Do not dump the full merge in one shot

### 4. Verify

- Markdown: invoke `md-verify`
- LaTeX: compile or syntax-check

## MCP Servers

| Server | Tools |
|--------|-------|
| `local-filesystem` | `read_multiple_files`, `read_text_file`, `write_file` |
| `sequential-thinking` | `sequentialthinking` |

## Anti-Patterns

- Merging without reading all sources first
- Writing merged text before the merge plan exists
- Using merge when inputs are raw (use `doc-spec` or `doc-migrate`)
