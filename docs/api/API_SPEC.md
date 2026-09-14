# API Specification

FastAPI owns the application API surface.

## Initial endpoints (MVP)

```text
GET    /api/v1/health

POST   /api/v1/auth/login

POST   /api/v1/leads
GET    /api/v1/leads
GET    /api/v1/leads/{id}
PATCH  /api/v1/leads/{id}

POST   /api/v1/conversations
GET    /api/v1/conversations/{id}

POST   /api/v1/messages
GET    /api/v1/conversations/{id}/messages

POST   /api/v1/leads/{id}/qualify

POST   /api/v1/follow-ups
GET    /api/v1/follow-ups
PATCH  /api/v1/follow-ups/{id}
```

## Principles

- Request validation with Pydantic schemas.
- Authentication / authorization for internal (sales) endpoints.
- Customer-facing message flow goes through FastAPI, which then triggers n8n; the customer never talks to n8n directly.
- Structured error responses.
- Idempotency considerations for message processing.

*Full request/response schemas, status codes, and detailed contracts are preserved in git history of the previous root file `API Specification.md`.*
