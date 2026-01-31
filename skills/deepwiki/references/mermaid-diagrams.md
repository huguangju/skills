---
name: mermaid-diagrams
description: Create various diagrams using Mermaid syntax for DeepWiki documentation
---

# Mermaid Diagrams

Mermaid allows creating diagrams using text and code, making version control and maintenance easy. It is the core visualization tool for DeepWiki documentation.

## Flowchart

Used to show processes and decision points.

```mermaid
flowchart TD
    A[Start] --> B{Valid?}
    B -->|Yes| C[Process]
    B -->|No| D[Error]
    C --> E[End]
    D --> E
```

**Syntax:**

```markdown
flowchart TD
    A[Start] --> B{Valid?}
    B -->|Yes| C[Process]
    B -->|No| D[Error]
```

## Sequence Diagram

Used to show interactions between entities over time.

```mermaid
sequenceDiagram
    participant A as Client
    participant B as Server
    participant C as Database

    A->>B: Request
    B->>C: Query
    C-->>B: Result
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

Used to show class hierarchies and relationships.

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

Used to show state machines and transitions.

```mermaid
stateDiagram-v2
    [*] --> Idle
    Idle --> Processing: Start
    Processing --> Complete: Success
    Processing --> Error: Failure
    Complete --> [*]
    Error --> Idle: Retry
```

## ER Diagram (Entity Relationship)

Used to show database entity relationships.

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

## Relationship Graph

Used for general directed or undirected relationships.

```mermaid
graph TB
    A[Parent] --> B[Child 1]
    A --> C[Child 2]
    B --> D[Grandchild]
    C --> D
```

Direction options:

- `TB` - Top to Bottom
- `BT` - Bottom to Top
- `LR` - Left to Right
- `RL` - Right to Left

## C4 Diagram

Used for software architecture (requires C4 extension).

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
4. **Limit complexity** - Split when exceeding 10-15 elements
5. **Use subgraphs** - Group related elements

## Common Symbols

| Shape | Syntax | Usage |
|-------|--------|-------|
| Rectangle | `[Text]` | Process, step |
| Diamond | `{Text}` | Decision |
| Circle | `((Text))` | Start/End |
| Database | `[(Text)]` | Data storage |
| Subroutine | `[[Text]]` | Predefined process |

## Style Customization

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
