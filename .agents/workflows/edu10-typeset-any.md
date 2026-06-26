---
description: Typesets any text source—including raw notes, formatted markdown, or emails—into a structured and highly readable LaTeX document adhering to strict voice and formatting standards.
---

# Workflow: edu10-typeset-any

## Trigger
Use this workflow when requested to "typeset", "format", or "proofread" text into a LaTeX document. **Source Input Flexibility:** The source material is not restricted to raw text. Any non-tex file, including formatted Markdown files, plain unformatted text, or emails, can and should be treated as a valid "source" to generate or proofread the resulting `.tex` file.

## Core Rules & Formatting Standards

> [!IMPORTANT]
> **Tone & Voice:**
> - Write in the **third person and passive voice** with a **formal, impersonal register** (avoid conversational language).
> - State the **core takeaway first**, followed by supporting detail.
> - **Never** use emojis or elaborate Unicode. Strictly prefer plain ASCII punctuation.
> - **Avoid** semicolons and colons within sentences. Use measured transitions (e.g., "There are several factors to consider as follows.").
> - Define technical terms inline and immediately.

> [!IMPORTANT]
> **Scannability & Readability:**
> - **Categorization by Context:** Base the decision to use paragraphs versus lists on the content's pattern, focus, and length.
>   - **Disconnected Facts:** When a paragraph contains multiple disconnected factual data points (e.g., job title, salary, location), do NOT mash them into a single block paragraph. Break them down into an `itemize` or `enumerate` list for clarity.
>   - **Closely Related Concepts:** Conversely, when multiple items within a list focus on one broad or closely related concept (e.g., grouping all technical requirements, or grouping all soft skills), merge those items into a cohesive paragraph within a single list item rather than itemizing each point individually, **UNLESS the resulting paragraph becomes excessively lengthy, dense, or contains enumerable measures.**
>   - **Dense Sub-Concepts & Enumerable Measures:** When a broad concept contains enumerable measures (e.g., tiered compensation across multiple years, sequential steps) or becomes excessively lengthy with sub-concepts (e.g., a vast array of technical frameworks broken down by layer), do NOT force them into a single block paragraph. Instead, introduce the broad concept with a transition sentence and unpack the sub-concepts or measures into a nested `itemize` or `enumerate` list to maximize scannability.
> - Ensure harmonic use of `itemize` and `enumerate` for breaking down complex bodies of text (lists of roles, qualifications, or tasks) to maximize readability.
> - **Dense Abbreviations:** When a dense series of abbreviations or domain terms (e.g., "EPV, PVWA, CPM, PSM") lacks natural sentence context, do NOT clump them together. Unpack them into a nested list, define each with a complete sentence, and use `\uline{...}` strictly on the 1-3 core defining words.
> - Set US default 1-inch margins globally using `\usepackage[margin=1in]{geometry}`.
> - Convert emails, URLs, and any natively linkable context into clickable links using `\usepackage{hyperref}` and `\href{url}{text}`.

> [!IMPORTANT]
> **Sectioning & Structure:**
> - Break the document into logical segments using `\section*{...}` and `\subsection*{...}` tags. Do NOT rely solely on bold text or page breaks for document structure. Ensure the document is easily navigable.

> [!IMPORTANT]
> **Key Definitions & Abbreviations:**
> - Use **boldface** for key definitions.
> - For abbreviations, write the abbreviation in bold, followed by the expanded term in parentheses with the initial letters bolded.
>   *Example:* `\textbf{PSM} (\textbf{P}rivileged \textbf{S}ession \textbf{M}anager)`
> - **First Occurrence Only:** Expand, boldface, and footnote an abbreviation ONLY on its first occurrence. All later uses are plain text (e.g., "PAM").
> - **Source Fidelity:** Do NOT invent abbreviations absent from the source. If a term is written in full (e.g., "Information Technology"), leave it in full.
> - **Globally Known Abbreviations:** Do NOT expand, boldface, or footnote globally understood abbreviations (e.g., "IT", "HR", "CEO"). Define only those requiring specialized domain knowledge.
> - **Mandatory Research:** When encountering domain abbreviations, you MUST research definitions using Search tools, following the `plan-search` tier order (native or `web-search` first, then `iask-search`, `monica-search`, broader discovery, then source verification). Do not guess. Phrase each definition to be accurate and easy to understand.

> [!IMPORTANT]
> **Inline Definitions:**
> - Use `\uline{...}` (from the `ulem` package) **sparingly and strictly** for very short phrases (1-3 words maximum).
> - Do NOT use `\uline` on entire clauses, sentences, or long definitions. Use natural sentence structure for longer definitions.
> - **Dependent Underlining:** `\uline{...}` is reserved for highlighting the definition of a corresponding **boldfaced keyword**. Do NOT use `\uline` in isolation.
> - **Natural Integration (No Parentheses):** Do NOT place conceptual definitions in parentheses (e.g., avoid `\textbf{Term} (\uline{definition})`). Merge the definition into the sentence and apply `\uline` only to the core words (e.g., `\textbf{Term}, which involves \uline{definition}, ...`). This restriction applies only to conceptual definitions. Standard abbreviation expansions still use parentheses.
> - **First Occurrence Rule:** Apply the `\textbf` + `\uline` treatment at the term's **earliest appearance**. If the same term or a close variant appears earlier without definition, move the treatment there. All later uses are plain text.

