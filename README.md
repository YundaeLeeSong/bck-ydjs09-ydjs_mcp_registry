# FreeCodeCamp Model Context Protocol (MCP) Tutorial

This repository contains the code and examples for the FreeCodeCamp course on Model Context Protocol (MCP). The repository is structured to provide both the course reference code and practice materials.

## Repository Structure

The repository is organized into two main sections:

### 1. MainCode/
This directory contains the original code used during the course tutorial. It includes:
- `Scenario1/`: Basic MCP calculator implementation
- `Scenario2/`: FastAPI integration with MCP
- `Scenario3/`: FreeCodeCamp RSS feed reader
- `deployment/`: Deployment configuration examples

### 2. Practice/
This directory contains tutorial-focused versions of the same code, with:
- Detailed step-by-step comments
- Comprehensive documentation
- Clear explanations of concepts
- Usage examples and instructions
Perfect for learning and experimenting on your own!

## Getting Started with MCP

To use MCP in Visual Studio Code, you need to configure it properly:

1. Create a `.vscode` folder in your project root:
```bash
mkdir .vscode
```

2. Create an `mcp.json` file inside the `.vscode` folder with this template:
```json
{
    "servers": {
        "Calculator-STDIO": {
            "command": "python",
            "args": [
                "Scenario1/fastmcp_calculator.py"
            ]
        },
        "Calculator-HTTP": {
            "command": "npx",
            "args": [
                "mcp-remote",
                "http://localhost:8002/mcp"
            ]
        }
    }
}
```

## Getting Started

1. Clone this repository
2. Set up your Python virtual environment
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Start with the Practice/ directory to learn the concepts
5. Reference MainCode/ to see the production-ready implementations

