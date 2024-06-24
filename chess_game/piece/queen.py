from .piece import Piece
from chess_game.color import Color  # Assuming Color is imported from a module named 'color'

class Queen(Piece):
    def __init__(self, color: Color, row: int, col: int):
        super().__init__(color, row, col)

    def can_move(self, board, dest_row: int, dest_col: int) -> bool:
        row_diff = abs(dest_row - self.row)
        col_diff = abs(dest_col - self.col)
        return (row_diff == col_diff) or (self.row == dest_row or self.col == dest_col)

# Example usage
if __name__ == "__main__":
    queen = Queen(Color.WHITE, 0, 3)
    print(queen.get_color())  # Output: Color.WHITE
    print(queen.get_row())    # Output: 0
    print(queen.get_col())    # Output: 3

    board = None  # Placeholder for the board object
    print(queen.can_move(board, 1, 4))  # Output: True (valid diagonal move)
    print(queen.can_move(board, 0, 7))  # Output: True (valid horizontal move)
    print(queen.can_move(board, 3, 3))  # Output: True (valid vertical move)
    print(queen.can_move(board, 2, 5))  # Output: False (invalid move)
