from tictactoe import terminal

X = "X"
O = "O"
EMPTY = None

BOARD_0 = [[EMPTY,EMPTY,EMPTY],[EMPTY,EMPTY,EMPTY],[EMPTY,EMPTY,EMPTY]]
BOARD_1 = [[X,EMPTY,EMPTY],[EMPTY,EMPTY,EMPTY],[EMPTY,EMPTY,EMPTY]]
BOARD_2 = [[X,EMPTY,EMPTY],[EMPTY,O,EMPTY],[EMPTY,EMPTY,EMPTY]]
BOARD_3 = [[X,EMPTY,EMPTY],[EMPTY,O,EMPTY],[X,EMPTY,EMPTY]]
BOARD_4 = [[X,EMPTY,EMPTY],[O,O,EMPTY],[X,EMPTY,EMPTY]]
BOARD_5 = [[X,EMPTY,EMPTY],[O,O,X],[X,EMPTY,EMPTY]]
BOARD_6 = [[X,O,EMPTY],[O,O,X],[X,EMPTY,EMPTY]]
BOARD_7 = [[X,O,EMPTY],[O,O,X],[X,X,EMPTY]]
BOARD_8 = [[X,O,EMPTY],[O,O,X],[X,X,O]]
BOARD_9 = [[X,O,X],[O,O,X],[X,X,O]]    

BOARD_10 = [[X,O,X],[X,O,EMPTY],[X,X,EMPTY]]    
BOARD_11 = [[X,O,X],[O,O,O],[EMPTY,EMPTY,EMPTY]]    
BOARD_12 = [[X,O,X],[O,O,X],[X,O,X]]    


def test_positive():
    assert terminal(BOARD_9) == True
    assert terminal(BOARD_10) == True
    assert terminal(BOARD_11) == True
    assert terminal(BOARD_12) == True

def test_negative():
    assert terminal(BOARD_8) == False
    assert terminal(BOARD_5) == False
    assert terminal(BOARD_4) == False
    assert terminal(BOARD_3) == False