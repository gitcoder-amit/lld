from enum import Enum
from .ball_type import BallType
from .runtype import RunType
import random
from ..score_updater.bowling_score_updater import BowlingScoreUpdater
from ..score_updater.batting_score_updater import BattingScoreUpdater
from ..team.team import Team
from ..team.wicket import Wicket
from ..team.wicket_type import WicketType
from .over_details import OverDetails


class BallDetails:
    def __init__(self, ballNumber):
        self.ballNumber = ballNumber
        self.ballType = BallType.NORMAL
        self.runType = None
        self.playedBy = None
        self.bowledBy = None
        self.wicket = None
        self.scoreUpdaterObserverList = [BowlingScoreUpdater(), BattingScoreUpdater()]

    def start_ball_delivery(self, battingTeam: Team, bowlingTeam: Team, over: OverDetails):
        self.playedBy = battingTeam.getStriker()
        self.bowledBy = over.bowledBy
        # THROW BALL AND GET THE BALL TYPE, assuming here that ball type is always NORMAL
        self.ballType = BallType.NORMAL

        # wicket or no wicket
        if self.isWicketTaken():
            self.runType = RunType.ZERO
            # considering only BOLD
            self.wicket = Wicket(WicketType.BOLD, bowlingTeam.getCurrentBowler(), over, self)
            # making only striker out for now
            battingTeam.setStriker(None)
        else:
            self.runType = self.getRunType()

            if self.runType == RunType.ONE or self.runType == RunType.THREE:
                # swap striker and non-striker
                temp = battingTeam.getStriker()
                battingTeam.setStriker(battingTeam.getNonStriker())
                battingTeam.setNonStriker(temp)

        # update player scoreboard
        self.notifyUpdaters()

    def notifyUpdaters(self):
        for observer in self.scoreUpdaterObserverList:
            observer.update(self)

    def getRunType(self):
        val = random.random()
        if val <= 0.2:
            return RunType.ONE
        elif 0.3 <= val <= 0.5:
            return RunType.TWO
        elif 0.6 <= val <= 0.8:
            return RunType.FOUR
        else:
            return RunType.SIX

    def isWicketTaken(self):
        # random function returns value between 0 and 1
        return random.random() < 0.2
