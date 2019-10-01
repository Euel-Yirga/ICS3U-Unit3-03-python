#!/usr/bin/env python3

# Created by: Euel Yirga
# Created on: Sept 9 2019
# This plays a guessing game 

import random


def main():
    # random number
    number = random.randint(0, 9)

    # input
    guess = int(input("Guess my number between 0 and 9: "))

    # process
    if guess == number:
        # output
        print()
        print("yes, indeed the number was", number)

    # process
    else:
        # output
        print()
        print("haha nope")
        print("My number was", number)


if __name__ == "__main__":
    main()