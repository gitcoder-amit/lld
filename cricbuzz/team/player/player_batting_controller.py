from collections import deque


class PlayerBattingController:
    def __init__(self, playing11):
        self.yet_to_play = deque(playing11)
        self.striker = None
        self.non_striker = None

    def get_next_player(self):
        if not self.yet_to_play:
            raise Exception("No more players to play")
        
        if self.striker is None:
            self.striker = self.yet_to_play.popleft()
        
        if self.non_striker is None:
            self.non_striker = self.yet_to_play.popleft()

    def get_striker(self):
        return self.striker

    def get_non_striker(self):
        return self.non_striker

    def set_striker(self, player_details):
        self.striker = player_details

    def set_non_striker(self, player_details):
        self.non_striker = player_details

# Example Usage
if __name__ == "__main__":
    # Assuming PlayerDetails has been properly defined elsewhere
    playing11 = [PlayerDetails(f"Player {i}") for i in range(1, 12)]
    batting_controller = PlayerBattingController(playing11)
    
    batting_controller.get_next_player()
    print(f"Striker: {batting_controller.get_striker().name}")
    print(f"Non-Striker: {batting_controller.get_non_striker().name}")
    
    batting_controller.get_next_player()  # Get next players as striker and non-striker are set
    print(f"Striker: {batting_controller.get_striker().name}")
    print(f"Non-Striker: {batting_controller.get_non_striker().name}")
