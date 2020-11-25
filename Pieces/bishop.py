from globals import make_color_text
from piece import Piece
import numpy as np


class Bishop(Piece):
    def __init__(self,black, row, col):
        self.id = 'B'
        self.text = str(5*self.id)
        self.color_text = make_color_text(black)
        Piece.__init__(self, black=black,  row=row, col=col)

    def check_move(self, new_pos, board):

        row_diff = np.abs(self.row - new_pos[0])
        col_diff = np.abs(self.col - new_pos[1])

        if row_diff != col_diff:
            print('Bishops must move diagonally!')
            return False
        # left
        if new_pos[1] < self.col:
            col_a = new_pos[1] + 1
            col_b = self.col
        # right
        else:
            col_a = self.col
            col_b = new_pos[1] + 1
        # up
        if new_pos[0] < self.row:
            row_a = new_pos[0] + 1
            row_b = self.row
        # down
        else:
            row_a = self.row
            row_b = new_pos[0] + 1

        for row, col in zip(range(row_a, row_b), range(col_a, col_b)):
            if board.board_mat[row, col].piece.black is not -1:
                print('Bishops cannot jump over pieces!')
                return False
