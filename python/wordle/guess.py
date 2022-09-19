import Wordle
import sys, json

guess_scores = []
hard_mode = False
debug = False

for arg in sys.argv:
    if arg.startswith("-"):
        if arg == "--hard":
            hard_mode = True
        if arg == "--debug":
            debug = True
    if "=" in arg:
        guess_scores.append(arg.split("="))

wordle = Wordle.Wordle(sqlite_folder="../db", sqlite_dbname = "wordle.sqlite", guess_scores = guess_scores, hard_mode=hard_mode, debug=debug)

print(json.dumps(wordle.guess()))
