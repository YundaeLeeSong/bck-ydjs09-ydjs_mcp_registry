---
description: Typesets any text source—including raw notes, formatted markdown, or emails—into a structured and highly readable LaTeX document adhering to strict voice and formatting standards.
---

# Workflow: edu10-tex-typeset

## Trigger
Use this workflow when requested to "typeset", "format", or "proofread" text into a LaTeX document. **Source Input Flexibility:** The source material is not restricted to raw text. Any non-tex file, including formatted Markdown files, plain unformatted text, or emails, can and should be treated as a valid "source" to generate or proofread the resulting `.tex` file.

## Core Rules & Formatting Standards

> [!IMPORTANT]
> **Tone & Voice (GEMINI Customization):** 
> - Output documents must be written in the **third person and passive voice**.
> - Maintain a **formal, impersonal register** (avoid conversational language).
> - State the **core takeaway first**, followed by supporting details.
> - **Never** use emojis or elaborate Unicode; strictly prefer plain ASCII punctuation.
> - **Avoid** semicolons and colons within sentences. Use measured transitions (e.g., "There are several factors to consider as follows.").
> - Define technical terms inline and immediately.

> [!IMPORTANT]
> **Scannability & Readability:**
> - **Categorization by Context:** Base the decision to use paragraphs versus lists on the content's pattern, focus, and length.
>   - **Disconnected Facts:** When a paragraph contains multiple disconnected factual data points (e.g., job title, salary, location), do NOT mash them into a single block paragraph. Break them down into an `itemize` or `enumerate` list for clarity.
>   - **Closely Related Concepts:** Conversely, when multiple items within a list focus on one broad or closely related concept (e.g., grouping all technical requirements, or grouping all soft skills), merge those items into a cohesive paragraph within a single list item rather than itemizing each point individually.
> - Ensure a harmonic and proper use of `itemize` and `enumerate` environments for breaking down complex bodies of text (like lists of roles, qualifications, or tasks) to maximize readability.
> - **Dense Abbreviations:** When encountering a dense series of abbreviations or domain-specific terms (e.g., "EPV, PVWA, CPM, PSM") that lack natural sentence context, do NOT clump them together. Unpack them into a nested `itemize` or `enumerate` list. Define each term using a complete, natural sentence, and use `\uline{...}` strictly on the 1-3 core words that represent the definition to highlight them organically within the sentence.
> - Set US default document margins (1-inch) globally using `\usepackage[margin=1in]{geometry}`.
> - Convert emails, URLs, and any natively linkable context into clickable hyperlinks using `\usepackage{hyperref}` and `\href{url}{text}`.

> [!IMPORTANT]
> **Key Definitions & Abbreviations:**
> - Use **boldface** for key definitions.
> - For abbreviations, write the abbreviation in bold, followed by the expanded term in parentheses where the initial letters are bolded.
>   *Example:* `\textbf{PSM} (\textbf{P}rivileged \textbf{S}ession \textbf{M}anager)`
> - **First Occurrence Only:** Expand, boldface, and footnote abbreviations ONLY upon their very first occurrence in the document. For all subsequent uses, write the abbreviation in plain text without bolding, expansion, or footnoting (e.g., "PAM").
> - **Source Fidelity:** Do NOT arbitrarily introduce abbreviations if they are not explicitly present in the source text. If a term is written in full (e.g., "Information Technology"), leave it written in full. If it is not abbreviated in the source context, do not over-engineer it by injecting acronyms.
> - **Globally Known Abbreviations:** Do NOT expand, boldface, or footnote abbreviations that are globally understood and not domain-specific (e.g., "IT", "HR", "CEO"). Leave them as plain text. Only format and define abbreviations that require specialized domain knowledge to understand.
> - **Mandatory Research:** When encountering abbreviations, you MUST utilize Search MCP tools (such as `web-search`, `iask-search`, or `monica-search`) to properly find the correct definition. Do not guess or rely on internal knowledge alone. Phrase the extracted definition so it is highly accurate and easy to understand.

> [!IMPORTANT]
> **Inline Definitions:**
> - Use `\uline{...}` (from the `ulem` package) **sparingly and strictly** for very short phrases (1-3 words maximum).
> - Do NOT use `\uline` on entire clauses, sentences, or long definitions, as this severely hurts readability. Instead, use natural sentence structure for longer definitions.
> - **Dependent Underlining:** The `\uline{...}` command is strictly reserved for highlighting the definition of a corresponding **boldfaced keyword**. Do NOT use `\uline` in isolation.
> - **Natural Integration (No Parentheses):** When providing an inline definition or supplemental explanation for a keyword, do NOT place the definition inside parentheses (e.g., avoid `\textbf{Term} (\uline{definition})`). Instead, naturally merge the definition into the surrounding sentence structure so it reads fluidly, applying `\uline` only to the core words (e.g., `\textbf{Term}, which involves \uline{definition}, ...`). Note: This restriction applies only to conceptual definitions; standard abbreviation expansions (e.g., `\textbf{PAM} (\textbf{P}rivileged...)`) must still use parentheses.
> - **First Occurrence Rule:** When a domain-specific term or concept (not an abbreviation) is given the `\textbf` + `\uline` definitional treatment, that treatment MUST be applied at the term's **earliest appearance** in the document. If the same term, or a closely related variant of the same underlying concept, appears earlier without definition, the boldfacing and inline definition must be moved to that earlier occurrence. All subsequent uses of the term should appear in plain text without bolding or underlining.

