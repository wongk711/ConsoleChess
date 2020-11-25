from board import Board
from player import Player

class Game:
    def __init__(self):
        self.turn = 0
        self.w_player = Player(black=0)
        self.b_player = Player(black=1)
        self.board = Board([self.b_player, self.w_player])
        self.prev_moves = []




