import MyMath as MyMath
import random

class FP3x3:

    ### CONSTRUCTOR ###

    def __init__(self):

        self.probA = 1.0 / 3
        self.probB = 1.0 / 3
        self.probC = 1.0 / 3
        self.choices_opponents = [0, 0, 0]

        self.beliefA = 0.0
        self.beliefB = 0.0
        self.beliefC = 0.0


    ### CHOICE FUNCTION ###

    def choice(self, game):

        if sum(self.choices_opponents) > 0:

            self.beliefA = self.choices_opponents[0] * 1.0 / sum(self.choices_opponents)
            self.beliefB = self.choices_opponents[1] * 1.0 / sum(self.choices_opponents)
            self.beliefC = self.choices_opponents[2] * 1.0 / sum(self.choices_opponents)


            exp_util_A = game.payoffs[0][0]*self.beliefA + game.payoffs[0][1]*self.beliefB + game.payoffs[0][2]*self.beliefC
            exp_util_B = game.payoffs[1][0]*self.beliefA + game.payoffs[1][1]*self.beliefB + game.payoffs[1][2]*self.beliefC
            exp_util_C = game.payoffs[2][0]*self.beliefA + game.payoffs[2][1]*self.beliefB + game.payoffs[2][2]*self.beliefC

            if exp_util_A > exp_util_B and exp_util_A > exp_util_C:
                self.probA = 1.0
                self.probB = 0.0
                self.probC = 0.0
            elif exp_util_B > exp_util_A and exp_util_B > exp_util_C:
                self.probA = 0.0
                self.probB = 1.0
                self.probC = 0.0
            elif exp_util_C > exp_util_A and exp_util_C > exp_util_B:
                self.probA = 0.0
                self.probB = 0.0
                self.probC = 1.0
            elif exp_util_A == exp_util_B and exp_util_A > exp_util_C:
                self.probA = 0.5
                self.probB = 0.5
                self.probC = 0.0
            elif exp_util_A == exp_util_C and exp_util_A > exp_util_B:
                self.probA = 0.5
                self.probB = 0.0
                self.probC = 0.5
            elif exp_util_B == exp_util_C and exp_util_B > exp_util_A:
                self.probA = 0.0
                self.probB = 0.5
                self.probC = 0.5
            else:
                self.probA = 1.0/3
                self.probB = 1.0/3
                self.probC = 1.0/3


        random_draw = random.random()

        if random_draw < self.probA:
            choice = 'A'
        elif random_draw < (self.probA+self.probB):
            choice = 'B'
        else:
            choice = 'C'

        return choice


    ### UPDATE FUNCTION ###

    def update(self, game, my_choice, opponent_choice):

        if opponent_choice == 'A':
            self.choices_opponents[0] += 1
        elif opponent_choice == 'B':
            self.choices_opponents[1] += 1
        else:
            self.choices_opponents[2] += 1


    ### RESET FUNCTION ###

    def reset(self):

        self.choices_opponents = [0, 0, 0]
        self.probA = 1.0 / 3
        self.probB = 1.0 / 3
        self.probC = 1.0 / 3

        self.beliefA = 0.0
        self.beliefB = 0.0
        self.beliefC = 0.0