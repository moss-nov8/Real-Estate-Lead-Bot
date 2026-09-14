# TASK.md

**Overall Status:** 🟡 Backend + Frontend MVP implemented — configure n8n & test locally

## Completed
- [x] Repository structure
- [x] SQLAlchemy models (leads, conversations, messages)
- [x] Lead / Conversation / Message APIs
- [x] Deterministic qualification scoring
- [x] n8n webhook client
- [x] React chat (orange/yellow) + leads page
- [x] Example n8n workflow + SETUP_AND_RUN.md

## Your next steps
1. Follow SETUP_AND_RUN.md
2. docker compose up -d postgres n8n
3. Backend: venv, pip install, scripts_create_tables.py, uvicorn
4. Import n8n workflow and activate
5. Frontend: npm install && npm run dev
6. Test chat end-to-end

## Still open
- [ ] JWT auth
- [ ] Full users/roles/follow_ups tables
- [ ] Real AI node in n8n (replace placeholder)
- [ ] HOT sales notification workflow
