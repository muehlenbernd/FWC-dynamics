import MyMath as MyMath

class NE:

    ### CONSTRUCTOR ###

    def __init__(self):

        self.prob_coop = 0.5


    ### CHOICE FUNCTION ###

    def choice(self, game):

        if game.type == 'PD':
            self.prob_coop = 0.0

        else:

            a = game.payoffs[0][0]
            b = game.payoffs[0][1]
            c = game.payoffs[1][0]
            d = game.payoffs[1][1]

            self.prob_coop = (d - b) * 1.0 / (a - b - c + d)

        if MyMath.prob_choice(self.prob_coop):
            choice = 'C'
        else:
            choice = 'D'


        return choice


    ### UPDATE FUNCTION ###

    def update(self, game, my_choice, opponent_choice):

        self.prob_coop = 0.5


    ### RESET FUNCTION ###

    def reset(self):

        self.prob_coop = 0.5