from agent.agent_result import AgentResult


class GeneralQAAgent:
    name = "GeneralQAAgent"
    capabilities = [
        "Answer general knowledge questions",
        "Provide customer support guidance",
        "Clarify product or service information",
    ]

    def run(self, prompt: str, context: dict, guardrails: list) -> AgentResult:
        for rule in guardrails:
            if rule.get("type") == "block_keyword" and rule["value"].lower() in prompt.lower():
                return AgentResult(
                    response="I'm sorry, I'm unable to assist with that request.",
                    trace={"agent": self.name, "blocked_by": rule["value"]},
                )

        response = (
            f"Thank you for your question. Based on what you've shared: '{prompt}', "
            "here is what I can help you with. Please provide more details if needed "
            "so I can give you the most accurate answer."
        )
        return AgentResult(
            response=response,
            trace={"agent": self.name, "intent": "general_qa"},
        )
