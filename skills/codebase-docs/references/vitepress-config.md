---
name: vitepress-config
description: Configuring VitePress for codebase documentation
---

# VitePress Configuration

VitePress is a static site generator powered by Vite, ideal for documentation sites.

## Basic Setup

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
├── 1. Project Overview.md
├── 2. Architecture Overview.md
├── 3. Workflow Overview.md
├── 4. Deep Dive/
│   └── Component.md
└── index.md               # Homepage
```

### Basic Config (docs/.vitepress/config.ts)

```typescript
import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'Project Documentation',
  description: 'Generated codebase documentation',

  // Clean URLs (no .html extension)
  cleanUrls: true,

  // Last updated timestamp
  lastUpdated: true,

  themeConfig: {
    // Navigation
    nav: [
      { text: 'Overview', link: '/1. Project Overview' },
      { text: 'Architecture', link: '/2. Architecture Overview' },
      { text: 'Workflows', link: '/3. Workflow Overview' },
      { text: 'Deep Dive', link: '/4. Deep Dive/' }
    ],

    // Sidebar
    sidebar: {
      '/4. Deep Dive/': [
        {
          text: 'Core Components',
          collapsed: false,
          items: [
            { text: 'Router', link: '/4. Deep Dive/Router' },
            { text: 'State Management', link: '/4. Deep Dive/State' },
            { text: 'API Client', link: '/4. Deep Dive/API-Client' }
          ]
        },
        {
          text: 'Features',
          collapsed: true,
          items: [
            // Feature components
          ]
        }
      ]
    },

    // Social links
    socialLinks: [
      { icon: 'github', link: 'https://github.com/username/repo' }
    ],

    // Footer
    footer: {
      message: 'Generated with codebase-docs skill',
      copyright: 'Copyright © 2026'
    },

    // Search
    search: {
      provider: 'local'
    },

    // Edit link
    editLink: {
      pattern: 'https://github.com/username/repo/edit/main/docs/:path'
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

## Scripts

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

## Homepage (index.md)

```markdown
---
layout: home

hero:
  name: Project Name
  text: Codebase Documentation
  tagline: Comprehensive guide to the architecture and implementation
  actions:
    - theme: brand
      text: Get Started
      link: /1. Project Overview
    - theme: alt
      text: View on GitHub
      link: https://github.com/username/repo

features:
  - title: Architecture Overview
    details: High-level system design and C4 diagrams
    link: /2. Architecture Overview
  - title: Workflows
    details: Key processes and data flows
    link: /3. Workflow Overview
  - title: Deep Dive
    details: Component-level documentation
    link: /4. Deep Dive/
---
```

## Mermaid Support

Install the mermaid plugin:

```bash
pnpm add -D vitepress-plugin-mermaid
```

Update config:

```typescript
import { defineConfig } from 'vitepress'
import { withMermaid } from 'vitepress-plugin-mermaid'

export default withMermaid({
  // ... your config
  mermaid: {
    theme: 'default'
  }
})
```

## Auto-Generated Sidebar

For large projects, generate sidebar from file structure:

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
      '/4. Deep Dive/': generateSidebar('docs/4. Deep Dive', '/4. Deep Dive')
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
