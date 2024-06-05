class Person:
    # Placeholder for Person class
    def __init__(self, name):
        self.name = name

class BattingScoreCard:
    # Placeholder for BattingScoreCard class
    def __init__(self):
        self.totalRuns = 0
        self.totalBallsPlayed = 0
        self.totalFours = 0
        self.totalSix = 0
        self.wicketDetails = None

class BowlingScoreCard:
    # Placeholder for BowlingScoreCard class
    def __init__(self):
        self.totalOversCount = 0
        self.runsGiven = 0
        self.wicketsTaken = 0

class PlayerDetails:
    def __init__(self, person, player_type):
        self.person = person
        self.player_type = player_type
        self.batting_score_card = BattingScoreCard()
        self.bowling_score_card = BowlingScoreCard()

    def print_batting_score_card(self):
        wicket_taken_by = "not out" if self.batting_score_card.wicket_details is None else self.batting_score_card.wicket_details.taken_by.person.name
        print(f"PlayerName: {self.person.name} -- totalRuns: {self.batting_score_card.totalRuns} -- totalBallsPlayed: {self.batting_score_card.totalBallsPlayed} -- 4s: {self.batting_score_card.totalFours} -- 6s: {self.batting_score_card.totalSix} -- outby: {wicket_taken_by}")

    def print_bowling_score_card(self):
        print(f"PlayerName: {self.person.name} -- totalOversThrown: {self.bowling_score_card.totalOversCount} -- totalRunsGiven: {self.bowling_score_card.runsGiven} -- WicketsTaken: {self.bowling_score_card.wicketsTaken}")

# Example Usage
if __name__ == "__main__":
    # Assuming Person and PlayerType have been properly defined elsewhere
    person = Person("Player 1")
    player_type = PlayerType("Bowler")
    player_details = PlayerDetails(person, player_type)

    player_details.batting_score_card.totalRuns = 50
    player_details.batting_score_card.totalBallsPlayed = 30
    player_details.batting_score_card.totalFours = 5
    player_details.batting_score_card.totalSix = 2
    player_details.batting_score_card.wicket_details = None

    player_details.print_batting_score_card()
