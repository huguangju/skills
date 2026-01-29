# Skills Guidelines

This repository contains hand-written Agent Skills.

## Repository Structure

```
.
├── meta.ts              # Skill metadata
├── README.md            # Project documentation
├── skills/              # Skill packages
│   ├── antfu/           # Anthony Fu's preferences
│   └── codebase-docs/   # Codebase documentation generator
│       ├── SKILL.md
│       └── references/
└── package.json
```

## Skill Format

Each skill must have:

1. **SKILL.md** - Main skill file with YAML frontmatter
2. **references/** - Individual reference documents

### SKILL.md Template

```markdown
---
name: skill-name
description: When to use this skill
metadata:
  author: Your Name
  version: "2026.1.30"
---

# Skill Title

Brief description of what this skill does.

## When to Use

**Use when:**
- Condition 1
- Condition 2

**Don't use when:**
- Condition A
- Condition B

## Workflow

Step-by-step instructions.

## References

| Topic | Description | Reference |
|-------|-------------|-----------|
| Topic | Description | [reference](references/file.md) |
```

## Reference Files

Each reference file should:
- Focus on one concept
- Include code examples
- Have YAML frontmatter with name and description
- End with source references (commented out)

## Maintenance

- Update version in SKILL.md when making changes
- Keep references focused and concise
- Test skill instructions before committing
