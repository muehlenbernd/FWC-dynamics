import MyMath as MyMath

class RL:

    ### CONSTRUCTOR ###

    def __init__(self):

        self.prob_coop = 0.5
        self.acc_utilities = [0.0, 0.0]


    ### CHOICE FUNCTION ###

    def choice(self, game):

        if self.acc_utilities[0] > 0.0 and self.acc_utilities[1] > 0.0:
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
