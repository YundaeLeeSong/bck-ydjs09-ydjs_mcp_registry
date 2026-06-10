"""
uvx pipreqs . --force
uv add -r requirements.txt
rm requirements.txt

uv build
uv run python main.py 
uv run python main.py mcp
uv run python -m unified_mcp_app
uv run python -m unified_mcp_app mcp
"""

import sys
from unified_mcp_app.__main__ import main

if __name__ == "__main__":
    main()
    # sys.exit(main())
