# Setup & Run — Real Estate Lead Bot (with n8n)

## Architecture

```text
Browser (React chat)
    → POST /api/v1/messages
        → FastAPI (store message + lead)
            → POST n8n webhook  /lead-process-message
                → (AI extraction + reply)
            ← bot reply JSON
        ← MessageResponse
```

## Quick start

### 1. Infrastructure
```bash
cp .env.example .env
docker compose up -d postgres n8n
```

### 2. Backend
```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python scripts_create_tables.py
uvicorn app.main:app --reload --port 8000
```

### 3. n8n
- Open http://localhost:5678
- Import `n8n/workflows/lead-process-message.example.json`
- Activate the workflow
- Webhook path: `lead-process-message`
- FastAPI calls: `http://localhost:5678/webhook/lead-process-message`

Expected n8n response:
```json
{
  "reply": "Thanks! ...",
  "lead_updates": {
    "transaction_type": "BUY",
    "property_type": "APARTMENT",
    "bedrooms": 3,
    "location": "Lekki",
    "budget_max": 80000000
  }
}
```

### 4. Frontend
```bash
cd frontend
npm install
npm run dev
```
Open http://localhost:5173 — chat (orange/yellow). `/leads` for sales list.

### 5. Test
Send: "3-bedroom apartment in Lekki, budget 80 million"
Check n8n Executions and `/leads`.

If n8n is down, FastAPI still saves the message and returns a fallback reply.

See full details in this file on the repo for troubleshooting.
