"""
Router: identifies intent and risk level from a user prompt.
Intent drives agent selection; risk is passed into trace info.
"""

# Keywords mapped to intent labels
INTENT_KEYWORDS = {
    "planner": ["plan", "step", "roadmap", "schedule", "breakdown", "how to"],
    "data":    ["database", "query", "table", "sql", "dataset", "records", "fetch"],
    "integration": ["integrate", "jira", "slack", "gmail", "webhook", "connect", "setup"],
}

# Keywords that raise the risk level
HIGH_RISK_KEYWORDS = ["hack", "illegal", "attack", "exploit", "bypass", "drop table",
                      "delete from", "truncate"]


def detect_intent(prompt: str) -> str:
    """Return the best-matching intent label for the given prompt."""
    lowered = prompt.lower()
    for intent, keywords in INTENT_KEYWORDS.items():
        if any(kw in lowered for kw in keywords):
            return intent
    return "general"


def detect_risk(prompt: str) -> str:
    """Return 'high' if the prompt contains risky keywords, else 'low'."""
    lowered = prompt.lower()
    return "high" if any(kw in lowered for kw in HIGH_RISK_KEYWORDS) else "low"
