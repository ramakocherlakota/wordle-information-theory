import Wordle
import sys, json

guess_scores = []
hard_mode = False
debug = False
dbname = "wordle.sqlite"

for arg in sys.argv[1:]:
    if arg.startswith("-"):
        if arg == "--hard":
            hard_mode = True
        if arg == "--debug":
            debug = True
        if arg.startswith("--dbname"):
            dbname = arg.split("=")[1]
    elif "=" in arg:
        guess_scores.append(arg.split("="))

wordle = Wordle.Wordle(sqlite_folder="../db", sqlite_dbname = dbname, guess_scores = guess_scores, hard_mode=hard_mode, debug=debug)

print(json.dumps(wordle.guess()))
