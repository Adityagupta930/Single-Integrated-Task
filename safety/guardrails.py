GLOBAL_BLOCKLIST = ["hack", "illegal", "attack", "exploit", "bypass"]


def is_safe(prompt: str, extra_rules: list = None) -> bool:
    lowered = prompt.lower()

    if any(kw in lowered for kw in GLOBAL_BLOCKLIST):
        return False

    if extra_rules:
        for rule in extra_rules:
            if rule.get("type") == "block_keyword" and rule["value"].lower() in lowered:
                return False

    return True
