# AI Specification — Real Estate Lead Bot

## Purpose

Defines what the AI layer must understand, extract, generate, and the boundaries it must not cross.

## Responsibilities

- Intent detection (BUY, RENT, SELL, LAND, PROPERTY_ENQUIRY, HUMAN_AGENT, OTHER)
- Entity extraction (property type, bedrooms, location, budget, timeline, contact details)
- Missing-information detection
- Clarification question generation
- Customer response generation
- Conversation summarization
- Human-handoff detection

## Non-responsibilities

AI must **not**:
- Authenticate or authorize users
- Write directly to PostgreSQL
- Decide final business rules or lead scores (scoring is deterministic in the application)
- Invent property availability, prices, or commitments
- Confirm bookings without system verification

## Expected Structured Output Example

```json
{
  "intent": "BUY",
  "transaction_type": "BUY",
  "property_type": "APARTMENT",
  "bedrooms": 3,
  "location": "Lekki",
  "budget_min": null,
  "budget_max": 80000000,
  "currency": "NGN",
  "timeline": "WITHIN_3_MONTHS",
  "customer_name": null,
  "email": null,
  "phone": null,
  "confidence": 0.96
}
```

## Principles

- Preserve unknown fields as null — never invent values.
- Maintain conversation context across turns.
- Prefer short, helpful, professional responses.
- Escalate to human when confidence is low, customer requests it, or the case is complex/high-value.

The full original AI Specification content remains available in git history.
