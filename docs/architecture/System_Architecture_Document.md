# System Architecture Document (SAD)

## High-level architecture

```text
CUSTOMER → REACT → FASTAPI → POSTGRESQL
                        ↘
                         N8N → AI / NOTIFY / SHEETS
```

## Responsibilities

| Layer | Responsibility |
|-------|----------------|
| React | User interface |
| FastAPI | API, validation, auth, business boundaries |
| PostgreSQL | Source of truth |
| n8n | Workflow orchestration and integrations |
| AI | Understanding and generation |
| Google Sheets | Optional operational reporting |

## Principles

- Modular monolith + n8n (no premature microservices).
- AI output is validated before persistence.
- Single VPS deployment for MVP.
- Clear separation of concerns; do not put business logic in React or let AI write the database.

*Full architecture diagrams, sequence flows, and non-functional detail are preserved in git history of the previous root file `System Architecture Document (SAD).md`.*
