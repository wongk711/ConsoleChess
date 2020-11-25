from Pieces.bishop import Bishop
from Pieces.king import King
from Pieces.knight import Knight
from Pieces.pawn import Pawn
from Pieces.queen import Queen
from Pieces.rook import Rook


def init_pieces(black):
    """
    :param black: playing black or white pieces
    :return: list of black's or white's pieces
    :note: order of these matter
    """
    if black is 1:
        pieces = [Rook(black=1, row=0, col=0), Knight(black=1, row=0, col=1), (Bishop(black=1, row=0, col=2)),
                  Queen(black=1, row=0, col=3), King(black=1, row=0, col=4), (Bishop(black=1, row=0, col=5)),
                  Knight(black=1, row=0, col=6), Rook(black=1, row=0, col=7)]
        for i in range(8):
            pieces.append(Pawn(black=1, row=1, col=i))
    else:
        pieces = []
        for i in range(8):
            pieces.append(Pawn(black=0, row=6, col=i))
        pieces.append(Rook(black=0, row=7, col=0))
        pieces.append(Knight(black=0, row=7, col=1))
        pieces.append((Bishop(black=0, row=7, col=2)))
        pieces.append(Queen(black=0, row=7, col=3))
        pieces.append(King(black=0, row=7, col=4))
        pieces.append((Bishop(black=0, row=7, col=5)))
        pieces.append(Knight(black=0, row=7, col=6))
        pieces.append(Rook(black=0, row=7, col=7))
    return pieces


class Player:
    def __init__(self, black):
        """
        :param black: 1 : black, 0 : white
        'pieces' holds current list of pieces
        """
        self.black = black
        self.pieces = init_pieces(self.black)


