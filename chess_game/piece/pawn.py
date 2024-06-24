from .piece import Piece
from chess_game.color import Color  # Assuming Color is imported from a module named 'color'

class Pawn(Piece):
    def __init__(self, color: Color, row: int, col: int):
        super().__init__(color, row, col)

    def can_move(self, board, dest_row: int, dest_col: int) -> bool:
        row_diff = dest_row - self.row
        col_diff = abs(dest_col - self.col)

        if self.color == Color.WHITE:
            return (row_diff == 1 and col_diff == 0) or \
                   (self.row == 1 and row_diff == 2 and col_diff == 0) or \
                   (row_diff == 1 and col_diff == 1 and board.get_piece(dest_row, dest_col) is not None)
        else:
            return (row_diff == -1 and col_diff == 0) or \
                   (self.row == 6 and row_diff == -2 and col_diff == 0) or \
                   (row_diff == -1 and col_diff == 1 and board.get_piece(dest_row, dest_col) is not None)
