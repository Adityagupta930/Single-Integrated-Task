"""
Safety guardrails: checks a prompt against a blocklist.
Accepts optional extra rules loaded from the agent DB.
"""

# Global blocklist applied to every request regardless of agent
GLOBAL_BLOCKLIST = ["hack", "illegal", "attack", "exploit", "bypass"]


def is_safe(prompt: str, extra_rules: list = None) -> bool:
    """
    Return False if the prompt contains any blocked keyword.
    extra_rules: list of {"type": "block_keyword", "value": "..."} dicts from the DB.
    """
    lowered = prompt.lower()

    # Check global blocklist
    if any(kw in lowered for kw in GLOBAL_BLOCKLIST):
        return False

    # Check agent-specific rules loaded from DB
    if extra_rules:
        for rule in extra_rules:
            if rule.get("type") == "block_keyword" and rule["value"].lower() in lowered:
                return False

    return True
