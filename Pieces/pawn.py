from globals import make_color_text
from piece import Piece
import numpy as np


class Pawn(Piece):
    def __init__(self, black, row, col):
        self.id = 'P'
        self.text = str(5*self.id)
        self.color_text = make_color_text(black)
        Piece.__init__(self, black=black,  row=row, col=col)

    def check_move(self, new_pos, board):

        row_diff = np.abs(self.row - new_pos[0])
        col_diff = np.abs(self.col - new_pos[1])

        if row_diff > 2 or col_diff > 1:
            return False
        pawn_row = 6 if self.black is 0 else 1
        # straight up
        if new_pos[1] == self.col:
            if board.board_mat[new_pos[0], new_pos[1]].piece.black is not -1:
                print('Pawns can only capture pieces by moving diagonally!')
                return False
            if row_diff is 2:
                if self.row is not pawn_row:
                    print('A pawn can only move 2 squares on its first move!')
                    return False
                if board.board_mat[np.average([self.row, new_pos[0]]), self.col].piece.black is not -1:
                    print('Pawns cannot jump over pieces!')
                    return False
                return True
            if self.black is 1:
                if self.row > new_pos[0]:
                    print('Pawns may only move forward!')
                    return False
            elif self.row < new_pos[0]:
                print('Pawns may only move forward!')
                return False
            return True
        # diag ( take )
        elif board.board_mat[new_pos[0], new_pos[1]].piece.black is -1:
            return False
        return True
