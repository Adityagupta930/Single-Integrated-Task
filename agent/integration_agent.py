from agent_result import Agent_result

class Integration_agent:

    name = "IntegrationAgent"
    capability = [
        "suggest integration",
        "provide requirement"
    ]


    def run(self, prompt, context,guardrails):

        configuration ={
            "Jira_api",
            "Slack_api",
            "Gmail_api",
            "Webhook_api"
        }

        
        return Agent_result(response="intgreation setup",
        actions= ["Intgraete slack", "gmail", "jira"])
    