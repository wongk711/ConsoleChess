import numpy as np


def make_color_text(black):
    if black is 1:
        return 'xxxxx'
    return 'ooooo'


class Piece:
    def __init__(self, char_id, row, col, black):
        self.id = char_id
        self.black = black
        self.row = row
        self.col = col
        self.text = str(5*self.id)
        self.color_text = make_color_text(self.black)

    """
    :function: check_move
    :param new_pos: [row,col] of desired move location
    :param board:   current board for board state
    :return:        boolean 'valid' if move is valid
    
    new_pos will not contain a piece of the same color.
    either empty square or enemy piece
    """
    def check_move(self, new_pos, board):

        row_diff = np.abs(self.row - new_pos[0])
        col_diff = np.abs(self.col - new_pos[1])

        # Rook
        if self.id is 'R':
            # check diagonal
            if new_pos[0] is not self.row:
                vert = True
                if new_pos[1] is not self.col:
                    return False
            else:
                vert = False

            if vert:
                # going up
                if new_pos[0] < self.row:
                    a = new_pos[0] + 1
                    b = self.row
                # down
                else:
                    a = self.row
                    b= new_pos[0] + 1
                for i in range(a, b):
                    if board.board_mat[i, self.col] is not 'E':
                        return False
            else:   # L/R
                if new_pos[1] < self.col:   # left
                    a = new_pos[1] + 1
                    b = self.col
                else:
                    a = self.col
                    b = new_pos[1] + 1
                for i in range(a, b):
                    if board.board_mat[self.row, i] is not 'E':
                        return False
        # Knight
        elif self.id is 'N':
            if row_diff is 0 or row_diff > 2 or col_diff is 0 or col_diff > 2:
                return False
            if row_diff == col_diff:
                return False


        # Bishop
        elif self.id is 'B':
            if row_diff != col_diff:
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
                row_a = new_pos[0]+1
                row_b = self.row
            # down
            else:
                row_a = self.row
                row_b = new_pos[0] + 1

            for row, col in zip(range(row_a, row_b), range(col_a, col_b)):
                if board.board_mat[row, col] is not 'E':
                    return False
        # Queen
        elif self.id is 'Q':
            # check up/down left right
            if new_pos[0] == self.row:  # up/down
                if new_pos[0] < self.row: # up
                    a = new_pos[0] + 1
                    b = self.row
                else:   # down
                    a = self.row
                    b= new_pos[0] + 1
                for i in range(a, b):
                    if board.board_mat[i, self.col] is not 'E':
                        return False
            elif new_pos[1] == self.col:  # L/R
                if new_pos[1] < self.col:   # left
                    a = new_pos[1] + 1
                    b = self.col
                else:   # right
                    a = self.col
                    b = new_pos[1] + 1
                for i in range(a, b):
                    if board.board_mat[self.row, i] is not 'E':
                        return False
            elif row_diff == col_diff:  # diag
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
                    if board.board_mat[row, col] is not 'E':
                        return False
            else:
                return False
        # Pawn
        elif self.id is 'P':
            if row_diff > 2 or col_diff > 1:
                return False
            pawn_row = 6 if self.black is 0 else 1
            # straight up
            if new_pos[1] == self.col:
                if row_diff is 2 and self.row is not pawn_row:
                    return False
                if board.board_mat[new_pos[0], new_pos[1]].piece.id is not 'E':
                    return False
                if self.black is 1:
                    if self.row > new_pos[0]:
                        return False
                elif self.row < new_pos[0]:
                    return False
            # diag ( take )
            elif board.board_mat[new_pos[0],new_pos[1]].piece.id is 'E':
                return False
        # King
        elif row_diff > 1 or col_diff > 1:
            return False
        return True
