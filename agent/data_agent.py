from agent.agent_result import AgentResult


class DataQueryAgent:
    name = "DataQueryAgent"
    capabilities = [
        "Ask clarifying questions about data needs",
        "Propose a safe database query plan without executing it",
        "Identify relevant tables and filters from user intent",
    ]

    def run(self, prompt: str, context: dict, guardrails: list) -> AgentResult:
        # Step 1 — ask clarifying questions to avoid unsafe or incorrect queries
        clarifying_questions = [
            "Which database or data source are you referring to?",
            "What specific table or dataset should be queried?",
            "What filters or conditions should be applied (e.g., date range, user ID)?",
            "Should the results be aggregated (count, sum, average) or raw rows?",
        ]

        # Step 2 — propose a query plan (no execution, safe by design)
        query_plan = [
            "STEP 1: Identify the target table based on your clarification",
            "STEP 2: Define SELECT columns (avoid SELECT * in production)",
            "STEP 3: Apply WHERE filters to scope the result set",
            "STEP 4: Add LIMIT clause to prevent large unintended result sets",
            "STEP 5: Review the query plan with a data owner before execution",
        ]

        return AgentResult(
            response="Before proposing a query, I need a few clarifications:",
            actions=clarifying_questions + ["--- Proposed Query Plan ---"] + query_plan,
            trace={"agent": self.name, "intent": "data_query", "execution": False},
        )
