---
inclusion: fileMatch
fileMatchPattern: "**/*.py,**/pyproject.toml,uv/**,uv.lock"
---

# Build Python

- **`uv` is used to run Python** - `uv run` is always used for scripts, tools, and tests.
  - Examples are `uv run python script.py`, `uv run pytest`, and `uv run poe sync-deps`.
  - Standard `python`, `python3`, or `pip` are never used directly, since the local environment relies on `uv` for isolated and correct dependency management.
