import MyMath as MyMath
import random

class NE3x3:

    ### CONSTRUCTOR ###

    def __init__(self):

        self.probA = 1.0 / 3
        self.probB = 1.0 / 3
        self.probC = 1.0 / 3


    ### CHOICE FUNCTION ###

    def choice(self, game):



        a = game.payoffs[0][0]
        b = game.payoffs[0][1]
        c = game.payoffs[1][0]
        d = game.payoffs[1][1]

        self.probA = (d - b) * 1.0 / (a - b - c + d)
        self.probB = 1.0-self.probA
        self.probC = 0.0

        random_draw = random.random()

        if random_draw < self.probA:
            choice = 'A'
        else:
            choice = 'B'


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