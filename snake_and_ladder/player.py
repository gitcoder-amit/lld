class Player:
    def __init__(self, id, current_position):
        self.id = id
        self.current_position = current_position

    # Getters and setters
    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_current_position(self):
        return self.current_position

    def set_current_position(self, current_position):
        self.current_position = current_position
