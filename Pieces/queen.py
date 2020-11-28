from globals import make_color_text
from piece import Piece
import numpy as np


class Queen(Piece):
    def __init__(self, black, row, col):
        self.id = 'Q'
        self.text = str(5 * self.id)
        self.color_text = make_color_text(black)
        Piece.__init__(self, black=black, row=row, col=col)

    def check_move(self, new_pos, board):
        row_diff = np.abs(self.row - new_pos[0])
        col_diff = np.abs(self.col - new_pos[1])

        # up/down
        if new_pos[0] == self.row:
            if new_pos[0] < self.row:  # up
                a = new_pos[0]
                b = self.row
            else:  # down
                a = self.row
                b = new_pos[0]
            for i in range(a + 1, b):
                if board.board_mat[i, self.col].piece.black is not -1:
                    print('Queens may not jump over other pieces!')
                    return False
            return True
        # L/R
        elif new_pos[1] == self.col:
            if new_pos[1] < self.col:  # left
                a = new_pos[1]
                b = self.col
            else:  # right
                a = self.col
                b = new_pos[1]
            for i in range(a + 1, b):
                if board.board_mat[self.row, i].piece.black is not -1:
                    print('Queens may not jump over other pieces!')
                    return False
            return True
        # diag
        elif row_diff == col_diff:
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
                if board.board_mat[row, col].piece.black is not -1:
                    print('Queens may not jump over other pieces!')
                    print('debug:', row, col)
                    return False
            return True
        return False
