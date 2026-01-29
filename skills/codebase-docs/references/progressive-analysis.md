---
name: progressive-analysis
description: Techniques for incrementally analyzing large codebases
---

# Progressive Analysis

Progressive analysis is a technique for understanding large codebases by breaking the analysis into manageable phases.

## Why Progressive Analysis?

- **Token efficiency** - Don't overwhelm the context window
- **Better understanding** - Build mental model incrementally
- **Quality output** - Time to reflect between phases
- **Early feedback** - Catch issues before they're embedded

## The 5-Phase Approach

### Phase 1: Project Discovery (5-10 min)

**Goal**: Understand what we're working with

**Activities**:
- Identify entry points
- Map directory structure
- Determine tech stack
- Find configuration files

**Output**:
- Project summary (1-2 paragraphs)
- Tech stack table
- Directory tree
- Key files list

**Prompt Template**:
```
Analyze this codebase at a high level:
1. What is this project's purpose?
2. What technologies are used?
3. What are the main entry points?
4. Summarize the directory structure
```

### Phase 2: Architecture Analysis (10-20 min)

**Goal**: Understand system design and relationships

**Activities**:
- Identify architectural patterns
- Map module dependencies
- Define system boundaries
- Create C4 Context and Container diagrams

**Output**:
- Architecture description
- C4 Level 1 (Context) diagram
- C4 Level 2 (Container) diagram
- Component relationship map

**Prompt Template**:
```
Based on the project structure:
1. What architectural patterns are used?
2. What are the main modules and their relationships?
3. Draw a C4 Context diagram showing system boundaries
4. Draw a C4 Container diagram showing main components
```

### Phase 3: Documentation Generation (20-40 min)

**Goal**: Create detailed documentation

**Activities**:
- Write Project Overview
- Document Architecture
- Describe Workflows
- Create Deep Dive component docs

**Output**:
- 1. Project Overview.md
- 2. Architecture Overview.md
- 3. Workflow Overview.md
- 4. Deep Dive/*.md files

**Prompt Template**:
```
Generate documentation for [component]:
1. What is its purpose?
2. What are the public APIs?
3. What are its dependencies?
4. Include code examples
```

### Phase 4: Diagram Generation (10-15 min)

**Goal**: Create visual representations

**Activities**:
- Convert text descriptions to Mermaid diagrams
- Create sequence diagrams for workflows
- Add class/ER diagrams where helpful
- Validate diagram syntax

**Output**:
- Mermaid diagrams embedded in docs
- Standalone diagrams for complex flows

**Diagram Checklist**:
- [ ] C4Context for system boundaries
- [ ] C4Container for component relationships
- [ ] Flowcharts for processes
- [ ] Sequence diagrams for interactions
- [ ] Class/ER diagrams for data models

### Phase 5: Quality Assurance (5-10 min)

**Goal**: Ensure documentation quality

**Activities**:
- Review all generated docs
- Verify links and references
- Check diagram rendering
- Validate code examples

**Checklist**:
- [ ] All links work
- [ ] Mermaid diagrams render
- [ ] Code examples are correct
- [ ] Naming is consistent
- [ ] No orphaned content
- [ ] VitePress builds successfully

## Tips for Each Phase

### Phase 1 Tips

- Start with README if it exists
- Look at package.json, Cargo.toml, etc.
- Find main entry files
- Note testing patterns

### Phase 2 Tips

- Follow imports/exports to understand relationships
- Identify layers (UI, business logic, data)
- Look for patterns (MVC, hexagonal, etc.)
- Note external dependencies

### Phase 3 Tips

- Document one component at a time
- Include code snippets
- Explain the "why" not just the "what"
- Cross-reference related components

### Phase 4 Tips

- Keep diagrams simple
- One main concept per diagram
- Use consistent colors/symbols
- Add explanatory text

### Phase 5 Tips

- Build the docs site locally
- Click through all links
- Review with fresh eyes
- Ask: "Would a new developer understand this?"

## Adapting to Codebase Size

| Codebase Size | Phase Adjustments |
|---------------|-------------------|
| Small (< 1k lines) | Combine phases 2-3 |
| Medium (1k-10k) | Follow standard approach |
| Large (10k-50k) | Extend phase 3, focus on key components |
| Very Large (> 50k) | Document modules separately, create module index |

## Common Pitfalls

1. **Too much detail early** - Start high-level
2. **Skipping the discovery phase** - Don't assume you know the codebase
3. **Inconsistent terminology** - Create a glossary
4. **Orphaned documentation** - Always link to related docs
5. **Stale code examples** - Verify examples still work

## Progressive Analysis in Practice

### Example Timeline

```
0:00  - Start Phase 1: Discovery
0:08  - Phase 1 complete, start Phase 2
0:22  - Phase 2 complete, start Phase 3
0:45  - Phase 3 complete, start Phase 4
0:58  - Phase 4 complete, start Phase 5
1:05  - Phase 5 complete, review and finalize
1:15  - Documentation complete
```

### When to Pause

- After completing each phase
- When you encounter unexpected complexity
- Before generating diagrams
- Before final review

<!--
This reference is based on the smart-docs skill workflow
and documentation best practices.
-->
