import Quordle
import sys, json

# usage is something like:
# python qsolve.py --start=trice,salon dough clump grass alibi 

hard_mode = False
debug = False
targets = []
start_with = []

for arg in sys.argv[1:]:
    if arg.startswith("-"):
        if arg == "--hard":
            hard_mode = True
        if arg == "--debug":
            debug = True
        if arg.startswith("--start"):
            start_with=arg.split("=")[1].split(",")
    else:
        targets.append(arg)

quordle = Quordle.Quordle(sqlite_dbname = "../db/wordle.sqlite", hard_mode=hard_mode, debug=debug)

print(json.dumps(quordle.solve(targets, start_with=start_with)))
