import Wordle
import sys, json

start_with = []
hard_mode = False
debug = False
target = None

for arg in sys.argv[1:]:
    if arg.startswith("-"):
        if arg == "--hard":
            hard_mode = True
        if arg == "--debug":
            debug = True
        if arg.startswith("--start"):
            start_with = arg.split("=")[1].split(",")
    else:
        target = arg

if not target:
    print("You must specify a target word!")
    sys.exit(1)

wordle = Wordle.Wordle(sqlite_folder="../db", sqlite_dbname = "wordle.sqlite", hard_mode=hard_mode, debug=debug)

print(json.dumps(wordle.solve(target, start_with=start_with)))
