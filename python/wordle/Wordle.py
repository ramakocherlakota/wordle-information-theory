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

    def solve(self, target_word, start_with="raise") :
        pass

    def guess(self) :
        remaining_answers = self.remaining_answers()
        if len(remaining_answers) == 0:
            raise Exception("Inconsistent data")
        if len(remaining_answers) <= 2:
            return {'guess': remaining_answers[0], 'uncertainty': 0, 'hard_mode' : True}
        else:
            next_guesses = self.expected_uncertainty_by_guess(remaining_answers)
            if self.hard_mode:
                next_guesses = filter(lambda x : x['hard_mode'], next_guesses)
            return next_guesses[0]

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
        self.hard_mode = hard_mode
        self.debug = debug

    def query(self, sql, title=None):
        with closing(sqlite3.connect(self.dbname)) as connection:
            connection.create_function('log2', 1, lambda x: math.log(x, 2))
            cursor = connection.cursor()
            if self.debug and title is not None:
                print(f">> {title}: {sql}")
            cursor.execute(sql)
            return cursor.fetchall()

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
            where_clauses.append(f"'{guess.lower()}' = {table}.guess")
            where_clauses.append(f"'{score.upper()}' = {table}.score")
            n = n + 1
        if n > 0:
            where_clause = f" where " + " and ".join(where_clauses)
        from_clause = ", ".join(froms)
        sql = f"select a.answer from {from_clause} {where_clause}"
        return list(map(lambda x : x[0], self.query(sql, "remaining_answers")))

    def expected_uncertainty_by_guess(self, remaining_answers) :
        answer_count = len(remaining_answers)
        answers_clause = ",".join(list(map(lambda x : f"'{x}'", remaining_answers)))
        subsql = f"select guess, score, count(*) as c from scores where answer in ({answers_clause}) group by 1, 2"
        sql = f"select guess, sum(c * log2(c)) / sum(c) from ({subsql}) group by 1 order by 2"
        uncertainty_by_guess = []
        for [guess, uncertainty] in self.query(sql):
            uncertainty_by_guess.append({"guess": guess,
                                         "uncertainty": uncertainty,
                                         "hard_mode": guess in remaining_answers})
        return uncertainty_by_guess
# print(list(wordle.expected_uncertainty_by_guess(remaining).items())[0:10])

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
    
