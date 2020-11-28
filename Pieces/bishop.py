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
        print('bishop on :', self.row, self.col)
        print('new_pos :', new_pos[0], new_pos[1])
        if row_diff != col_diff:
            print('Bishops must move diagonally!')
            return False
        # left
        if new_pos[1] < self.col:
            col_range = list(range(new_pos[1] + 1, self.col))
            # up
            if new_pos[0] < self.row:
                row_range = list(range(new_pos[0] + 1, self.row))
            # down
            else:
                row_range = list(range(self.row + 1, new_pos[0]))
                row_range.reverse()
        # right
        else:
            col_range = list(range(self.col + 1, new_pos[1]))
            # up
            if new_pos[0] < self.row:
                row_range = list(range(new_pos[0] + 1, self.row))
                row_range.reverse()
            # down
            else:
                row_range = list(range(self.row + 1, new_pos[0]))

        for row, col in zip(row_range, col_range):
            print('debug:', row, col)
            if board.board_mat[row, col].piece.black is not -1:
                print('Bishops cannot jump over pieces!')
                return False
        return True
