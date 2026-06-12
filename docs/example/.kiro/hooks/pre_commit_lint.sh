#!/bin/bash
# -----------------------------------------------------------------------------
# HOOK: pre_commit_lint.sh
# DESCRIPTION: Automates systemic checking against the structure.md manifesto.
#              Rejects changes if the agent utilizes forbidden patterns.
# -----------------------------------------------------------------------------
set -e

echo "[HOOK] Inspecting structural system integrity..."

# Search files for forbidden relative module paths
if grep -q "from \.\." src/**/*.py 2>/dev/null; then
    echo "[ERROR] Architectural violation: Relative imports detected!"
    echo "[ERROR] System constraints defined in structure.md explicitly ban relative paths."
    exit 1
fi

echo "[HOOK] Integrity validations passed. Workspace state conforms to standards."