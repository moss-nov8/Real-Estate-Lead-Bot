# PRD — Real Estate Lead Bot

**Product:** PrimeHomes Realty — Real Estate Lead Bot  
**Document:** Product Requirements Document (PRD)  
**Version:** 1.0  
**Status:** Draft  
**Primary Stack:** React + FastAPI + n8n + SQL Database + Google Sheets  
**Product Type:** AI-powered Lead Management & Qualification System

---

## 1. Executive Summary

PrimeHomes Realty receives potential customer enquiries through digital channels. These enquiries vary significantly in structure, completeness, and intent.

The Real Estate Lead Bot will act as an AI-powered digital receptionist that:

1. Receives customer messages.
2. Understands customer intent.
3. Extracts structured requirements.
4. Identifies missing information.
5. Continues the conversation when necessary.
6. Creates and stores a lead.
7. Scores and classifies the lead.
8. Responds appropriately to the customer.
9. Notifies the sales team when required.
10. Allows sales representatives to follow up.
11. Tracks the lead lifecycle.
12. Maintains a record of customer interactions.

---

## 2–9. Vision, Problem, Goals, Users, Journey, Lead Information

(See original full PRD content in git history of `PrimeHomes_Real_Estate_Lead_Bot_PRD_v1.0.md` for complete detail.)

Core lead information includes customer details, property requirements, transaction intent (BUY/RENT/SELL/INQUIRE), timeline, and status lifecycle (NEW → QUALIFYING → QUALIFIED → … → CONVERTED / LOST / NURTURE).

---

## 10–16. AI, Qualification, Routing, Responses, Handoff, Sales, Lifecycle

AI performs intent detection, entity extraction, missing-information detection, and conversation understanding. Final scoring is deterministic and owned by the application. HOT leads trigger immediate sales notification. Human handoff is supported for high-value or complex cases.

---

## 17–20. Components, Functional & Non-Functional Requirements, Data Ownership

**Components:** React, FastAPI, n8n, PostgreSQL (source of truth), Google Sheets (optional operational reporting).

**Principle:** Google Sheets must not become the authoritative database.

Full functional requirements (FR-001 … FR-017) and non-functional requirements (performance, reliability, security, observability, scalability) are defined in the original PRD.

---

*Note: This is a structured summary placed under `docs/PRD.md` for navigation. The complete original text is preserved in the repository git history from the previous root file `PrimeHomes_Real_Estate_Lead_Bot_PRD_v1.0.md`.*
