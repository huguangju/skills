---
name: vitepress-config
description: Configure VitePress for DeepWiki-style documentation
---

# VitePress Configuration

VitePress is a Vite-based static site generator, suitable for building DeepWiki-style documentation sites.

## Basic Configuration

### Installation

```bash
pnpm add -D vitepress
```

### Directory Structure

```
docs/
├── .vitepress/
│   ├── config.ts          # Main configuration
│   └── theme/
│       └── custom.css     # Custom styles (optional)
├── overview.md            # Project overview
├── architecture.md        # Architecture design
├── flows.md               # Flow documentation
├── design-decisions.md    # Design decisions
├── modules/               # Module documentation
│   └── [module-name].md
├── appendix.md            # Appendix
└── index.md               # Home page
```

### Basic Configuration (docs/.vitepress/config.ts)

```typescript
import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'Project Documentation',
  description: 'DeepWiki-style project documentation',

  // Clean URLs (no .html suffix)
  cleanUrls: true,

  // Last updated timestamp
  lastUpdated: true,

  themeConfig: {
    // Navigation bar
    nav: [
      { text: 'Overview', link: '/overview' },
      { text: 'Architecture', link: '/architecture' },
      { text: 'Modules', link: '/modules/' },
      { text: 'Flows', link: '/flows' },
      { text: 'Design Decisions', link: '/design-decisions' }
    ],

    // Sidebar
    sidebar: {
      '/modules/': [
        {
          text: 'Core Modules',
          collapsed: false,
          items: [
            // Generate based on actual modules
            { text: 'core', link: '/modules/core' },
            { text: 'api', link: '/modules/api' },
          ]
        }
      ]
    },

    // Search
    search: {
      provider: 'local'
    },

    // Edit link
    editLink: {
      pattern: 'https://github.com/username/repo/edit/main/docs/:path'
    },

    // Footer
    footer: {
      message: 'Generated with deepwiki skill',
      copyright: 'Copyright © 2026'
    }
  },

  // Markdown configuration
  markdown: {
    lineNumbers: true,
    config: (md) => {
      // Custom plugins
    }
  }
})
```

## Script Commands

Add to package.json:

```json
{
  "scripts": {
    "docs:dev": "vitepress dev docs",
    "docs:build": "vitepress build docs",
    "docs:preview": "vitepress preview docs"
  }
}
```

## Home Page (index.md)

```markdown
---
layout: home

hero:
  name: Project Name
  text: DeepWiki Documentation
  tagline: Engineering cognitive assets, human-readable and AI-searchable
  actions:
    - theme: brand
      text: Start Reading
      link: /overview
    - theme: alt
      text: GitHub
      link: https://github.com/username/repo

features:
  - title: Project Overview
    details: Tech stack, directory structure, entry points
    link: /overview
  - title: Architecture Design
    details: Module division, dependency relationships, architecture diagrams
    link: /architecture
  - title: Module Details
    details: Responsibilities, boundaries, and usage of each module
    link: '/modules/'
  - title: Flow Documentation
    details: How the system runs
    link: /flows
  - title: Design Decisions
    details: Why designed this way
    link: /design-decisions
---
```

## Mermaid Support

Install mermaid plugin:

```bash
pnpm add -D vitepress-plugin-mermaid
```

Update configuration:

```typescript
import { defineConfig } from 'vitepress'
import { withMermaid } from 'vitepress-plugin-mermaid'

export default withMermaid({
  // ... your configuration
  mermaid: {
    theme: 'default'
  }
})
```

## Auto-Generate Sidebar

For large projects, automatically generate sidebar based on file structure:

```typescript
import { defineConfig } from 'vitepress'
import fs from 'fs'
import path from 'path'

function generateSidebar(dir: string, basePath: string = '') {
  const items = []
  const files = fs.readdirSync(dir)

  for (const file of files) {
    const fullPath = path.join(dir, file)
    const stat = fs.statSync(fullPath)

    if (stat.isDirectory()) {
      items.push({
        text: file,
        items: generateSidebar(fullPath, path.join(basePath, file))
      })
    } else if (file.endsWith('.md')) {
      const name = file.replace('.md', '')
      items.push({
        text: name,
        link: path.join(basePath, name)
      })
    }
  }

  return items
}

export default defineConfig({
  themeConfig: {
    sidebar: {
      '/modules/': generateSidebar('docs/modules', '/modules')
    }
  }
})
```

## Deployment

### GitHub Pages

Create `.github/workflows/deploy.yml`:

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: pnpm/action-setup@v2
      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: pnpm

      - run: pnpm install
      - run: pnpm docs:build

      - uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: docs/.vitepress/dist
```

<!--
Source references:
- https://vitepress.dev/reference/site-config
- https://vitepress.dev/guide/getting-started
-->
