from tictactoe import player

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



def test_O_turn():
    assert player(BOARD_1) == O
    assert player(BOARD_3) == O
    assert player(BOARD_5) == O
    assert player(BOARD_7) == O

def test_X_turn():
    assert player(BOARD_0) == X
    assert player(BOARD_2) == X
    assert player(BOARD_4) == X
    assert player(BOARD_6) == X
    assert player(BOARD_8) == X

def test_Empty():
    assert player(BOARD_9) == None


