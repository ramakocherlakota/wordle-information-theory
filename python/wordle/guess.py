import Wordle

wordle = Wordle.Wordle("../db/wordle.sqlite", [["trice", "ww--w"], ["salon", "-----"]])

print(wordle.guess())
