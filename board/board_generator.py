from random import choice

from board.helpers import InitialValuesOfField
from settings import VALUES_OF_BOARD_FIELDS


def pos_correct(height, width, x, y):
    return 0 <= x < height and 0 <= y < width


class BoardGenerator:
    def __init__(self, height, width, mine_amount):
        self.height = height
        self.width = width
        self.mine_amount = mine_amount

    def get_initial_board(self):
        board = []
        for i in range(0, self.height):
            tmp = [InitialValuesOfField() for j in range(0, self.width)]
            board.append(tmp)
        return board

    def get_indexes_of_fields(self):
        indexes_of_fields = []
        for i in range(0, self.height):
            for j in range(0, self.width):
                indexes_of_fields.append((i, j))
        return indexes_of_fields

    @staticmethod
    def add_mines(board, indexes_of_fields, mine_amount):
        # Adding mines, coordinates of the mines are random.
        for i in range(mine_amount):
            coordinates = choice(indexes_of_fields)
            x, y = coordinates
            indexes_of_fields.remove(coordinates)
            board[x][y].value = VALUES_OF_BOARD_FIELDS["BOMB"]

    def add_nearby_mines(self, board):
        for x in range(0, self.height):
            for y in range(0, self.width):
                mines_around = 0
                if (pos_correct(self.height, self.width, x - 1, y) is True) and (
                    board[x - 1][y].value == VALUES_OF_BOARD_FIELDS["BOMB"]
                ):
                    mines_around += 1
                if (pos_correct(self.height, self.width, x - 1, y - 1) is True) and (
                    board[x - 1][y - 1].value == VALUES_OF_BOARD_FIELDS["BOMB"]
                ):
                    mines_around += 1
                if (pos_correct(self.height, self.width, x, y - 1) is True) and (
                    board[x][y - 1].value == VALUES_OF_BOARD_FIELDS["BOMB"]
                ):
                    mines_around += 1
                if (pos_correct(self.height, self.width, x + 1, y - 1) is True) and (
                    board[x + 1][y - 1].value == VALUES_OF_BOARD_FIELDS["BOMB"]
                ):
                    mines_around += 1
                if (pos_correct(self.height, self.width, x + 1, y) is True) and (
                    board[x + 1][y].value == VALUES_OF_BOARD_FIELDS["BOMB"]
                ):
                    mines_around += 1
                if (pos_correct(self.height, self.width, x + 1, y + 1) is True) and (
                    board[x + 1][y + 1].value == VALUES_OF_BOARD_FIELDS["BOMB"]
                ):
                    mines_around += 1
                if (pos_correct(self.height, self.width, x, y + 1) is True) and (
                    board[x][y + 1].value == VALUES_OF_BOARD_FIELDS["BOMB"]
                ):
                    mines_around += 1
                if (pos_correct(self.height, self.width, x - 1, y + 1) is True) and (
                    board[x - 1][y + 1].value == VALUES_OF_BOARD_FIELDS["BOMB"]
                ):
                    mines_around += 1

                board[x][y].nearby_mines = mines_around

    def set_values_for_non_bomb_fields(self, board):
        # Change of particular fields values depending on
        # the number of mines near the specified field.
        for x in range(0, self.height):
            for y in range(0, self.width):
                if board[x][y].nearby_mines > 0:
                    if board[x][y].value != VALUES_OF_BOARD_FIELDS["BOMB"]:
                        board[x][y].value = str(board[x][y].nearby_mines)

    @classmethod
    def get_game_board(cls, height, width, mine_amount):
        # Array will have dimensions increased by 1 in order to
        # avoid collisions resulting from exceeding the range of an array
        # while updating the neighbours.
        board_generator = cls(
            height=height,
            width=width,
            mine_amount=mine_amount,
        )
        board = board_generator.get_initial_board()
        indexes_of_fields = board_generator.get_indexes_of_fields()
        board_generator.add_mines(
            board=board, indexes_of_fields=indexes_of_fields, mine_amount=mine_amount
        )
        board_generator.add_nearby_mines(board=board)
        board_generator.set_values_for_non_bomb_fields(board=board)
        return board
