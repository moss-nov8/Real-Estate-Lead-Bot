# UI/UX Specification

## Customer interface

- Chat window
- Message list
- Message input + send
- Loading / typing indicator
- Error + retry states
- Progressive collection of lead information

## Sales dashboard

- Lead list (search, filter, sort)
- Lead details (requirements, score, classification, status, assignment)
- Conversation history
- Follow-up management
- Activity timeline

## Principles

- React is the only UI layer.
- No direct database access from the frontend.
- Business rules and scoring stay on the backend.
- Clear loading and error states for every network action.

*Full screen-by-screen and component specifications are preserved in git history of the previous root file `UI-UX Specification.md`.*
