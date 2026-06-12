# Agent Monorepo Suite

This repository acts as a localized reference workspace demonstrating a complete, closed-loop AI agent automation architecture. It resolves common structural points of confusion by explicitly dividing execution into four foundational pillars: Steering, Specs, Skills, and Hooks.

---

## What Was Wrong with the Abstract Setup?

When context boundaries are described only in abstract definitions, AI developer agents (and human developers) face several operational points of failure:

1. **Context Fragmentation (Where are the rules?):** Without dedicated root-level mapping files (`product.md`, `tech.md`, `structure.md`), the AI agent is forced to guess project standards or infer them purely from existing files. This leads to inconsistent formatting, mismatched dependencies, and code that breaks style conventions.
   
2. **Ambiguous Execution Boundaries (What can the AI do?):** If tools are not explicitly bounded into programmatic wrappers like **Skills**, the agent might attempt to execute arbitrary, unverified shell actions or install bloated, non-standard third-party frameworks.
   
3. **Missing Automated Enforcement (Who checks the AI?):** Relying on human code review to catch minor structural syntax rule violations defeats the speed benefits of an automated agent loop. Integrating targeted validation checks directly into **Hooks** allows the repository architecture to self-correct code prior to review.

---

## Architectural Breakdown of This Repository

### 1. The Global Steering Layer (Root Directory)
These global markdown manuals act as the constant internal boundary layer for the AI agent across all modifications.
* **`product.md` (The "Why"):** Declares high-level product objectives, security mandates (Zero-Trust context execution), and user expectations.
* **`tech.md` (The "What"):** Constrains development tools, locking down Python 3.11, FastAPI, and asynchronous configurations. It strictly mandates `pipreqs` for package management.
* **`structure.md` (The "How"):** Mandates structural directories, module patterns, snake_case naming structures, and explicitly bans relative imports.

### 2. The Task Layer (Specifications)
* **`specs/core-auth.md`:** The localized, explicit blueprint outlining requirements for a single operational feature (cryptographic signature verification). The agent consumes this document to know *what* to build, while matching the execution constraints outlined in the steering layer.

### 3. The Capabilities Layer (Skills)
* **`.kiro/skills/register_dependency.sh`:** A discrete, sandbox-safe tool provided to the agent to cleanly parse and synchronize package requirements utilizing `pipreqs` without generating arbitrary system overhead.

### 4. The Guardrail Layer (Agent Hooks)
* **`.kiro/hooks/pre_commit_lint.sh`:** An automated verification check triggered at the conclusion of an assignment. If the AI agent accidentally breaks a rule documented in `structure.md` (such as utilizing a banned relative import pattern), this hook halts the execution lifecycle and notifies the agent to perform immediate refactoring.

---

## Local Inspection Map

```text
agent-monorepo-suite/
├── README.md               <-- You are here (Conceptual and system map)
├── product.md              <-- Global constraints: Core product context
├── tech.md                 <-- Global constraints: Frameworks & dependency tool choices
├── structure.md            <-- Global constraints: Directory boundaries & style guides
├── .kiro/
│   ├── hooks/
│   │   └── pre_commit_lint.sh  <-- Automated quality control hook
│   └── skills/
│       └── register_dependency.sh <-- Controlled execution capability
├── specs/
│   └── core-auth.md        <-- Feature spec blueprint
└── src/
    ├── core/
    │   └── security.py     <-- Target application source implementation
    └── mcp_server/
        └── app.py          <-- Core service mounting execution routes
```

### 2. `product.md` (Steering Layer: The Why)
# Product Overview

## Core Intent
The Agent Monorepo Suite provides isolated, high-performance, and lightweight Model Context Protocol (MCP) server wrappers enabling secure artificial intelligence execution loops over local environments.

## Target Audience
* Infrastructure engineers constructing modular AI automation toolkits.
* Security operations looking to strictly partition automated devops runs.

## Constraints & System Guardrails
* **Zero-Trust Boundaries:** All contextual processes must undergo explicit signature verification.
* **Minimal Footprint:** Eradicate any redundant dependency overhead to optimize execution speed.


Product Overview ( product .md ) - Defines your product's purpose, target users, key features, and business objectives. This helps Kiro understand the "why" behind technical decisions and suggest solutions aligned with your product goals.

Technology Stack ( tech.md ) - Documents your chosen frameworks, libraries, development tools, and technical constraints. When Kiro suggests implementations, it will prefer your established stack over alternatives.

Project Structure ( structure.md ) - Outlines file organization, naming conventions, import patterns, and architectural decisions. This ensures generated code fits seamlessly into your existing codebase.