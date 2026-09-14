# Backend — Real Estate Lead Bot

FastAPI application that owns the API, validation, authentication, and business boundaries.

## Structure

```
backend/
├── app/
│   ├── main.py              # FastAPI entrypoint
│   ├── api/v1/              # Versioned API routes
│   ├── core/                # Config, security helpers
│   ├── db/                  # Database session / engine
│   ├── models/              # SQLAlchemy models
│   ├── schemas/             # Pydantic schemas
│   ├── services/            # Business logic
│   └── repositories/        # Data access
├── tests/
├── requirements.txt
└── README.md
```

## Quick start (local)

```bash
# From repository root
cp .env.example .env
# Edit .env with real values

cd backend
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

API docs: http://localhost:8000/docs  
Health: http://localhost:8000/api/v1/health

## Development order

1. Health endpoint (done in scaffolding)
2. Database connection + models
3. Auth
4. Leads / Conversations / Messages APIs
5. Qualification service
6. Integration with n8n webhooks

See `docs/DEVELOPMENT_SETUP.md` and `docs/api/API_SPEC.md` for details.
