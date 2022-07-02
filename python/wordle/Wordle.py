import math
from functools import reduce

class Wordle :

    # wordle api functions

    def solve(self, target_word, start_with) :
        pass

    def guess(self, guess_score_pairs, count=1) :
        remaining_answers = self.remaining_answers(guess_score_pairs)
        if len(remaining_answers) == 1:
            return remaining_answers[0]
        else:
            next_guesses = self.next_guesses_sorted(self.next_guesses(remaining_answers))
            return next_guesses[0:count]

    # quordle api functions

    def qsolve(self, target_words, start_with) :
        pass

    def qguess(self, guesses, scores) :
        pass

    # to compute the next guess given a set of guesses and scores, look for a guess
    # that minimizes the expected remaining uncertainty.  Each guess has associated
    # with it a set of pairs [answer, score] where answer is taken from the remaining
    # possible answers and score is the corresponding score

    # so iterate through the remining possible answers computing the relevant score
    # For each possible score, collate the number of answers that correspond
    # to it.  Then take sum_guess(num(ans) * log(num(ans))) / num(guess)

    # need to be able to efficiently query the following:
    #  (guess, answer) => score
    #  ([guess, score]) => {answers}

    def __init__(self, scores_file) :
        raw_scores = self.split_by("|", self.load_file(scores_file))
        self.answers = self.extract_column(raw_scores, 0)
        self.guesses = self.extract_column(raw_scores, 1)
        self.score_by_answer_and_guess = self.extract_score_by_answer_and_guess(raw_scores)
        self.answers_by_guess_and_score = self.extract_answers_by_guess_and_score(raw_scores)

    def next_guesses(self, remaining_answers) :
        guesses = {}
        for guess in self.guesses:
            guesses[guess] = {"guess" : guess,
                              "expected_uncertainty" : self.expected_uncertainty_of_guess(guess, remaining_answers),
                              "hard_mode" : guess in remaining_answers}
        return guesses

    def next_guesses_sorted(self, next_guesses):
        return guesses.values().sort(key=lambda x: x["expected_uncertainty"])

    def remaining_answers(self, guess_score_pairs):
        remaining_answers = []
        for answer in self.answers:
            for [guess, score] in guess_score_pairs:
                if self.score_by_answer_and_guess[answer][guess] != score:
                    next
            remaining_answers.append(answer)
        return remaining_answers

    def expected_uncertainty_of_guess(self, guess, remaining_answers):
        counts_by_score = {}
        remaining_answer_count = 0
        for answer in remaining_answers:
            score = self.score_by_answer_and_guess[answer][guess]
            if not score in counts_by_score:
                counts_by_score[score] = 0
            counts_by_score[score] = counts_by_score[score] + 1
            remaining_answer_count = remaining_answer_count + 1
        sum = 0
        for score in counts_by_score:
            sum = sum + math.log(counts_by_score[score], 2) 
        return (sum / remaining_answer_count)

    # quordle-related methods (for handling multiple wordles at once)

    def merge_maps(self, g, maps_to_merge) :
        merged = {"guess": g}
        merged['guess'] = g

        # qualifies as hard mode if any of them are hard mode
        merged['hard_mode'] = reduce(lambda x, y: x or y, map(lambda x: x['hard_mode']))
        # expected uncertainty is the sum of the expected uncertainties
        merged['expected_uncertainty'] = reduce(lambda x, y: x + y, map(lambda x: x['expected_uncertainty']))

        return merged

    def merge_next_guesses(self, next_guess_maps) :
        merged_guesses = {}
        for g in self.guesses:
            merged_guesses[g] = self.merge_maps(g, map(lambda m: m[g], next_guess_maps))
        return merged_guesses
    

    # utility methods

    def load_file(self, fname) :
        lines = []
        with open(fname) as a:
            while True:
                line = a.readline()
                if not line:
                    break
                lines.append(line.rstrip())
        return lines

    def split_by(self, char, lines):
        rows = []
        for line in lines:
            rows.append(line.split(char))
        return rows

    def extract_score_by_answer_and_guess(self, rows) :
        score_by_answer_and_guess = {}
        for [answer, guess, score] in rows:
            if not answer in score_by_answer_and_guess:
                score_by_answer_and_guess[answer] = {}
            score_by_answer_and_guess[answer][guess] = score
        return score_by_answer_and_guess

    def extract_answers_by_guess_and_score(self, rows):
        answers_by_guess_and_score = {}
        for [answer, guess, score] in rows:
            if not guess in answers_by_guess_and_score:
                answers_by_guess_and_score[guess] = {}
            if not score in answers_by_guess_and_score[guess]:
                answers_by_guess_and_score[guess][score] = []
            answers_by_guess_and_score[guess][score].append(answer)
        return answers_by_guess_and_score

    def extract_column(self, rows, i) :
        col = []
        for row in rows:
            col.append(row[i])
        return col
    
