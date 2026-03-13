# Master Agent 

class Agent_result:     
    def __init__(self, response,actions, config):   # contructor take the arugument 
        self.response= response
        self.actions = actions or []

        self.config= config or []
    def to_dict(self):
        return {
            "assistant_response":self.response,
            "action_item":self.actions,
            "required_connection":self.config
        }