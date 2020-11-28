from globals import make_color_text
from piece import Piece


class Rook(Piece):
    def __init__(self, black, row, col):
        self.id = 'R'
        self.text = str(5*self.id)
        self.color_text = make_color_text(black)
        Piece.__init__(self, black=black, row=row, col=col)

    def check_move(self, new_pos, board):
        # check diagonal
        if new_pos[0] is not self.row:
            vert = True
            if new_pos[1] is not self.col:
                print('Cannot move rooks diagonally!')
                return False
        else:
            vert = False

        if vert:
            # going up
            if new_pos[0] < self.row:
                a = new_pos[0]
                b = self.row
            # down
            else:
                a = self.row
                b = new_pos[0]
            for i in range(a + 1, b):
                if board.board_mat[i, self.col].piece.black is not -1:
                    print('Rooks cannot jump pieces!')
                    return False
        else:  # L/R
            if new_pos[1] < self.col:  # left
                a = new_pos[1]
                b = self.col
            else:
                a = self.col
                b = new_pos[1]
            for i in range(a + 1, b):
                if board.board_mat[self.row, i].piece.black is not -1:
                    print('Rooks cannot jump pieces!')
                    return False

        return True
