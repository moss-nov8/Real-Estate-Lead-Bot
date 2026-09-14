# Real Estate Lead Bot

**PrimeHomes Realty**

> An AI-powered real estate lead management system that receives customer enquiries, understands their requirements, qualifies leads, stores customer information, and helps the sales team follow up efficiently.

---

## Overview

The Real Estate Lead Bot acts as a digital receptionist for PrimeHomes Realty.

Customers can send natural-language messages such as:

> "Hi, I'm looking for a 3-bedroom apartment around Lekki. My budget is around ₦80 million."

The system:

1. Receives the message
2. Understands intent and extracts structured requirements
3. Identifies missing information and asks clarifying questions when needed
4. Creates / updates the lead
5. Scores and classifies the lead (HOT / WARM / COLD / UNQUALIFIED)
6. Responds to the customer
7. Notifies the sales team when required
8. Supports human follow-up and full conversation history

---

## Architecture

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

| Layer        | Technology   | Responsibility                          |
|--------------|--------------|-----------------------------------------|
| Frontend     | React        | Customer chat + sales dashboard         |
| Backend      | FastAPI      | API, validation, business rules, auth   |
| Automation   | n8n          | Workflows, AI orchestration, notifications |
| Database     | PostgreSQL   | Source of truth                         |
| AI           | LLM          | Understanding, extraction, responses    |
| Reporting    | Google Sheets| Optional operational projection         |

**Principle:** Use the simplest technology that correctly solves the problem.

---

## Repository Structure

```text
real-estate-lead-bot/
│
├── frontend/                 # React application
├── backend/                  # FastAPI application
├── n8n/                      # Workflow definitions
├── database/                 # Migrations / seeds (shared)
├── tests/                    # Cross-cutting tests
├── docs/                     # All specifications & guides
│   ├── PRD.md
│   ├── DEVELOPMENT_SETUP.md
│   ├── IMPLEMENTATION.md
│   ├── TASK.md
│   ├── database/
│   ├── api/
│   ├── automation/
│   ├── ai/
│   ├── frontend/
│   ├── architecture/
│   └── deployment/
│
├── .env.example
├── .gitignore
├── docker-compose.yml
├── LICENSE
└── README.md
```

---

## Quick Start (Local)

### 1. Clone & environment

```bash
git clone https://github.com/moss-nov8/Real-Estate-Lead-Bot.git
cd Real-Estate-Lead-Bot
cp .env.example .env
# Edit .env with your values
```

### 2. Start infrastructure

```bash
docker compose up -d postgres n8n
```

### 3. Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

- API docs: http://localhost:8000/docs  
- Health: http://localhost:8000/api/v1/health

### 4. Frontend (when ready)

```bash
cd frontend
npm install
npm run dev
```

---

## Documentation

All product and technical documentation lives under [`docs/`](./docs/).

| Document | Description |
|----------|-------------|
| [PRD](./docs/PRD.md) | Product requirements |
| [Development Setup](./docs/DEVELOPMENT_SETUP.md) | How to develop |
| [Implementation Log](./docs/IMPLEMENTATION.md) | Progress & decisions |
| [Task Tracker](./docs/TASK.md) | Current tasks |
| [Database Design](./docs/database/DATABASE_DESIGN.md) | Schema & models |
| [API Spec](./docs/api/API_SPEC.md) | Endpoints & contracts |
| [n8n Workflow Spec](./docs/automation/N8N_WORKFLOW_SPEC.md) | Automation design |
| [AI Spec](./docs/ai/AI_SPEC.md) | Extraction & responses |
| [UI/UX Spec](./docs/frontend/UI_UX_SPEC.md) | Screens & components |
| [Architecture](./docs/architecture/System_Architecture_Document.md) | System design |
| [Deployment](./docs/deployment/DEPLOYMENT_SPEC.md) | VPS / production |

---

## Development Phases

1. **Foundation** — Repository structure, env, Docker (current)
2. **Database** — Models, migrations, seed data
3. **Backend APIs** — Health → Auth → Leads → Conversations → Messages
4. **Customer Interface** — React chat
5. **n8n + AI** — Message processing workflow
6. **Lead Qualification** — Scoring service
7. **Sales Dashboard** — Lead list, details, follow-ups
8. **Testing & Hardening**
9. **VPS Deployment**

See [`docs/TASK.md`](./docs/TASK.md) and [`docs/IMPLEMENTATION.md`](./docs/IMPLEMENTATION.md) for the live tracker.

---

## License

See [LICENSE](./LICENSE).
