import Wordle

wordle = Wordle.Wordle("../db/wordle.sqlite", [["trice", "-b--w"], ["salon", "--w--"]])

print(wordle.guess())
