import Quordle
import sys, json

# example 
# python qguess.py --guesses=trice,salon --scores="-----,bbb--;bb--b,-w---;--w--,-ww-b;w-b--,--w-w"

guesses = []
scores_list = []
hard_mode = False
debug = False

for arg in sys.argv:
    if arg.startswith("-"):
        if arg == "--hard":
            hard_mode = True
        if arg == "--debug":
            debug = True
        if arg.startswith("--guess"):
            guesses = arg.split("=")[1].split(",")
        if arg.startswith("--score"):
            for scores in arg.split("=")[1].split(";"):
                scores_list.append(scores.split(","))

quordle = Quordle.Quordle(sqlite_dbname = "../db/wordle.sqlite", guesses=guesses, scores_list=scores_list, hard_mode=hard_mode, debug=debug)

print(json.dumps(quordle.guess()))
