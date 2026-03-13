def detector(self, prompt):
    prompt= prompt.lower()

    if "plan" in prompt or "step" in prompt:
        return "planner"


    elif  "database" in prompt or "query" in prompt:
        return "data"

    elif  "integrate" in prompt :
        return "integration"

    else:
        return "general"



