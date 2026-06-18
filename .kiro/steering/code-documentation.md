---
inclusion: fileMatch
fileMatchPattern: "**/*.c,**/*.h,**/*.cpp,**/*.cc,**/*.cxx,**/*.java,**/*.kt,**/*.kts,**/*.scala,**/*.groovy,**/*.gradle,**/*.vb,**/*.py,**/*.pyw,**/*.pyi,**/*.rb,**/*.php,**/*.js,**/*.jsx,**/*.mjs,**/*.cjs,**/*.ts,**/*.tsx,**/*.mts,**/*.cts,**/*.go,**/*.rs,**/*.swift,**/*.dart,**/*.lua,**/*.pl,**/*.pm,**/*.r,**/*.R,**/*.asm,**/*.cmake,**/*.awk,**/*.css,**/*.scss,**/*.sass,**/*.sh,**/*.bash,**/*.zsh,**/*.ps1"
---

# Code documentation

## Two audiences

- **Maintainers** — comments in source/config, directly above the code they explain.
- **Consumers** — official API docs on public surface; README or docs/ for how to run and use the project.

Do not put run instructions in source comments. Do not put maintainer notes in public API docs.

## Maintainer block comments

Place a block directly above the related code. Put `[Label]` on its own line, then a short plain explanation (what, when it matters, one example if needed).

Use this file type's native block delimiter (`/* */`, `{- -}`, `--[[ ]]`, etc.). Example (C-family):

```
/*
 * [Label]
 * Explanation here.
 */
```

Line comments (`//`, `#`, `--`, `;`, `%`, `!`, `::`, `REM`) are for single-line maintainer notes only, not multi-line explanations.

## Public API docs

Use this language's standard doc format on exported or callable API only (Javadoc, KDoc, JSDoc, TSDoc, rustdoc, XML doc, etc.). Include a summary; add `@param`, `@returns`, `@author`, `@since` when the project already uses them.

## When editing

- Smallest change that solves the task.
- Match existing naming, layout, and comment style in the file.
