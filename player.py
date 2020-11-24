from Pieces.bishop import Bishop
from Pieces.king import King
from Pieces.knight import Knight
from Pieces.pawn import Pawn
from Pieces.queen import Queen
from Pieces.rook import Rook


def init_pieces(black):
    if black is 1:
        pieces = [Rook(char_id='R', black=1, row=0, col=0)]
        pieces.append(Knight(char_id='K', black=1, row=0, col=1))
        pieces.append((Bishop(char_id='B', black=1, row=0, col=2)))
        pieces.append(Queen(char_id='Q', black=1, row=0, col=3))
        pieces.append(King(char_id='K', black=1, row=0, col=4))
        pieces.append((Bishop(char_id='B', black=1, row=0, col=5)))
        pieces.append(Knight(char_id='K', black=1, row=0, col=6))
        pieces.append(Rook(char_id='R', black=1, row=0, col=7))
        for i in range(8):
            pieces.append(Pawn(char_id='P', black=1, row=1, col=i))
    else:
        pieces = []
        for i in range(8):
            pieces.append(Pawn(char_id='P', black=0, row=6, col=i))
        pieces.append(Rook(char_id='R', black=0, row=7, col=0))
        pieces.append(Knight(char_id='K', black=0, row=0, col=1))
        pieces.append((Bishop(char_id='B', black=0, row=0, col=2)))
        pieces.append(Queen(char_id='Q', black=0, row=0, col=3))
        pieces.append(King(char_id='K', black=0, row=0, col=4))
        pieces.append((Bishop(char_id='B', black=0, row=0, col=5)))
        pieces.append(Knight(char_id='K', black=0, row=0, col=6))
        pieces.append(Rook(char_id='R', black=0, row=0, col=7))
    return pieces

class Player:
    def __init__(self, black):
        """
        :param black: 1 : black, 0 : white
        """
        self.black = black
        self.pieces = init_pieces(self.black)


