import MyMath as MyMath
import math
import numpy as np


class RL:

    ### CONSTRUCTOR ###

    def __init__(self, softmax=False, lambada=0.0):

        self.prob_coop = 0.5
        self.acc_utilities = [0.0, 0.0]

        self.softmax = softmax
        self.lambada=lambada


    ### CHOICE FUNCTION ###

    def choice(self, game):

        if self.acc_utilities[0] > 0.0 and self.acc_utilities[1] > 0.0:

            if self.softmax:

                exp_coop = np.exp(self.lambada * self.acc_utilities[0])
                exp_def = np.exp(self.lambada * self.acc_utilities[1])

                self.prob_coop = exp_coop / (exp_coop + exp_def)

            else:
                self.prob_coop = self.acc_utilities[0]*1.0/sum(self.acc_utilities)

        if MyMath.prob_choice(self.prob_coop):
            choice = 'C'
        else:
            choice = 'D'

        return choice


    ### UPDATE FUNCTION ###

    def update(self, game, my_choice, opponent_choice):

        if my_choice == 'C':
            self.acc_utilities[0] += game.payoffs[0][0 if opponent_choice=='C' else 1]
        else:
            self.acc_utilities[1] += game.payoffs[1][0 if opponent_choice=='C' else 1]


    ### RESET FUNCTION ###

    def reset(self):

        self.prob_coop = 0.5
        self.acc_utilities = [0.0, 0.0]