# Migration Patterns Reference

## Directory Mapping Patterns

### Mode A: Structure-Preserving Examples

#### Pattern 1: Flat Directory
```
source/
├── intro.md
├── setup.md
└── advanced.md

→ docs/
  ├── intro.md      → /intro
  ├── setup.md      → /setup
  └── advanced.md   → /advanced
```

#### Pattern 2: Nested Directory
```
source/
├── guide/
│   ├── README.md      → /guide/
│   ├── installation.md → /guide/installation
│   └── config.md      → /guide/config
└── api/
    ├── README.md      → /api/
    └── endpoints.md   → /api/endpoints
```

#### Pattern 3: Mixed Content
```
source/
├── README.md          → /
├── getting-started.md → /getting-started
└── deep-dive/
    ├── index.md       → /deep-dive/
    └── details.md     → /deep-dive/details
```

### Mode B: Structure-Redesign Examples

#### Before (Source)
```
legacy/
├── notes/
│   ├── meeting-2024-01.md
│   ├── meeting-2024-02.md
│   └── random-thoughts.md
├── drafts/
│   ├── idea-v1.md
│   └── idea-v2.md
└── exported/
    ├── export-1.md
    └── export-2.md
```

#### After (Target)
```
docs/
├── getting-started/
│   ├── index.md
│   └── quickstart.md
├── core-concepts/
│   ├── index.md
│   ├── architecture.md
│   └── design-patterns.md
├── advanced/
│   ├── index.md
│   └── optimization.md
└── reference/
    ├── index.md
    └── api.md
```

## Filename Normalization Rules

### Required Changes
| Invalid | Valid | Reason |
|---------|-------|--------|
| `My File.md` | `my-file.md` | Spaces in URLs |
| `file@v1.0.md` | `file-v1-0.md` | Special characters |
| `中文.md` | `chinese.md` | URL encoding issues |
| `01-intro.md` | `intro.md` | Remove numeric prefixes |

### Optional Changes
| Original | Alternative | When to Use |
|----------|-------------|-------------|
| `README.md` | `index.md` | Keep README for GitHub, use index for VitePress |

## Link Transformation Examples

### Internal Links
```markdown
# Before (Obsidian style)
[[Another Page]]
[[Folder/Another Page]]
[[Another Page|Custom Text]]

# After (VitePress style)
[Another Page](/another-page)
[Another Page](/folder/another-page)
[Custom Text](/another-page)
```

### Image Links
```markdown
# Before (Obsidian embedded)
![[image.png]]
![[assets/image.png]]

# After (Standard Markdown)
![Alt text](./image.png)
![Alt text](./assets/image.png)
```

### Cross-Document Links
```markdown
# Before (Relative path)
[Link](../other-folder/file.md)

# After (VitePress route)
[Link](/other-folder/file)
```

## Heading Level Corrections

### Problem: Multiple H1s
```markdown
# Title 1

Content...

# Title 2  ← Wrong

More content...
```

### Solution
```markdown
# Title 1

Content...

## Title 2  ← Correct

More content...
```

### Problem: Skipped Levels
```markdown
# Title

### Subsection  ← Wrong (skipped H2)

Content...
```

### Solution
```markdown
# Title

## Section      ← Correct

### Subsection  ← Correct

Content...
```

## Content Splitting Strategies

### When to Split
- File > 500 lines
- Multiple unrelated topics
- Clear logical boundaries

### When to Merge
- Files < 50 lines each
- Related content scattered
- Duplicate introductions

### Splitting Example
```markdown
# Before: all-in-one.md (800 lines)
# Project Overview
...200 lines

# API Reference
...300 lines

# Deployment Guide
...300 lines

# After:
# docs/
#   ├── index.md          (overview only)
#   ├── api/
#   │   ├── index.md
#   │   └── reference.md
#   └── deployment/
#       └── index.md
```
