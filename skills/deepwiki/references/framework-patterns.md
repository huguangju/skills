---
name: framework-patterns
description: Framework-specific analysis focus for DeepWiki docs
---

# Framework-Specific Patterns

## Vue 3 Projects

**Focus:** Composables, components, reactive state, Props/Emits

**Entry:** `main.ts`, `App.vue`

**Config:** `vite.config.ts`, `tsconfig.json`

**Key patterns:**
- Composables: reusable logic extraction
- Provide/Inject: cross-level state sharing
- Pinia: global state management
- Component communication: props down, events up

## React Projects

**Focus:** Hooks, components, Context, state management

**Entry:** `main.tsx`, `App.tsx`

**Config:** `vite.config.ts`, `tsconfig.json`

**Key patterns:**
- Custom hooks: reusable logic
- Context API: cross-level state sharing
- Zustand/Redux: global state management
- Component composition patterns

## TypeScript/JavaScript

**Focus:** Modules, exports, types, interfaces

**Entry:** `index.ts`, `main.ts`

**Config:** `tsconfig.json`, `package.json`

<!-- Sources: none -->
