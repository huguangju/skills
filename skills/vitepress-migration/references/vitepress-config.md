# VitePress Configuration Reference

## Basic Configuration

### Minimal Config
```typescript
// .vitepress/config.ts
import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'My Documentation',
  description: 'Documentation site',
  base: '/my-project/',

  themeConfig: {
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Guide', link: '/guide/' }
    ],

    sidebar: {
      '/guide/': [
        {
          text: 'Guide',
          items: [
            { text: 'Introduction', link: '/guide/' },
            { text: 'Getting Started', link: '/guide/getting-started' }
          ]
        }
      ]
    }
  }
})
```

## Sidebar Patterns

### Auto-Generated Sidebar (Mode A)

```typescript
import { generateSidebar } from 'vitepress-sidebar'

export default defineConfig({
  themeConfig: {
    sidebar: generateSidebar({
      documentRootPath: '/docs',
      useTitleFromFileHeading: true,
      useFolderTitleFromIndexFile: true,
      useFolderLinkFromIndexFile: true,
      hyphenToSpace: true,
      capitalizeFirst: true
    })
  }
})
```

Requires: `npm install vitepress-sidebar`

### Manual Sidebar (Mode B)

```typescript
export default defineConfig({
  themeConfig: {
    sidebar: [
      {
        text: 'Getting Started',
        collapsed: false,
        items: [
          { text: 'Introduction', link: '/getting-started/' },
          { text: 'Installation', link: '/getting-started/installation' },
          { text: 'Quick Start', link: '/getting-started/quick-start' }
        ]
      },
      {
        text: 'Core Concepts',
        collapsed: true,
        items: [
          { text: 'Architecture', link: '/concepts/architecture' },
          { text: 'Design Patterns', link: '/concepts/patterns' }
        ]
      },
      {
        text: 'Reference',
        collapsed: true,
        items: [
          { text: 'API', link: '/reference/api' },
          { text: 'Configuration', link: '/reference/config' }
        ]
      }
    ]
  }
})
```

## Navigation Configuration

### Top Navigation

```typescript
themeConfig: {
  nav: [
    { text: 'Home', link: '/' },
    {
      text: 'Guide',
      items: [
        { text: 'Getting Started', link: '/guide/' },
        { text: 'Advanced', link: '/guide/advanced' }
      ]
    },
    {
      text: 'v1.0',
      items: [
        { text: 'Changelog', link: '/changelog' },
        { text: 'Contributing', link: '/contributing' }
      ]
    }
  ]
}
```

## Markdown Configuration

### Code Blocks

```typescript
export default defineConfig({
  markdown: {
    theme: {
      light: 'github-light',
      dark: 'github-dark'
    },
    lineNumbers: true,
    config: (md) => {
      // Add custom plugins
    }
  }
})
```

### Custom Containers

```typescript
// .vitepress/theme/index.ts
import DefaultTheme from 'vitepress/theme'
import './custom.css'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    // Register global components
  }
}
```

## Head and Meta

```typescript
export default defineConfig({
  head: [
    ['link', { rel: 'icon', href: '/favicon.ico' }],
    ['meta', { name: 'author', content: 'Your Name' }],
    ['meta', { property: 'og:title', content: 'Documentation' }]
  ],

  // SEO
  sitemap: {
    hostname: 'https://example.com'
  }
})
```

## Build Configuration

```typescript
export default defineConfig({
  srcDir: './src',
  outDir: './dist',
  cacheDir: './.vitepress/cache',

  // Ignore dead links (not recommended)
  ignoreDeadLinks: false,

  // Clean URLs (no .html extension)
  cleanUrls: true,

  // Rewrites for URL mapping
  rewrites: {
    'source/:page': 'target/:page'
  }
})
```

## Search Configuration

### Local Search (Default)

```typescript
export default defineConfig({
  themeConfig: {
    search: {
      provider: 'local',
      options: {
        translations: {
          button: {
            buttonText: 'Search',
            buttonAriaLabel: 'Search docs'
          }
        }
      }
    }
  }
})
```

### Algolia Search

```typescript
export default defineConfig({
  themeConfig: {
    search: {
      provider: 'algolia',
      options: {
        appId: 'YOUR_APP_ID',
        apiKey: 'YOUR_SEARCH_API_KEY',
        indexName: 'YOUR_INDEX_NAME'
      }
    }
  }
})
```

## Social Links

```typescript
themeConfig: {
  socialLinks: [
    { icon: 'github', link: 'https://github.com/username/repo' },
    { icon: 'twitter', link: 'https://twitter.com/username' },
    { icon: 'discord', link: 'https://discord.gg/invite' }
  ]
}
```

## Footer Configuration

```typescript
themeConfig: {
  footer: {
    message: 'Released under the MIT License.',
    copyright: 'Copyright © 2024-present Your Name'
  },

  // Edit link
  editLink: {
    pattern: 'https://github.com/username/repo/edit/main/docs/:path',
    text: 'Edit this page on GitHub'
  },

  // Last updated
  lastUpdated: {
    text: 'Updated at',
    formatOptions: {
      dateStyle: 'full',
      timeStyle: 'medium'
    }
  }
}
```

## Appearance

```typescript
export default defineConfig({
  appearance: true,  // Enable dark mode toggle

  themeConfig: {
    logo: '/logo.svg',

    // Custom labels
    outline: {
      label: 'On this page'
    },

    docFooter: {
      prev: 'Previous page',
      next: 'Next page'
    },

    returnToTopLabel: 'Return to top',
    sidebarMenuLabel: 'Menu',
    darkModeSwitchLabel: 'Appearance'
  }
})
```

## Common Pitfalls

### 1. Base URL
If deploying to a subdirectory, always set `base`:
```typescript
base: '/my-project/'  // Note: leading AND trailing slash
```

### 2. Sidebar Links
Links in sidebar should match file paths without `.md`:
```typescript
// File: docs/guide/intro.md
{ text: 'Intro', link: '/guide/intro' }  // Correct
{ text: 'Intro', link: '/guide/intro.md' }  // Wrong
```

### 3. Index Pages
Always include trailing slash for index pages:
```typescript
{ text: 'Guide', link: '/guide/' }  // Correct (maps to /guide/index.md)
{ text: 'Guide', link: '/guide' }   // May not work correctly
```

### 4. Relative Links
Use absolute paths from root in sidebar:
```typescript
// Good
{ text: 'Page', link: '/guide/page' }

// Avoid
{ text: 'Page', link: './page' }
```
