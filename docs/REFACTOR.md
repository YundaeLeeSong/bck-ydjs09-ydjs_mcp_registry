Including the [build-system] table tells Python build frontends (like uv or pip) how to package your project. When using hatchling, it automatically detects your src/ layout by default so that your source code stays clean and separated from configuration files.

Since you are using the src/ layout with hatchling, we just need to make sure your package directories inside src/ match your project names.

Here is the updated, unified guide reflecting your hatchling setup.

1. Updated Directory Structure
Notice how both app and libs/core-lib use the src/ layout. The folder inside src/ must be a valid Python package name (using underscores instead of dashes).

Plaintext
my-workspace/
├── pyproject.toml         # Root workspace config
├── uv.lock                # Shared lockfile
├── .venv/                 # Shared virtual environment
│
├── app/                   # Main Entry Point Application
│   ├── pyproject.toml
│   └── src/
│       └── app/           # Package name matches project name
│           └── main.py
│
└── libs/
    └── core-lib/          # Shared Library
        ├── pyproject.toml
        └── src/
            └── core_lib/  # Package name (uses underscore)
                └── utils.py
2. Updated File Configurations
Step A: Root Workspace (my-workspace/pyproject.toml)
This remains the master controller telling uv where to find your sub-projects.

Ini, TOML
[tool.uv.workspace]
members = ["app", "libs/*"]
Step B: Shared Library (my-workspace/libs/core-lib/pyproject.toml)
Here, we add your hatchling build system. Because Hatchling looks inside src/ by default, it will find the core_lib directory automatically.

Ini, TOML
[project]
name = "core-lib"
version = "0.1.0"
description = "Shared utilities using hatchling"
dependencies = []

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
Step C: Main Application (my-workspace/app/pyproject.toml)
Your entry point app also uses hatchling and explicitly lists core-lib as a dependency fetched straight from the workspace.

Ini, TOML
[project]
name = "app"
version = "0.1.0"
description = "Main application entry point"
dependencies = [
    "core-lib", 
]

[tool.uv.sources]
core-lib = { workspace = true }

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
3. Writing and Importing the Code
Because Hatchling maps the src/ directory, your import statements will ignore the src folder entirely and start directly with the package name.

In your library:

Python
# my-workspace/libs/core-lib/src/core_lib/utils.py
def get_welcome_message():
    return "Hello from the hatchling-powered core library!"
In your main application:

Python
# my-workspace/app/src/app/main.py
# The IDE will resolve this perfectly with Workspace Mode enabled
from core_lib.utils import get_welcome_message

def run():
    print(f"App started: {get_welcome_message()}")

if __name__ == "__main__":
    run()
4. Syncing and Running
Run your sync command at the root of your workspace:

Bash
uv sync
uv will scan both folders, see they both use hatchling to parse the src/ directory, and install them into the root .venv.

When you turn on Workspace Mode in the IDE, it reads these exact configurations, maps the paths through hatchling's structure, and links your cross-project code seamlessly.