from agent_result import Agent_result

class Data_agent:

    name = "DataqueryAgent"   # Name of the agent
    capability = [                                # Agent prompt
        "Ask the clarifying the question",
        "Suggest db query plan"
    ]

    def run(self, prompt, context,guardrails):

        clarify="which database table or dataset required"   # Agent argument which pass to the master agent 
        query = "select * from employee"
        
        return Agent_result(
            response=clarify,
            actions=[query]
        )