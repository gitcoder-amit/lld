from abc import ABC, abstractmethod
from LLDCricbuzz.Match.Inning import BallDetails

class ScoreUpdaterObserver(ABC):
    @abstractmethod
    def update(self, ballDetails: BallDetails):
        pass
