# Cursor Setup for Gemini-to-Cursor Migration

This directory contains the modular configuration for Cursor IDE, converted from the `.gemini` and `GEMINI.md` setup.

## 1. How to use (The "Plug-in"):
1. Copy the `.cursor` folder from this directory to your project root.
2. Cursor will automatically recognize the rules in `.cursor/rules/*.mdc`.
3. Cursor will automatically trigger the automation in `.cursor/hooks.json`.

## 2. System Configuration (.json):
We maintain structured system configurations in the `.cursor/` folder for clarity and future automation:
- **`hooks.json`**: Configures active automation (e.g., the `afterFileEdit` lint check).
- **`mcp.json`**: Contains the full definitions of available MCP servers. Use this as a reference when configuring **Cursor Settings > Features > MCP**.

## 3. Automation Scripts:
- **`lint-check.js`**: Located in `.cursor/scripts/`. Handles the automated ESLint setup and verification.

## 4. Converted Rules (Behavioral .mdc):
- **project_rules.mdc**: Core execution rules (`uv`, `npx`, `git status`).
- **server_testing.mdc**: Safe server testing and protocol inspection.
- **search_strategy.mdc**: Multi-tier research hierarchy.
