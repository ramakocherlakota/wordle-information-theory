import Wordle

class Quordle:
    def __init__(self, dbname, guesses=[], scores_list=[[]], hard_mode=False, debug=False) :
        self.wordles = []
        for scores in scores_list:
            guess_scores = self.create_guess_scores(guesses, scores)
            self.wordles.append(Wordle.Wordle(dbname = dbname, hard_mode = hard_mode, debug = debug))

    def guess(self):
        remaining_answers_list = []
        found_guess = None
        for wordle in self.wordles:
            if not wordle.is_solved():
                remaining_answers = wordle.remaining_answers()
                if len(remaining_answers) == 0:
                    raise Exception("Inconsistent data")
                if len(remaining_answers) == 1:
                    found_guess = remaining_answers[0]
                remaining_answers_list.append(remaining_answers)
        expected_uncertainties = []
        for n in range(len(self.wordles)):
            wordle = self.wordles[n]
            remaining_answers = remaining_answers[n]
            expected_uncertainties.append(wordle.expected_uncertainty_by_guess(remaining_answers, found_guess))
            
            

    def qsolve(self, targets, start_with) :
        pass

    def qguess(self, guesses, scores) :
        pass

    # quordle-related methods (for handling multiple wordles at once)

    def merge_maps(self, g, maps_to_merge) :
        merged = {"guess": g}

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
    
    
