# Gemini Agent Guide

This guide describes how an AI agent behaves inside this repository once the custom Gemini CLI configuration is active. The configuration spans five rule sections in `GEMINI.md`, nine skills, one hook, and ten MCP servers. Each section below maps a common interaction to the parts of the configuration that respond to it.

## How Gemini loads this configuration

Gemini CLI sources its configuration differently from an editor-based agent, so two distinctions matter.

- **Rules are concatenated into every prompt.** All rule sections live in `GEMINI.md`, which the CLI loads hierarchically and sends with every turn. The loaded context can be inspected with `/memory show` and reloaded with `/memory refresh`. There is no rules directory.
- **Skills are loaded on demand.** Each skill in `.gemini/skills/` exposes only its `name` and `description` until a request matches, at which point the full `SKILL.md` body is loaded. Skills are listed with `/skills list`. Triggering is driven entirely by the description, since Gemini skill frontmatter has no file-path field.

## Active configuration at a glance

### Rule sections (`GEMINI.md`)

| Section | Effect |
| --- | --- |
| Response Voice | Sets the formal third-person passive register for every reply |
| Search Strategy | Defines the search tier order and the handoff to research |
| Research Workflow | Triages, fetches, synthesizes, and grounds findings after a search |
| Python Execution | Routes all Python execution through `uv run` |
| Node Execution | Routes all Node tooling through `npx` |

### Skills (`.gemini/skills/`)

| Skill | Purpose |
| --- | --- |
| `code-spec` | Scaffolds loose code into an official project layout |
| `code-develop` | Applies design principles and patterns to a built project, with numbered inline comments |
| `code-migrate` | Integrates a snippet into an existing project |
| `code-document` | Adds formal API documentation such as docstrings, Javadoc, or JSDoc |
| `doc-spec` | Formats raw content into a document from an industry spec |
| `doc-migrate` | Reformats raw content to match an existing document layout |
| `doc-merge` | Combines two or more formatted documents into one |
| `md-verify` | Lints and fixes Markdown through the markdown-tools server |
| `server-test` | Starts and exercises a local server without blocking the agent loop |

### MCP servers (`.gemini/settings.json`)

| Server | Role |
| --- | --- |
| `local-filesystem` | Reads, writes, edits, and searches files |
| `git-history` | Inspects commit history and blame |
| `github` | Works with GitHub issues, pull requests, and repositories |
| `fetch` | Pulls a web page or spec as Markdown |
| `web-search` | Runs DuckDuckGo web search |
| `postgres-db` | Queries a PostgreSQL database |
| `sequential-thinking` | Structured step-by-step reasoning |
| `memory` | Stores and recalls facts across a session |
| `large-file` | Summarizes and chunks very large files |
| `markdown-tools` | Lints and fixes Markdown |

Servers are listed with `/mcp list`. Adding, renaming, or changing a server requires a CLI restart, while internal logic changes can be picked up with `/mcp reload`.

### Hook (`.gemini/settings.json`)

| Event | Command | Effect |
| --- | --- | --- |
| `BeforeAgent` | `git status --short` | The working-tree state is attached before each turn, so pending changes are always visible to the agent |

The hook panel is opened with `/hooks panel`, and a hook is toggled with `/hooks enable` or `/hooks disable`. A brand-new hook entry requires a CLI restart.

## Always-on behavior

Two parts of the configuration apply to every interaction regardless of the request.

- **Response voice.** Replies are written in a formal third-person register in the passive voice. Emoji and elaborate Unicode are avoided, scannable formatting is used only when complexity warrants it, and necessary terms are defined inline. This is set by the Response Voice section of `GEMINI.md`.
- **Working-tree awareness.** Before each turn is processed, the `BeforeAgent` hook runs `git status --short`, so the agent knows which files are modified or untracked without being told.

## Interaction scenarios

### Looking up a library, API, or standard

When current information about an API, library, or specification is needed, the Search Strategy section sets the order of search. Native and web search are tried first, MCP search fallbacks follow, and DuckDuckGo through the `web-search` server widens coverage when results are thin. Official documentation pages are opened last for verification.

When the results need real processing rather than a single fact, the Research Workflow takes over. Sources are triaged by authority and recency, the canonical page is pulled in full with `fetch`, the findings are reasoned through with `sequential-thinking`, and each claim is tied back to a source before any file is written.

Example request - "Find the current FastAPI lifespan API and update the server accordingly."

### Running Python

Any Python execution is routed through `uv` by the Python Execution rule. Scripts, tests, and tools are launched with `uv run`, and bare `python`, `python3`, or `pip` are not used. This matches the uv workspace described in the project README.

