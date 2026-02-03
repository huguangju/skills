---
name: concise-editing-guide
description: Rules and examples for meaning-preserving doc simplification
---

# Core Rules

- Remove redundancy and filler
- Keep technical terms, API names, paths, and config keys unchanged
- Merge near-duplicate sentences while preserving logic and order
- Prefer active, compact phrasing
- Keep table “description/usage” cells short but precise

# Common Patterns

## Pattern 1: Remove Redundancy

**Before**
```text
This module is mainly responsible for sending, receiving, storing, and updating message states.
```

**After**
```text
This module handles sending, receiving, storing, and updating message states.
```

## Pattern 2: Merge Duplicates

**Before**
```text
The system provides multiple window types. Each window type has its own presets.
```

**After**
```text
The system provides multiple window types with their own presets.
```

## Pattern 3: Compress Lists

**Before**
```text
- Login: supports username/password login
- Register: supports phone registration
- Manage: supports account management
```

**After**
```text
- Login/registration: supports username/password and phone registration
- Account management
```

## Pattern 4: Shorten Table Descriptions

**Before**
```text
| Field | Description |
|------|------|
| status | The current status of the message, including sending, success, or failure |
```

**After**
```text
| Field | Description |
|------|------|
| status | Message status (sending/success/failure) |
```

# Do Not Change

- Code blocks, commands, paths, API names, and config keys
- Version numbers and environment names
- Conditional constraints or sequence logic

<!-- Sources: none -->
