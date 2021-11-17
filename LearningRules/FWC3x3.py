import random

class FWC3x3:

    ### CONSTRUCTOR ###

    def __init__(self):

        self.probA = 1.0 / 3
        self.probB = 1.0 / 3
        self.probC = 1.0 / 3

        self.harmony = 1.0 / 4
        self.greed1 = 1.0 / 4
        self.greed2 = 1.0 / 4
        self.greed3 = 1.0 / 4

        self.opponent_choices = []

        self.last_opponent_choice = -1
        self.before_last_opponent_choice = -1

        self.counter = [0, 0, 0, 0, 0]



    ### CHOICE FUNCTION ###

    def choice(self, game):

        # get the game features EFF, TEMP and RISK
        a1 = game.payoffs[0][0]
        a2 = game.payoffs[0][1]
        a3 = game.payoffs[0][2]
        b1 = game.payoffs[1][0]
        b2 = game.payoffs[1][1]
        b3 = game.payoffs[1][2]
        c1 = game.payoffs[2][0]
        c2 = game.payoffs[2][1]
        c3 = game.payoffs[2][2]

        glob_max = max(a1,a2,a3,b1,b2,b3,c1,c2,c3)

        TEMP1 = (max(b1,c1)-a1)*1.0 / glob_max
        TEMP2 = (max(a2,c2)-b2)*1.0 / glob_max
        TEMP3 = (max(a3,b3)-c3)*1.0 / glob_max

        EFF = (c3 - a1) * 1.0 / glob_max


        # compute the dispositions as product of game features and weights
        disp_EFF = EFF * self.harmony
        disp_TEMP1 = TEMP1 * self.greed1
        disp_TEMP2 = TEMP2 * self.greed2
        disp_TEMP3 = TEMP3 * self.greed3

        # set positive and negative part of disp_TEMP1
        TEMP1_A = 0.0
        TEMP1_B = 0.0
        TEMP1_C = 0.0
        if a1 > b1 and a1 > c1:
            TEMP1_A = disp_TEMP1
        else:
            if b1 > c1:
                TEMP1_B = disp_TEMP1
            else:
                TEMP1_C = disp_TEMP1

        # set positive and negative part of disp_TEMP1
        TEMP2_A = 0.0
        TEMP2_B = 0.0
        TEMP2_C = 0.0
        if  b2 > a2 and b2 > c2:
            TEMP2_B = disp_TEMP2
        else:
            if a2 > c2:
                TEMP2_A = disp_TEMP2
            else:
                TEMP2_C = disp_TEMP2



        # set positive and negative part of disp_TEMP1
        TEMP3_A = 0.0
        TEMP3_B = 0.0
        TEMP3_C = 0.0
        if c3 > a3 and c3 > b3:
            TEMP3_C = disp_TEMP3
        else:
            if a3 > b3:
                TEMP3_A = disp_TEMP3
            else:
                TEMP3_B = disp_TEMP3

        divider = TEMP1_A+TEMP2_A+TEMP3_A+TEMP1_B+TEMP2_B+TEMP3_B+TEMP1_C+TEMP2_C+TEMP3_C+disp_EFF

        self.probA = (TEMP1_A + TEMP2_A + TEMP3_A) / divider
        self.probB = (TEMP1_B + TEMP2_B + TEMP3_B) / divider
        self.probC = (TEMP1_C + TEMP2_C + TEMP3_C + disp_EFF) / divider

        rand_number = random.random()

        if rand_number < self.probA:

            choice = 'A'

        elif rand_number < (self.probA + self.probB):

            choice = 'B'

        else:
            choice = 'C'


        return choice


    ### UPDATE FUNCTION ###

    def update(self, game, my_choice, opponent_choice):

        # update the memory of the opponents' choice
        self.last_opponent_choice = opponent_choice

        if self.before_last_opponent_choice != -1:

            # compute learning rate
            learning_rate = min(1.0-self.probA, 1.0-self.probB, 1.0-self.probC,self.probA,self.probB,self.probC)

            if self.last_opponent_choice == 'A':
                self.greed1 += learning_rate
                self.counter[2] += 1

            if self.last_opponent_choice == 'B':
                self.greed2 += learning_rate
                self.counter[3] += 1

            if self.last_opponent_choice == 'C':
                self.greed3 += learning_rate
                self.counter[4] += 1

            total_sum =  self.harmony1 + self.harmony2 + self.greed1 + self.greed2 + self.greed3

            self.harmony1 /= total_sum
            self.harmony2 /= total_sum
            self.greed1 /= total_sum
            self.greed2 /= total_sum
            self.greed3 /= total_sum

    ### RESET FUNCTION ###

    def reset(self):

        self.probA = 1.0 / 3
        self.probB = 1.0 / 3
        self.probC = 1.0 / 3

        self.harmony1 = 1.0 / 4
        self.harmony2 = 0.0
        self.greed1 = 1.0 / 4
        self.greed2 = 1.0 / 4
        self.greed3 = 1.0 / 4

        self.opponent_choices = []

        self.last_opponent_choice = -1
        self.before_last_opponent_choice = -1
