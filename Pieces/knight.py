from globals import make_color_text
from piece import Piece
import numpy as np


class Knight(Piece):
    def __init__(self,black, row, col):
        self.id = 'N'
        self.text = str(5*self.id)
        self.color_text = make_color_text(black)
        Piece.__init__(self, black=black, row=row, col=col)

    def check_move(self, new_pos, board):
        row_diff = np.abs(self.row - new_pos[0])
        col_diff = np.abs(self.col - new_pos[1])

        if row_diff is 0 or col_diff is 0:
            print('Knights cannot move in straight line!')
            return False
        if row_diff > 2 or col_diff > 2:
            print('debug:', self.row, new_pos[0])
            print('Knights must move 2 squares in one direction then 1 square left or right.')
            return False
        if row_diff == col_diff:
            print('Knights cannot move diagonally!')
            return False
        return True
