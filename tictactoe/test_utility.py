from tictactoe import utility

X = "X"
O = "O"
EMPTY = None

BOARD_9 = [[X,O,X],[O,O,X],[X,X,O]]    

BOARD_10 = [[X,O,X],[X,O,EMPTY],[X,X,EMPTY]]    
BOARD_11 = [[X,O,X],[O,O,O],[EMPTY,EMPTY,EMPTY]]    
BOARD_12 = [[X,O,X],[O,O,X],[X,O,X]]    

# Maybe test More things later, Wokring correctly right now

def test_X_won():
    assert utility(BOARD_10) == 1
    assert utility(BOARD_12) == 1

def test_O_won():
    assert utility(BOARD_11) == -1

def test_Draw():
    assert utility(BOARD_9) == 0