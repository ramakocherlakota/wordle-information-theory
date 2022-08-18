# RAISE as a first guess

How good is a first guess of RAISE?

Well, test-all-raises.sh computes, for all of the possible scorss that come back, what is the
expected uncertainty if you guess optimally (to achieve minimal uncertainty).  The output from
that, suitably massaged, is in raise\_second\_guess\_scores.txt - if you crunch the numbers that
tells you that the expected uncertainty *after an optimal second guess* from a first guess of
RAISE is about 1.2963 bits.  Which isn't bad, but it assumes you can guess optimally for
your second guess.  

By comparison, if you blindly guess TRICE / SALON then you would expect 1.5924 bits of uncertainty after that second guess.  The best you can do with a blind guess after RAISE is CLOTH, whcih has an expected uncertainty after guessing of 1.776 bits.


