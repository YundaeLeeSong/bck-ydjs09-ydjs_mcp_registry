# Gemini CLI: The AI Agent's Advanced Architecture

This document serves as a comprehensive reference for the advanced features of the Gemini CLI AI Agent. While you can interact with the agent using natural language and basic commands, understanding these underlying systems allows you to customize, steer, and automate the agent's behavior to fit complex enterprise workflows.


# Gemini CLI Component Cheatsheet

Quick-reference mapping of list and refresh commands inside the Gemini CLI session workspace (`REPL`).

| Component | List Command | Refresh Command | Storage Location | Restart Required? |
| :--- | :--- | :--- | :--- | :--- |
| **MCPs** | `/mcp list` | `/mcp reload` | `settings.json` | **Yes**, for adding/removing/renaming servers. |
| **Skills** | `/skills list` | `/skills reload` | `.gemini/skills/` | No. Reloads `SKILL.md` logic instantly. |
| **Hooks** | `/hooks panel` | `/hooks enable/disable` | `settings.json` | **Yes**, for entirely new hook entries. |
| **Specs & Steerings** | `/memory show` | `/memory reload` | `GEMINI.md` / `*.md` | No. Instant update on reload. |

---

## 1. Instruction Files (`GEMINI.md`)

Instruction files are plain-text markdown files used to define the core "Employee Handbook" for the AI. They dictate architectural rules, coding conventions, and project-specific workflows.

### What it looks like
```markdown
# UI Component Guidelines
- Always use React Functional Components.
- NEVER use inline styles; always use Tailwind CSS utility classes.
- Use `lucide-react` for all icons.

# Testing Workflow
To run unit tests for a specific file, use: `npm run test -- <filename>.test.ts`
```

### Where it is saved
*   **Locally (Project-Wide):** `[Project Root]/GEMINI.md`
    *   *Effect:* Applies to the entire repository. Should be committed to Git.
*   **Locally (Directory-Scoped):** `[Project Root]/src/components/GEMINI.md`
    *   *Effect:* Applies *only* when the agent is working inside the `src/components/` folder.
*   **Globally (Personal):** `~/.gemini/GEMINI.md` (e.g., `C:\Users\username\.gemini\GEMINI.md` on Windows)
    *   *Effect:* These are your cross-project personal preferences (e.g., "I always prefer Python over Go"). They follow you into every workspace on your machine.

Note: *Gemini CLI uses a hierarchical context system. It automatically traverses upwards from your current working directory to find and load GEMINI.md files until it hits a boundary marker (**like a .git folder**) or your user home directory.*

---

## 2. Model Context Protocol (MCP)

MCPs are external tools and services (Databases, Web Search, GitHub, Browsers) that the AI can interact with. Because these servers run as independent subprocesses, their configuration has a specific lifecycle.

### Lifecycle: Restart vs. Reload
When you modify MCP settings in `settings.json`, you must distinguish between updating **logic** and updating **configuration**.

| Action | Operation | Why? |
| :--- | :--- | :--- |
| **Add a new server** | **Full CLI Restart** | The CLI must spawn a new subprocess during the startup discovery phase. |
| **Rename a server** | **Full CLI Restart** | Tool-to-server mapping happens once at boot. |
| **Change `args` or `env`** | **Full CLI Restart** | Arguments are passed to the process at the moment of instantiation. |
| **Update `mcp.allowed`** | **Full CLI Restart** | Security allowlists are parsed once for safety. |
| **Update server logic** | `/mcp reload` | Use this if you are developing a server and changed its internal tool definitions, but the server name/command remains the same. |

### Where it is saved
MCP servers are defined in the `mcpServers` block of your `settings.json`:
*   **Globally:** `~/.gemini/settings.json`
*   **Locally:** `[Project Root]/.gemini/settings.json`

---

## 3. Hooks

Hooks are executable scripts (Bash, Python, Node, PowerShell, etc.) that the CLI runs automatically before or after the AI generates a response. They act as dynamic context injectors, allowing the AI to "see" the real-time state of your environment without you having to copy-paste terminal output.

### ⚠️ Best Practice: Read-Only Context Injection
Hooks run on **every single conversational turn**. Therefore, they should be strictly **read-only**. 
- **DO:** Use hooks to read git status, check linting errors, tail logs, or fetch the current date.
- **DO NOT:** Use hooks to mutate state, install dependencies, download files, or auto-install `.skill` files. Modifying your system state on every AI response will destroy performance and lead to unpredictable bugs.

### What it looks like
You define hooks in your `settings.json` file. Hooks are organized by execution stage (e.g., `BeforeAgent`) and can use matchers to target specific files or conditions.

**`[Project Root]/.gemini/settings.json`**
```json
{
  "hooks": {
    "BeforeAgent": [
      {
        "matcher": "*",
        "hooks": [
          {
            "name": "Git Status",
            "type": "command",
            "command": "git status --short"
          },
          {
            "name": "Intelligent Lint Check",
            "type": "command",
            "command": "node .gemini/hooks/lint-check.js"
          }
        ]
      }
    ]
  }
}
```

