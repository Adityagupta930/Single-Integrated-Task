from agent.agent_result import AgentResult


class TaskPlannerAgent:
    name = "TaskPlannerAgent"
    capabilities = [
        "Break a goal into structured action steps",
        "Produce prioritized task plans",
        "Identify dependencies between steps",
    ]

    def run(self, prompt: str, context: dict, guardrails: list) -> AgentResult:
        steps = [
            f"1. Understand the goal: '{prompt}'",
            "2. Identify required resources and dependencies",
            "3. Break the goal into smaller, actionable sub-tasks",
            "4. Assign priority and estimated effort to each sub-task",
            "5. Execute sub-tasks in order and validate each result",
            "6. Review the final outcome against the original goal",
        ]
        return AgentResult(
            response="Here is your structured action plan:",
            actions=steps,
            trace={"agent": self.name, "intent": "task_planning", "steps_count": len(steps)},
        )
