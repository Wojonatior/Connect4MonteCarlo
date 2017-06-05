from ast import literal_eval
from argparse import ArgumentParser
from sys import exit, argv
from random import choice
from copy import deepcopy
from time import time

class Monte_Carlo_AI(object):
    def __init__(self, board, num_games, ai_player, timeout):
        # Init the overall game state
        self.board = board
        self.num_games = num_games
        self.ai_player = ai_player
        # timeout is assumed to be provided in MS
        self.timeout = timeout / 1000
        self.legal_moves = find_legal_moves(self.board)
        self.win_counter = {}
        self.play_counter = {}
        self.start_time = time()

    def calculate_best_move(self):
        #Bail out early here
        if len(self.legal_moves) == 1:
            exit(self.legal_moves[0])

        self.simulated_games = 0
        end_time = time() + self.timeout

        while self.simulated_games < self.num_games and time() < end_time:
            self.simulate_one_game(self.board)
            self.simulated_games += 1

        self.execute_best_move()

    def simulate_one_game(self, board):
        visited_boards = set()
        simulated_board = deepcopy(board)
        no_new_node_added = True
        moving_player = self.ai_player
        # 0 represents that no player is currently winning
        winning_player = 0

        # Maximum number of moves is 42, so just play until there aren't moves left or someone wins
        while not winning_player:
            possible_moves = find_legal_moves(simulated_board)
            pending_move = choice(possible_moves)
            simulated_board = make_move(simulated_board, pending_move, moving_player)
            str_board = str(simulated_board)

            if no_new_node_added and not (str_board in self.play_counter):
                no_new_node_added = False
                self.play_counter[str_board] = 0
                self.win_counter[str_board] = 0

            visited_boards.add(str_board)
            # Flip the moving_player and check for a win

            moving_player = 1 if moving_player == 2 else 2
            winning_player = find_bb_win(simulated_board)

        #Aggregate the results of the game into the play_counter and win_counter
        for board_string in visited_boards:
            if board_string not in self.play_counter:
                continue
            self.play_counter[board_string] += 1
            if self.ai_player == winning_player:
                self.win_counter[board_string] += 1

    def execute_best_move(self):
        # Moves are in the form of (colToPlay, newBoardState)
        moves_to_consider = [(play, str(make_move(deepcopy(self.board), play, self.ai_player))) for play in self.legal_moves]

        win_percentage, best_move = max([ (self.win_counter.get(board_string, 0)/ self.play_counter.get(board_string, 1) , play) for play, board_string in moves_to_consider ])

        print("\n")
        print("--------------------------------------------------------------------------------")
        print("Seconds: ", time() - self.start_time)
        print("Moves: ", self.simulated_games)
        print("--------------------------------------------------------------------------------")
        exit(best_move)

def generate_bitboard(two_dim_board):
    p1_bboard = 49 * ["0"]
    p2_bboard = 49 * ["0"]
    bit_index = 47

    for x in range(7)[::-1]:
        for y in range(6):
            if two_dim_board[y][x] == 1:
                p1_bboard[bit_index] = "1"
            elif two_dim_board[y][x] == 2:
                p2_bboard[bit_index] = "1"
            bit_index -= 1
        # This is to generate the empty row at the "top" of the bitboard
        bit_index -= 1
    p1_bstring = "".join(p1_bboard)
    p2_bstring = "".join(p2_bboard)

    return (int(p1_bstring, 2), int(p2_bstring, 2))

def check_one_bitboard(bitboard):
    # Check \
    temp_bboard = bitboard & (bitboard >> 6)
    if(temp_bboard & (temp_bboard >> 2 * 6)):
        return True
    # Check -
    temp_bboard = bitboard & (bitboard >> 7)
    if(temp_bboard & (temp_bboard >> 2 * 7)):
        return True
    # Check /
    temp_bboard = bitboard & (bitboard >> 8)
    if(temp_bboard & (temp_bboard >> 2 * 8)):
        return True
    # Check |
    temp_bboard = bitboard & (bitboard >> 1)
    if(temp_bboard & (temp_bboard >> 2 * 1)):
        return True
    
def find_bb_win(board):
    p1_bitboard, p2_bitboard = generate_bitboard(board)
    if check_one_bitboard(p1_bitboard):
        return 1
    elif check_one_bitboard(p1_bitboard):
        return 2
    else:
        if len(find_legal_moves(board)) == 0:
            return -1
        else:
            return 0

def make_move(board, column, player):
    row = 5
    while row >= 0:
        if board[row][column] == 0:
            board[row][column] = player
            return board
        else:
            row -= 1
    return False

def find_legal_moves(board):
    return [index for index, value in enumerate(board[0]) if value == 0]

# accepts the argv object and returns the 3 values as a relevant types
def parse_args(argv):
    parser = ArgumentParser()
    parser.add_argument("-b")
    parser.add_argument("-p")
    parser.add_argument("-t")
    pargs = vars(parser.parse_args())
    board, player, ms_time = literal_eval(pargs["b"]), 1 if pargs["p"] == "player-one" else 2, int(pargs["t"])
    return (board, player, ms_time)

def main(argv):
    board, player, ms_time = parse_args(argv)
    ai = Monte_Carlo_AI(board, 500000, player, ms_time - 5000)
    ai.calculate_best_move()

if __name__ == "__main__":
    main(argv)
