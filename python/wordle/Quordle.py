import Wordle
from functools import reduce

class Quordle:

    def guess(self):
        found_guess = None
        still_unsolved = []
        remaining_answers_list = []
        for n in range(len(self.wordles)):
            wordle = self.wordles[n]
            if not wordle.is_solved():
                still_unsolved.append(n)
                remaining_answers = wordle.remaining_answers()
                if len(remaining_answers) == 0:
                    raise Exception(f"Inconsistent data in wordle {n}")
                if len(remaining_answers) == 1:
                    found_guess = remaining_answers[0]
                remaining_answers_list.append(remaining_answers)
        if len(still_unsolved) == 0:
            return "Done"
            
        wordle_expected_uncertainties = []
        for n in range(len(still_unsolved)):
            wordle = self.wordles[still_unsolved[n]]
            remaining_answers = remaining_answers_list[n]
            wordle_expected_uncertainties.append(self.list_to_dict_keyed_on(wordle.expected_uncertainty_by_guess(remaining_answers, found_guess), 'guess'))
        expected_uncertainties = list(self.merge_by_guess(wordle_expected_uncertainties).values())
        expected_uncertainties.sort(key=lambda x: x['expected_uncertainty_after_guess'])
        return expected_uncertainties[0]
            
    def solve(self, targets, start_with=[]):
        guesses = []
        assert len(targets) == len(self.wordles)
        for n in range(len(targets)):
            target = targets[n]
            wordle = self.wordles[n]
            for guess in start_with:
                score = wordle.score_guess(target, guess)
                wordle.guess_scores.append([guess, score])
        while not self.is_solved():
            next_guess = self.guess()
            guess = next_guess['guess']
            for wordle in self.wordles:
                if not wordle.is_solved():
                    score = wordle.score_guess(target, guess)
                    wordle.guess_scores.append([guess, score])
            guesses.append(next_guess)
        return guesses

    def __init__(self, guesses=[], scores_list=[[]], hard_mode=False, debug=False,
                 sqlite_dbname=None, 
                 mysql_username=None, 
                 mysql_password=None,
                 mysql_host=None,
                 mysql_database=None) :
        self.wordles = []
        for scores in scores_list:
            guess_scores = self.create_guess_scores(guesses, scores)
            self.wordles.append(Wordle.Wordle(guess_scores=guess_scores, hard_mode = hard_mode, debug = debug, sqlite_dbname=sqlite_dbname, mysql_username = mysql_username, mysql_password = mysql_password, mysql_host = mysql_host, mysql_database = mysql_database))

    def create_guess_scores(self, guesses, scores):
        guess_scores = []
        for n in range(len(guesses)):
            if n < len(scores):
                guess_scores.append([guesses[n], scores[n]])
        return guess_scores

    def is_solved(self):
        for w in self.wordles:
            if not w.is_solved():
                return False
        return True

    # list should be a list of dicts, each with a unique `key` value
    def list_to_dict_keyed_on(self, list, key):
        retval = {}
        for dict in list:
            retval[dict[key]] = dict
        return retval

    # wordle_expected_uncertainties is a list of dicts
    # keys of each dict are guesses, values are next_guess objects
    # return value is a dict keyed on guess
    def merge_by_guess(self, wordle_expected_uncertainties) :
        return reduce(self.merge_all_guesses, wordle_expected_uncertainties)

    def merge_all_guesses(self, dict1, dict2) :
        dict3 = {}
        for key in dict1:
            g1 = dict1[key]
            g2 = dict2[key]
            dict3[key] = self.merge_guesses(g1, g2)
        return dict3

    def merge_guesses(self, g1, g2) :
        if not g1:
            return g2
        if not g2:
            return g1
        g = {}
        g['guess'] = g1['guess']
        g['compatible'] = g1['compatible'] or g2['compatible'] 
        g['uncertainty_before_guess'] = g1['uncertainty_before_guess'] + g2['uncertainty_before_guess']
        g['expected_uncertainty_after_guess'] = g1['expected_uncertainty_after_guess'] + g2['expected_uncertainty_after_guess']
        return g

