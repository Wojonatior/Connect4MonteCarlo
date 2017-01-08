import sys, argparse, ast

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
    return 0

def main(argv):
    board, player, msTime = parse_args(argv)
    debug_output([board, type(board), player, msTime])
    sys.exit(4)

if __name__ == "__main__":
    print(sys.argv)
    main(sys.argv)

    
