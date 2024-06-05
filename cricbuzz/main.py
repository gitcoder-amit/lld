class Main:
    def main(self):
        team_a = self.add_team("India")
        team_b = self.add_team("SriLanka")

        match_type = T20MatchType()
        match = Match(team_a, team_b, None, "SMS STADIUM", match_type)
        match.start_match()

    def add_team(self, name: str) -> Team:
        player_details = deque()

        p1 = self.add_player(name + "1", PlayerType.ALLROUNDER)
        p2 = self.add_player(name + "2", PlayerType.ALLROUNDER)
        p3 = self.add_player(name + "3", PlayerType.ALLROUNDER)
        p4 = self.add_player(name + "4", PlayerType.ALLROUNDER)
        p5 = self.add_player(name + "5", PlayerType.ALLROUNDER)
        p6 = self.add_player(name + "6", PlayerType.ALLROUNDER)
        p7 = self.add_player(name + "7", PlayerType.ALLROUNDER)
        p8 = self.add_player(name + "8", PlayerType.ALLROUNDER)
        p9 = self.add_player(name + "9", PlayerType.ALLROUNDER)
        p10 = self.add_player(name + "10", PlayerType.ALLROUNDER)
        p11 = self.add_player(name + "11", PlayerType.ALLROUNDER)

        player_details.extend([p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11])

        bowlers = [p8, p9, p10, p11]

        team = Team(name, player_details, [], bowlers)
        return team

    def add_player(self, name: str, player_type: PlayerType) -> PlayerDetails:
        person = Person(name)
        player_details = PlayerDetails(person, player_type)
        return player_details

if __name__ == "__main__":
    main_instance = Main()
    main_instance.main()