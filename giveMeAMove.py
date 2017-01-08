import sys, argparse, ast

def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("-b")
    parser.add_argument("-p")
    parser.add_argument("-t")
    pargs = vars(parser.parse_args())
    board, player, msTime = ast.literal_eval(pargs["b"]), 1 if pargs["p"] == "player-one" else 2, int(pargs["t"])
    print("--------------------------------------------------------------")
    print(board)
    print(type(board))
    print(type(board[1]))
    print(player)
    print(msTime)
    print("--------------------------------------------------------------")
    sys.exit(4)

if __name__ == "__main__":
    print(sys.argv)
    main(sys.argv)

    
