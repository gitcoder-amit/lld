from chess_game.color import Color  # Assuming Color enum is defined in color.py
from chess_game.board import Board  # Assuming Board class is defined in board.py
from chess_game.move import Move  # Assuming Move class is defined in move.py
from chess_game.invalid_exception import InvalidMoveException  # Assuming InvalidMoveException is defined in exceptions.py

class Player:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def make_move(self, board, move):
        piece = move.get_piece()
        dest_row = move.get_dest_row()
        dest_col = move.get_dest_col()

        if board.is_valid_move(piece, dest_row, dest_col):
            source_row = piece.get_row()
            source_col = piece.get_col()
            board.set_piece(source_row, source_col, None)
            board.set_piece(dest_row, dest_col, piece)
            piece.set_row(dest_row)
            piece.set_col(dest_col)
        else:
            raise InvalidMoveException("Invalid move!")


