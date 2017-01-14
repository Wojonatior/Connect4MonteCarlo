import pytest, giveMeAMove

base_input = ['../myAI/giveMeAMove.py', '-b', '[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]', '-p', 'player-one', '-t', '15000']

def test_makes_a_move():
    with pytest.raises(SystemExit):
        giveMeAMove.main(base_input)

def test_find_no_winner():
    empty_board = [[0,0,0,0,0,0,0]
                 ,[0,0,0,0,0,0,0]
                 ,[0,0,0,0,0,0,0]
                 ,[0,0,0,0,0,0,0]
                 ,[0,0,0,0,0,0,0]
                 ,[0,0,0,0,0,0,0]]
    assert giveMeAMove.find_win(empty_board) == 0
    assert giveMeAMove.find_bb_win(empty_board) == 0

def test_find_tie():
    tie_board = [[1,1,1,2,1,1,1],
                [2,2,2,1,2,2,2],
                [1,1,1,2,1,1,1],
                [2,2,2,1,2,2,2],
                [1,1,1,2,1,1,1],
                [2,2,2,1,2,2,2]]
    assert giveMeAMove.find_win(tie_board) == -1
    assert giveMeAMove.find_bb_win(tie_board) == -1

def test_find_horizontal_winner():
    horizontal_win_board =   [[0,0,0,0,0,0,0]
                           ,[0,0,0,0,0,0,0]
                           ,[0,0,0,0,0,0,0]
                           ,[0,0,0,0,0,0,0]
                           ,[0,0,0,2,2,2,0]
                           ,[0,0,0,1,1,1,1]]
    assert giveMeAMove.find_win(horizontal_win_board) == 1
    assert giveMeAMove.find_bb_win(horizontal_win_board) == 1

def test_find_vertical_winner():
    vertical_win_board = [[0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,1],
                        [0,0,0,0,0,2,1],
                        [0,0,0,0,0,2,1],
                        [0,0,0,0,0,2,1]]
    assert giveMeAMove.find_win(vertical_win_board) == 1
    assert giveMeAMove.find_bb_win(vertical_win_board) == 1

def test_find_right_diag_winner():
    r_diag_win_board =   [[0,0,0,0,0,0,0]
                      ,[0,0,0,0,0,0,0]
                      ,[0,0,0,1,0,0,0]
                      ,[0,0,1,2,0,0,0]
                      ,[0,1,2,2,0,0,0]
                      ,[1,2,2,2,0,0,0]]
    assert giveMeAMove.find_win(r_diag_win_board) == 1
    assert giveMeAMove.find_bb_win(r_diag_win_board) == 1

def test_find_left_diag_winner():
    l_diag_win_board =   [[0,0,0,0,0,0,0]
                      ,[0,0,0,0,0,0,0]
                      ,[0,0,0,1,0,0,0]
                      ,[0,0,0,2,1,0,0]
                      ,[0,0,0,2,2,1,0]
                      ,[0,0,0,2,2,2,1]]
    assert giveMeAMove.find_win(l_diag_win_board) == 1
    assert giveMeAMove.find_bb_win(l_diag_win_board) == 1

def test_get_legal_plays():
    open_board = [[0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0]]

    full_board = [[1,2,1,2,1,2,1],
                 [1,2,1,2,1,2,1],
                 [1,2,1,2,1,2,1],
                 [1,2,1,2,1,2,1],
                 [1,2,1,2,1,2,1],
                 [1,2,1,2,1,2,1]]

    sorta_full_board = [[1,0,0,2,0,2,0],
                      [1,0,0,2,0,2,0],
                      [1,0,0,2,0,2,0],
                      [1,0,0,2,0,2,0],
                      [1,0,0,2,0,2,0],
                      [1,0,0,2,0,2,0]]

    assert giveMeAMove.find_legal_moves(open_board) == [0,1,2,3,4,5,6]
    assert giveMeAMove.find_legal_moves(full_board) == []
    assert giveMeAMove.find_legal_moves(sorta_full_board) == [1,2,4,6]

def test_make_move():
    sample_board =[[1,0,0,2,0,2,0],
                  [1,0,0,2,0,2,0],
                  [1,0,0,2,0,2,0],
                  [1,0,0,2,0,2,0],
                  [1,0,0,2,0,2,0],
                  [1,0,0,2,0,2,0]]
    sample_board_after =[[1,0,0,2,0,2,0],
                       [1,0,0,2,0,2,0],
                       [1,0,0,2,0,2,0],
                       [1,0,0,2,0,2,0],
                       [1,0,0,2,0,2,0],
                       [1,0,1,2,0,2,0]]
    assert giveMeAMove.make_move(sample_board, 2, 1) == sample_board_after

def test_make_invalid_move():
    sample_board =[[1,0,0,2,0,2,0],
                  [1,0,0,2,0,2,0],
                  [1,0,0,2,0,2,0],
                  [1,0,0,2,0,2,0],
                  [1,0,0,2,0,2,0],
                  [1,0,0,2,0,2,0]]
    assert giveMeAMove.make_move(sample_board, 0, 1) == False

def test_why_is_this_not_winning():
    sample_board = [[1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 2, 2, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [2, 1, 2, 2, 1, 1, 1], [2, 1, 2, 2, 1, 1, 2]]
    assert giveMeAMove.find_win(sample_board) == 1
