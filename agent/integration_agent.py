from agent.agent_result import AgentResult


class IntegrationAgent:
    name = "IntegrationAgent"
    capabilities = [
        "Suggest relevant third-party integrations",
        "Provide required configuration fields for each integration",
        "Guide setup for Jira, Slack, Gmail, and Webhooks",
    ]

    # Required config fields per integration type
    INTEGRATION_CONFIGS = {
        "Jira": {
            "base_url": "<your-jira-domain>.atlassian.net",
            "api_token": "<jira-api-token>",
            "project_key": "<PROJECT_KEY>",
            "issue_type": "Task",
        },
        "Slack": {
            "bot_token": "<slack-bot-token>",
            "channel_id": "<channel-id>",
            "signing_secret": "<slack-signing-secret>",
        },
        "Gmail": {
            "client_id": "<google-oauth-client-id>",
            "client_secret": "<google-oauth-client-secret>",
            "refresh_token": "<oauth-refresh-token>",
            "sender_email": "<sender@example.com>",
        },
        "Webhook": {
            "endpoint_url": "<https://your-endpoint.com/webhook>",
            "auth_header": "Authorization: Bearer <token>",
            "payload_format": "JSON",
        },
    }

    def run(self, prompt: str, context: dict, guardrails: list) -> AgentResult:
        prompt_lower = prompt.lower()

        # Select integrations relevant to the prompt; default to all if none matched
        selected = [name for name in self.INTEGRATION_CONFIGS if name.lower() in prompt_lower]
        if not selected:
            selected = list(self.INTEGRATION_CONFIGS.keys())

        actions = [f"Set up {name} integration" for name in selected]
        config = {name: self.INTEGRATION_CONFIGS[name] for name in selected}

        return AgentResult(
            response=f"Based on your request, I recommend the following integration(s): {', '.join(selected)}.",
            actions=actions,
            config=config,
            trace={"agent": self.name, "intent": "integration_setup", "integrations": selected},
        )
