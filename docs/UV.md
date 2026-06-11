# UV Workspace Maintenance and Dependency Management

This document explains how the workspace manages dependencies, specifically focusing on isolated maintenance scripts and local source resolution.

## 1. Isolated Maintenance Scripts (PEP 723)

The script located at `uv/pipreqs.uv.py` uses **PEP 723 Inline Script Metadata**. This allows the script to declare its own dependencies independently of the project's `pyproject.toml`.

### How it works
At the top of the script, you will see:
```python
# /// script
# dependencies = ["tomlkit"]
# ///
```

When you run this script using `uv run uv/pipreqs.uv.py`, `uv` performs the following actions:
1. **Transient Environment**: It creates a temporary, isolated virtual environment specifically for this execution.
2. **On-the-fly Installation**: It installs `tomlkit` (and any other declared dependencies) into that temporary environment.
3. **Zero Clutter**: These dependencies are **not** added to your project's `pyproject.toml` or your main `.venv`. Once the script finishes, the environment is managed by `uv`'s cache and does not affect your development setup.

## 2. Smart Dependency Discovery (`uvx pipreqs`)

The maintenance script automates dependency discovery using `pipreqs`. Instead of installing `pipreqs` as a project dependency, we use `uvx`:

```python
subprocess.run(["uvx", "pipreqs", ...])
```

- **`uvx`** is the `uv` equivalent of `npx`. It downloads and runs a tool in a temporary environment.
- This keeps your development environment clean of "utility" tools that aren't part of your application's runtime.

## 3. Local Source Isolation and Resolution

In a `uv` workspace, members often depend on each other (e.g., `app-api-feed` depends on `mcp-core`). `uv` handles this through the `[tool.uv.sources]` table in the sub-project's `pyproject.toml`.

### Resolution Logic
When the maintenance script runs `uv add --package <member-name> -r requirements.txt`:
1. **Workspace Check**: `uv` first checks if any of the discovered imports (like `mcp_core`) correspond to a member already defined in the workspace.
2. **Source Mapping**: It uses the mapping in `pyproject.toml`:
   ```toml
   [tool.uv.sources]
   mcp-core = { workspace = true }
   ```
3. **Isolation**: Because `uv` is "Workspace Aware," it knows that `mcp-core` is a local directory, not a package to be downloaded from PyPI. This prevents version conflicts and ensures you are always coding against your local changes.

## 4. Automation with `poethepoet`

To simplify these operations, we use `poethepoet` (aliased as `poe`) as a task runner.

### Running the Sync
```bash
uv run poe sync-deps
```

This task is defined in the root `pyproject.toml` and triggers the isolated Python script, which in turn orchestrates the entire workspace dependency synchronization.
