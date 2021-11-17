import MyMath as MyMath
import math
import numpy as np

class FP:

    ### CONSTRUCTOR ###

    def __init__(self, softmax=False, lambada=0.0):

        self.prob_coop = 0.5
        self.choices_opponents = [0, 0]
        self.belief_coop = 0.0

        self.softmax = softmax
        self.lambada = lambada


    ### CHOICE FUNCTION ###

    def choice(self, game):

        if self.choices_opponents[0] > 0 and self.choices_opponents[1] > 0:

            self.belief_coop = self.choices_opponents[0]*1.0/sum(self.choices_opponents)

            #print believe_coop,

            exp_util_C = game.payoffs[0][0] * self.belief_coop + game.payoffs[0][1] * (1.0 - self.belief_coop)
            exp_util_D = game.payoffs[1][0] * self.belief_coop + game.payoffs[1][1] * (1.0 - self.belief_coop)

            if self.softmax == False:
                if exp_util_C > exp_util_D:
                    self.prob_coop = 1.0
                elif exp_util_C < exp_util_D:
                    self.prob_coop = 0.0
                else:
                    self.prob_coop = 0.5

            else:
                exp_coop = np.exp(self.lambada * exp_util_C)
                exp_def = np.exp(self.lambada * exp_util_D)

                self.prob_coop = exp_coop / (exp_coop + exp_def)

        if MyMath.prob_choice(self.prob_coop):
            choice = 'C'
        else:
            choice = 'D'

        return choice


    ### UPDATE FUNCTION ###

    def update(self, game, my_choice, opponent_choice):

        if opponent_choice == 'C':
            self.choices_opponents[0] += 1
        else:
            self.choices_opponents[1] += 1


    ### RESET FUNCTION ###

    def reset(self):

        self.choices_opponents = [0, 0]
        self.prob_coop = 0.5
        self.belief_coop = 0.0