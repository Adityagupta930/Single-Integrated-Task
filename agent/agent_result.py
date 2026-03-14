class AgentResult:
    def __init__(self, response: str, actions: list = None, config: dict = None, trace: dict = None):
        self.response = response
        self.actions = actions or []
        self.config = config or {}
        self.trace = trace or {}

    def to_dict(self) -> dict:
        return {
            "assistant_response": self.response,
            "action_items": self.actions,
            "required_connection_config": self.config,
            "trace": self.trace,
        }
