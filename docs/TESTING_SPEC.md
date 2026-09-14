# TESTING_SPEC.md

# Real Estate Lead Bot — Testing Specification

## 1. Purpose

This document defines the testing strategy for the Real Estate Lead Bot.

Testing should happen continuously alongside development, not only at the end.

---

## 2. Testing Levels

### Backend
- Unit tests
- API / integration tests
- Validation tests
- Authentication / authorization tests
- Business-rule tests (especially lead scoring)

### Database
- Model and relationship tests
- Constraint and index tests
- Migration tests
- Transaction tests

### AI
- Intent detection
- Entity extraction (budget, location, bedrooms, etc.)
- Missing-information detection
- Human-handoff detection
- Failure / invalid-output handling

### n8n Workflows
- Successful happy path
- Duplicate / idempotent events
- AI failure
- API / database failure
- Notification failure

### Frontend
- Chat send / receive
- Loading and error states
- Retry behaviour
- Lead list / details / status updates

### End-to-End
- Complete customer journey
- HOT lead journey (notification)
- Incomplete lead journey (clarification questions)
- Human handoff journey
- Failed AI journey (graceful degradation)

---

## 3. Key Scenarios to Cover

**Customer messages**
- “I want a 3 bedroom apartment in Lekki, budget around 80m.”
- “Looking for land around Ibadan under 20 million.”
- “I need somewhere to rent in Ikeja.”
- “I don’t know exactly what I want yet.”
- “Can I speak with someone?”

**Edge cases**
- Empty or very short messages
- Duplicate messages
- Invalid / hallucinated AI output
- Missing contact information
- Score boundary values (0, 29, 30, 59, 60, 79, 80, 100)

---

## 4. Principles

- Prefer simple, deterministic tests for scoring and business rules.
- AI tests should focus on structured output validation and critical behaviours rather than every possible phrasing.
- Failures in AI or n8n should not lose the customer message or lead record when possible.
- Keep the test suite fast enough to run frequently during development.

---

## 5. Definition of Done for Features

A feature is not complete until:
- Implementation exists
- Relevant validation exists
- Relevant tests pass
- Errors are handled reasonably
- Documentation / task tracker is updated

See also `docs/TASK.md` and `docs/IMPLEMENTATION.md`.
