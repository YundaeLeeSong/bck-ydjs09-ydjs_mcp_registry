---
description: Partitions a large markdown document (like a comprehensive study note) into smaller, logically grouped, and sequentially numbered markdown files while preserving all formatting.
---

# Workflow: edu01-document-partition

## Core Principle: Context Preservation
> [!IMPORTANT]
> **Zero-Destructive Editing:** During any partitioning or extraction phase, you must ensure a reasonable level of modification that **minimizes the dramatic deletion of existing contexts**. Do not outright delete legacy or pre-existing theoretical explanations; instead, preserve the historical or broader context of the document.

> [!IMPORTANT]
> **Unconditional Deep Processing:** To handle massive source files securely without token limits, you MUST use the `large-file` MCP (e.g., `read_large_file_chunk`, `get_file_structure`) and the `sequential-thinking` MCP for deep processing **every single time**, regardless of your assumptions about the file size. This guarantees exhaustive context extraction and safe file handling.

## Trigger
Use this workflow when requested to "partition", "split", or "break down" a large markdown file.

## Steps

1. **Analyze the Source Document**:
   - Use the `large-file` MCP to read the target markdown file (e.g., `original-doc.md`) to safely process the entire structure without truncation.
   - Use `sequential-thinking` to systematically identify the main top-level headers (`#` or `##`) that represent distinct topics or chapters.
   
2. **Determine the Partitions**:
   - Group the content into logical sections (e.g., Core, Components, Templates, Services, etc.).
   - Assign a sequential numbering scheme and a descriptive topic name to each partition.

3. **Establish Naming Convention**:
   - Use the prefix of the original file or the main topic.
   - Example format: `[topic][number]-[subtopic].md` (e.g., `topic01-core.md`, `topic02-components.md`).

4. **Extract and Write Content**:
   - Extract the full, exact content for each identified section without summarizing or truncating.
   - Write each extracted section into its respective new `.md` file in the same directory.
   - Ensure that the original markdown structure, code blocks, tables, and links are fully preserved.

5. **Verify**:
   - Check that all original content has been accurately distributed among the new files.
   - Confirm that the files follow the defined naming convention.
   - Validate that no markdown formatting was broken during the split.

## Required MCP Servers & Tools
| Server / Tool | Purpose |
|---------------|---------|
| `large-file` | Safely reading and navigating massive markdown documents without context truncation. |
| `sequential-thinking` | Systematically managing the partition mapping logic. |
| Native File Tools | Writing the partitioned files to the disk. |
