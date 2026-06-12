# Project Structure

## Layout Mapping
* `src/core/`: Security engines, global cryptographic filters, and validation setups.
* `src/mcp_server/`: Service endpoints and runtime lifecycle registration blocks.
* `.kiro/skills/`: Shell utilities giving the agent authorization to run explicit tool routines.
* `.kiro/hooks/`: Interceptor hooks validating structural states before task confirmation.

## Coding Style Directives
* **Naming Structures:** Enforce pure snake_case configuration for modules and local metrics.
* **Module Paths:** Use absolute module notation relative to `src/`. Relative import pathways (`from ..core import`) are explicitly banned.
* **Documentation Constraints:** Every independent module must present a clear docstring establishing operational scope.