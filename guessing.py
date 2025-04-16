#!/usr/bin/env python

import random

def main():
    """start a colour guessing game."""
    print("guess the colour!")

    rainbow = ["red","orange","yellow","green","blue","indiogo","violet",]

    x = random.choice(rainbow)
    print(x)
    guess = None

    while x != guess:

        guess = str(input("what colour am i thinking of? "))

        if x == guess:
            print("You guessed {}. Congratulation you got it right!".format(guess))
            break
        else:
            print("you guessed {}. Unfortunately its wrong. Try again!".format(guess))

main()