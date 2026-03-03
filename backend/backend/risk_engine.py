def calculate_risk(impact: int, probability: int) -> dict:
    score = impact * probability

    if score <= 4:
        level = "Low"
        escalation = "Monitor"
    elif score <= 9:
        level = "Medium"
        escalation = "Notify Manager"
    elif score <= 15:
        level = "High"
        escalation = "Escalate to Compliance"
    else:
        level = "Critical"
        escalation = "Immediate Executive Escalation"

    return {
        "risk_score": score,
        "risk_level": level,
        "recommended_action": escalation
    }
