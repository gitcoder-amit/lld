from abc import ABC, abstractmethod

class MatchType(ABC):

    @abstractmethod
    def no_of_overs(self):
        pass

    @abstractmethod
    def max_over_count_bowlers(self):
        pass
