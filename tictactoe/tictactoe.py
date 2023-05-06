"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    num_X = 0
    num_O = 0
    num_Empty = 0
    for row in range(len(board)):
        for column in range (len(board[row])):
            if board[row][column]==X:
                num_X += 1
                #console.log("🚀 ~ file: tictactoe.py:29 ~ num_X:", num_X)
            elif board[row][column]==O:
                num_O += 1
                #console.log("🚀 ~ file: tictactoe.py:32 ~ num_O:", num_O)
            else:
                num_Empty +=1
                #console.log("🚀 ~ file: tictactoe.py:35 ~ num_empty:", num_empty)
    
    #print(num_X)
    #print(num_O)
    #print(num_Empty)
    # This means that the whole board is full
    if num_Empty == 0:
        return None
    elif num_X > num_O:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    #raise NotImplementedError
    moves = []
    for row in range(len(board)):
        for column in range (len(board[row])):
            if(board[row][column]==EMPTY):
                moves.append((row,column))

    return moves    


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #raise NotImplementedError
    if ((board[0][0] == X and board[0][1] == X and board[0][2] == X) or
        (board[1][0] == X and board [1][1] == X and board[1][2] == X) or
        (board[2][0] == X and board [2][1] == X and board[2][2] == X) or 
        (board[0][0] == X and board [1][0] == X and board[2][0] == X) or 
        (board[0][1] == X and board [1][1] == X and board[2][1] == X) or 
        (board[0][2] == X and board [1][2] == X and board[2][2] == X) or 
        (board[0][0] == X and board [1][1] == X and board[2][2] == X) or 
        (board[0][2] == X and board [1][1] == X and board[2][0] == X) ):

        return X
    elif ((board[0][0] == O and board[0][1] == O and board[0][2] == O) or
        (board[1][0] == O and board [1][1] == O and board[1][2] == O) or
        (board[2][0] == O and board [2][1] == O and board[2][2] == O) or 
        (board[0][0] == O and board [1][0] == O and board[2][0] == O) or 
        (board[0][1] == O and board [1][1] == O and board[2][1] == O) or 
        (board[0][2] == O and board [1][2] == O and board[2][2] == O) or 
        (board[0][0] == O and board [1][1] == O and board[2][2] == O) or 
        (board[0][2] == O and board [1][1] == O and board[2][0] == O) ):

        return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #raise NotImplementedError
    if winner(board) is None:
        for row in range(len(board)):
            for column in range (len(board[row])):
                if board[row][column] is EMPTY:
                    return False
    else:
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    #raise NotImplementedError
    if terminal(board) is True:
        if ((board[0][0] == X and board[0][1] == X and board[0][2] == X) or
            (board[1][0] == X and board [1][1] == X and board[1][2] == X) or
            (board[2][0] == X and board [2][1] == X and board[2][2] == X) or 
            (board[0][0] == X and board [1][0] == X and board[2][0] == X) or 
            (board[0][1] == X and board [1][1] == X and board[2][1] == X) or 
            (board[0][2] == X and board [1][2] == X and board[2][2] == X) or 
            (board[0][0] == X and board [1][1] == X and board[2][2] == X) or 
            (board[0][2] == X and board [1][1] == X and board[2][0] == X) ):

            return 1
        elif ((board[0][0] == O and board[0][1] == O and board[0][2] == O) or
            (board[1][0] == O and board [1][1] == O and board[1][2] == O) or
            (board[2][0] == O and board [2][1] == O and board[2][2] == O) or 
            (board[0][0] == O and board [1][0] == O and board[2][0] == O) or 
            (board[0][1] == O and board [1][1] == O and board[2][1] == O) or 
            (board[0][2] == O and board [1][2] == O and board[2][2] == O) or 
            (board[0][0] == O and board [1][1] == O and board[2][2] == O) or 
            (board[0][2] == O and board [1][1] == O and board[2][0] == O) ):

            return -1
        else:
            return 0
    else:
        raise ValueError("Board has not reached a terminal state yet")


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError