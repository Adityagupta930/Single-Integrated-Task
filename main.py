from fastapi import FastAPI
from router.router import detector
from safety.guardrails import safe

from agent.gneral_agent import generalAgent
from agent.task_agent import taskAgent
from agent.data_agent import Data_agent
from agent.integration_agent import Integration_agent


app= FastAPI()



agents= {
    "general":generalAgent,
    "planner": taskAgent,
    "integration": Integration_agent,
    "data": Data_agent
}


@app.post("/ask")
def ask(prompt:str):
    if not safe(prompt):
        return {"assistant_response":"sorry . i cannot assist you becuase of the safety issue"}

    intent = detector(prompt)
    agent = agent[intent]
    res= agent.run(prompt,{},[])
    return res.to_dict()