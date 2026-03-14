from fastapi import FastAPI
from pydantic import BaseModel

from router.router import detect_intent, detect_risk
from safety.guardrails import is_safe
from db.agent_db import get_agent_config

from agent.gneral_agent import GeneralQAAgent
from agent.task_agent import TaskPlannerAgent
from agent.data_agent import DataQueryAgent
from agent.integration_agent import IntegrationAgent

app = FastAPI(title="Dynamic Agent System")

AGENTS = {
    "general":     GeneralQAAgent(),
    "planner":     TaskPlannerAgent(),
    "data":        DataQueryAgent(),
    "integration": IntegrationAgent(),
}


class PromptRequest(BaseModel):
    prompt: str


@app.post("/ask")
def ask(request: PromptRequest):
    prompt = request.prompt

    intent = detect_intent(prompt)
    risk = detect_risk(prompt)

    db_config = get_agent_config(intent)
    instruction = db_config["instruction"]
    guardrails = db_config["guardrails"]

    if not is_safe(prompt, extra_rules=guardrails):
        return {
            "assistant_response": "I'm sorry, I'm unable to assist with that request due to safety guidelines.",
            "action_items": [],
            "required_connection_config": {},
            "trace": {
                "intent": intent,
                "risk": "high",
                "agent_selected": None,
                "blocked": True,
            },
        }

    agent = AGENTS[intent]
    result = agent.run(prompt, context={"instruction": instruction}, guardrails=guardrails)

    result.trace.update({
        "intent": intent,
        "risk": risk,
        "agent_selected": agent.name,
        "blocked": False,
        "db_instruction_applied": instruction,
    })

    return result.to_dict()
