from agent_result  import Agent_result


class generalAgent:
    name = "genral agent"
    capability = [
        "answer general question",
        "custom support assistant"
    ]

    def run(self, prompt, context, guardrails):
        response = f" i will understand your question {prompt} "

        return Agent_result(response = response,
        action=[])