Example request - "Run the calculator tests."
Resulting command form - `uv run pytest`, or `uv run poe sync-deps` after new imports are added.

### Running Node tooling

Node-packaged binaries are run through `npx` by the Node Execution rule, so linters, type checkers, and MCP servers are resolved locally or fetched on the fly rather than assumed global.

Example request - "Lint the TypeScript files."
Resulting command form - `npx eslint .` or `npx tsc`.

### Scaffolding loose code into a project

When a loose script or snippet has no project structure yet, the `code-spec` skill is applied. The official layout for the stack is fetched, a directory tree and config are created first, and the code is placed into the correct package paths. This is the typical first step before design work.

Example request - "Turn these scripts into a proper uv package."

### Designing or refactoring a built project

When design principles or patterns are applied to an existing project, the `code-develop` skill is used. Patterns are matched to their true purpose rather than forced, refactors preserve behavior, and the reasoning is recorded as concise numbered inline comments such as the following.

```text
// [1] Strategy: define the common algorithm interface
// [2] Strategy: implement one concrete variant per behavior
// [3] Strategy: inject the chosen variant at the call site
```

This skill defaults to projects that already have structure, and it commonly runs after `code-spec` and before `code-migrate`.

Example request - "Refactor the feed parser to use the Strategy pattern."

### Integrating a snippet into the existing codebase

When a piece of code must land inside the current repository, the `code-migrate` skill is used. The snippet is formatted to match neighboring modules, placed in the right package, wired through exports and registries, and verified with the project toolchain.

Example request - "Add this handler to mcp-core like the others."

### Adding formal API documentation

When public functions, classes, or modules need official API documentation, the `code-document` skill is used. Docstrings, Javadoc, or JSDoc are added in the style of neighboring code, and behavior is left unchanged. This is distinct from `code-develop`, which writes inline reasoning rather than API contracts.

Example request - "Add docstrings to the calculator module."

### Producing or reformatting documents

Document work is split across four skills.

- Raw content with no model document is formatted from an industry spec by `doc-spec`.
- Raw content that must match an existing file's layout is handled by `doc-migrate`.
- Two or more formatted documents are combined by `doc-merge`.
- Any Markdown output is then linted and fixed by `md-verify` through the `markdown-tools` server.

Example request - "Format these notes the same way as docs/guide.md." This is handled by `doc-migrate`, then `md-verify`.

### Testing a local or MCP server

When a local server must be started and exercised, the `server-test` skill is used. The server is started in the background so the agent loop does not freeze, its logs are read to confirm it is listening, and a client such as `curl` then inspects the raw protocol. The process is terminated during cleanup. This pairs with the STDIO and SSE servers documented in the README.

Example request - "Start the SSE system-status server and verify the stream opens."

### Working with GitHub and git history

GitHub issues, pull requests, and repository data are reached through the `github` server. Local commit history and blame are read through the `git-history` server, which also supports the design and integration skills when the reason behind existing code matters.

Example request - "Summarize the open pull requests", or "Show why this function changed last."

### Querying a database

When repository data in PostgreSQL must be read or inspected, the `postgres-db` server is used. Connection details are supplied through the environment variables declared in `settings.json`.

Example request - "List the tables in the configured database and describe the feed schema."

### Handling very large files

When a file is too large to read at once, the `large-file` server provides a summary and chunked reads, so context is gathered without loading the whole file. The document skills already reach for this server on large raw input.

### Carrying context across a session

Durable facts gathered during a session are stored and recalled through the `memory` server, so repeated context does not have to be restated.

## How the pieces chain together

Several parts of the configuration are designed to run in sequence.

- **Build then design then integrate.** `code-spec` scaffolds a project, `code-develop` applies the design, and `code-migrate` integrates the result elsewhere.
- **Search then research.** The Search Strategy gathers evidence and hands off to the Research Workflow when sources conflict, versions matter, or the answer feeds writing.
- **Write then verify.** Each document skill ends by invoking `md-verify` on Markdown output.
- **Document alongside design.** `code-develop` records implementation reasoning inline while `code-document` writes the formal API surface, so the two cover different layers without overlap.

## Notes

- The execution rules assume the uv workspace and Node tooling described in the project README.
- The search and research rules favor official sources over snippets, which keeps generated changes grounded in current specifications.
- The response voice and the working-tree hook are the only parts that act on every turn. Everything else is triggered by the request, since Gemini skills are matched by description rather than by file scope.
