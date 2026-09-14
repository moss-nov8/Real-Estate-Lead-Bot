# API Specification — Real Estate Lead Bot

## Overview

FastAPI is the application/API boundary. All client traffic goes through versioned REST endpoints under `/api/v1`.

## Core Endpoints (MVP)

```text
GET    /api/v1/health

POST   /api/v1/auth/login

POST   /api/v1/leads
GET    /api/v1/leads
GET    /api/v1/leads/{id}
PATCH  /api/v1/leads/{id}
POST   /api/v1/leads/{id}/qualify

POST   /api/v1/conversations
GET    /api/v1/conversations/{id}

POST   /api/v1/messages
GET    /api/v1/conversations/{id}/messages

POST   /api/v1/follow-ups
GET    /api/v1/follow-ups
PATCH  /api/v1/follow-ups/{id}
```

## Responsibilities of the API Layer

- Request validation (Pydantic)
- Authentication / authorization
- Business rules and lead status transitions
- Database access
- Triggering n8n workflows (webhooks)
- Returning structured JSON errors

## Principles

- Customers never talk directly to n8n.
- AI output is validated before persistence.
- Idempotency for message processing where practical.
- Clear separation: FastAPI owns application boundaries; n8n owns automation.

Full detailed request/response schemas and error contracts are in the original API Specification (available in git history).
