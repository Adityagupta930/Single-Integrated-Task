from agent_result import Agent_result



class taskAgent:
    name = "Task planner agent"
    capability = [
        "create a structured plan",
        "break task into step"
    ]

    

    def run(self, prompt, context,guardrails):

        steps=[
            "understand the task "
            "identify the required task "
            "execute the step",
            "validate the resukt"
        ]
        return Agent_result(response="here is a structured task plan",
                            actions= steps
                            
                            )