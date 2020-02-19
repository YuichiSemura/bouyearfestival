class UserStatus:
    random_str = ""
    
    def __init__(self, q1, q2, q3):
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3

    def to_string(self):
        return self.random_str + (
            "q1" + str(self.q1) +
            "q2" + str(self.q2) +
            "q3" + str(self.q3)
        )
    
