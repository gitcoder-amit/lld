from .player import Player
from .game import Game

class TicTacToeDemo:
    @staticmethod
    def run():
        player1 = Player("Player 1", 'X')
        player2 = Player("Player 2", 'O')

        game = Game(player1, player2)
        game.play()

if __name__ == "__main__":
    TicTacToeDemo.run()