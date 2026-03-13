def safe(self, prompt):  # WE add the keyword if this keyword in user promt then it dont process it simply say sorry

    blk = [
        "hack",
        "illegal",
        "attack"
    ]

    for i in blk:
        if  i in prompt.lower():
            return False
    return True
