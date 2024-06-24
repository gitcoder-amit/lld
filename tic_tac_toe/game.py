from .player import Player
from .board import Board

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.board = Board()
        self.current_player = player1

    def play(self):
        self.board.print_board()

        while not self.board.is_full() and not self.board.has_winner():
            print(f"{self.current_player.name}'s turn.")
            row = self.get_valid_input("Enter row (0-2): ")
            col = self.get_valid_input("Enter column (0-2): ")

            try:
                self.board.make_move(row, col, self.current_player.symbol)
                self.board.print_board()
                self.switch_player()
            except ValueError as e:
                print(e)

        if self.board.has_winner():
            self.switch_player()
            print(f"{self.current_player.name} wins!")
        else:
            print("It's a draw!")

    def switch_player(self):
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1

    def get_valid_input(self, message):
        while True:
            try:
                input_val = int(input(message))
                if 0 <= input_val <= 2:
                    return input_val
            except ValueError:
                pass
            print("Invalid input! Please enter a number between 0 and 2.")

if __name__ == "__main__":
    player1 = Player("Player 1", 'X')
    player2 = Player("Player 2", 'O')
    game = Game(player1, player2)
    game.play()
