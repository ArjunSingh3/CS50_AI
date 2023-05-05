from tictactoe import actions

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

def test_actions():
    assert actions(BOARD_9) == []
    assert actions(BOARD_8) == [(0,2)]
    assert actions(BOARD_7) == [(0,2),(2,2)]
    assert actions(BOARD_6) == [(0,2),(2,1),(2,2)]
    assert actions(BOARD_5) == [(0,1),(0,2),(2,1),(2,2)]
    assert actions(BOARD_0) == [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]