> [!IMPORTANT]
> **Inline Emphasis (Action Keywords):**
> - Use `\textit{...}` on single directive words that signal the reader to check, fulfill, or act on an obligation (e.g., "required", "expected", "preferred", "sought", "necessary", "recommended", "mandatory").
> - **Scope:** Italicize the directive word itself only (one word). Do NOT italicize surrounding phrases or the subject being described.
> - **Restraint:** Do NOT italicize generic verbs or adjectives that merely describe a state without a reader-directed action (e.g., "supported", "documented", "gained").

> [!IMPORTANT]
> **Footnotes:**
> - Use `\footnote{...}` for useful, minor, or secondary detail not essential to the primary reading flow.
> - **Redundant Information:** Do NOT duplicate information already extended in the text or embedded in an abbreviation expansion (e.g., a self-explanatory expansion like "Banking, Financial Services, and Insurance"). Use footnotes only for non-duplicated, supplementary context.
> - **CRITICAL:** Do NOT place a footnote next to the closing parenthesis of an expanded abbreviation. Always attach it to the original abbreviation, before the parenthesis.
>   *Example:* `\textbf{PSM}\footnote{A component utilized to isolate, control, and record privileged sessions.} (\textbf{P}rivileged \textbf{S}ession \textbf{M}anager)`

> [!IMPORTANT]
> **Source Code Readability:**
> - Keep the LaTeX source itself highly readable with consistent alignment and indentation.
> - Wrap long text lines at approximately 80 characters to prevent excessive horizontal scrolling.
> - **No Grouping Comments:** Do NOT place source headings or grouping labels (e.g., "Role Overview", "Qualifications") in LaTeX comments. Introduce each logical section with a natural transition sentence that absorbs the heading's context into the prose. The typeset structure must be self-evident without hidden commentary.

> [!IMPORTANT]
> **Modularization & Wrapper `main.tex`:**
> - Assume a standard `main.tex` wrapper at the project root already holds the preamble and document environments.
> - The `.tex` file you output must **NOT** contain `\documentclass`, `\usepackage`, `\begin{document}`, or `\end{document}`.
> - Output strictly the typeset body content, importable via `\input{...}`.
> - Native modularization is also available. One Antigravity workflow or document may chain another via the `/workflow-name` slash command when orchestration across files is needed.

## Steps

1. **Analyze & Research:**
   - Identify the core takeaway (e.g., job title, location, main announcement, or core conclusion).
   - Inventory technical terms, abbreviations, and concepts that need defining.
   - **Consolidate & Group:** Reorganize scattered source information logically by topic (e.g., group all platforms, all benefits, all policies together) before writing, ensuring the final document flows coherently without random categorization.
   - Research all domain abbreviations and terms using Search tools per the `plan-search` tier order, prioritizing accuracy over token cost.
   - Note any informal language or active voice to convert to formal passive voice.
   - Identify lists or complex bodies of text to transition into `itemize` or `enumerate` blocks.

2. **Structure the Document:**
   - **Modular Output:** Do NOT include a preamble or `\begin{document}` / `\end{document}` wrappers. Begin directly with the typeset content.
   - **Wrapper Context (`main.tex`):** Only if asked to generate or verify `main.tex` itself, structure it as follows.
     - Include the necessary packages:
       ```latex
       \usepackage[margin=1in]{geometry}
       \usepackage[normalem]{ulem}
       \usepackage{hyperref}
       ```
     - Configure paragraph formatting and suppress box warnings:
       ```latex
       \setlength{\parindent}{0pt}           % No paragraph indentation
       \hbadness=10000                       % Suppress Warnings (Horizontal)
       \vbadness=10000                       % Suppress Warnings (Vertical)
       ```
     - Open `\begin{document}` and use `\input{filename}` to manage the documents.

3. **Draft the Core Takeaway:**
   - Write the first paragraph summarizing the main point clearly in passive voice and third person.

4. **Typeset the Body:**
   - Convert raw text (bullet points, fragmented notes) into cohesive paragraphs or structured `itemize` / `enumerate` environments using measured transitions.
   - Apply `\textbf{}`, `\uline{}`, and `\footnote{}` meticulously to definitions, key concepts, and abbreviations.
   - Apply `\href{...}{...}` to any hyperlinkable context.

5. **Review and Refine:**
   - [ ] Opening paragraph states the core takeaway in third-person passive voice.
   - [ ] No semicolons or colons appear mid-sentence, and all punctuation is plain ASCII.
   - [ ] Tone is strictly formal, third-person, and passive throughout.
   - [ ] Output is modular body content with no preamble or document wrappers, unless `main.tex` was requested.
   - [ ] Every domain abbreviation is researched and given first-occurrence treatment only.
   - [ ] Footnotes attached to abbreviations sit before the expansion parenthesis, not after.
   - [ ] `\uline` is limited to 1-3 words and always paired with a bold keyword.
   - [ ] Paragraph-versus-list choices follow the three-pattern categorization, with dense sub-concepts unpacked into lists.
   - [ ] Emails and URLs are rendered with `\href{...}{...}`.
   - [ ] Source lines are wrapped near 80 characters with no comment-based section headings.
   - [ ] Logical transitions are accompanied by proper `\section*{}` or `\subsection*{}` headers.
