from tictactoe import winner

X = "X"
O = "O"
EMPTY = None

BOARD_9 = [[X,O,X],[O,O,X],[X,X,O]]    

BOARD_10 = [[X,O,X],[X,O,EMPTY],[X,X,EMPTY]]    
BOARD_11 = [[X,O,X],[O,O,O],[EMPTY,EMPTY,EMPTY]]    
BOARD_12 = [[X,O,X],[O,O,X],[X,O,X]]    

# Maybe test More things later, Wokring correctly right now

def test_X_won():
    assert winner(BOARD_10) == X
    assert winner(BOARD_12) == X

def test_O_won():
    assert winner(BOARD_11) == O

def test_otherwise():
    assert winner(BOARD_9) == None