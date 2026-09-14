# n8n Workflow Specification

## Core workflows

| ID | Purpose |
|----|--------|
| `PRH-LEAD-PROCESS-MESSAGE` | Main message processing pipeline |
| `PRH-LEAD-QUALIFY` | Deterministic scoring & classification |
| `PRH-LEAD-NOTIFY-SALES` | HOT lead notifications |
| `PRH-FOLLOWUP-REMINDER` | Due follow-up reminders |
| `PRH-ERROR-HANDLER` | Centralized error handling |
| `PRH-SHEET-SYNC-LEAD` | Optional Google Sheets sync |

## Main flow (PRH-LEAD-PROCESS-MESSAGE)

```text
Webhook → Validate → Idempotency → Context → AI Extraction →
Validate AI → Merge Lead → Missing Fields → Qualify →
Generate Response → Save → Return / Notify
```

## Principle

n8n orchestrates workflows and integrations. FastAPI owns application boundaries. AI does not write directly to the database.

*Full node-level design, payload contracts, and error paths are preserved in git history of the previous root file `n8n Workflow Specification.md`.*
