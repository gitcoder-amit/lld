class Cell:
    def __init__(self, jump=None):
        self.jump = jump

    # Getters and setters
    def get_jump(self):
        return self.jump

    def set_jump(self, jump):
        self.jump = jump
