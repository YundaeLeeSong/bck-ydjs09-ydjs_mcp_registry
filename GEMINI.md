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
