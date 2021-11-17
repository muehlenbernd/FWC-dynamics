import MyMath as MyMath
import random

class RL3x3:

    ### CONSTRUCTOR ###

    def __init__(self):

        self.probA = 1.0 / 3
        self.probB = 1.0 / 3
        self.probC = 1.0 / 3
        self.acc_utilities = [0.0, 0.0, 0.0]


    ### CHOICE FUNCTION ###

    def choice(self, game):

        if self.acc_utilities[0] > 0.0 and self.acc_utilities[1] > 0.0 and self.acc_utilities[2] > 0.0:
            self.probA = self.acc_utilities[0] * 1.0 / sum(self.acc_utilities)
            self.probB = self.acc_utilities[1] * 1.0 / sum(self.acc_utilities)
            self.probC = self.acc_utilities[2] * 1.0 / sum(self.acc_utilities)

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

        if my_choice == 'A':
            if opponent_choice=='A':
                self.acc_utilities[0] += game.payoffs[0][0]
            elif opponent_choice=='B':
                self.acc_utilities[0] += game.payoffs[0][1]
            else:
                self.acc_utilities[0] += game.payoffs[0][2]
        elif my_choice == 'B':
            if opponent_choice == 'A':
                self.acc_utilities[1] += game.payoffs[1][0]
            elif opponent_choice == 'B':
                self.acc_utilities[1] += game.payoffs[1][1]
            else:
                self.acc_utilities[1] += game.payoffs[1][2]
        elif my_choice == 'C':
            if opponent_choice == 'A':
                self.acc_utilities[2] += game.payoffs[2][0]
            elif opponent_choice == 'B':
                self.acc_utilities[2] += game.payoffs[2][1]
            else:
                self.acc_utilities[2] += game.payoffs[2][2]


    ### RESET FUNCTION ###

    def reset(self):

        self.probA = 1.0 / 3
        self.probB = 1.0 / 3
        self.probC = 1.0 / 3
        self.acc_utilities = [0.0, 0.0, 0.0]