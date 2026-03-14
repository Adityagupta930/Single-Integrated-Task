AGENT_DB: dict = {
    "general": {
        "instruction": (
            "You are a professional customer support assistant. "
            "Be helpful, polite, and accurate. Never guess — ask for clarification when needed."
        ),
        "guardrails": [
            {"type": "block_keyword", "value": "hack"},
            {"type": "block_keyword", "value": "illegal"},
            {"type": "block_keyword", "value": "attack"},
            {"type": "block_keyword", "value": "exploit"},
        ],
    },
    "planner": {
        "instruction": (
            "You are a task planning assistant. Break user goals into clear, ordered action steps. "
            "Be specific and realistic."
        ),
        "guardrails": [
            {"type": "block_keyword", "value": "hack"},
            {"type": "block_keyword", "value": "illegal"},
        ],
    },
    "data": {
        "instruction": (
            "You are a data query assistant. Ask clarifying questions before proposing any query. "
            "Never execute queries — only propose plans."
        ),
        "guardrails": [
            {"type": "block_keyword", "value": "drop table"},
            {"type": "block_keyword", "value": "delete from"},
            {"type": "block_keyword", "value": "truncate"},
        ],
    },
    "integration": {
        "instruction": (
            "You are an integration assistant. Suggest relevant integrations and provide "
            "the required configuration fields. Never expose real credentials."
        ),
        "guardrails": [
            {"type": "block_keyword", "value": "hack"},
            {"type": "block_keyword", "value": "bypass"},
        ],
    },
}


def get_agent_config(intent: str) -> dict:
    return AGENT_DB.get(intent, AGENT_DB["general"])
