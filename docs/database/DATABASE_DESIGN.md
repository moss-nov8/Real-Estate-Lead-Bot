# Database & Data Model Specification — Real Estate Lead Bot

## Source of Truth

PostgreSQL is the primary system of record.

## Primary Tables

- `users`
- `roles`
- `leads`
- `conversations`
- `messages`
- `lead_scores`
- `lead_assignments`
- `follow_ups`
- `activities`
- `integration_syncs`

## Key Principles

- UUIDs for primary keys where appropriate
- Timestamps (created_at / updated_at)
- Soft status transitions recorded in activities
- Never invent missing customer data
- Google Sheets is secondary / operational only

## Implementation Order

1. Database connection
2. SQLAlchemy models
3. Alembic
4. Initial migration
5. Seed data
6. Database tests

Full original Database & Data Model Specification content (detailed columns, relationships, constraints) is available in git history.
