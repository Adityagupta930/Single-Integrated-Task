def safe(self, prompt):

    blk = [
        "hack",
        "illegal",
        "attack"
    ]

    for i in blk:
        if  i in prompt.lower():
            return False
    return True
