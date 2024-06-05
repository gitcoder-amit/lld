from LLDCricbuzz.Match.Inning import RunType

class BattingScoreUpdater(ScoreUpdaterObserver):
    def update(self, ballDetails):
        run = 0

        if ballDetails.runType == RunType.ONE:
            run = 1
        elif ballDetails.runType == RunType.TWO:
            run = 2
        elif ballDetails.runType == RunType.FOUR:
            run = 4
            ballDetails.playedBy.battingScoreCard.totalFours += 1
        elif ballDetails.runType == RunType.SIX:
            run = 6
            ballDetails.playedBy.battingScoreCard.totalSix += 1

        ballDetails.playedBy.battingScoreCard.totalRuns += run
        ballDetails.playedBy.battingScoreCard.totalBallsPlayed += 1

        if ballDetails.wicket is not None:
            ballDetails.playedBy.battingScoreCard.wicketDetails = ballDetails.wicket
