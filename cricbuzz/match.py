class Match:
    def __init__(self, team_a, team_b, match_date, venue, match_type):
        self.team_a = team_a
        self.team_b = team_b
        self.match_date = match_date
        self.venue = venue
        self.match_type = match_type
        self.toss_winner = None
        self.innings = [None, None]

    def start_match(self):
        # Toss
        self.toss_winner = self.toss(self.team_a, self.team_b)

        # Start the innings; there are 2 innings in a match
        for inning in range(1, 3):
            if inning == 1:
                batting_team = self.toss_winner
                bowling_team = self.team_b if self.toss_winner.get_team_name() == self.team_a.get_team_name() else self.team_a
                inning_details = InningDetails(batting_team, bowling_team, self.match_type)
                inning_details.start(-1)
            else:
                bowling_team = self.toss_winner
                batting_team = self.team_b if self.toss_winner.get_team_name() == self.team_a.get_team_name() else self.team_a
                inning_details = InningDetails(batting_team, bowling_team, self.match_type)
                inning_details.start(self.innings[0].get_total_runs())
                if bowling_team.get_total_runs() > batting_team.get_total_runs():
                    bowling_team.is_winner = True

            self.innings[inning - 1] = inning_details

            # Print inning details
            print(f"\nINNING {inning} -- total Run: {batting_team.get_total_runs()}")
            print(f"---Batting ScoreCard : {batting_team.get_team_name()}---")
            batting_team.print_batting_score_card()
            print(f"\n---Bowling ScoreCard : {bowling_team.get_team_name()}---")
            bowling_team.print_bowling_score_card()

        print("\n---WINNER---", end="")
        if self.team_a.is_winner:
            print(self.team_a.get_team_name())
        else:
            print(self.team_b.get_team_name())

    def toss(self, team_a, team_b):
        # Random function to return either teamA or teamB
        return team_a if random.random() < 0.5 else team_b