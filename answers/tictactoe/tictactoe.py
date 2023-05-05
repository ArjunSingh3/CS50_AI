"""
Tic Tac Toe Player
"""
import copy
import math

# raise NotImplementedError

X = "X"
O = "O"
EMPTY = None

move = [0, 0]

score_board = -1;

is_x_turn = True
global_row = 0
global_column = 0


class MoveScoreType:
    def __init__(self, row, column, score):
        self.row = row
        self.column = column
        self.score = score


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


"""
Returns player who has the next turn on a board. **
"""


def global_x_turn():
    global is_x_turn
    is_x_turn = ~is_x_turn

    return is_x_turn


def player(board):
    x_turn = -1
    o_turn = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                x_turn += 1
            elif board[i][j] == O:
                o_turn += 1

    if x_turn < o_turn:
        return X
    else:
        return O

    # raise NotImplementedError


"""
Returns set of all possible actions (i, j) available on the board. **
"""


def actions(board):
    possible_moves = []
    if player(board) is X:
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    possible_moves.append([i, j])
    elif player(board) is O:
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    possible_moves.append([i, j])

    return possible_moves


"""
Returns the board that results from making move (i, j) on the board.
"""


def result(board, action):
    # Depends on whose turn it is or was
    # Check on this
    board2 = copy.deepcopy(board)
    if action is None:
        raise exit(5)
    else:
        (i, j) = action
        if board[i][j] is not EMPTY:
            raise exit(7)
        elif player(board) == X:
            board2[i][j] = X
        else:
            board2[i][j] = O
    return board2


""" 
Returns the winner of the game, if there is one.
"""


def winner(board):
    if utility(board) == 1:
        return X
    elif utility(board) == -1:
        return O
    else:
        return None


"""
       Returns True if game is over, False otherwise. **
"""


def terminal(board):
    if utility(board) == 5:
        return False
    else:
        return True


"""
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise. **
"""


def utility(board):
    if player(board) is X:
        if (((board[0][0] is X) and (board[0][1] is X) and (board[0][2] is X)) or
                ((board[1][0] is X) and (board[1][1] is X) and (board[1][2] is X)) or
                ((board[2][0] is X) and (board[2][1] is X) and (board[2][2] is X)) or
                ((board[0][0] is X) and (board[1][0] is X) and (board[2][0] is X)) or
                ((board[0][1] is X) and (board[1][1] is X) and (board[2][1] is X)) or
                ((board[0][2] is X) and (board[1][2] is X) and (board[2][2] is X)) or
                ((board[0][0] is X) and (board[1][1] is X) and (board[1][2] is X)) or
                ((board[0][2] is X) and (board[1][1] is X) and (board[2][0] is X))):
            return 1
        else:
            for k in range(3):
                for l in range(3):
                    if board[k][l] != X or board[k][l] != O:
                        return 5
        return 0
    else:
        if (((board[0][0] is O) and (board[0][1] is O) and (board[0][2] is O)) or
                ((board[1][0] is O) and (board[1][1] is O) and (board[1][2] is O)) or
                ((board[2][0] is O) and (board[2][1] is O) and (board[2][2] is O)) or
                ((board[0][0] is O) and (board[1][0] is O) and (board[2][0] is O)) or
                ((board[0][1] is O) and (board[1][1] is O) and (board[2][1] is O)) or
                ((board[0][2] is O) and (board[1][2] is O) and (board[2][2] is O)) or
                ((board[0][0] is O) and (board[1][1] is O) and (board[1][2] is O)) or
                ((board[0][2] is O) and (board[1][1] is O) and (board[2][0] is O))):
            return -1
        else:
            for k in range(3):
                for l in range(3):
                    if board[k][l] != X or board[k][l] != O:
                        return 5
        return 0


"""
    Returns the optimal action for the current player on the board.
    Minimax Algorithm
"""


def max_value(board):
    v = -math.inf
    if terminal(board):
        return utility(board)

    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def min_value(board):
    v = math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v


def minimax(board):
    min_move = [0, 0]
    max_move = [0, 0]
    if terminal(board) is True:
        return utility(board)

    elif player(board) is X:
        move_array = []
        for action in actions(board):
            move_array.append([min_value(result(board, action)), action])
        z = math.inf
        for i in move_array:
            if i[0] < z:
                min_move = i[1]
        print("move X: " + str(min_move))
        return min_move
    elif player(board) is O:
        move_array = []
        for action in actions(board):
            move_array.append([max_value(result(board, action)), action])
        z = -math.inf
        for i in move_array:
            if i[0] > z:
                max_move = i[1]
        print("move O: " + str(max_move))
        return max_move
