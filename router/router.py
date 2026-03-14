INTENT_KEYWORDS = {
    "planner":     ["plan", "step", "roadmap", "schedule", "breakdown", "how to"],
    "data":        ["database", "query", "table", "sql", "dataset", "records", "fetch"],
    "integration": ["integrate", "jira", "slack", "gmail", "webhook", "connect", "setup"],
}

HIGH_RISK_KEYWORDS = ["hack", "illegal", "attack", "exploit", "bypass", "drop table", "delete from", "truncate"]


def detect_intent(prompt: str) -> str:
    lowered = prompt.lower()
    for intent, keywords in INTENT_KEYWORDS.items():
        if any(kw in lowered for kw in keywords):
            return intent
    return "general"


def detect_risk(prompt: str) -> str:
    lowered = prompt.lower()
    return "high" if any(kw in lowered for kw in HIGH_RISK_KEYWORDS) else "low"
