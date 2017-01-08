import sys, argparse, ast

def parse_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("-b")
    parser.add_argument("-p")
    parser.add_argument("-t")
    pargs = vars(parser.parse_args())
    board, player, msTime = ast.literal_eval(pargs["b"]), 1 if pargs["p"] == "player-one" else 2, int(pargs["t"])
    return (board, player, msTime)

def debug_output(valuesToPrint):
    print("----------------------------------------------------------------------------------------------------------------------------")
    print(*valuesToPrint, sep='\n')
    print("----------------------------------------------------------------------------------------------------------------------------")

def main(argv):
    board, player, msTime = parse_args(argv)
    debug_output([board, type(board), player, msTime])
    sys.exit(4)

if __name__ == "__main__":
    print(sys.argv)
    main(sys.argv)

    
