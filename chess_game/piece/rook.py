from .piece import Piece
from chess_game.color import Color  # Assuming Color is imported from a module named 'color'

class Rook(Piece):
    def __init__(self, color: Color, row: int, col: int):
        super().__init__(color, row, col)

    def can_move(self, board, dest_row: int, dest_col: int) -> bool:
        return self.row == dest_row or self.col == dest_col

# Example usage
if __name__ == "__main__":
    rook = Rook(Color.WHITE, 0, 0)
    print(rook.get_color())  # Output: Color.WHITE
    print(rook.get_row())    # Output: 0
    print(rook.get_col())    # Output: 0

    board = None  # Placeholder for the board object
    print(rook.can_move(board, 0, 3))  # Output: True (valid horizontal move)
    print(rook.can_move(board, 3, 0))  # Output: True (valid vertical move)
    print(rook.can_move(board, 1, 1))  # Output: False (invalid diagonal move)
