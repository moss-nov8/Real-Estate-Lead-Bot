# Database — Real Estate Lead Bot

PostgreSQL is the primary source of truth.

## Planned tables

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

## Structure

```
database/
├── migrations/   # Alembic (or SQL) migration files
├── seeds/        # Seed data scripts
└── README.md
```

Alembic will live under `backend/` for convenience (standard FastAPI + SQLAlchemy layout).  
This folder can hold shared SQL scripts, ER diagrams, and seed data.

See `docs/database/DATABASE_DESIGN.md` for the full data model.
