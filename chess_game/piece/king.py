from abc import ABC, abstractmethod
# import math
from .piece import Piece
from ..color import Color



class King(Piece):
    def __init__(self, color: Color, row: int, col: int):
        super().__init__(color, row, col)

    def can_move(self, board, dest_row: int, dest_col: int) -> bool:
        row_diff = abs(dest_row - self._row)
        col_diff = abs(dest_col - self._col)
        return (row_diff <= 1 and col_diff <= 1)