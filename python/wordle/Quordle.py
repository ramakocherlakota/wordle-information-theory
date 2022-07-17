import Wordle
from functools import reduce

class Quordle:

    def __init__(self, dbname, guesses=[], scores_list=[[]], hard_mode=False, debug=False) :
        self.wordles = []
        for scores in scores_list:
            guess_scores = self.create_guess_scores(guesses, scores)
            self.wordles.append(Wordle.Wordle(dbname = dbname, hard_mode = hard_mode, debug = debug)

    def create_guess_scores(self, guesses, scores):
        

    def is_solved(self):
        for w in self.wordles:
            if not w.is_solved():
                return False
        return True

    def guess(self):
        remaining_answers_list = []
        found_guess = None
        remaining_wordles = []
        for wordle in self.wordles:
            if not wordle.is_solved():
                remaining_answers = wordle.remaining_answers()
                remaining_wordles_list.append(wordle)
                if len(remaining_answers) == 0:
                    raise Exception("Inconsistent data")
                if len(remaining_answers) == 1:
                    found_guess = remaining_answers[0]
                remaining_answers_list.append(remaining_answers)
        wordle_expected_uncertainties = []
        for n in range(len(remaining_wordles)):
            wordle = reamining_wordles_list[n]
            remaining_answers = remaining_answers_list[n]
            wordle_expected_uncertainties.append(list_to_dict_keyed_on(wordle.expected_uncertainty_by_guess(remaining_answers, found_guess)), 'guess')
        expected_uncertainties = merge_by_guess(wordle_expected_uncertainties)
        expected_uncertainties.sort(key=lambda x: x['expected_uncertainty_after_guess'])
        return expected_uncertainties[0]
            
    # list should be a list of dicts, each with a unique `key` value
    def list_to_dict_keyed_on(list, key):
        retval = {}
        for dict in list:
            retval[dict[key]] = dict
        return retval

    # wordle_expected_uncertainties is a list of dicts
    # keys of each dict are guesses, values are next_guess objects
    # return value is a dict keyed on guess
    def merge_by_guess(self, wordle_expected_uncertainties) :
        return reduce(merge_all_guesses, wordle_expected_uncertainties)

    def merge_all_guesses(dict1, dict2) :
        dict3 = {}
        for key in dict1:
            g1 = dict1[key]
            g2 = dict2[key]
            dict3[key] = merge_guesses(g1, g2)
        return dict3

    def merge_guesses(g1, g2) :
        g = {}
        g['guess'] = g1['guess']
        g['hard_mode'] = g1['hard_mode'] or g2['hard_mode'] # hard_mode in quordle means at least of the guesses is hard_mode
        g['uncertainty_before_guess'] = g1['uncertainty_before_guess'] + g2['uncertainty_before_guess']
        g['expected_uncertainty_after_guess'] = g1['expected_uncertainty_after_guess'] + g2['expected_uncertainty_after_guess']