#### Why use a script for hooks?
1.  **Cross-Platform Reliability**: Shell operators like `&&` or `;` behave differently on Windows vs. Linux. A Node or Python script ensures the hook works everywhere.
2.  **Idempotency**: A script can intelligently check if dependencies (like ESLint) are installed and only install them once, keeping subsequent conversational turns fast.
3.  **Complex Logic**: You can add "ignores," custom globals, and fallback configurations that would be impossible to maintain in a single-line shell command.

*When the AI reads the context, it receives the output wrapped in `<hook_context>` tags automatically.*

### Where it is saved
Hooks are configured in your `settings.json` file:
*   **Globally:** `~/.gemini/settings.json` (Runs on every project on your machine)
*   **Locally:** `[Project Root]/.gemini/settings.json` (Runs only in this specific project)

### Refreshing Hooks
While the Gemini CLI uses a file watcher to pick up changes to existing hook logic or enable/disable states automatically:
*   **Toggle State:** Use `/hooks enable <name>` or `/hooks disable <name>` for immediate control.
*   **New Hooks:** Adding an **entirely new hook entry** to `settings.json` requires a complete session restart for the CLI to register the new hook into the execution pipeline.

---

## 4. Skills

Skills are highly specialized, pre-packaged expert workflows. While `GEMINI.md` provides general rules, a Skill provides deep, procedural expertise on a specific framework, tool, or complex task. The agent must explicitly "activate" a skill using a tool call (`activate_skill`) when it recognizes the task requires it.

Skills are built for reuse and efficiency. Instead of placing massive workflow instructions in `GEMINI.md` (which the AI must read on *every* turn, wasting context), you package them into a Skill. The AI only loads the Skill's instructions when the user's request triggers the Skill's description.

### Directory Structure of a Skill
When creating a custom skill, you structure it like this:

```text
my-custom-workflow/
├── SKILL.md                 # REQUIRED: The core metadata and instructions
├── scripts/                 # OPTIONAL: Executable scripts the AI can run
│   └── format_data.py
├── references/              # OPTIONAL: Deep documentation the AI can read
│   └── api_schema.md
└── assets/                  # OPTIONAL: Templates or files the AI can copy
    └── component_template.tsx
```

### What the files look like

**1. `SKILL.md` (The core file)**
This file requires a YAML frontmatter header so the AI knows *when* to trigger it, followed by the instructions.
```markdown
---
name: my-custom-workflow
description: Use when the user asks to format a dataset or create a new React component using the company's internal templates.
---

# Instructions
1. First, check if the user wants to format data or create a component.
2. If formatting data, run the `scripts/format_data.py` script.
3. If creating a component, copy the file from `assets/component_template.tsx`.
4. If you need to understand our API, read `references/api_schema.md`.
```

**2. `scripts/`**
Contains executable code (Python, Bash, Node). The AI can run these directly using its shell tools without needing to read the code into its "brain," saving massive amounts of context.

**3. `references/`**
Contains dense documentation. The AI will use its file-reading tools to open these *only if it decides it needs more detail*. This keeps `SKILL.md` lightweight.

**4. `assets/`**
Contains boilerplate code, images, or configuration files that the AI can copy into your project.

### Installation & Storage

Gemini CLI automatically detects skills by scanning specific hidden directories at the start of a session. You do not need to pack, compile, or use installation commands; you can simply place the raw skill folder (containing the `SKILL.md` and optional folders) into the appropriate location.

*   **Workspace Scope (Current Project Only):**
    Place the skill folder in `[Project Root]/.gemini/skills/`.
    *Effect:* Automatically loads for anyone working in this specific repository. Committing this `.gemini/skills/` folder to Git is the recommended way to share workflows with your team, as it requires zero setup.
*   **User Scope (Global across all projects):**
    Place the skill folder in `~/.gemini/skills/` (e.g., `C:\Users\username\.gemini\skills\` on Windows).
    *Effect:* Automatically loads for you across every project on your machine.

---

## 5. Specs / Steering Files

Unlike the other features which are configurations, "Specs" (Specifications) or "Steering files" are simply a workflow methodology. It refers to writing a detailed plan document that "steers" the AI to build something exactly as you envision it, rather than letting the AI guess your architecture.

### What it looks like
It is a highly detailed markdown file outlining a feature request.

**`feature-login-spec.md`**
```markdown
# Feature: OAuth Login System

## Goal
Implement a Google OAuth login flow using NextAuth.js.

## Requirements
1. Use the `@auth/core` package.
2. The login button must be placed in `src/components/Header.tsx`.
3. Upon successful login, redirect the user to `/dashboard`.
4. Ensure the session token is securely stored in an HttpOnly cookie.

## Out of Scope
- Do not implement Apple or Github login at this time.
- Do not build the `/dashboard` page itself.
```

### Where it is saved
*   **Locally:** Anywhere in your project! (e.g., `docs/specs/login-spec.md` or just in the root).
*   **How to use it:** You simply tell the AI: *"Please implement the feature described in `docs/specs/login-spec.md`."* The AI will read the spec and execute the plan exactly as written.