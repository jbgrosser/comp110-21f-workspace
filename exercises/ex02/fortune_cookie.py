"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730475279"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
r_integer: int = randint(1,4)
print("Your fortune cookie says...")
if r_integer == 1:
    print("Tomorrow you will meet a celebrity!")
else:
    if r_integer == 2:
        print("You will fall in love.")
    else:
        if r_integer == 3:
            print("You will win 1 million dollars!")
        else:
            print("Your favorite sports team will win a game!")
print("Now, go spread positive vibes!")