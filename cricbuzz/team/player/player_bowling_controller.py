from collections import deque

class PlayerBowlingController:
    def __init__(self, bowlers):
        self.bowlers_list = deque(bowlers)
        self.bowler_vs_over_count = {bowler: 0 for bowler in bowlers}
        self.current_bowler = None

    def get_next_bowler(self, max_over_count_per_bowler):
        player_details = self.bowlers_list.popleft()
        if self.bowler_vs_over_count[player_details] + 1 == max_over_count_per_bowler:
            self.current_bowler = player_details
        else:
            self.current_bowler = player_details
            self.bowlers_list.append(player_details)
            self.bowler_vs_over_count[player_details] += 1

    def get_current_bowler(self):
        return self.current_bowler

# Example Usage
if __name__ == "__main__":
    # Assuming PlayerDetails has been properly defined elsewhere
    bowlers = [PlayerDetails(f"Bowler {i}") for i in range(1, 6)]
    bowling_controller = PlayerBowlingController(bowlers)
    
    for i in range(4):
        bowling_controller.get_next_bowler(2)  # Get next bowler, allowing 2 overs per bowler
        print(f"Current Bowler: {bowling_controller.get_current_bowler().name}")
