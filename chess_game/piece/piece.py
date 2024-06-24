from abc import ABC, abstractmethod
from ..color import Color

class Piece(ABC):
    def __init__(self, color: Color, row: int, col: int):
        self._color = color
        self._row = row
        self._col = col

    @abstractmethod
    def can_move(self, board, dest_row: int, dest_col: int) -> bool:
        pass

    @property
    def color(self) -> Color:
        return self._color

    @property
    def row(self) -> int:
        return self._row

    @row.setter
    def row(self, row: int):
        self._row = row

    @property
    def col(self) -> int:
        return self._col

    @col.setter
    def col(self, col: int):
        self._col = col
