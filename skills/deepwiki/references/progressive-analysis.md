---
name: progressive-analysis
description: DeepWiki five-phase progressive codebase analysis method
---

# Progressive Analysis

Progressive analysis is a technique for breaking down large codebase analysis into manageable phases, aligning with DeepWiki's "top-down cognition" methodology.

## Why Use Progressive Analysis?

- **Cognitive Efficiency** - Don't overwhelm context all at once
- **Better Understanding** - Gradually build mental models
- **High Quality Output** - Reflection time between phases
- **Early Feedback** - Discover issues before they solidify

## Five-Phase Analysis Flow

### Phase 1: Codebase Reconnaissance

**Goal**: Answer "What kind of project is this?"

**Actions**:

- Scan overall directory structure
- Identify primary language / framework / build method
- Determine project type (application / library / tool / multi-module project)
- Find entry points and key configuration files

**Output**:

- Project type determination
- Tech stack tags
- Directory structure overview
- Primary subsystem candidates

**Analysis Checklist (Agent Checklist)**:

- [ ] Confirm project type (Application/Library/Tool/Multi-module)
- [ ] Confirm tech stack (language, framework, build tool)
- [ ] Find exact entry file paths
- [ ] Understand top-level directory organization logic

---

### Phase 2: Structure Modeling

**Goal**: Answer "How is the project organized?"

**Actions**:

- **System-Subsystem decomposition**: Identify hierarchical structure of systems, subsystems, and modules
- **Build semantic graph**: Extract dependencies and call relationships between modules
- Build module boundaries (based on directory + dependency relationships)
- Analyze module dependency directions
- Identify core modules vs peripheral modules
- Define system boundaries

**Output**:

- `architecture.md`
- Module responsibility overview
- Architecture relationship diagrams (Mermaid)
- C4 Context and Container diagrams
- System-Subsystem hierarchy table

**Analysis Checklist (Agent Checklist)**:

- [ ] Identify architecture pattern used (MVC/DDD/Clean Arch, etc.)
- [ ] **Decompose System-Subsystem-Module hierarchy** (System -> Subsystem -> Module)
- [ ] **Build semantic graph**: List key dependencies and call directions between modules
- [ ] Prepare data for C4 Context diagram (system boundaries)
- [ ] Prepare data for C4 Container diagram (main containers)

---

### Phase 3: Module Understanding

**Goal**: Answer "What is the purpose of each module?"

**Actions**:

- For each core module, extract key files and public API
- **Build internal semantic graph**: Extract key entities (classes/interfaces/functions) and their call, inheritance, and dependency relationships
- Summarize module responsibilities and boundaries
- Identify typical usage patterns

**Output**:

- `modules/[module-name].md`
- Module responsibility overview
- Key interface explanations
- Key entity relationship diagrams

**Module Documentation Unified Structure**:

- Purpose
- Position and Boundary
- Core Files
- Key Interfaces and Entity Relationships
- When to Care About This Module

**Analysis Checklist (Agent Checklist)**:

- [ ] Clarify module's purpose (Solve what?)
- [ ] Define module's responsibility boundary (Do what?)
- [ ] **Build internal semantic graph**: Extract key entities (classes/interfaces) and their relationships (inheritance/calls)
- [ ] Extract core file list and Public API
- [ ] Analyze collaboration patterns with other modules
- [ ] Summarize typical scenarios where developers need to care about this module

---

### Phase 4: Flow Synthesis

**Goal**: Answer "How does the system run?"

**Actions**:

- Locate entry points (CLI / main / server / job)
- Track main call chains
- Abstract key flows and control transfers

**Output**:

- `flows.md`
- Main process explanation
- Optional flows / exception paths
- Sequence diagrams and flowcharts

**Diagram Checklist**:

- [ ] Main flow sequence diagram
- [ ] Flowchart for key decision points
- [ ] Exception handling flows
- [ ] Data flow diagrams

---

### Phase 5: Design Insight

**Goal**: Answer "Why was it designed this way?"

**Actions**:

- **Auto-summary and completion**: Summarize key information and complete missing logical explanations based on context
- Identify obvious design patterns
- Infer historical decisions and engineering trade-offs
- Annotate certainty / uncertainty of inferences

**Output**:

- `design-decisions.md`
- Design decision records
- Engineering trade-off explanations

**Quality Checklist**:

- [ ] Each page answers "What is its purpose"
- [ ] Each page answers "Where is its position and boundary"
- [ ] Each page answers "When should I care about it"
- [ ] **Semantic-level explanation**: Explains design intent of key entities, not line-by-line code
- [ ] Use engineering language rather than teaching language
- [ ] Explain big picture before details
- [ ] Explain responsibilities before implementation
- [ ] Mermaid diagrams render correctly
- [ ] Documentation links are valid
- [ ] Naming is consistent

## Tips for Each Phase

### Phase 1 Tips

- Start from README (if exists)
- Check package.json, Cargo.toml, and other configuration files
- Find main entry files
- Note testing patterns

### Phase 2 Tips

- Understand module relationships through import/export
- Identify layers (UI, business logic, data)
- Look for patterns (MVC, Hexagonal, etc.)
- Note external dependencies

### Phase 3 Tips

- Document one module at a time
- Include code snippets
- Explain "why" not just "what"
- Cross-reference related modules

### Phase 4 Tips

- Keep diagrams simple
- One main concept per diagram
- Use consistent colors/symbols
- Add explanatory text

### Phase 5 Tips

- Build documentation site locally
- Click all links to check
- Review with fresh eyes
- Ask yourself: "Can a new developer understand this?"

## Adjust Based on Codebase Size

| Codebase Size | Phase Adjustment |
|---------------|------------------|
| Small (< 1k lines) | Merge Phase 2-3 |
| Medium (1k-10k) | Follow standard flow |
| Large (10k-50k) | Expand Phase 3, focus on key modules |
| Extra Large (> 50k) | Document by module, create module index |

## Common Pitfalls

1. **Diving into details too early** - Start from high level
2. **Skipping reconnaissance** - Don't assume you know the codebase
3. **Inconsistent terminology** - Create a glossary
4. **Isolated documentation** - Always link to related docs
5. **Outdated code examples** - Verify examples are still valid

## Progressive Analysis in Practice

### Example Timeline

```
0:00  - Start Phase 1: Codebase Reconnaissance
0:08  - Phase 1 complete, start Phase 2
0:22  - Phase 2 complete, start Phase 3
0:45  - Phase 3 complete, start Phase 4
0:58  - Phase 4 complete, start Phase 5
1:05  - Phase 5 complete, review and finalize
1:15  - Documentation complete
```

### When to Pause

- After completing each phase
- When encountering unexpected complexity
- Before generating diagrams
- Before final review

<!--
Based on smart-docs skill workflow and documentation best practices
-->
