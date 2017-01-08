import pytest, giveMeAMove

baseInput = ['../myAI/giveMeAMove.py', '-b', '[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]', '-p', 'player-one', '-t', '15000']

def test_makes_a_move():
    with pytest.raises(SystemExit):
        giveMeAMove.main(baseInput)
