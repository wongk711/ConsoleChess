import numpy as np
from square import Square
from piece import Piece


class Board:
    def __init__(self):
        self.board_mat = init_mat()
        # print('board created')
        return

    def draw_board(self):
        text_list = []
        ranks = ['A','B','C','D','E','F','G','H']
        n = len(self.board_mat[0,0].text_rows)
        for i in range(8):  # square rows
            for j in range(n):   # text_rows
                text = ' '
                if j is 2:
                    text = str(8-i)
                for k in range(8):  # columns
                    text += self.board_mat[i,k].text_rows[j]
                if j is 0:
                    text += '+'
                else:
                    text += '|'
                text_list.append(text)

        for i in range(len(text_list)):
            print(text_list[i])
        print(' ' + (8*'+-----------')+'+')

        text = ''
        for i in range(8):
            text += ('      ' + ranks[i] + '     ')
        print(text)


def init_mat():
    board_mat = np.empty(shape=(8,8), dtype=Square)

    # id_list = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
    row1_pieces = []
    row1_pieces.append(Rook())
    row7_pieces = []
    # for i in range(8):
    #     row1_pieces.append(Piece(char_id=id_list[i], row=0, col=i, black=1))
    #     row7_pieces.append(Piece(char_id=id_list[i], row=7, col=i, black=0))

    for i in range(8):
        board_mat[0, i] = Square(black=(i % 2), piece=row1_pieces[i])
    for i in range(8):
        board_mat[1, i] = Square(black=((i+1) % 2), piece=Piece(char_id='P', row=1, col=i, black=1))
    for i in range(2, 6):
        for j in range(8):
            board_mat[i, j] = Square(black=((j + i) % 2), piece=Piece(char_id='E', row=i, col=j, black=-1))
    for i in range(8):
        board_mat[6, i] = Square(black=(i % 2), piece=Piece(char_id='P', row=6, col=i, black=0))
    for i in range(8):
        board_mat[7, i] = Square(black=((i+1) % 2), piece=row7_pieces[i])

    return board_mat
