from chess_game.board import Board  # Assuming Board class is defined in board.py
from chess_game.player import Player  # Assuming Player class is defined in player.py
from chess_game.color import Color  # Assuming Color enum is defined in color.py
from chess_game.move import Move  # Assuming Move class is defined in move.py
from chess_game.invalid_exception import InvalidMoveException  # Assuming InvalidMoveException is defined in exceptions.py
import sys

class ChessGame:
    def __init__(self):
        self.board = Board()
        self.players = [Player(Color.WHITE), Player(Color.BLACK)]
        self.currentPlayer = 0

    def start(self):
        # Game loop
        while not self.is_game_over():
            player = self.players[self.currentPlayer]
            print(f"{player.get_color()}\'s turn.")

            # Get move from the player
            move = self.get_player_move(player)

            # Make the move on the board
            try:
                player.make_move(self.board, move)
            except InvalidMoveException as e:
                print(e)
                print("Try again!")
                continue

            # Switch to the next player
            self.currentPlayer = (self.currentPlayer + 1) % 2

        # Display game result
        self.display_result()

    def is_game_over(self):
        return (self.board.is_checkmate(self.players[0].get_color()) or
                self.board.is_checkmate(self.players[1].get_color()) or
                self.board.is_stalemate(self.players[0].get_color()) or
                self.board.is_stalemate(self.players[1].get_color()))

    def get_player_move(self, player):
        # TODO: Implement logic to get a valid move from the player
        # For simplicity, let's assume the player enters the move via console input
        print("Enter source row:")
        source_row = int(input())
        print("Enter source column:")
        source_col = int(input())
        print("Enter destination row:")
        dest_row = int(input())
        print("Enter destination column:")
        dest_col = int(input())

        piece = self.board.get_piece(source_row, source_col)
        if piece is None or piece.get_color() != player.get_color():
            raise ValueError("Invalid piece selection!")

        return Move(piece, dest_row, dest_col)

    def display_result(self):
        if self.board.is_checkmate(Color.WHITE):
            print("Black wins by checkmate!")
        elif self.board.is_checkmate(Color.BLACK):
            print("White wins by checkmate!")
        elif self.board.is_stalemate(Color.WHITE) or self.board.is_stalemate(Color.BLACK):
            print("The game ends in a stalemate!")


