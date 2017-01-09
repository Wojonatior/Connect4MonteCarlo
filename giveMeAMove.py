import sys, argparse, ast
from threading import Timer
from random import choice
from copy import deepcopy
#TODO Cull imports to just required functions

class MonteCarloAI(object):
    def __init__(self, board, numGames, aiPlayer, timeout):
        self.board = board
        self.numGames = numGames
        self.aiPlayer = aiPlayer
        # timeout is assumed to be provided in MS
        self.timeout = timeout / 1000
        self.legalMoves = findLegalMoves(self.board)
        self.winCounter = {}
        self.playCounter = {}

    def calculate_best_move(self):
        #Bail out early here
        
        simulatedGames = 0
        move_timeout = Timer(self.timeout, self.execute_best_move)
        move_timeout.start()

        # for move in self.legalMoves:
            # strBoard = str(make_move(self.board, move, self.aiPlayer))
            # self.playCounter[strBoard] = 0
            # self.winCounter[strBoard] = 0


        while True:
            self.simulate_one_game(self.board)
            simulatedGames += 1
            # if simulatedGames == self.numGames:
                # self.execute_best_move()


    def simulate_one_game(self, board):
        visitedBoards = set()
        simulatedBoard = deepcopy(board)
        playerToOptimize = self.aiPlayer
        noNewNodeAdded = True
        movingPlayer = playerToOptimize
        winningPlayer = 0
        numMovesMade = 0


        # Maximum number of moves is 42, so just play util there aren't moves left
        while not winningPlayer:
            possibleMoves = findLegalMoves(simulatedBoard)
            pendingMove = choice(possibleMoves)
            simulatedBoard = make_move(simulatedBoard, pendingMove, movingPlayer)
            strBoard = str(simulatedBoard)

            if noNewNodeAdded and not (strBoard in self.playCounter):
                noNewNodeAdded = False
                self.playCounter[strBoard] = 0
                self.winCounter[strBoard] = 0

            visitedBoards.add(strBoard)
            # Flip the activePlayer and check for a win
            movingPlayer = 1 if movingPlayer == 2 else 2
            winningPlayer = findWin(simulatedBoard)
        
        
        #Aggregate the results of the game into the playCounter and winCounter
        for boardString in visitedBoards:
            if boardString not in self.playCounter:
                continue
            self.playCounter[boardString] += 1
            if self.aiPlayer == winningPlayer:
                self.winCounter[boardString] += 1


    def execute_best_move(self):
        # Moves are in the form of (colToPlay, newBoardState)
        moves_to_consider = [(play, str(make_move(deepcopy(self.board), play, self.aiPlayer))) for play in self.legalMoves]

        for play, boardString in moves_to_consider:
            print("Trimmed String: ", boardString.replace(" ", ""))
            print("wins: ", self.winCounter.get(boardString))
            print("plays: ", self.playCounter.get(boardString))
            print("pendingPlay: ", play)

        winPercentage, bestMove = max([ (self.winCounter.get(boardString, 0)/ self.playCounter.get(boardString, 1) , play) for play, boardString in moves_to_consider ])

        sys.exit(bestMove)

# accepts the argv object and returns the relevant 3 values as a relevant type 
def parse_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("-b")
    parser.add_argument("-p")
    parser.add_argument("-t")
    pargs = vars(parser.parse_args())
    board, player, msTime = ast.literal_eval(pargs["b"]), 1 if pargs["p"] == "player-one" else 2, int(pargs["t"])
    return (board, player, msTime)

#Prints each item in a list  with some lines ahead/after to make output easily visible
def debug_output(valuesToPrint):
    print("----------------------------------------------------------------------------------------------------------------------------")
    print(*valuesToPrint, sep='\n')
    print("----------------------------------------------------------------------------------------------------------------------------")

#returns the player number if the board contains a winning player, 0 if no winner
def findWin(board):
    height = 6
    width = 7
    # Checking for Horizontal
    for y in range(height):
        for x in range(width-3):
            if board[y][x:x+4].count(1) == 4:
                return 1
            if board[y][x:x+4].count(2) == 4:
                return 2

    # Checking for Vertical
    for x in range(width):
        for y in range(height-3):
            if board[y][x] == 1 and board[y+1][x] == 1 and board[y+2][x] == 1 and board[y+3][x] == 1:
                return 1
            if board[y][x] == 2 and board[y+1][x] == 2 and board[y+2][x] == 2 and board[y+3][x] == 2:
                return 2
    # Checking for Right Diagonal
    for y in range(height-1, height-3, -1):
        for x in range(width-3):
            if board[y][x] == 1 and board[y-1][x+1] == 1 and board[y-2][x+2] == 1 and board[y-3][x+3] == 1:
                return 1
            if board[y][x] == 2 and board[y-1][x+1] == 2 and board[y-2][x+2] == 2 and board[y-3][x+3] == 2:
                return 2
    # Checking for Left Diagonal
    for y in range(height-1, height-3, -1):
        for x in range(width-1, width-3, -1):
            if board[y][x] == 1 and board[y-1][x-1] == 1 and board[y-2][x-2] == 1 and board[y-3][x-3] == 1:
                return 1
            if board[y][x] == 2 and board[y-1][x-1] == 2 and board[y-2][x-2] == 2 and board[y-3][x-3] == 2:
                return 2
    # Checking for Tie
    if len(findLegalMoves(board)) == 0:
        return -1
    # No winner or tie
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

def findLegalMoves(board):
    return [index for index, value in enumerate(board[0]) if value == 0]

def main(argv):
    board, player, msTime = parse_args(argv)
    ai = MonteCarloAI(board, 1000, player, msTime - 1000)
    ai.calculate_best_move()

if __name__ == "__main__":
    main(sys.argv)
