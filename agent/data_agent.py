from agent_result import Agent_result

class Data_agent:

    name = "DataqueryAgent"
    capability = [
        "Ask the clarifying the question",
        "Suggest db query plan"
    ]

    def run(self, prompt, context,guardrails):

        clarify="which database table or dataset required"
        query = "select * from employee"
        
        return Agent_result(
            response=clarify,
            actions=[query]
        )