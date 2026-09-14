# n8n Workflows — Real Estate Lead Bot

n8n handles workflow orchestration, AI processing, notifications, and integrations.

## Planned workflows

| Workflow ID | File | Purpose |
|-------------|------|---------|
| `PRH-LEAD-PROCESS-MESSAGE` | `workflows/lead-process-message.json` | Main message processing pipeline |
| `PRH-LEAD-QUALIFY` | `workflows/lead-qualify.json` | Deterministic scoring & classification |
| `PRH-LEAD-NOTIFY-SALES` | `workflows/lead-notify-sales.json` | HOT lead notifications |
| `PRH-FOLLOWUP-REMINDER` | `workflows/followup-reminder.json` | Due follow-up reminders |
| `PRH-ERROR-HANDLER` | `workflows/error-handler.json` | Centralized error handling |
| `PRH-SHEET-SYNC-LEAD` | (optional) | Google Sheets sync |

## Local n8n

```bash
# From repository root (with Docker)
docker compose up -d n8n

# Open http://localhost:5678
```

Import JSON workflow files from `workflows/` once they are created.

**Principle:** FastAPI owns application boundaries. n8n orchestrates automation. AI does not write directly to the database.

See `docs/automation/N8N_WORKFLOW_SPEC.md` for full specifications.
