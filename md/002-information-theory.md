# Guessing Games and Information Theory

Wordle is a guessing game. One player chooses an answer and the other player tries to arrive at it by making guesses, getting hints after each one as to how close the guess is to the answer.  Moreover, it's a finite game - the list of possible answers is finite and known to both players (at least to the extent that the answer must be a five-letter English word, but more on that shortly).

It's actually similar, at least in principle, to a game that you probably played as a kid.  Player one says, "I'm thinking of a number between 1 and 10" and player two has to guess it.  After each guess, player one says "higher" or "lower' to indicate whether the target number is higher or lower than the guess.  It's the kind of game that would only amuse a child for any length of time but such games are actually extremely valuable for parents around the world.

Once you'd played the game a few times, you probably realized that your best strategy is to guess a number near the middle of the remaining possibilities.  So to start with, guess "5" or "6".  If the response is "lower" then you do the same again, guessing "3".  Etc.

The question arises, why is this such a good strategy? After all, if you guessed "2" as your first guess, if the answer was "lower" you would have no difficulty at all in guessing the right answer in your next turn.  Granted, the probability of this happening is low - you're much more likely to get back "higher".  So the strategy balances off the "quality" of an outcome against the probability of it happening.

How do we evaluate the "quality" of the response?  You could just say "the number of remaining possibilities", but that isn't quite right.  After all, the initial setup has a "number of remaining possibilities" of 10, but it probably makes more sense to think in terms of "how uncertain am I about the answer?"  Is playing the number guessing game twice as hard if there are 20 possibilities to start with instead of 10?  

Information theory is a branch of mathematics that addresses questions like this.  How do you evaluate a situation where you're trying to guess something based on what you know?  It's really a branch of probability theory, since in all these situations there are things that are unknown and (at laast implicitly) expectations about how likely different outcomes are.  It was developed in the middle of the twentieth century by scientists and engineers at Bell Labs, most notably Claude Shannon.

The fundamental quantity measured in information theory is called `uncertainty` or `entropy` and it is a measure of how uncertain the outcome of a particular experiment is.  Let's start with a a very simple case: the toss of a fair coin.  There are two equally likely outcomes, heads or tails, and let's denote the amount of uncertainty in that outcome as "one bit".

Let's also say that uncertainty should be additive.  That is, if you have two independent experiments, the uncertainty in the outcome of the two of them together should be the sum of the two uncertainties.  So, the outcome of flipping two coins is twice as uncertain as flipping one coin. Extending this, flipping n coins has an uncertainty of n bits.

How does this help us?  Well, let's go back to the "guess a number" game but to simplify things (you'll see why in a minute) suppose we say "I'm thinking of a number between 0 and 15".  Now, that really means "I'm thinking of four independent binary digits".  Choosing a binary digit has an uncertainty of 1 bit and, by additivity, this means the uncertainty of this game is 4 bits.

More generally, let's just define the uncertainty of an experiment with n equally likely outcomes to be log(n) bits.  Then log(2) = 1 bit (there are two outcomes two a coin flip) and log(16) = 4 bits for our sixteen-choice game.

Of course, the uncertainty won't always be a nice integer - for the 1-10 guess game we started with, there are 10 possibilities, so the uncertainty is log(10) which is about 3.322 bits.

Let's apply this to try to understand the "guess the number in the middle" strategy.  Say you guess n.  What is the expected uncertainty after you get back the response?  There are three possibilities:

1. You got it right!  Uncertainty is now 0 and the probability of that happening is 0.1.
2. The response is "lower".  Uncertainty is now log(n-1) and the probability of that happening is (n-1) / 10.
3. The response is "higher".  Uncertainty is now log(10-n) and the probability of that happening is (10 - n) / 10.

So the expected uncertainty from a guess of n is:
```
U(n) = log(n-1) * (n-1) / 10 + log(10-n) * (10 - n) / 10
```

This isn't hard to compute:

| n | U(n) |
|---|------|
|1|2.853|
|2|2.400|
|3|2.165|
|4|2.026|
|5|1.961|
|6|1.961|
|7|2.026|
|8|2.165|
|9|2.400|
|10|2.853|

Note that guessing 5 or 6 gives you the lowest possible expected uncertainy.  This is exactly what you figured out after playing this game seven or eight times with your older brother (but with more math and less teasing).
