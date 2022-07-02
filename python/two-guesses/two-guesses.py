import math

log2 = math.log(2)

answers = []
with open("../../data/answers.txt") as a:
    while True:
        line = a.readline()
        if not line:
            break
        answers.append(line.rstrip())

scores = {}
with open("../../data/scores.txt") as s:
    while True:
        line = s.readline()
        if not line:
            break
        (answer, guess, score) = line.rstrip().split("|")
        if not answer in scores:
            scores[answer] = {}
        scores[answer][guess] = score

for guess1 in answers:
    for guess2 in answers:
        if guess1 < guess2:
            guess_scores = {}
            for answer in answers:
                score = scores[answer][guess1] + "|" + scores[answer][guess2]
                if not score in guess_scores:
                    guess_scores[score] = 0
                guess_scores[score] = guess_scores[score] + 1
            tot = 0
            sum = 0
            for score in guess_scores:
                num = guess_scores[score]
                tot = tot + num
                sum = sum + num * math.log(num) / log2
            assert tot == len(answers)
            print(f"{sum / tot} {guess1} {guess2}")
