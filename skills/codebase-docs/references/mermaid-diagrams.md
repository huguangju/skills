---
name: mermaid-diagrams
description: Creating various diagram types using Mermaid syntax
---

# Mermaid Diagrams

Mermaid allows you to create diagrams using text and code, making version control and maintenance easier.

## Flowchart

For showing process flows and decision points.

```mermaid
flowchart TD
    A[Start] --> B{Is it valid?}
    B -->|Yes| C[Process]
    B -->|No| D[Error]
    C --> E[End]
    D --> E
```

**Syntax:**
```markdown
flowchart TD
    A[Start] --> B{Is it valid?}
    B -->|Yes| C[Process]
    B -->|No| D[Error]
```

## Sequence Diagram

For showing interactions between entities over time.

```mermaid
sequenceDiagram
    participant A as Client
    participant B as Server
    participant C as Database

    A->>B: Request
    B->>C: Query
    C-->>B: Results
    B-->>A: Response
```

**Syntax:**
```markdown
sequenceDiagram
    participant A as Client
    participant B as Server
    A->>B: Message
    B-->>A: Reply
```

## Class Diagram

For showing class hierarchies and relationships.

```mermaid
classDiagram
    class User {
        +String id
        +String name
        +login()
        +logout()
    }

    class Admin {
        +manageUsers()
    }

    User <|-- Admin
```

## State Diagram

For showing state machines and transitions.

```mermaid
stateDiagram-v2
    [*] --> Idle
    Idle --> Processing: Start
    Processing --> Complete: Success
    Processing --> Error: Failure
    Complete --> [*]
    Error --> Idle: Retry
```

## ER Diagram

For showing database entity relationships.

```mermaid
erDiagram
    USER ||--o{ ORDER : places
    USER {
        string id PK
        string email
        string name
    }
    ORDER {
        string id PK
        string userId FK
        date createdAt
    }
```

## Graph

For general directed or undirected relationships.

```mermaid
graph TB
    A[Parent] --> B[Child 1]
    A --> C[Child 2]
    B --> D[Grandchild]
    C --> D
```

Direction options:
- `TB` - Top to bottom
- `BT` - Bottom to top
- `LR` - Left to right
- `RL` - Right to left

## C4 Diagrams

For software architecture (requires C4 extension).

```mermaid
C4Context
title System Context Diagram
Person(user, "User")
System(app, "Application")
Rel(user, app, "Uses")
```

## Diagram Best Practices

1. **Keep it simple** - One concept per diagram
2. **Use consistent naming** - Match code naming
3. **Add titles** - Explain what the diagram shows
4. **Limit nodes** - Split if more than 10-15 elements
5. **Use subgraphs** - Group related elements

## Common Notation

| Shape | Syntax | Use For |
|-------|--------|---------|
| Rectangle | `[Text]` | Process, step |
| Diamond | `{Text}` | Decision |
| Circle | `((Text))` | Start/End |
| Database | `[(Text)]` | Data store |
| Subroutine | `[[Text]]` | Predefined process |

## Styling

Apply custom styles:

```mermaid
flowchart LR
    A[Default]:::className --> B[Styled]

    classDef className fill:#f9f,stroke:#333,stroke-width:2px
    classDef error fill:#f96,stroke:#333

    B:::error
```

<!--
Source references:
- https://mermaid.js.org/intro/
- https://mermaid.js.org/syntax/flowchart.html
-->
