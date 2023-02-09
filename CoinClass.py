import random

# The Coin class simulates a coin that can
# be flipped.


class Coin:
    # The _ _init_ _ method initializes the
    # initialization method (__init__)
    # sideup data attribute with 'Heads'.
    # dont have to call it in the main program, auto runs

    def __init__(self):
        self.__sideup = "Heads"

    # The toss method generates a random number
    # in the range of 0 through 1. If the number
    # is 0, then sideup is set to 'Heads'.
    # Otherwise, sideup is set to 'Tails'.
    # toss method effects the value of the attribute
    # when it is called
    # mutator method --> "set method"

    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"

    # The get_sideup method returns the value
    # referenced by sideup.
    # accessor method --> "get method"

    def get_sideup(self):
        return self.__sideup

    # everytime you make a change you must save it so the
    # changes are affected
