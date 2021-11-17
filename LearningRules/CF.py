import MyMath as MyMath

class CF:

    ### CONSTRUCTOR ###

    def __init__(self):

        self.prob_coop = 0.5


    ### CHOICE FUNCTION ###

    def choice(self, game):

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