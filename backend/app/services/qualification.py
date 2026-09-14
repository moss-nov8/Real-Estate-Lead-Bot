"""Deterministic lead scoring (AI extracts data; this service scores)."""

from dataclasses import dataclass

from app.models.lead import Lead, LeadClassification, Timeline, TransactionType


@dataclass
class ScoreResult:
    score: int
    classification: LeadClassification
    reasons: list[str]


def score_lead(lead: Lead) -> ScoreResult:
    score = 0
    reasons: list[str] = []

    if lead.transaction_type in (TransactionType.BUY, TransactionType.RENT):
        score += 20
        reasons.append("Clear BUY/RENT intent (+20)")
    elif lead.transaction_type == TransactionType.SELL:
        score += 10
        reasons.append("SELL intent (+10)")
    elif lead.transaction_type == TransactionType.INQUIRE:
        score += 5
        reasons.append("General enquiry (+5)")

    if lead.property_type and lead.bedrooms:
        score += 15
        reasons.append("Specific property + bedrooms (+15)")
    elif lead.property_type:
        score += 10
        reasons.append("Property type only (+10)")

    if lead.location:
        if len(lead.location.strip()) >= 4:
            score += 15
            reasons.append(f"Location provided: {lead.location} (+15)")
        else:
            score += 8
            reasons.append("Vague location (+8)")

    if lead.budget_max is not None or lead.budget_min is not None:
        score += 20
        reasons.append("Budget provided (+20)")

    timeline_scores = {
        Timeline.IMMEDIATE: 20,
        Timeline.WITHIN_1_MONTH: 18,
        Timeline.WITHIN_3_MONTHS: 15,
        Timeline.WITHIN_6_MONTHS: 10,
        Timeline.RESEARCHING: 5,
        Timeline.UNKNOWN: 0,
    }
    t_score = timeline_scores.get(lead.timeline, 0)
    if t_score:
        score += t_score
        reasons.append(f"Timeline {lead.timeline.value} (+{t_score})")

    if lead.phone or lead.email:
        score += 10
        reasons.append("Contact info provided (+10)")

    score = min(100, max(0, score))

    if score >= 80:
        classification = LeadClassification.HOT
    elif score >= 60:
        classification = LeadClassification.WARM
    elif score >= 30:
        classification = LeadClassification.COLD
    else:
        classification = LeadClassification.UNQUALIFIED

    return ScoreResult(score=score, classification=classification, reasons=reasons)


def apply_score(lead: Lead) -> Lead:
    result = score_lead(lead)
    lead.score = result.score
    lead.classification = result.classification
    lead.score_reasons = "; ".join(result.reasons)
    return lead
