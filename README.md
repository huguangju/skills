# codebase-docs Skill

An [Agent Skill](https://agentskills.io/home) for generating DeepWiki-style documentation from source code and integrating it with VitePress.

## Installation

```bash
pnpx skills add huguangju/skills --skill codebase-docs
```

## Features

- **Progressive Analysis** - 5-phase workflow for understanding codebases incrementally
- **C4 Model Diagrams** - System Context, Container, and Component diagrams
- **Mermaid Visualization** - Flowcharts, sequence diagrams, class diagrams, ER diagrams
- **VitePress Integration** - Ready-to-deploy documentation site configuration
- **Multi-language Support** - TypeScript, Python, Rust, Go, Java, and more

## Usage

When you want to document a codebase:

```
Use the codebase-docs skill to generate documentation for this project.
```

The skill will guide you through:

1. **Project Discovery** - Identify tech stack, entry points, and structure
2. **Architecture Analysis** - Create C4 diagrams and component relationships
3. **Documentation Generation** - Write comprehensive markdown with code examples
4. **Diagram Creation** - Generate Mermaid diagrams for visual representation
5. **Quality Assurance** - Validate links, diagrams, and VitePress setup

## Output Structure

```
docs/
├── 1. Project Overview.md          # High-level summary, tech stack
├── 2. Architecture Overview.md     # C4 diagrams, system design
├── 3. Workflow Overview.md         # Key workflows and data flows
├── 4. Deep Dive/                   # Component-level documentation
│   └── [Component-Name].md
└── .vitepress/
    └── config.ts                   # VitePress configuration
```

## References

The skill includes detailed references for:

- [C4 Model](skills/codebase-docs/references/c4-model.md) - Software architecture visualization
- [Mermaid Diagrams](skills/codebase-docs/references/mermaid-diagrams.md) - Diagram syntax and examples
- [VitePress Config](skills/codebase-docs/references/vitepress-config.md) - Documentation site setup
- [Progressive Analysis](skills/codebase-docs/references/progressive-analysis.md) - Incremental codebase analysis

## License

[MIT](LICENSE.md)
