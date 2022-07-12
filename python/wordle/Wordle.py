import math
from functools import reduce
from contextlib import closing
import sqlite3

class Wordle :

    # all incoming payloads should include:
    # - name of sqlite db
    # - hard mode?
    # - list of guesses, possibly empty
    # - list of list of scores (or list of scores for wordle)
    
    # endpoints
    # - guess: send in above payload and get back
    #   word (next guess)
    #   expected entropy
    #   - details element, includes entropy before and after score for each response.  if more than one target word then split entropies out?

    # - solve: above payload, plus list of target words


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

    def __init__(self, dbname, guess_scores, hard_mode=False, debug=False) :
        self.dbname = dbname
        self.guess_scores = guess_scores
        self.hard_mdoe = hard_mode
        self.debug = debug

    def query(self, sql, title=None):
        with closing(sqlite3.connect(self.dbname)) as connection:
            cursor = connection.cursor()
            if self.debug and title is not None:
                print(f">> {title}: {sql}")
            cursor.execute(sql)
            return cursor.fetchall()

    def next_guesses(self, remaining_answers) :
        guesses = {}
        for guess in self.guesses:
            guesses[guess] = {"guess" : guess,
                              "expected_uncertainty" : self.expected_uncertainty_of_guess(guess, remaining_answers),
                              "hard_mode" : guess in remaining_answers}
        return guesses

    def next_guesses_sorted(self, next_guesses):
        return guesses.values().sort(key=lambda x: x["expected_uncertainty"])

    def remaining_answers(self):
        remaining_answers = []
        froms = ["answers as a"]
        where_clauses = []
        where_clause = ""
        n = 0
        for [guess, score] in self.guess_scores:
            table = f"scores_{n}"
            froms.append(f"scores as {table}")
            where_clauses.append(f"a.answer = {table}.answer")
            where_clauses.append(f"'{guess}' = {table}.guess")
            where_clauses.append(f"'{score}' = {table}.score")
            n = n + 1
        if n > 0:
            where_clause = f" where " + " and ".join(where_clauses)
        from_clause = ", ".join(froms)
        sql = f"select a.answer from {from_clause} {where_clause}"
        return list(map(lambda x : x[0], self.query(sql)))

    def expected_uncertainty_by_guess(self, remaining_answers) :
        answer_count = len(remaining_answers)
        answers_clause = ",".join(list(map(lambda x : f"'{x}'", remaining_answers)))
        sql = f"select guess, score, count(*) from scores where answer in ({answers_clause}) group by 1, 2"
        uncertainty_by_guess = {}
        for [guess, score, count] in self.query(sql):
            if not guess in uncertainty_by_guess:
                uncertainty_by_guess[guess] = 0
            uncertainty_by_guess[guess] += count * math.log(count, 2) / answer_count
        return {k: v for k, v in sorted(uncertainty_by_guess.items(), key=lambda item: item[1])}
# print(list(wordle.expected_uncertainty_by_guess(remaining).items())[0:10])

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
    
