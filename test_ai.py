import pytest, giveMeAMove

baseInput = ['../myAI/giveMeAMove.py', '-b', '[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]', '-p', 'player-one', '-t', '15000']

def test_makes_a_move():
    with pytest.raises(SystemExit):
        giveMeAMove.main(baseInput)

def test_find_no_winner():
    emptyBoard = [[0,0,0,0,0,0,0]
                 ,[0,0,0,0,0,0,0]
                 ,[0,0,0,0,0,0,0]
                 ,[0,0,0,0,0,0,0]
                 ,[0,0,0,0,0,0,0]
                 ,[0,0,0,0,0,0,0]]
    assert giveMeAMove.findWin(emptyBoard) == 0

def test_find_tie():
    tieBoard = [[1,1,1,2,1,1,1],
                [2,2,2,1,2,2,2],
                [1,1,1,2,1,1,1],
                [2,2,2,1,2,2,2],
                [1,1,1,2,1,1,1],
                [2,2,2,1,2,2,2]]
    assert giveMeAMove.findWin(tieBoard) == -1

def test_find_horizontal_winner():
    horizontalWinBoard =   [[0,0,0,0,0,0,0]
                           ,[0,0,0,0,0,0,0]
                           ,[0,0,0,0,0,0,0]
                           ,[0,0,0,0,0,0,0]
                           ,[0,0,0,2,2,2,0]
                           ,[0,0,0,1,1,1,1]]
    assert giveMeAMove.findWin(horizontalWinBoard) == 1

def test_find_vertical_winner():
    verticalWinBoard = [[0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,1],
                        [0,0,0,0,0,2,1],
                        [0,0,0,0,0,2,1],
                        [0,0,0,0,0,2,1]]
    assert giveMeAMove.findWin(verticalWinBoard) == 1

def test_find_right_diag_winner():
    rDiagWinBoard =   [[0,0,0,0,0,0,0]
                      ,[0,0,0,0,0,0,0]
                      ,[0,0,0,1,0,0,0]
                      ,[0,0,1,2,0,0,0]
                      ,[0,1,2,2,0,0,0]
                      ,[1,2,2,2,0,0,0]]
    assert giveMeAMove.findWin(rDiagWinBoard) == 1

def test_find_left_diag_winner():
    lDiagWinBoard =   [[0,0,0,0,0,0,0]
                      ,[0,0,0,0,0,0,0]
                      ,[0,0,0,1,0,0,0]
                      ,[0,0,0,2,1,0,0]
                      ,[0,0,0,2,2,1,0]
                      ,[0,0,0,2,2,2,1]]
    assert giveMeAMove.findWin(lDiagWinBoard) == 1

def test_get_legal_plays():
    openBoard = [[0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0]]

    fullBoard = [[1,2,1,2,1,2,1],
                 [1,2,1,2,1,2,1],
                 [1,2,1,2,1,2,1],
                 [1,2,1,2,1,2,1],
                 [1,2,1,2,1,2,1],
                 [1,2,1,2,1,2,1]]

    sortaFullBoard = [[1,0,0,2,0,2,0],
                      [1,0,0,2,0,2,0],
                      [1,0,0,2,0,2,0],
                      [1,0,0,2,0,2,0],
                      [1,0,0,2,0,2,0],
                      [1,0,0,2,0,2,0]]

    assert giveMeAMove.findLegalMoves(openBoard) == [0,1,2,3,4,5,6]
    assert giveMeAMove.findLegalMoves(fullBoard) == []
    assert giveMeAMove.findLegalMoves(sortaFullBoard) == [1,2,4,6]

def test_make_move():
    sampleBoard =[[1,0,0,2,0,2,0],
                  [1,0,0,2,0,2,0],
                  [1,0,0,2,0,2,0],
                  [1,0,0,2,0,2,0],
                  [1,0,0,2,0,2,0],
                  [1,0,0,2,0,2,0]]
    sampleBoardAfter =[[1,0,0,2,0,2,0],
                       [1,0,0,2,0,2,0],
                       [1,0,0,2,0,2,0],
                       [1,0,0,2,0,2,0],
                       [1,0,0,2,0,2,0],
                       [1,0,1,2,0,2,0]]
    assert giveMeAMove.make_move(sampleBoard, 2, 1) == sampleBoardAfter

def test_make_invalid_move():
    sampleBoard =[[1,0,0,2,0,2,0],
                  [1,0,0,2,0,2,0],
                  [1,0,0,2,0,2,0],
                  [1,0,0,2,0,2,0],
                  [1,0,0,2,0,2,0],
                  [1,0,0,2,0,2,0]]
    assert giveMeAMove.make_move(sampleBoard, 0, 1) == False

def test_why_is_this_not_winning():
    sampleBoard = [[1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 2, 2, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [2, 1, 2, 2, 1, 1, 1], [2, 1, 2, 2, 1, 1, 2]]
    assert giveMeAMove.findWin(sampleBoard) == 1
