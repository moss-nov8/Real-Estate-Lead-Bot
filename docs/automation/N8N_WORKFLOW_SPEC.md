# n8n Workflow Specification — Real Estate Lead Bot

## Core Workflows

| ID | Purpose |
|----|---------|
| `PRH-LEAD-PROCESS-MESSAGE` | Main message pipeline (validate → AI → merge → qualify → respond → notify) |
| `PRH-LEAD-QUALIFY` | Deterministic scoring & classification |
| `PRH-LEAD-NOTIFY-SALES` | HOT lead notifications |
| `PRH-FOLLOWUP-REMINDER` | Due follow-up reminders |
| `PRH-ERROR-HANDLER` | Centralized error handling |
| `PRH-SHEET-SYNC-LEAD` | Optional Google Sheets sync |

## Principle

FastAPI owns application boundaries. n8n orchestrates automation and integrations. AI does not write directly to the database.

## First Workflow to Build

`PRH-LEAD-PROCESS-MESSAGE`:

```text
Webhook → Validate → Idempotency → Context → AI Extraction → Validate AI → Merge Lead → Missing Fields → Qualify → Generate Response → Save → Return
```

Full original n8n Workflow Specification content is available in git history.
