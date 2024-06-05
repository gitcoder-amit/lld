from LLDCricbuzz.Match.Inning import BallType, RunType

class BowlingScoreUpdater(ScoreUpdaterObserver):
    def update(self, ballDetails):
        if ballDetails.ballNumber == 6 and ballDetails.ballType == BallType.NORMAL:
            ballDetails.bowledBy.bowlingScoreCard.totalOversCount += 1

        if ballDetails.runType == RunType.ONE:
            ballDetails.bowledBy.bowlingScoreCard.runsGiven += 1
        elif ballDetails.runType == RunType.TWO:
            ballDetails.bowledBy.bowlingScoreCard.runsGiven += 2
        elif ballDetails.runType == RunType.FOUR:
            ballDetails.bowledBy.bowlingScoreCard.runsGiven += 4
        elif ballDetails.runType == RunType.SIX:
            ballDetails.bowledBy.bowlingScoreCard.runsGiven += 6

        if ballDetails.wicket is not None:
            ballDetails.bowledBy.bowlingScoreCard.wicketsTaken += 1

        if ballDetails.ballType == BallType.NOBALL:
            ballDetails.bowledBy.bowlingScoreCard.noBallCount += 1

        if ballDetails.ballType == BallType.WIDEBALL:
            ballDetails.bowledBy.bowlingScoreCard.wideBallCount += 1
