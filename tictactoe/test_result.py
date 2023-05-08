from tictactoe import result

X = "X"
O = "O"
EMPTY = None

BOARD_0_Input = [[EMPTY,EMPTY,EMPTY],[EMPTY,EMPTY,EMPTY],[EMPTY,EMPTY,EMPTY]]
BOARD_0_Result = [[X,EMPTY,EMPTY],[EMPTY,EMPTY,EMPTY],[EMPTY,EMPTY,EMPTY]]
ACTION_0 =[0,0]

BOARD_1_Input = [[X,EMPTY,EMPTY],[EMPTY,O,EMPTY],[EMPTY,EMPTY,EMPTY]]
BOARD_1_Result = [[X,EMPTY,EMPTY],[EMPTY,O,EMPTY],[X,EMPTY,EMPTY]]
ACTION_1 = [2,0]

BOARD_2_Input = [[X,EMPTY,EMPTY],[O,O,EMPTY],[X,EMPTY,EMPTY]]
BOARD_2_Result = [[X,EMPTY,EMPTY],[O,O,X],[X,EMPTY,EMPTY]]
ACTION_2 = [1,2]

BOARD_3_Input = [[X,O,EMPTY],[O,O,X],[X,EMPTY,EMPTY]]
BOARD_3_Result = [[X,O,EMPTY],[O,O,X],[X,X,EMPTY]]
ACTION_3 = [2,1]

BOARD_4_Input = [[X,O,EMPTY],[O,O,X],[X,X,O]]
BOARD_4_Result = [[X,O,X],[O,O,X],[X,X,O]]    
ACTION_4 = [0,2]
    
BOARD_5_Input = [[X,O,X],[X,EMPTY,O],[X,X,EMPTY]]    
BOARD_5_Result = [[X,O,X],[X,O,O],[X,X,EMPTY]]    
ACTION_5 = [1,1]

BOARD_6_Exception = [[X,O,X],[O,O,X],[X,O,X]]    
ACTION_6 = [1,1]

BOARD_7_Exception = [[X,O,X],[O,O,EMPTY],[X,O,EMPTY]]    
ACTION_7 = [0,0]

def test_move_X():
    assert result(BOARD_0_Input,ACTION_0) == BOARD_0_Result
    assert result(BOARD_1_Input,ACTION_1) == BOARD_1_Result
    assert result(BOARD_2_Input,ACTION_2) == BOARD_2_Result
    assert result(BOARD_3_Input,ACTION_3) == BOARD_3_Result
    assert result(BOARD_4_Input,ACTION_4) == BOARD_4_Result 
    assert result(BOARD_5_Input,ACTION_5) == BOARD_5_Result

"""
This function causes exception
"""
def test_exception():
    result(BOARD_6_Exception,ACTION_6)
    result(BOARD_7_Exception,ACTION_7)
