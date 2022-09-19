import Wordle
import sys, json

guess_scores = []
hard_mode = False
debug = False
for_guess = None

for arg in sys.argv[1:]:
    if arg.startswith("-"):
        if arg == "--hard":
            hard_mode = True
        if arg == "--debug":
            debug = True
    elif "=" in arg:
        guess_scores.append(arg.split("="))
    else:
        for_guess = arg

wordle = Wordle.Wordle(sqlite_folder="../db", sqlite_dbname = "wordle.sqlite", guess_scores = guess_scores, hard_mode=hard_mode, debug=debug)

print(json.dumps(wordle.rate_guess(for_guess)))
