---
name: deepwiki
description: Generate DeepWiki-style source code documentation for local codebases, transforming engineering experience into reusable cognitive structures
metadata:
  author: Carson
  version: "2026.2.3"
---

# DeepWiki Documentation Generator

Generate DeepWiki-style documentation for local codebases with a clear, repeatable pipeline and explicit outputs.

---

## When to Use

**Use this Skill when you need to:**
- Produce structured codebase documentation for onboarding or long-term maintenance
- Capture architecture, modules, and key flows using consistent templates

**Do NOT use this Skill when:**
- You only need API reference docs (use TypeDoc/JSDoc)
- The codebase is trivial (< 100 lines)
- A proprietary tool format is required

---

## Core Principles

1. **Big picture before details**
2. **Responsibilities before implementation**
3. **Semantic-level explanation** (avoid line‑by‑line translation)
4. **Use domain terminology**, not tutorial tone

---

## Output Contract

```
docs/
├── overview.md              # Project overview: what it is, tech stack, entry points
├── architecture.md          # Architecture design: module division, dependencies, diagrams
├── modules/                 # Module-level documentation
│   ├── [module-name].md     # Independent documentation for each core module
│   └── ...
├── flows.md                 # Behavior and flows: how the system runs
├── design-decisions.md      # Design decisions: why designed this way
└── appendix.md              # Glossary and references (optional)
```

Each page must be independently readable and RAG‑friendly.

---

## Workflow (Five-Phase Analysis)

### Phase 1: Codebase Reconnaissance

**Goal:** Identify project type and tech stack.

**Actions:**
- Scan directory structure
- Identify primary language/framework/build system
- Determine project type (app / library / tool / mono‑repo)

**Ignored by default:**
- `node_modules/`, `dist/`, `build/`, `.git/`
- Generated/cache directories

**Output:**
- Overview draft + tech stack tags

---

### Phase 2: Structure Modeling

**Goal:** Explain how the project is organized.

**Actions:**
- System/subsystem decomposition
- Module boundaries from directory + dependencies
- Identify core vs peripheral modules

**Output:**
- `architecture.md`
- Dependency diagrams (Mermaid)
- System/subsystem hierarchy table

**Template:** use [templates.md](references/templates.md).

---

### Phase 3: Module Understanding

**Goal:** Explain each core module’s purpose and boundaries.

**Actions:**
- Extract key entities (classes/functions/interfaces)
- Summarize responsibilities and public API
- Identify common usage patterns

**Output:**
- `modules/[module-name].md`
- Key entity relationship diagrams

**Template:** use [templates.md](references/templates.md).

---

### Phase 4: Flow Synthesis

**Goal:** Describe how the system runs end‑to‑end.

**Actions:**
- Find entry points (CLI / main / server / job)
- Trace main call chains
- Summarize critical flows and exceptions

**Output:**
- `flows.md`

**Template:** use [templates.md](references/templates.md).

---

### Phase 5: Design Insight

**Goal:** Explain *why* the system is designed this way.

**Actions:**
- Summarize trade‑offs and design patterns
- Mark inferred reasoning vs confirmed facts

**Output:**
- `design-decisions.md`

**Template:** use [templates.md](references/templates.md).

---

## Quality Gates

- Every page answers: purpose / boundary / when to care
- No line‑by‑line code narration
- Mermaid diagrams render correctly
- Internal links are valid
- Terminology is consistent

---

## References

| Topic | Description | Reference |
|-------|-------------|-----------|
| Templates | Page templates for each document | [reference](references/templates.md) |
| Mermaid Guide | Diagram conventions | [reference](references/mermaid-diagrams.md) |
| VitePress Config | Docs site setup | [reference](references/vitepress-config.md) |
| Framework Patterns | Framework-specific analysis focus | [reference](references/framework-patterns.md) |
