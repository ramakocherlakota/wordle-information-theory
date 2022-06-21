# Using Information Theory to Play Wordle

## Wordle Basics

Let's apply all this machinery to a more interesting game: Wordle.  If you look at the javscript source code (I didn't but somebody else did an posted the results on the internet) you'll see that there are 2315 words that could be the solution to your daily Wordle.  These are basically the reasonably common five-letter English words, but without plurals and, for the most part, past tenses.  If you want to see the list in alphaabetical order, (click here)[../py/answers.txt[.

So let's make some assumptions about the way the game works.  We'll assume that on any given day, the answer word is chosen at random from among those 2315.  That's not actually trye - the daily answer is determined in advance and is itself in the javascript code but let's pretend we don't have access to that information (as most Wordle players don't) and that we don't remember what yesterday's word was (it was LOSER, which felt a little personal but I solved it in three, so take that, Mr. Wordle!).  Based on how we defined uncertainty, the uncertainty involved in trying to guess the word with no clues is log(2315) = 11.176 bits.

## Best First Guess

Okay, so a standard question among Wordle players is, "what is your favorite first guess?"  What does information theory tell us about this question?  If we use the same approach we used so successfully for the 1-10 game, we're looking for a guess where the expected uncertainty after we make the guess and get the response is minimized.

Of course, the situation is a little more complicated than in the 1-10 game.  There are 2315 possible guesses (actually Wordle will let you guess words from a larger set of 12000 or so words but let's ignore that, it turns out not to make much difference and why would you guess a word that you know for a fact isn't a possible answer?) and for each guess, 243 possible responses.

Where do we get that 243?  Well, for each letter in the guess it could either be "not in the answer" or "in the answer but in the wrong place" or "in the answer in the right place".  Total number of possible responses is thus 3^5 = 243.  To simplify the notation a bit, we'll denote an answer of (say) "first letter right but in the wrong place, fourth letter right and in the right place as "W--B-".  (The W stands for white and the B for black - the original Mastermind game used black and white pegs for "right in the right place" and "right in the wrong place.)

We can impose some order on all this by storing the data in a database. I created a mysql database on my laptop and added a table `scores` with three columns: `answer`, `guess` and `score`.  This table has 2315 * 2315 = 5.36 million rows in it, which is a lot for a person but nothing scary for a database.

If you send in a guess G and get back a score S, then the set of possible answers has been reduced from 2315 to

```
select answer from scores where guess = G and score = S;
```

If, for example, you guess "LOSER" and the score is "-BW-W" you're down to six possibilities:


```
select answer from scores where guess='loser' and score='-BW-W';
+--------+
| answer |
+--------+
| roast  |
| roost  |
| sorry  |
| torso  |
| torus  |
| worst  |
+--------+
```
That means that if the response is "-BW-W" then the uncertainty is log(6) = 2.58 bits, a pretty good reduction from 11.176 bits.  Of course, this is not a likely outcome - it only happens for 6/2315 = 0.25% of the time.

On the other hand, if the score is 'W--W-', then there are 101 possibilities, so the uncertainty is log(101) = 6.66 bits.  This is more likely, occurring 101/2315 = 4.36% of the time.

To decide if "LOSER" is a good or a bad first guess, we need to figure out the expected uncertainty after we get the response back.  We do this by adding up, for each possible response, the product of the uncertainty after getting the response times the probability of getting that response.  We can write this as a SQL query:

```
select sum(c * log(c) / log(2)) / sum(c) from
  (select score, count(*) as c from scores where guess = 'LOSER' group by 1) as t;
```
And that returns 5.712 bits - so "LOSER" reduces the uncertainty from 11.176 to 5.712 bits, about a fifty percent reduction.  Is that good?  Is "LOSER" a good first guess?

Let's try the same computation for some other words.  Actually, let's do it for ALL the words.

```
select guess, truncate(sum(c * log(c) / log(2)) / sum(c), 3) as h from
  (select guess, score, count(*) as c from scores where guess in
     (select answer from answers) group by 1, 2) as t
   group by 1 order by 2;

+-------+-------+
| guess | h     |
+-------+-------+
| raise | 5.298 |
| slate | 5.321 |
| crate | 5.341 |
| irate | 5.345 |
| trace | 5.346 |
| arise | 5.355 |
| stare | 5.369 |
| snare | 5.406 |
| arose | 5.408 |
| least | 5.425 |
| alert |  5.43 |
| crane | 5.434 |
| stale | 5.438 |
| saner | 5.443 |
| alter | 5.463 |
| later |  5.47 |
| react |  5.48 |
| leant | 5.492 |
| trade | 5.495 |
| learn |  5.52 |
| cater |  5.53 |
| roast | 5.531 |
| aisle | 5.539 |
...
| rouse | 5.705 |
| paler | 5.711 |
| loser | 5.712 |
| suite | 5.717 |
| tripe | 5.717 |
| crest | 5.718 |
| shear |  5.72 |
...
| jiffy | 8.668 |
| fizzy | 8.669 |
| mummy | 8.697 |
| mamma | 8.778 |
| jazzy | 8.867 |
| fuzzy | 8.871 |
+-------+-------+
2315 rows in set (39.17 sec)
```

"LOSER" turns out to be #74 in the list of words, "RAISE" is #1.

## Information

If you think in terms not of remaining uncertainty but in terms of how much your guess has reduced the uncertainty, that quantity is referred to as the amount of information your guess provides.  That's actually a better way of thinking about it in smoe ways.  

```
select guess, truncate(log(2315) / log(2) - (sum(c * log(c) / log(2))  / sum(c)), 3) as I from
  (select guess, score, count(*) as c from scores where guess in
    (select answer from answers) group by 1, 2) as t
  group by 1 order by 2 desc;
+-------+-------+
| guess | I     |
+-------+-------+
| raise | 5.877 |
| slate | 5.855 |
| crate | 5.834 |
| irate | 5.831 |
| trace |  5.83 |
| arise |  5.82 |
| stare | 5.807 |
| snare |  5.77 |
| arose | 5.767 |
| least | 5.751 |
| alert | 5.745 |
| crane | 5.742 |
| stale | 5.738 |
| saner | 5.733 |
| alter | 5.713 |
| later | 5.706 |
| react | 5.696 |
| leant | 5.684 |
| trade | 5.681 |
| learn | 5.656 |
| cater | 5.646 |
| roast | 5.645 |
| aisle | 5.636 |
...
| rouse | 5.471 |
| loser | 5.464 |
| paler | 5.464 |
| crest | 5.458 |
| suite | 5.458 |
| tripe | 5.458 |
| shear | 5.455 |
...
| jiffy | 2.508 |
| fizzy | 2.506 |
| mummy | 2.479 |
| mamma | 2.398 |
| jazzy | 2.309 |
| fuzzy | 2.305 |
+-------+-------+
2315 rows in set (37.89 sec)
```

This means that, in a very precise sense, the best first guess, "RAISE" (5.877 bits) is expected to be more than twice as informative as the worst guess "FUZZY" (2.305 bits).  Even compared to a superficially similar word like "LOSER" (couple of vowels, some common consonants, no repated letters), it is 0.412 bits, or about 7.5% better.


