import MyMath as MyMath

class FWC:

    ### CONSTRUCTOR ###

    def __init__(self):

        self.prob_coop = 0.5

        self.harmony = 1.0/3
        self.greed = 1.0/3
        self.fear = 1.0/3

        self.last_opponent_choice = -1
        self.before_last_opponent_choice = -1


    ### CHOICE FUNCTION ###

    def choice(self, game):

        # get the game features EFF, TEMP and RISK
        a = game.payoffs[0][0]
        b = game.payoffs[0][1]
        c = game.payoffs[1][0]
        d = game.payoffs[1][1]

        EFF = (a-d)*1.0/a
        TEMP = abs(a-c)*1.0/max(a,c)
        RISK = (d-b)*1.0/d

        # compute the dispositions as product of game features and weights
        disp_EFF =  EFF  * self.harmony
        disp_TEMP = TEMP * self.greed
        disp_RISK = RISK * self.fear

        # compute cooperation probability due to dispositions and game type
        if game.type == "SH":
            self.prob_coop = (disp_EFF + disp_TEMP)/(disp_EFF + disp_TEMP + disp_RISK)
        elif game.type == "PD":
            self.prob_coop = (disp_EFF) / (disp_EFF + disp_TEMP + disp_RISK)

        # make a probabilistic choice
        if MyMath.prob_choice(self.prob_coop):
            choice = 'C'
        else:
            choice = 'D'

        return choice


    ### UPDATE FUNCTION ###

    def update(self, game, my_choice, opponent_choice):

        # update the memory of the last two opponents' choices
        self.before_last_opponent_choice = self.last_opponent_choice
        self.last_opponent_choice = opponent_choice

        # update weights as soon as two rounds were played
        if self.before_last_opponent_choice != -1:

            # compute learning rate
            learning_rate = min(self.prob_coop, 1.0 - self.prob_coop)

            # update according to opponents' behavior
            if self.last_opponent_choice == 'C' and self.before_last_opponent_choice == 'D':
                self.harmony += learning_rate
                #self.greed -= (learning_rate * 0.5)
                #self.fear -= (learning_rate * 0.5)

            elif self.last_opponent_choice == 'C' and self.before_last_opponent_choice == 'C':
                #self.harmony -= (learning_rate * 0.5)
                self.greed += learning_rate
                #self.fear -= (learning_rate * 0.5)

            elif self.last_opponent_choice == 'D' and self.before_last_opponent_choice == 'D':
                #self.harmony -= (learning_rate * 0.5)
                #self.greed -= (learning_rate * 0.5)
                self.fear += learning_rate

            # normalize so that all values are >= 0, <= 1 and the sum is 1
            normalized_values = MyMath.normalize_triple([self.harmony,self.greed,self.fear])
            self.harmony = normalized_values[0]
            self.greed = normalized_values[1]
            self.fear = normalized_values[2]


    ### RESET FUNCTION ###

    def reset(self):

        self.prob_coop = 0.5

        self.harmony = 1.0 / 3
        self.greed = 1.0 / 3
        self.fear = 1.0 / 3

        self.last_opponent_choice = -1
        self.before_last_opponent_choice = -1
