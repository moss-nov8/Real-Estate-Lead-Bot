# Database & Data Model Specification

PostgreSQL is the primary source of truth for the Real Estate Lead Bot.

## Planned core tables

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

## Key principles

- Leads and conversations are the centre of the model.
- Messages belong to conversations and are linked to leads.
- Lead scores are versioned / historied so changes are auditable.
- Activities record important state changes (created, qualified, assigned, contacted, converted, lost, etc.).
- UUIDs for primary keys are preferred.
- Timestamps (`created_at`, `updated_at`) on all main entities.
- Soft-delete or status flags where appropriate rather than hard deletes of lead history.

## Implementation order

1. Database connection (SQLAlchemy + async)
2. Models
3. Alembic configuration
4. Initial migration
5. Seed data (roles, sample users if needed)
6. Model / relationship tests

*Full original field-level design, relationships, indexes, and constraints are preserved in git history of the previous root file `Database & Data Model Specification.md`.*
