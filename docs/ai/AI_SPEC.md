# AI Specification

AI is responsible for natural-language understanding and generation. It must not own authentication, database integrity, or final business rules.

## Core tasks

1. Intent detection (BUY, RENT, SELL, LAND, PROPERTY_ENQUIRY, GENERAL_ENQUIRY, HUMAN_AGENT, OTHER)
2. Entity extraction (name, email, phone, property type, bedrooms, location, budget, timeline, etc.)
3. Missing-information detection
4. Clarification question generation
5. Customer response generation
6. Conversation summarization
7. Human-handoff detection

## Output

AI should return structured JSON, for example:

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

The application validates this output before using it.

## Non-responsibilities

AI must not:
- Authenticate or authorize users
- Write directly to PostgreSQL
- Invent property availability or prices
- Make binding commitments without system verification

*Full prompt guidelines, edge cases, and evaluation criteria are preserved in git history of the previous root file `AI Specification.md`.*