> [!IMPORTANT]
> **Inline Emphasis (Action Keywords):**
> - Use `\textit{...}` on single directive words that signal the reader to actively check, fulfill, or act on an obligation or expectation. Typical examples include words such as "required", "expected", "preferred", "sought", "necessary", "recommended", and "mandatory".
> - **Scope:** Apply italics strictly to the directive word itself (one word). Do NOT italicize surrounding phrases, clauses, or the subject being described.
> - **Purpose:** These keywords serve as visual cues that distinguish obligations and expectations from general descriptive text, prompting the reader to pay focused attention to what is being asked of them.
> - **Restraint:** Do NOT italicize generic verbs or adjectives that merely describe a state without implying a reader-directed action (e.g., "supported", "documented", "gained"). The emphasis is reserved for words that carry a directive or evaluative weight toward the reader.

> [!IMPORTANT]
> **Footnotes:**
> - Use `\footnote{...}` for useful, minor information, or secondary definitions that are not essential for the primary flow and overall reading experience.
> - **Redundant Information:** Do NOT use footnotes to duplicate information that is already naturally extended within the document's text or embedded in an abbreviation expansion (e.g., if a term is already defined in a natural sentence, or if the abbreviation expansion itself is self-explanatory like "Banking, Financial Services, and Insurance"). Only use footnotes when providing non-duplicated, supplementary context.
> - **CRITICAL:** Do NOT place footnotes right next to the closing parenthesis of an expanded abbreviation. Always place the footnote next to the original abbreviation (before the parenthesis).
>   *Example:* `\textbf{PSM}\footnote{A component utilized to isolate, control, and record privileged sessions.} (\textbf{P}rivileged \textbf{S}ession \textbf{M}anager)`

> [!IMPORTANT]
> **Source Code Readability:**
> - Ensure the LaTeX source code itself is highly readable.
> - Maintain consistent alignment and indentation.
> - Wrap long text lines at approximately 80 characters to prevent excessive horizontal scrolling.
> - **No Grouping Comments:** Section headings or grouping labels from the source material (e.g., "Role Overview", "Qualifications", "Learning Outcomes") are not placed in LaTeX comments. Instead, each logical section is introduced by a natural transition sentence that absorbs the heading's context into the document's prose flow. The typeset document is the final readable content, and its structure must be self-evident to the reader without any hidden commentary.

> [!IMPORTANT]
> **Modularization & Wrapper `main.tex`:**
> - Assume that there is a standard `main.tex` wrapper file at the project root that already contains the standard preamble and document environments.
> - The `.tex` file you output must **NOT** contain `\documentclass`, `\usepackage`, `\begin{document}`, or `\end{document}` tags.
> - Output strictly the typeset body content, making it modularly importable via the `\input{...}` command.

## Steps

1. **Analyze the Source Text**:
   - Identify the core takeaway (e.g., job title, location, main announcement, or core conclusion).
   - Identify technical terms, abbreviations, and concepts that need defining.
   - Use Search MCP tools to comprehensively research all abbreviations and technical terms to ensure your definitions are accurate and easily understood, regardless of token consumption.
   - Note any informal language or active voice that must be converted to formal passive voice.
   - Identify lists or complex text bodies that should be transitioned into `itemize` or `enumerate` blocks.

2. **Structure the Document**:
   - **Modular Output:** Do NOT include a LaTeX preamble or `\begin{document}` / `\end{document}` wrappers in the generated file. Begin directly with the typeset content of the source material.
   - **Wrapper Context (`main.tex`):** Assume that all generated files will be modularly included via `\input{}` into a central `main.tex` file. If you are asked to generate or verify `main.tex` itself, its structure must be defined as follows:
     - Begin with a standard LaTeX preamble including necessary packages:
       ```latex
       \usepackage[margin=1in]{geometry}
       \usepackage[normalem]{ulem}
       \usepackage{hyperref}
       ```
     - Configure paragraph formatting to have no indentation and suppress `\hbox` and `\vbox` warnings for all LaTeX main compilation files (entry files) by including:
       ```latex
       \setlength{\parindent}{0pt}           % No paragraph indentation
       \hbadness=10000                       % Suppress Warnings (Horizontal)
       \vbadness=10000                       % Suppress Warnings (Vertical)
       ```
     - Open the `\begin{document}` environment and use `\input{filename}` to manage the documents.

3. **Draft the Core Takeaway**:
   - Write the first paragraph summarizing the main point clearly in passive voice and third person.

4. **Typeset the Body**:
   - Convert raw text (like bullet points or fragmented notes) into cohesive paragraphs or structured `itemize`/`enumerate` environments using measured transitions.
   - Apply formatting rules (`\textbf{}`, `\uline{}`, `\footnote{}`) meticulously to definitions, key concepts, and abbreviations.
   - Apply `\href{...}{...}` meticulously to any hyperlinkable contexts.

5. **Review and Refine**:
   - Proofread to ensure NO semicolons or colons are used mid-sentence.
   - Ensure all ASCII punctuation is plain.
   - Validate that the tone remains strictly formal, third-person, and passive throughout the text.
   - Ensure the LaTeX source code lines are manually wrapped around 80 characters and properly indented.
   - Verify that all footnotes attached to abbreviations are correctly placed adjacent to the acronym, NOT the closing parenthesis.
