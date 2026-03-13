# Is is router function which decide based on the user prompt which Agent is called


def detector(self, prompt):
    prompt= prompt.lower()

    if "plan" in prompt or "step" in prompt:
        return "planner"                      # planner agent called


    elif  "database" in prompt or "query" in prompt:
        return "data"        # data agent called

    elif  "integrate" in prompt :
        return "integration"  # integrtion agent called

    else:
        return "general"   # if none of the prompt is matched tehn i defualt called genrqal agent



