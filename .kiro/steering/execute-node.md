---
inclusion: fileMatch
fileMatchPattern: "**/*.js,**/*.ts,**/*.tsx,**/*.jsx,**/*.mjs,**/*.cjs,**/package.json"
---

# Execute Node

- **`npx` is used to run Node tools** - npm-packaged binaries are always prefixed with `npx`.
  - Examples are `npx eslint .`, `npx tsc`, `npx jest`, and `npx -y @modelcontextprotocol/server-filesystem`.
  - npm packages are never assumed to be installed globally. Commands are prefixed with `npx` so they run against the local `node_modules` installation or are fetched securely on the fly.
- **MCP configuration** - MCP servers in configuration json files are configured with `npx` or `uvx`, and bare package names are not used.
