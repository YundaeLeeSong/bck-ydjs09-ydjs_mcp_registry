---
inclusion: fileMatch
fileMatchPattern: "**/*.html,**/*.htm,**/*.xhtml,**/*.xml,**/*.xsd,**/*.xsl,**/*.targets,**/*.config,**/*.manifest,**/*.xaml,**/*.sitemap"
---

# Markup documentation

## Two audiences

- **Maintainers** — XML/HTML comments directly above the element or block they describe.
- **Consumers** — project README or docs/ for usage; schema docs for public contracts when this repo publishes them.

Do not put maintainer essays in user-facing pages. Do not put run instructions inside markup files.

## Maintainer block comments

Use `<!-- ... -->`. Put `[Label]` on its own line inside the comment, then a short explanation.

```xml
<!--
  [Label]
  What this element or block does and when to change it.
-->
```

For one-line notes only, `<!-- [Label] short note -->` is acceptable.

## Public documentation

HTML/XML rarely use Javadoc-style API docs. Document public structure in README, OpenAPI, XSD annotations, or external specs—not inline maintainer comments.

## When editing

- Smallest change that solves the task.
- Match existing indentation and comment style in the file.
