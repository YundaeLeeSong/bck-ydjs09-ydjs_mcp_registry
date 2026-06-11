# /// script
# dependencies = ["tomlkit"]
# ///
"""
Maintenance script to automatically discover and sync dependencies across the uv workspace.

This script performs the following steps:
1. Identifies all workspace members from the root 'pyproject.toml'.
2. Iterates through each member and scans its 'src/' directory using 'pipreqs'.
3. Discovers third-party imports and creates a temporary requirements file.
4. Uses 'uv add --package' to update each member's 'pyproject.toml'.
5. Cleans up temporary files.

The script uses PEP 723 inline metadata to define its own dependencies,
ensuring it runs in an isolated environment without affecting the workspace.
"""

import os
import subprocess
from pathlib import Path
import tomlkit

def run_uv(args: list[str], cwd: Path = None):
    """
    Executes a uv command with the given arguments.
    
    Args:
        args: List of command line arguments for uv.
        cwd: Optional directory to run the command in.
    """
    subprocess.run(["uv"] + args, cwd=cwd, check=True)

def main():
    """
    Main execution logic for the dependency synchronization script.
    """
    root_dir = Path.cwd()
    root_toml_path = root_dir / "pyproject.toml"
    
    if not root_toml_path.exists():
        print("[ERROR] Run this script from the workspace root.")
        return

    # Load root workspace configuration
    try:
        root_toml = tomlkit.parse(root_toml_path.read_text())
    except Exception as e:
        print(f"[ERROR] Failed to parse {root_toml_path}: {e}")
        return

    members_patterns = root_toml.get("tool", {}).get("uv", {}).get("workspace", {}).get("members", [])
    
    # Resolve all member directories based on glob patterns in pyproject.toml
    member_dirs = []
    for pattern in members_patterns:
        member_dirs.extend([p.parent for p in root_dir.glob(f"{pattern}/pyproject.toml")])

    if not member_dirs:
        print("[INFO] No workspace members found.")
        return

    print(f"[INFO] Found {len(member_dirs)} workspace members. Starting dependency sync...")

    for member_dir in member_dirs:
        member_rel = member_dir.relative_to(root_dir)
        print(f"\n[MEMBER] Processing: {member_rel}")
        
        src_path = member_dir / "src"
        if not src_path.exists():
            print(f"  [SKIP] No 'src' directory found in {member_rel}")
            continue
        
        # Discover dependencies using pipreqs via 'uvx'
        # uvx runs the tool in a transient environment without installing it project-wide
        req_file = member_dir / "requirements_tmp.txt"
        print(f"  [EXEC] Scanning imports in {src_path}...")
        
        try:
            subprocess.run(
                ["uvx", "pipreqs", str(src_path), "--force", "--savepath", str(req_file)],
                check=True,
                capture_output=True
            )
        except subprocess.CalledProcessError as e:
            if b"No imported modules found" in e.stderr:
                print(f"  [INFO] No third-party imports found in {member_rel}.")
            else:
                print(f"  [ERROR] pipreqs failed: {e.stderr.decode()}")
            if req_file.exists(): req_file.unlink()
            continue

        if not req_file.exists() or req_file.stat().st_size == 0:
            print(f"  [INFO] No new dependencies discovered for {member_rel}.")
            if req_file.exists(): req_file.unlink()
            continue

        # Extract project name to target the correct workspace member
        try:
            pkg_toml = tomlkit.parse((member_dir / "pyproject.toml").read_text())
            pkg_name = pkg_toml.get("project", {}).get("name")
        except Exception as e:
            print(f"  [ERROR] Failed to parse {member_dir}/pyproject.toml: {e}")
            req_file.unlink()
            continue
        
        if not pkg_name:
            print(f"  [ERROR] Missing 'project.name' in {member_rel}/pyproject.toml")
            req_file.unlink()
            continue

        # Update the specific member's pyproject.toml and the root uv.lock
        print(f"  [EXEC] Updating dependencies for package: {pkg_name}...")
        try:
            run_uv(["add", "--package", pkg_name, "-r", str(req_file)])
            print(f"  [SUCCESS] {pkg_name} dependencies synchronized.")
        except subprocess.CalledProcessError as e:
            print(f"  [ERROR] Failed to add dependencies for {pkg_name}: {e}")
        
        # Cleanup temporary files
        if req_file.exists():
            req_file.unlink()

    print("\n[COMPLETE] Workspace dependency synchronization finished.")

if __name__ == "__main__":
    main()
