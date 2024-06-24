from .piece import Piece
from chess_game.color import Color  # Assuming Color is imported from a module named 'color'

class Bishop(Piece):
    def __init__(self, color: Color, row: int, col: int):
        super().__init__(color, row, col)

    def can_move(self, board, dest_row: int, dest_col: int) -> bool:
        row_diff = abs(dest_row - self.row)
        col_diff = abs(dest_col - self.col)
        return row_diff == col_diff

