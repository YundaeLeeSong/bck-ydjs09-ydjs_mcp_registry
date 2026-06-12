#!/bin/bash
# -----------------------------------------------------------------------------
# SKILL: register_dependency.sh
# DESCRIPTION: Grants the AI agent a safe mechanism to recompile imports
#              adhering to the pipreqs constraint stated in tech.md.
# -----------------------------------------------------------------------------
set -e

echo "[SKILL] Recalculating project dependencies via pipreqs..."
pipreqs . --force --ignore .kiro,venv
echo "[SKILL] Requirements files normalized successfully."