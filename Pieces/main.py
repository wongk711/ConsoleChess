# import time
from game import Game
from piece import Piece
from square import Square
from globals import cols, rows, files


def get_piece(board, turn):
    valid = False
    piece = None
    while not valid:
        turn_text = 'Black\'s Move' if turn is 1 else 'White\'s Move'
        print(turn_text)
        print('Enter desired piece coordinate ( like \'g1\' ) :')

        pos = str(input())
        while pos is '':
            pos = str(input())

        if len(pos) != 2:
            print('Invalid input!')
            continue
        if pos[0].lower() not in files:
            print('Invalid input!')
            continue
        if int(pos[1]) not in range(1, 9):
            print('Invalid input!')
            continue

        file = str(pos[0]).lower()
        rank = int(pos[1])
        col = cols[file]
        row = rows[rank]

        piece = board.board_mat[row, col].piece

        if piece.id is 'E':
            print('no piece at ' + str(file) + str(rank))
            continue
        if piece.black != turn:
            print('Wrong Team!')
            continue

        valid = True

    return piece


def get_move(piece, board):
    valid = False
    black = piece.black
    input_pos = ''
    while not valid:

        print('Enter your move coordinate ( or press space for new piece ) :')
        input_pos = str(input())
        while input_pos is '':
            input_pos = str(input())

        if input_pos is ' ':
            return -1
        if len(input_pos) != 2:
            print('Invalid input!')
            continue
        if input_pos[0].lower() not in files:
            print('Invalid input!')
            continue
        if int(input_pos[1]) not in range(1, 9):
            print('Invalid input!')
            continue

        file = str(input_pos[0])
        rank = int(input_pos[1])
        input_pos = (rows[rank], cols[file])

        victim_piece = board.board_mat[input_pos[0], input_pos[1]].piece
        # 1 : black, 0 : white, -1 : E
        if victim_piece.black is not black:
            valid = piece.check_move(input_pos, board)
        if not valid:
            print('Invalid move!')

    return [input_pos[0], input_pos[1]]


def move_piece(this_piece, move, board):
    this_id = this_piece.id
    this_piece_color = this_piece.black
    prev = this_piece.row, this_piece.col
    mat = board.board_mat

    prev_piece = Piece('E', prev[0], prev[1], -1)
    prev_square = Square(mat[prev[0], prev[1]].black, prev_piece)
    mat[prev[0], prev[1]] = prev_square

    new_piece = Piece(this_id, move[0], move[1], this_piece_color)
    next_square = Square(mat[move[0], move[1]].black, new_piece)
    mat[move[0], move[1]] = next_square

    board.board_mat = mat
    board.draw_board()
    return board


def log_move(piece, move):
    rank = {0: 8, 1: 7, 2: 6, 3: 5, 4: 4, 5: 3, 6: 2, 7: 1}
    file = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H'}
    move = piece.id+'.'+file[move[1]]+str(rank[move[0]])
    return move


def play(game):

    this_board = game.board
    this_board.draw_board()

    while True:

        this_piece = get_piece(this_board, game.turn)
        this_move = get_move(this_piece, this_board)
        while this_move is -1:
            this_piece = get_piece(this_board, game.turn)
            this_move = get_move(this_piece, this_board)
        this_board = move_piece(this_piece, this_move, this_board)

        game.prev_moves.append(log_move(this_piece, this_move))
        game.turn = len(game.prev_moves) % 2


my_game = Game()
play(my_game)
