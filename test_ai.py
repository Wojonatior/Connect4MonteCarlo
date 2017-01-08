import pytest, giveMeAMove

baseInput = ['../myAI/giveMeAMove.py', '-b', '[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]', '-p', 'player-one', '-t', '15000']

def test_makes_a_move():
    with pytest.raises(SystemExit):
        giveMeAMove.main(baseInput)

def test_find_no_winner():
    emptyBoard = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
    assert giveMeAMove.findWin(emptyBoard) == 0

def test_find_horizontal_winner():
    horizontalWinBoard = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,2,2,2,0],[0,0,0,1,1,1,1]]
    assert giveMeAMove.findWin(horizontalWinBoard) == 1

def test_find_vertical_winner():
    horizontalWinBoard = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,1],[0,0,0,0,0,2,1],[0,0,0,0,0,2,1],[0,0,0,0,0,2,1]]
    assert giveMeAMove.findWin(horizontalWinBoard) == 1
