---
name: md-verify
description: >-
  Lints and fixes Markdown via the markdown-tools MCP server
  (@dougis/markdown-lint-mcp). Use after doc-merge,
  doc-migrate, or doc-spec Write step, or when the user asks to lint, fix, or
  validate Markdown. Calls lint_markdown and fix_markdown.
paths:
  - "**/*.md"
---

# Markdown Verify

## When to Use

- After the Write step of `doc-merge`, `doc-migrate`, or `doc-spec`
- User asks to lint, fix, or validate Markdown
- Before declaring documentation work complete

## Instructions

### 1. Lint

Call `lint_markdown` on the output file. Review rule IDs and line numbers.

### 2. Fix

Call `fix_markdown` for auto-fixable issues. Write results back via `local-filesystem` or editor tools.

### 3. Re-lint

Repeat until clean or only intentional warnings remain.

### doc-migrate note

When `doc-migrate` output intentionally diverges from markdownlint, keep the formatted doc's layout and note the exception.

## MCP Servers

`markdown-tools` - `lint_markdown`, `fix_markdown`, `get_configuration`
