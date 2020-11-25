from globals import make_color_text
from piece import Piece
import numpy as np


class King(Piece):
    def __init__(self, black, row, col):
        self.id = 'K'
        self.text = str(5*self.id)
        self.color_text = make_color_text(black)
        Piece.__init__(self, black=black, row=row, col=col)

    def check_move(self, new_pos, board):
        row_diff = np.abs(self.row - new_pos[0])
        col_diff = np.abs(self.col - new_pos[1])
        if row_diff > 1 or col_diff > 1:
            print('Kings may only move 1 square in any direction!')
            return False
        return True
