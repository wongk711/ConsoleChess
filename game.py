from board import Board


class Game:
    def __init__(self, num_players=1):
        self.turn = 0
        self.board = Board()
        self.num_players = num_players
        self.prev_moves = []



