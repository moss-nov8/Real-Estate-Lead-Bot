# LEAD_QUALIFICATION_SPEC.md

# Real Estate Lead Bot — Lead Qualification & Scoring

## 1. Purpose

This document defines how the Real Estate Lead Bot should qualify incoming real estate leads.

The objective is simple:

> Determine how ready and valuable a customer appears to be so the sales team knows which leads deserve the most immediate attention.

The qualification system should be:

- Simple.
- Understandable.
- Consistent.
- Easy to modify.
- Easy to explain to the sales team.

The system uses a score from 0–100 and a classification of HOT / WARM / COLD / UNQUALIFIED.

AI extracts the information. The application applies the scoring rules.

---

## 2. Score Breakdown (Total 100)

| Signal | Max Points |
|--------|------------|
| Intent | 20 |
| Property Requirement | 15 |
| Location | 15 |
| Budget | 20 |
| Timeline | 20 |
| Contact Information | 10 |
| **TOTAL** | **100** |

---

## 3. Classification

```text
80–100 → HOT
60–79  → WARM
30–59  → COLD
0–29   → UNQUALIFIED
```

---

## 4. Scoring Rules (Summary)

### Intent (20)
- Clear BUY or RENT with specific details: 20
- Clear intent but incomplete: 15
- Vague interest: 5–10
- No clear intent: 0

### Property Requirement (15)
- Specific type + bedrooms: 15
- Type only: 10
- Very vague: 0–5

### Location (15)
- Specific area/neighbourhood: 15
- City only: 10
- Unknown: 0

### Budget (20)
- Clear max or range: 20
- Approximate: 15
- Missing: 0

### Timeline (20)
- Immediate / within 1 month: 20
- Within 3 months: 15
- Within 6 months: 10
- Researching / unknown: 0–5

### Contact (10)
- Phone or email provided: 10
- Missing: 0

---

## 5. Implementation Principle

```text
AI
 ↓
Structured extraction
 ↓
Validation
 ↓
Qualification service (deterministic rules)
 ↓
Score + Classification
 ↓
Store + notify if HOT
```

The full detailed rules and examples are maintained in the original specification content. The scoring must remain explainable and auditable.

---

## 6. Notes

- Do not invent missing fields.
- Score can be recalculated when new information arrives.
- HOT leads trigger immediate sales notification.
