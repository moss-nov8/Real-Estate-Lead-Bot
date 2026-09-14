# Frontend — Real Estate Lead Bot

React application for:

- Customer chat interface
- Sales dashboard
- Lead management & follow-ups

## Recommended structure

```
frontend/
├── src/
│   ├── components/
│   │   ├── ui/          # Shared UI primitives
│   │   ├── chat/        # Customer chat components
│   │   ├── leads/       # Lead list / cards
│   │   ├── dashboard/   # Dashboard widgets
│   │   └── followups/   # Follow-up UI
│   ├── pages/
│   │   ├── customer/    # Customer-facing pages
│   │   ├── auth/        # Login / auth
│   │   └── dashboard/   # Sales dashboard pages
│   ├── services/        # API client
│   ├── hooks/
│   ├── types/
│   ├── utils/
│   └── app/             # App shell, providers, routes
├── package.json
└── README.md
```

## Quick start

```bash
cd frontend
npm install
npm run dev
```

Default Vite port is usually http://localhost:5173

Set `VITE_API_BASE_URL` in the root `.env` (or frontend `.env`) to point at the FastAPI backend.

See `docs/frontend/UI_UX_SPEC.md` for screen and component specifications.
