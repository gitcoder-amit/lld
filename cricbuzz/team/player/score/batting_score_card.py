from typing import Optional
from ...wicket import Wicket

class BattingScoreCard:
    def __init__(self):
        self.totalRuns: int = 0
        self.totalBallsPlayed: int = 0
        self.totalFours: int = 0
        self.totalSix: int = 0
        self.strikeRate: float = 0.0
        self.wicketDetails: Optional[Wicket] = None
