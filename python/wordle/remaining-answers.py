import Wordle
import sys
import json

guess_scores = []
for arg in sys.argv:
    if "=" in arg:
        guess_scores.append(arg.split("="))

wordle = Wordle.Wordle(dbname = "../db/wordle.sqlite", guess_scores = guess_scores)

remaining_answers = wordle.remaining_answers()
print(json.dumps(remaining_answers, indent=4, sort_keys=True))

