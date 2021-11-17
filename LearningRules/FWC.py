import MyMath as MyMath
import math

class FWC:

    ### CONSTRUCTOR ###

    def __init__(self, modus = 'new', learning_rate = 0, softmax = False, lambada = 0.0):

        self.prob_coop = 0.5

        self.harmony = 1.0/3
        self.greed = 1.0/3
        self.fear = 1.0/3

        self.last_opponent_choice = -1
        self.last_choice = -1

        # last strategy feature for nxn games with n >= 3
        self.last_strategy = -1
        self.last_opp_strategy = -1

        self.modus = modus

        self.history = []
        self.opp_history = []

        self.learning_rate = learning_rate

        self.softmax = softmax
        self.lambada = lambada


    ### CHOICE FUNCTION ###

    def choice(self, game):

        # get the game features EFF, TEMP and RISK
        a = game.payoffs[0][0]
        b = game.payoffs[0][1]
        c = game.payoffs[1][0]
        d = game.payoffs[1][1]


        if self.modus == 'new':

            EFF = (a-d)*1.0/(max(a,b,c,d) - min(a,b,c,d))     #a
            TEMP = (c-a)*1.0/(max(a,b,c,d) - min(a,b,c,d))
            RISK = (d-b)*1.0/(max(a,b,c,d) - min(a,b,c,d))

        else:

            EFF = (a - d) * 1.0 / a
            TEMP = (c - a) * 1.0 / max(a,c)
            RISK = (d - b) * 1.0 / max(d,b)


        # compute the dispositions as product of game features and weights
        disp_EFF =  EFF  * self.harmony
        disp_TEMP = TEMP * self.greed
        disp_RISK = RISK * self.fear

        # set positive and negative part of disp_TEMP
        if disp_TEMP < 0.0:
            pos_TEMP = 0.0
            neg_TEMP = disp_TEMP * -1.0
        else:
            pos_TEMP = disp_TEMP
            neg_TEMP = 0.0

        # set positive and negative part of disp_RISK
        if disp_RISK < 0.0:
            pos_RISK = 0.0
            neg_RISK = disp_RISK * -1.0
        else:
            pos_RISK = disp_RISK
            neg_RISK = 0.0

        potential_coop = neg_TEMP+neg_RISK+disp_EFF
        potential_def = pos_TEMP+pos_RISK

        if self.softmax:
            exp_coop = math.exp(self.lambada * potential_coop)
            exp_def = math.exp(self.lambada * potential_def)

            self.prob_coop = exp_coop / (exp_coop + exp_def)

        else:
            self.prob_coop = (neg_TEMP+neg_RISK+disp_EFF)/(pos_TEMP+neg_TEMP+pos_RISK+neg_RISK+disp_EFF)


        # make a probabilistic choice
        if MyMath.prob_choice(self.prob_coop):
            choice = 'C'
        else:
            choice = 'D'

        return choice


    ### UPDATE FUNCTION ###

    def update(self, game, my_choice, opponent_choice):

        if game.type == 'PD':
            h_factor = 0.0
        elif game.type == 'SH':
            h_factor = 1.0
        elif game.type == 'CH':
            h_factor = 0.0


        if my_choice == 'C':
            self.history.append(0)
        else:
            self.history.append(1)
        if opponent_choice == 'C':
            self.opp_history.append(0)
        else:
            self.opp_history.append(1)



        # update the memory of the last two opponents' choices
        #self.before_last_opponent_choice = self.last_opponent_choice
        self.last_opponent_choice = opponent_choice

        #self.before_last_choice = self.last_choice
        self.last_choice = my_choice

        # new modus
        if self.modus == 'new':

            # update weights as soon as two rounds were played
            if self.last_opponent_choice != -1:

                # compute learning rate
                if self.learning_rate == 0:
                    learning_rate = min(self.prob_coop, 1.0 - self.prob_coop)
                else:
                    learning_rate = self.learning_rate

                if self.last_opponent_choice == 'C':
                    self.greed += learning_rate
                if self.last_opponent_choice == 'D':
                    self.fear +=  learning_rate

                if self.last_opponent_choice == 'C':
                   self.harmony += h_factor*learning_rate

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
        self.last_choice = -1

        self.last_strategy = -1
        self.last_opp_strategy = -1

        self.history = []
        self.opp_history = []