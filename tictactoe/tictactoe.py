"""
Tic Tac Toe Player
"""

import math

# raise NotImplementedError

X = "X"
O = "O"
EMPTY = None

move = [0, 0]

# DO NOT NEED TO DEFINE TRUE AND FALSE, BUT WHATEVER
TRUE = 1
FALSE = 0
MINIMAX_X_WINNING_SCORE = 10  # // This means that X will win.
MINIMAX_O_WINNING_SCORE = -10  # // This means that O will win.
MINIMAX_DRAW_SCORE = 0  # // Nobody wins.
MINIMAX_NOT_ENDGAME = -1  # // Not an end-game.

score_board = -1;
is_x_turn = True


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


"""
Returns player who has the next turn on a board.
"""


def player(board):
    not_empty = 0
    for i in board:
        if i != EMPTY:
            not_empty += 1

    # returning an error code
    # returning x_turn
    if not_empty > 0:
        return 1;
    elif is_x_turn > 0:
        return X
    else:
        return O

    # raise NotImplementedError


"""
Returns set of all possible actions (i, j) available on the board.
"""


def actions(board):
    # This will choose the correct move and load it into the variable
    minimax(board)
    # This will return the move that is chosen by the computer
    return move

    raise NotImplementedError


"""
Returns the board that results from making move (i, j) on the board.
"""


def result(board, action):
    # Depends on whose turn it is or was
    # Check on this
    if is_x_turn:
        board[action.x, action.y] = X
    else:
        board[action.x, action.y] = O

    # raise NotImplementedError


"""
Returns the winner of the game, if there is one.
"""


def winner(board):
    raise NotImplementedError


"""
       Returns True if game is over, False otherwise.
"""


def terminal(board):
    if score_board == MINIMAX_NOT_ENDGAME:
        return False
    else:
        return True


"""
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
"""


def utility(board):
    if (is_x_turn):
        if ((board[0][0] == X and board[0][1] == X and board[0][2] == X) or
                (board[0][0] == X and board[0][1] == X and board[0][2] == X) or (board[0][0] == X and board[0][1] == X and board[0][2] == X) or (board[0][0] == X and board[0][1] == X and board[0][2] == X) or (board[0][0] == X and board[0][1] == X and board[0][2] == X) or (board[0][0] == X and board[0][1] == X and board[0][2] == X) or (board[0][0] == X and board[0][1] == X and board[0][2] == X) or (board[0][0] == X and board[0][1] == X and board[0][2] == X)) :
            return 1
    else:
        return -1



"""
    Returns the optimal action for the current player on the board.
    Minimax Algorithm
"""


def minimax(board):

    if(terminal(board)):
        return

    #raise NotImplementedError
