import sys, argparse

def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("-b")
    parser.add_argument("-p")
    parser.add_argument("-t")
    pargs = vars(parser.parse_args())
    board, player, msTime = pargs["b"], pargs["p"], pargs["t"]
    print("--------------------------------------------------------------")
    print(board)
    print(player)
    print(msTime)
    print("--------------------------------------------------------------")
    sys.exit(4)

if __name__ == "__main__":
    main(sys.argv)
