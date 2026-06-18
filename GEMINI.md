# Project Agent Rules

These rules apply to every interaction in this repository. They define the response voice, the search and research workflow, and how scripts are executed. Specialized workflows are packaged as skills under `.gemini/skills/` and load on demand, so they are not repeated here.

## Response Voice

- Responses are written in the third person and the passive voice, in a formal impersonal register rather than a conversational one.
- The core takeaway is stated first, ahead of supporting detail.
- Emoji and elaborate Unicode are never used, and plain ASCII punctuation is preferred.
- Semicolons and colons are avoided within sentences. Measured transitions are allowed, for example "There are several factors to consider as follows."
- Scannable formatting such as bullets and headings is used only when complexity warrants it.
- Necessary technical terms are defined inline and immediately.

## Search Strategy

Evidence is gathered with this tier order, and the next tier is used immediately when one method fails or returns thin results.

1. **Primary** - native and web search for direct lookup and quick grounding.
2. **iask-search** - concise, fact-focused answers and rapid query iteration.
3. **monica-search** - broader synthesis, multi-model perspective, and alternative phrasing.
4. **DuckDuckGo** through the `web-search` server - broad discovery when prior tiers are thin.
5. **Source verification** - official docs and spec pages are opened and validated against before final conclusions.

The search stops once a higher-authority tier corroborates the answer. A handoff to the research workflow is made when sources conflict, versions matter, results require cross-source synthesis, or the answer feeds writing or editing. A single authoritative source that settles a simple lookup is answered directly without a handoff.

## Research Workflow

When search results need processing before action, these phases are worked in order, and a loop back is made when one exposes a gap.

1. **Triage** - results are ranked by authority (official spec over blog over tutorial over forum) and recency, duplicates are dropped, and anything still unanswered is noted.
2. **Fetch** - canonical URLs are pulled in full with `fetch`, keeping section, version, and permalink. Conclusions are never drawn from snippets alone.
3. **Synthesize** - reasoning is done with `sequential-thinking` before writing. Conflicts and version mismatches are flagged, confirmed is separated from inferred, and an outline is drafted then revised.
4. **Ground** - each claim is tied to a source and version, residual uncertainty is stated plainly, and a search tier is escalated if grounding fails.

## Python Build (`uv`)

- `uv run` is ALWAYS used to execute Python scripts, tools, and tests. Example - `uv run python script.py`, `uv run pytest`.
- `python`, `python3`, or `pip` are NEVER used directly. The workspace relies on `uv` for isolated and correct dependency management.
- This repository is a `uv` workspace. `uv sync` and `uv run --directory <path> python ...` are preferred per the project layout.

## Node Build (`npx`)

- npm-packaged binaries are ALWAYS prefixed with `npx`. Example - `npx eslint .`, `npx tsc`, `npx jest`.
- npm packages are NEVER assumed to be installed globally, so commands run against the local `node_modules` install or are fetched on the fly.
- MCP servers in configuration json files use `npx` or `uvx`, and bare package names are not used.

## Code Documentation

These rules apply across all source code, markup (XML/HTML), and SQL files.

- **Two Audiences:** Maintainer comments go directly in the source or config above the code they explain. Consumer documentation (usage, public API contracts, run instructions, published schemas) goes in `README.md`, `docs/`, or language-standard API doc formats (Javadoc, JSDoc, OpenAPI, etc.).
- **Maintainer Comments:** Only ASCII characters are used. Block comments are placed directly above the related code.
  - Format: `[Label]` on its own line, followed by a blank line, then a multi-line explanation without semicolons.
  - Inline concept names: A short concept name is added on each related code line (e.g., `// JUnit`, `<!-- setting -->`, `-- user id`).
  - `[Past version]`: For replaced code, past lines are listed first (with inline concept names), a blank line, then the explanation. Active lines follow with the same concept name.
  - One-line notes are permitted using the file type's line comment syntax or short block syntax (e.g., `// [Label] short note`, `<!-- [Label] short note -->`, `-- [Label] short note`).
- **Public API Docs:** The language's standard doc format (Javadoc, KDoc, docstrings, etc.) is used on exported or callable APIs only, including a summary and standard tags (`@param`, `@returns`). Maintainer essays or run instructions are never put in public API docs or user-facing pages.
- **When Editing:** The smallest change that solves the task is made. Existing naming, layout, indentation, and comment style are matched.

## LaTeX Exam Conventions

Applies when editing `.tex` files that use the `exam` document class.

- **Question Types:**
  - **MCQ:** `\CorrectChoice` is used on the right option. Answers are provided in a `\begin{solution}...\end{solution}` block *after* `\begin{choices}`.
  - **FRQ (student writes work):** `\begin{solutionorbox}[height]` is used with the key inside.
  - **FRQ / narrative:** No box is used; prose or `\begin{itemize}` is put in the question.
- **Layout:** For MCQs, the order is: stimulus (table, listing, diagram, prose), then choices, then a short solution. For CS/REST styles, `\begin{lstlisting}[style=http]`, four choices, and a one-paragraph solution are used. For FRQs with parts, `\begin{enumerate}` is used with `\renewcommand{\labelenumi}{(\alph{enumi})}`.
- **Listings and Images:**
  - Block: `\begin{lstlisting}[style=java]` (or `http`, `json`, `pseudo`, etc.) is used. Custom environments like `cspcode` are not used.
  - Inline: `\lstinline[style=javainline]|...|` or bare `\lstinline` is used if Java is default.
  - Images: Placed per module (`{module}/images/...`), not in a shared hub.
- **Restrictions:** `solutionorbox` is not used on MCQs. `\begin{solution}` is not used where the student must show written work (`solutionorbox` is used instead).
