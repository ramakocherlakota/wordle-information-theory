# List of Best First Two Words

## The script

This directory contains code and output for computing the best pairs of starting words for Wordle, assuming you don't use any information from the outcome of the first guess in choosing the second guess. So, the idea is you just blindly guess the first two words and then really start using the scores in your third guess.

Run the python script in this directory:
```
python two-guesses.py | sort -n 
```
Be patient.  On my laptop it took about twenty hours to run.  Or you can just use the `sorted-two-guess-list.txt` in this directory.

## How it works

The script is simple but a little time-consuming.  It loads up a list of all the allowed answers and then all the scores.  It then computes the expected uncertainty in the answer if you guessed each pair of words.  That is, for each pair of words `guess1` and `guess2`, it
1. Iterates through all the answers, computing the scores for `guess1` and `guess2`.
2. Keeps track of how often each pair of scores `score1` and `score2` shows up.  The more often a given pair shows up, the higher the leftover uncertainty after you've made those guesses and received those scores.  For instance, suppose
    * You guess 'golly' and get back 'b-w--'
    * You guess 'stick' and get back '--b--'
The only word that matches those starting guesses and scores is 'glide' so there is no uncertainty left at this point - you can guess the answer on your third guess.
Of course, this isn't necessarily a very likely situation.  If the scores that come back are 'w----' and '--b--' instead, then there are ten words that match ("aging", "aping", "being", "bring", "deign", "feign", "neigh", "reign", "weigh", "wring") and the uncertainty after these two guesses and responses is log(10) = 3.32 bits.
3. Computes the expected uncertainty for each pair.  This is just the sum of the uncertainties, weighted for how likely they are.  It turns out that the expected uncertainty for `golly` and `stick` is 3.45 bits.  Is this good?  Well, out of the 2678455 possible pairs of first guesses, `golly` and `stick` is ranked as number 989868.  So solidly mediocre.
    


