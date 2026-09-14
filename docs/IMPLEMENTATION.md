# IMPLEMENTATION.md

**Status:** Backend + Frontend MVP + n8n hook ready for local test (2026-09-14)

## Backend
- Models: Lead, Conversation, Message
- APIs: health, leads CRUD/qualify, conversations, messages
- Qualification service (0–100 → HOT/WARM/COLD/UNQUALIFIED)
- n8n client posts to `/webhook/lead-process-message`

## Frontend
- Vite React TS, orange/yellow theme
- Chat at `/`, leads at `/leads`

## Flow
Chat → POST /messages → DB → n8n → reply + lead_updates → score → UI

Fallback bot reply if n8n unavailable.

See SETUP_AND_RUN.md.
