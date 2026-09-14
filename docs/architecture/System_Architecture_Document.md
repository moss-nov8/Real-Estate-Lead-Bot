# System Architecture Document (SAD) — Real Estate Lead Bot

## High-Level Architecture

```text
             CUSTOMER
                 │
                 ▼
              REACT
                 │
                 ▼
             FASTAPI
              /    \
             /      \
            ▼        ▼
      POSTGRESQL    N8N
                     │
              ┌──────┼──────┐
              ▼      ▼      ▼
             AI  NOTIFY  SHEETS
```

## Component Responsibilities

| Component   | Responsibility |
|-------------|----------------|
| React       | Customer chat UI + Sales dashboard |
| FastAPI     | API, validation, auth, business rules, DB access |
| PostgreSQL  | Source of truth for leads, conversations, scores, activities |
| n8n         | Workflow orchestration, AI calls, notifications, Sheets sync |
| AI (LLM)    | Understanding, extraction, response generation |
| Google Sheets | Optional operational reporting (never source of truth) |

## Key Principles

- Modular monolith + n8n (no premature microservices)
- AI does not write directly to the database
- Deterministic qualification scoring in the application layer
- Single VPS deployment for MVP

Full original SAD content is available in git history.
