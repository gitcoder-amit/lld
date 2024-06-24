from .piece import Piece  # Assuming Piece class is defined in piece.py

class Move:
    def __init__(self, piece, dest_row, dest_col):
        self.piece = piece
        self.dest_row = dest_row
        self.dest_col = dest_col

    def get_piece(self):
        return self.piece

    def get_dest_row(self):
        return self.dest_row

    def get_dest_col(self):
        return self.dest_col

