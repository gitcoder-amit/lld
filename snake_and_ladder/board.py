import random
from .cell import Cell
from .jump import Jump


class Board:
    def __init__(self, board_size, number_of_snakes, number_of_ladders):
        self.cells = self.initialize_cells(board_size)
        self.add_snakes_ladders(self.cells, number_of_snakes, number_of_ladders)

    def initialize_cells(self, board_size):
        cells = [[Cell() for _ in range(board_size)] for _ in range(board_size)]
        return cells

    def add_snakes_ladders(self, cells, number_of_snakes, number_of_ladders):
        board_size = len(cells)
        max_position = board_size * board_size - 1

        while number_of_snakes > 0:
            snake_head = random.randint(1, max_position)
            snake_tail = random.randint(1, max_position)
            if snake_tail >= snake_head:
                continue

            snake_obj = Jump(snake_head, snake_tail)
            cell = self.get_cell(snake_head)
            cell.jump = snake_obj

            number_of_snakes -= 1

        while number_of_ladders > 0:
            ladder_start = random.randint(1, max_position)
            ladder_end = random.randint(1, max_position)
            if ladder_start >= ladder_end:
                continue

            ladder_obj = Jump(ladder_start, ladder_end)
            cell = self.get_cell(ladder_start)
            cell.jump = ladder_obj

            number_of_ladders -= 1

    def get_cell(self, player_position):
        board_row = player_position // len(self.cells)
        board_column = player_position % len(self.cells)
        return self.cells[board_row][board_column]
