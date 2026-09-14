# TESTING_SPEC.md

# Real Estate Lead Bot — Testing Specification

## 1. Purpose

This document defines the testing strategy for the Real Estate Lead Bot.

Testing should happen alongside development rather than only at the end.

---

## 2. Testing Levels

### Backend
- Unit tests
- API tests
- Validation tests
- Authentication tests
- Database / model tests

### AI
- Extraction tests
- Intent tests
- Missing-field tests
- Human-handoff tests
- Failure / timeout tests

### n8n
- Workflow success
- Duplicate events
- AI failure
- API failure
- Notification failure

### Frontend
- Chat tests
- Error / loading / retry states
- Lead dashboard tests

### End-to-End
- Complete customer journey
- HOT lead journey
- Incomplete lead journey
- Human handoff journey
- Failed AI journey

---

## 3. Backend Test Focus

- Health endpoint
- Authentication
- Lead creation / retrieval / update
- Message creation
- Validation and authorization
- Lead qualification scoring

---

## 4. AI Test Scenarios

Examples to cover:

- BUY scenario (3-bedroom Lekki, budget given)
- RENT scenario
- LAND scenario
- Missing information
- Human-agent request
- Unclear / ambiguous message
- Hallucination prevention

---

## 5. n8n Workflow Tests

- Successful end-to-end processing
- Invalid input
- Duplicate event / idempotency
- AI failure handling
- Database/API failure
- Notification failure
- Google Sheets failure (non-blocking)

---

## 6. Frontend Tests

- Send message
- Receive response
- Loading state
- Error state + retry
- Lead list / details / update

---

## 7. Definition of Done for Tests

A feature is not complete until relevant tests pass and failure paths are handled.

See also the original detailed TESTING_SPEC content in git history if needed for expanded test cases.
