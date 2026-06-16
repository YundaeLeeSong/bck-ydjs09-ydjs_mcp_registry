---
inclusion: fileMatch
fileMatchPattern: "docs/**,**/*.md,**/*.tex"
---

# Analysis Research

Research synthesis workflow that runs after `analysis-search` to triage results, fetch canonical sources, reason with sequential-thinking, and ground claims. Use when investigating specs, APIs, or standards before writing or editing documentation.

Research runs after `analysis-search`, where search gathers and research reasons. The phases are worked in order, and a loop back is made when one exposes a gap.

1. **Triage** - Results are ranked by authority (official spec > blog > tutorial > forum) and recency, duplicates are dropped, and anything still unanswered is noted.
2. **Fetch** - Canonical URLs are pulled in full via `fetch`, with section, version, and permalink kept. Conclusions are never drawn from snippets alone.
3. **Synthesize** - `sequential-thinking` is run before writing, so conflicts and version mismatches are flagged, confirmed is separated from inferred, and an outline is drafted and revised.
4. **Ground** - Each claim is tied to a source and version, residual uncertainty is stated plainly, and a loop back or a search-tier escalation is made if grounding fails.
