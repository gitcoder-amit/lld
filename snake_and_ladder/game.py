from collections import deque
from .board import Board
from .dice import Dice
from .player import Player

class Game:
    def __init__(self):
        self.initialize_game()

    def initialize_game(self):
        self.board = Board(10, 5, 4)
        self.dice = Dice(1)
        self.winner = None
        self.players_list = deque()
        self.add_players()

    def add_players(self):
        player1 = Player("p1", 0)
        player2 = Player("p2", 0)
        self.players_list.append(player1)
        self.players_list.append(player2)

    def start_game(self):
        while self.winner is None:
            # check whose turn now
            player_turn = self.find_player_turn()
            print(f"player turn is: {player_turn.id}, current position is: {player_turn.current_position}")

            # roll the dice
            dice_numbers = self.dice.roll_dice()

            # get the new position
            player_new_position = player_turn.current_position + dice_numbers
            player_new_position = self.jump_check(player_new_position)
            player_turn.current_position = player_new_position

            print(f"player turn is: {player_turn.id}, new position is: {player_new_position}")

            # check for winning condition
            if player_new_position >= len(self.board.cells) * len(self.board.cells) - 1:
                self.winner = player_turn

        print(f"WINNER IS: {self.winner.id}")

    def find_player_turn(self):
        player_turn = self.players_list.popleft()
        self.players_list.append(player_turn)
        return player_turn

    def jump_check(self, player_new_position):
        if player_new_position > len(self.board.cells) * len(self.board.cells) - 1:
            return player_new_position

        cell = self.board.get_cell(player_new_position)
        if cell.jump is not None and cell.jump.start == player_new_position:
            jump_by = "ladder" if cell.jump.start < cell.jump.end else "snake"
            print(f"jump done by: {jump_by}")
            return cell.jump.end
        return player_new_position
