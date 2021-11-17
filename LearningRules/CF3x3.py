import MyMath as MyMath
import random

class CF3x3:

    ### CONSTRUCTOR ###

    def __init__(self):

        self.probA = 1.0 / 3
        self.probB = 1.0 / 3
        self.probC = 1.0 / 3


    ### CHOICE FUNCTION ###

    def choice(self, game):

        random_draw = random.random()

        if random_draw < self.probA:
            choice = 'A'
        elif random_draw < (self.probA + self.probB):
            choice = 'B'
        else:
            choice = 'C'

        return choice


    ### UPDATE FUNCTION ###

    def update(self, game, my_choice, opponent_choice):

        self.probA = 1.0 / 3
        self.probB = 1.0 / 3
        self.probC = 1.0 / 3


    ### RESET FUNCTION ###

    def reset(self):

        self.probA = 1.0 / 3
        self.probB = 1.0 / 3
        self.probC = 1.0 / 3